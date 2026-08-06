from pathlib import Path
import base64
import contextlib
import gzip
import hashlib
import io
import re
import runpy
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "scripts/_validate_repository_core.py"
_ORIGINAL_PATH_RGLOB = Path.rglob
EXPECTED_READ_ORDER = ["bootstrap/BOOTSTRAP_CANONICO.md", "handoffs/CURRENT.md", "docs/PROJECT_STATUS.md", "docs/NEXT_SAFE_ACTION.md", "docs/BLOCKED_ACTIONS.md", "config/project.yaml", "config/gpts.yaml"]
EXPECTED_TRANSITIONS = [
    {"id": "verify_merged_main", "when": "pull_request_is_merged_and_main_verification_is_absent", "action": "verify_merge_commit_and_main_then_record_external_evidence"},
    {"id": "report_completed_lifecycle", "when": "pull_request_is_merged_and_main_verification_is_present", "action": "report_lifecycle_complete_without_mutation"},
    {"id": "report_closed_unmerged", "when": "pull_request_is_closed_and_not_merged", "action": "report_closed_unmerged_and_require_explicit_reopen_or_abandon_decision"},
    {"id": "stop_on_drift_or_material_finding", "when": "open_pull_request_has_head_or_base_drift_or_material_unresolved_finding", "action": "stop_and_reconcile_under_explicit_authorization"},
    {"id": "require_successful_workflow", "when": "latest_canonical_workflow_attempt_for_exact_head_is_not_completed_success", "action": "wait_or_rerun_only_if_authorized"},
    {"id": "run_gpt0_read_only", "when": "latest_canonical_workflow_attempt_for_exact_head_is_completed_success_and_no_current_gpt0_gate", "action": "execute_documentary_gate_without_mutation"},
    {"id": "stop_on_gpt0_block", "when": "current_gpt0_gate_verdict_is_block", "action": "stop_and_require_material_remediation_authorization"},
    {"id": "stop_on_gpt0_inconclusive", "when": "current_gpt0_gate_verdict_is_inconclusive", "action": "stop_and_require_missing_evidence_or_access"},
    {"id": "run_gpt4_read_only", "when": "current_gpt0_gate_verdict_is_passing_and_no_current_gpt4_gate", "action": "execute_lifecycle_gate_without_mutation"},
    {"id": "stop_on_gpt4_block", "when": "current_gpt4_gate_verdict_is_block", "action": "stop_and_require_material_remediation_authorization"},
    {"id": "stop_on_gpt4_inconclusive", "when": "current_gpt4_gate_verdict_is_inconclusive", "action": "stop_and_require_missing_evidence_or_access"},
    {"id": "require_ready_authorization", "when": "current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_draft_and_exact_head_and_base_ready_authorization_is_absent", "action": "require_explicit_ready_authorization_for_exact_head_and_base"},
    {"id": "execute_ready_transition", "when": "current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_draft_and_exact_head_and_base_ready_authorization_is_present", "action": "mark_pull_request_ready_only"},
    {"id": "recheck_ready_reviews", "when": "current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_ready_and_review_state_changed_since_latest_eligible_gate_or_recheck", "action": "adjudicate_material_findings_before_merge"},
    {"id": "require_merge_authorization", "when": "current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_ready_review_state_is_current_no_material_threads_remain_and_post_ready_exact_head_and_base_merge_authorization_is_absent", "action": "require_explicit_post_ready_merge_authorization_for_exact_head_and_base"},
    {"id": "execute_merge_and_verify_main", "when": "current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_ready_review_state_is_current_no_material_threads_remain_and_post_ready_exact_head_and_base_merge_authorization_is_present", "action": "merge_exact_head_then_verify_merge_commit_and_main_without_propagating_authority"},
]
NEXT_ACTION_ID = "resolve-live-lifecycle-transition-v1"
DERIVED_SUMMARY = "resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle."
NEXT_ACTION_DOCUMENTS = ["bootstrap/BOOTSTRAP_CANONICO.md", "handoffs/CURRENT.md", "docs/PROJECT_STATUS.md", "docs/NEXT_SAFE_ACTION.md", "docs/BLOCKED_ACTIONS.md"]
DERIVED_SUMMARY_DOCUMENTS = ["bootstrap/BOOTSTRAP_CANONICO.md", "handoffs/CURRENT.md", "docs/PROJECT_STATUS.md"]
UPSTREAM_REPOSITORY = "wagnerjfjunior/StopJuniorMode"
UPSTREAM_REF = "d03d477c3b329aa973a38ec4e949c249fa017929"
UPSTREAM_PATH = "docs/CANONICAL_BOOTSTRAP_PROTOCOL.md"
UPSTREAM_BLOB = "7befd02533aad6c2df5544c7307e4a66dce28844"
UPSTREAM_SIZE = 7960
UPSTREAM_LOCAL_COPY = "docs/references/sfjm/CANONICAL_BOOTSTRAP_PROTOCOL.md.gz.b64"
UPSTREAM_EVIDENCE = "docs/evidence/sfjm-upstream-anchor.md"
EXPECTED_EVIDENCE_FIELDS = {"Repositório upstream": UPSTREAM_REPOSITORY, "Revisão congelada": UPSTREAM_REF, "Caminho upstream": UPSTREAM_PATH, "Git blob SHA observado": UPSTREAM_BLOB, "Cópia local imutável": UPSTREAM_LOCAL_COPY}
TEST_COMMAND = 'python -m unittest discover -s tests -p "test_*.py"'
errors = []

def fail(message): errors.append(message)
def read(path):
    try: return (ROOT / path).read_text(encoding="utf-8")
    except Exception as exc: fail(f"{path}: leitura falhou: {exc}"); return ""

def _cache_filtered_rglob(path_object, pattern):
    for candidate in _ORIGINAL_PATH_RGLOB(path_object, pattern):
        if "__pycache__" in candidate.parts or candidate.suffix.lower() in {".pyc", ".pyo"}: continue
        yield candidate

def extract_numbered_paths(text, heading, path):
    match = re.search(rf"(?ms)^{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s|\Z)", text)
    if not match: fail(f"{path}: seção de ordem ausente: {heading}"); return []
    numbers, paths = [], []
    for line in match.group("body").splitlines():
        item = re.match(r"^\s*(\d+)\.\s+(.*?)\s*$", line)
        if not item: continue
        exact = re.fullmatch(r"`([^`]+)`", item.group(2))
        if not exact: fail(f"{path}: item numerado malformado em {heading}: {line.strip()}"); continue
        numbers.append(int(item.group(1))); paths.append(exact.group(1))
    if not paths: fail(f"{path}: nenhuma entrada numerada encontrada em {heading}")
    if numbers and numbers != list(range(1, len(numbers) + 1)): fail(f"{path}: numeração inválida em {heading}; encontrada={numbers}")
    if len(paths) != len(set(paths)): fail(f"{path}: ordem contém entradas duplicadas")
    return paths

def extract_transition_table(text):
    match = re.search(r"(?ms)^## 2\. Máquina de transição\s*$\n(?P<body>.*?)(?=^##\s|\Z)", text)
    if not match: fail("docs/NEXT_SAFE_ACTION.md: tabela de transição ausente"); return []
    rows, priorities = [], []
    for line in match.group("body").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"): continue
        if stripped.startswith("| Prioridade") or re.fullmatch(r"\|[\s:|\-]+\|", stripped): continue
        row = re.fullmatch(r"\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", stripped)
        if not row: fail(f"docs/NEXT_SAFE_ACTION.md: linha de transição malformada: {stripped}"); continue
        priorities.append(int(row.group(1))); rows.append({"id": row.group(2), "when": row.group(3), "action": row.group(4)})
    if priorities != list(range(len(priorities))): fail(f"docs/NEXT_SAFE_ACTION.md: prioridades inválidas: {priorities}")
    return rows

def extract_next_action_id(text, path):
    matches = re.findall(r"(?m)^- Next action ID: `([^`]+)`\s*$", text)
    if len(matches) != 1: fail(f"{path}: marcador Next action ID ausente ou duplicado"); return None
    return matches[0]

def extract_evidence_field(text, label):
    payloads = re.findall(rf"(?m)^- {re.escape(label)}: (.+?)\s*$", text)
    if len(payloads) != 1: fail(f"{UPSTREAM_EVIDENCE}: campo ausente ou duplicado: {label}"); return None
    exact = re.fullmatch(r"`([^`]+)`", payloads[0])
    if not exact: fail(f"{UPSTREAM_EVIDENCE}: campo malformado: {label}"); return None
    return exact.group(1)

def workflow_step(steps, name):
    matches = [step for step in steps if step.get("name") == name]
    if len(matches) != 1:
        fail(f"workflow: passo ausente ou duplicado: {name}")
        return {}
    return matches[0]

def validate_workflow_semantics(text):
    try: data = yaml.safe_load(text) or {}
    except Exception as exc: fail(f"workflow: YAML inválido: {exc}"); return
    steps = data.get("jobs", {}).get("validate", {}).get("steps", [])
    if not isinstance(steps, list): fail("workflow: jobs.validate.steps inválido"); return
    pr = workflow_step(steps, "Checkout exact pull request head")
    non_pr = workflow_step(steps, "Checkout exact non-PR revision")
    before = workflow_step(steps, "Validate canonical framework")
    tests = workflow_step(steps, "Run SFJM adversarial tests")
    after = workflow_step(steps, "Revalidate canonical framework after tests")
    builder = workflow_step(steps, "Validate GPT Builder Action compatibility")
    if pr.get("if") != "${{ github.event_name == 'pull_request' }}": fail("workflow: condição do checkout PR incorreta")
    if pr.get("uses") != "actions/checkout@v4": fail("workflow: action de checkout PR incorreta")
    if pr.get("with", {}).get("ref") != "${{ github.event.pull_request.head.sha }}": fail("workflow: ref do checkout PR incorreto")
    if non_pr.get("if") != "${{ github.event_name != 'pull_request' }}": fail("workflow: condição do checkout não-PR incorreta")
    if non_pr.get("uses") != "actions/checkout@v4": fail("workflow: action de checkout não-PR incorreta")
    if non_pr.get("with", {}).get("ref") is not None: fail("workflow: checkout não-PR não deve sobrescrever ref")
    if before.get("run") != "python scripts/validate_repository.py": fail("workflow: validação inicial incorreta")
    if tests.get("run") != TEST_COMMAND: fail("workflow: comando de testes adversariais incorreto")
    if after.get("run") != "python scripts/validate_repository.py": fail("workflow: revalidação incorreta")
    if builder.get("run") != "python scripts/validate_builder_action.py": fail("workflow: validação Builder incorreta")
    names = [step.get("name") for step in steps]
    required_order = ["Checkout exact pull request head", "Checkout exact non-PR revision", "Validate canonical framework", "Run SFJM adversarial tests", "Revalidate canonical framework after tests", "Validate GPT Builder Action compatibility"]
    indices = [names.index(name) for name in required_order if name in names]
    if len(indices) != len(required_order) or indices != sorted(indices): fail("workflow: ordem dos passos canônicos incorreta")

def git_blob_sha(data): return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def run_core():
    if not CORE.is_file(): print("VALIDATION FAILED\n- scripts/_validate_repository_core.py: ausente"); sys.exit(1)
    output = io.StringIO(); Path.rglob = _cache_filtered_rglob
    try:
        with contextlib.redirect_stdout(output): runpy.run_path(str(CORE), run_name="__main__")
    except SystemExit as exc:
        if output.getvalue(): print(output.getvalue(), end="")
        sys.exit(exc.code if isinstance(exc.code, int) and exc.code else 1)
    finally: Path.rglob = _ORIGINAL_PATH_RGLOB

run_core()
try: sfjm = yaml.safe_load((ROOT / "config/sfjm.yaml").read_text(encoding="utf-8")) or {}
except Exception as exc: fail(f"config/sfjm.yaml: YAML inválido: {exc}"); sfjm = {}
spec, model = sfjm.get("spec", {}), sfjm.get("spec", {}).get("transition_model", {})
expected_upstream = {"repository": UPSTREAM_REPOSITORY, "ref": UPSTREAM_REF, "protocol_path": UPSTREAM_PATH, "protocol_blob_sha": UPSTREAM_BLOB, "local_copy": UPSTREAM_LOCAL_COPY, "evidence": UPSTREAM_EVIDENCE, "local_copy_encoding": "gzip_base64"}
for key, expected in expected_upstream.items():
    if spec.get("upstream", {}).get(key) != expected: fail(f"config/sfjm.yaml: âncora upstream incorreta para {key}")
if spec.get("read_order") != EXPECTED_READ_ORDER: fail("config/sfjm.yaml: ordem mínima divergente")
for key, expected in {"next_action_id": NEXT_ACTION_ID, "state_source": "github_live", "versioned_state": "policy_not_volatile_snapshot", "workflow_attempt_selection": "latest_attempt_for_exact_head", "documentary_gate_evidence": "exact_head_bound_external_evidence", "lifecycle_gate_evidence": "exact_head_and_base_bound_external_evidence", "authorization_evidence": "exact_head_and_base_bound_external_evidence", "merge_authorization_ordering": "granted_after_ready_transition", "post_merge_verification_evidence": "exact_merge_commit_and_main_external_evidence", "execute_only_first_applicable_transition": True}.items():
    if model.get(key) != expected: fail(f"config/sfjm.yaml: transition_model incorreto para {key}")
if model.get("transitions") != EXPECTED_TRANSITIONS: fail("config/sfjm.yaml: máquina de transição divergente")
for invariant in ("published_transition_table_matches_manifest", "merge_authorization_must_postdate_ready_transition", "head_drift_invalidates_all_gates_and_authorizations", "base_drift_invalidates_lifecycle_gate_and_transition_authorizations", "only_passing_gates_allow_ready_or_merge", "terminal_pull_request_states_are_calculable", "latest_canonical_workflow_attempt_is_authoritative", "workflow_checks_out_exact_pull_request_head", "workflow_semantics_are_structurally_validated", "repeated_validation_ignores_generated_bytecode", "live_state_must_be_resolved_not_versioned_as_snapshot", "same_head_gate_progression_requires_no_intermediate_commit", "durable_records_not_rewritten_for_same_head_lifecycle"):
    if spec.get("invariants", {}).get(invariant) is not True: fail(f"config/sfjm.yaml: invariante ausente: {invariant}")
for path in NEXT_ACTION_DOCUMENTS:
    observed = extract_next_action_id(read(path), path)
    if observed and observed != NEXT_ACTION_ID: fail(f"{path}: Next action ID divergente")
for path in DERIVED_SUMMARY_DOCUMENTS:
    summaries = re.findall(r"(?m)^- Resumo derivado: (.+?)\s*$", read(path))
    if summaries != [DERIVED_SUMMARY]: fail(f"{path}: resumo derivado divergente")
if extract_transition_table(read("docs/NEXT_SAFE_ACTION.md")) != EXPECTED_TRANSITIONS: fail("docs/NEXT_SAFE_ACTION.md: tabela publicada diverge do manifesto")
blocked, agents, adr = read("docs/BLOCKED_ACTIONS.md"), read("AGENTS.md"), read("docs/decisions/ADR-0002-adopt-sfjm-operational-bootstrap.md")
if "não atualizar os registros versionados apenas por conclusão de gate" not in blocked.lower(): fail("docs/BLOCKED_ACTIONS.md: regra antíloop ausente")
if "merge só aceita autorização concedida depois de Ready" not in agents: fail("AGENTS.md: ordem Ready/merge ausente")
if "Mudanças de estado exigem atualização dos registros aplicáveis" in adr: fail("ADR-0002: obrigação volátil de reescrita ainda presente")
workflow_text = read(".github/workflows/validate-agent-framework.yml"); validate_workflow_semantics(workflow_text)
for path in ("README.md", ".github/pull_request_template.md", ".github/workflows/validate-agent-framework.yml"):
    if TEST_COMMAND not in read(path): fail(f"{path}: testes adversariais ausentes")
if extract_numbered_paths(read("bootstrap/BOOTSTRAP_CANONICO.md"), "## Ordem mínima de leitura", "bootstrap/BOOTSTRAP_CANONICO.md") != EXPECTED_READ_ORDER[1:]: fail("bootstrap: ordem divergente")
if extract_numbered_paths(read("handoffs/CURRENT.md"), "## Ordem de continuidade", "handoffs/CURRENT.md") != EXPECTED_READ_ORDER: fail("handoff: ordem divergente")
copy_path, evidence_path = ROOT / UPSTREAM_LOCAL_COPY, ROOT / UPSTREAM_EVIDENCE
if not copy_path.is_file(): fail(f"{UPSTREAM_LOCAL_COPY}: ausente")
if not evidence_path.is_file(): fail(f"{UPSTREAM_EVIDENCE}: ausente")
if copy_path.is_file():
    try:
        data = gzip.decompress(base64.b64decode("".join(copy_path.read_text(encoding="utf-8").split()), validate=True))
        if git_blob_sha(data) != UPSTREAM_BLOB: fail(f"{UPSTREAM_LOCAL_COPY}: blob divergente")
        if len(data) != UPSTREAM_SIZE: fail(f"{UPSTREAM_LOCAL_COPY}: tamanho divergente")
    except Exception as exc: fail(f"{UPSTREAM_LOCAL_COPY}: inválida: {exc}")
if evidence_path.is_file():
    evidence = evidence_path.read_text(encoding="utf-8")
    for label, expected in EXPECTED_EVIDENCE_FIELDS.items():
        observed = extract_evidence_field(evidence, label)
        if observed is not None and observed != expected: fail(f"{UPSTREAM_EVIDENCE}: campo {label} divergente")
    sizes = re.findall(r"(?m)^- Tamanho do conteúdo decodificado: (.+?)\s*$", evidence)
    if len(sizes) != 1 or not re.fullmatch(r"`7960` bytes UTF-8", sizes[0]): fail(f"{UPSTREAM_EVIDENCE}: tamanho declarado inválido")
if errors:
    print("VALIDATION FAILED")
    for item in errors: print(f"- {item}")
    sys.exit(1)
print("VALIDATION PASSED: máquina, última tentativa de CI, workflow estrutural, autorizações, evidência e registros SFJM estão sincronizados.")
