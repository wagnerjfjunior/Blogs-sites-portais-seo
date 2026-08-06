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
EXPECTED_READ_ORDER = [
    "bootstrap/BOOTSTRAP_CANONICO.md",
    "handoffs/CURRENT.md",
    "docs/PROJECT_STATUS.md",
    "docs/NEXT_SAFE_ACTION.md",
    "docs/BLOCKED_ACTIONS.md",
    "config/project.yaml",
    "config/gpts.yaml",
]
EXPECTED_TRANSITIONS = [
    {
        "id": "stop_on_drift_or_material_finding",
        "when": "head_or_base_drift_or_material_unresolved_finding",
        "action": "stop_and_reconcile_under_explicit_authorization",
    },
    {
        "id": "require_successful_workflow",
        "when": "exact_head_has_no_completed_successful_canonical_workflow",
        "action": "wait_or_rerun_only_if_authorized",
    },
    {
        "id": "run_gpt0_read_only",
        "when": "exact_head_has_successful_workflow_and_no_eligible_gpt0_gate",
        "action": "execute_documentary_gate_without_mutation",
    },
    {
        "id": "run_gpt4_read_only",
        "when": "exact_head_has_eligible_gpt0_pass_and_no_eligible_gpt4_gate",
        "action": "execute_lifecycle_gate_without_mutation",
    },
    {
        "id": "require_ready_authorization",
        "when": "gates_are_current_and_pull_request_is_draft_and_exact_head_ready_authorization_is_absent",
        "action": "require_explicit_ready_authorization_for_exact_head",
    },
    {
        "id": "execute_ready_transition",
        "when": "gates_are_current_and_pull_request_is_draft_and_exact_head_ready_authorization_is_present",
        "action": "mark_pull_request_ready_only",
    },
    {
        "id": "recheck_ready_reviews",
        "when": "pull_request_is_ready_and_review_state_changed_since_latest_eligible_gate_or_recheck",
        "action": "adjudicate_material_findings_before_merge",
    },
    {
        "id": "require_merge_authorization",
        "when": "pull_request_is_ready_gates_are_current_no_material_threads_remain_and_exact_head_merge_authorization_is_absent",
        "action": "require_explicit_merge_authorization_for_exact_head",
    },
    {
        "id": "execute_merge_and_verify_main",
        "when": "pull_request_is_ready_gates_are_current_no_material_threads_remain_and_exact_head_merge_authorization_is_present",
        "action": "merge_exact_head_then_verify_main_without_propagating_authority",
    },
]
NEXT_ACTION_ID = "resolve-live-lifecycle-transition-v1"
NEXT_ACTION_DOCUMENTS = [
    "bootstrap/BOOTSTRAP_CANONICO.md",
    "handoffs/CURRENT.md",
    "docs/PROJECT_STATUS.md",
    "docs/NEXT_SAFE_ACTION.md",
    "docs/BLOCKED_ACTIONS.md",
]
UPSTREAM_REPOSITORY = "wagnerjfjunior/StopJuniorMode"
UPSTREAM_REF = "d03d477c3b329aa973a38ec4e949c249fa017929"
UPSTREAM_PATH = "docs/CANONICAL_BOOTSTRAP_PROTOCOL.md"
UPSTREAM_BLOB = "7befd02533aad6c2df5544c7307e4a66dce28844"
UPSTREAM_SIZE = 7960
UPSTREAM_LOCAL_COPY = "docs/references/sfjm/CANONICAL_BOOTSTRAP_PROTOCOL.md.gz.b64"
UPSTREAM_EVIDENCE = "docs/evidence/sfjm-upstream-anchor.md"
EXPECTED_EVIDENCE_FIELDS = {
    "Repositório upstream": UPSTREAM_REPOSITORY,
    "Revisão congelada": UPSTREAM_REF,
    "Caminho upstream": UPSTREAM_PATH,
    "Git blob SHA observado": UPSTREAM_BLOB,
    "Cópia local imutável": UPSTREAM_LOCAL_COPY,
}
errors = []


def fail(message):
    errors.append(message)


def read(relative_path):
    path = ROOT / relative_path
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"{relative_path}: leitura falhou: {exc}")
        return ""


def extract_numbered_paths(text, heading, relative_path):
    match = re.search(
        rf"(?ms)^{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s|\Z)",
        text,
    )
    if not match:
        fail(f"{relative_path}: seção de ordem ausente: {heading}")
        return []

    numbers = []
    paths = []
    for line in match.group("body").splitlines():
        numbered = re.match(r"^\s*(\d+)\.\s+(.*?)\s*$", line)
        if not numbered:
            continue
        number = int(numbered.group(1))
        payload = numbered.group(2)
        exact_path = re.fullmatch(r"`([^`]+)`", payload)
        if not exact_path:
            fail(
                f"{relative_path}: item numerado malformado em {heading}: "
                f"{line.strip()}"
            )
            continue
        numbers.append(number)
        paths.append(exact_path.group(1))

    if not paths:
        fail(f"{relative_path}: nenhuma entrada numerada encontrada em {heading}")
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        fail(
            f"{relative_path}: numeração inválida em {heading}; "
            f"encontrada={numbers}"
        )
    if len(paths) != len(set(paths)):
        fail(f"{relative_path}: ordem contém entradas duplicadas")
    return paths


def extract_next_action_id(text, relative_path):
    matches = re.findall(r"(?m)^- Next action ID: `([^`]+)`\s*$", text)
    if len(matches) != 1:
        fail(
            f"{relative_path}: deve conter exatamente um marcador "
            "'- Next action ID: `...`'"
        )
        return None
    return matches[0]


def extract_backticked_evidence_field(text, label):
    matches = re.findall(
        rf"(?m)^- {re.escape(label)}: `([^`]+)`\s*$",
        text,
    )
    if len(matches) != 1:
        fail(
            f"{UPSTREAM_EVIDENCE}: campo canônico ausente ou duplicado: {label}"
        )
        return None
    return matches[0]


def git_blob_sha(data):
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def run_core_validator():
    if not CORE.is_file():
        print("VALIDATION FAILED")
        print("- scripts/_validate_repository_core.py: validador-base ausente")
        sys.exit(1)

    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            runpy.run_path(str(CORE), run_name="__main__")
    except SystemExit as exc:
        diagnostics = output.getvalue()
        if diagnostics:
            print(diagnostics, end="")
        code = exc.code if isinstance(exc.code, int) else 1
        sys.exit(code or 1)


run_core_validator()

sfjm_path = ROOT / "config/sfjm.yaml"
try:
    sfjm = yaml.safe_load(sfjm_path.read_text(encoding="utf-8")) or {}
except Exception as exc:
    fail(f"config/sfjm.yaml: YAML inválido: {exc}")
    sfjm = {}

spec = sfjm.get("spec", {})
upstream = spec.get("upstream", {})
expected_upstream = {
    "repository": UPSTREAM_REPOSITORY,
    "ref": UPSTREAM_REF,
    "protocol_path": UPSTREAM_PATH,
    "protocol_blob_sha": UPSTREAM_BLOB,
    "local_copy": UPSTREAM_LOCAL_COPY,
    "evidence": UPSTREAM_EVIDENCE,
    "local_copy_encoding": "gzip_base64",
}
for key, expected in expected_upstream.items():
    if upstream.get(key) != expected:
        fail(f"config/sfjm.yaml: âncora upstream incorreta para {key}")

manifest_order = spec.get("read_order")
if manifest_order != EXPECTED_READ_ORDER:
    fail(
        "config/sfjm.yaml: ordem mínima divergente; "
        f"esperada={EXPECTED_READ_ORDER}; encontrada={manifest_order}"
    )

transition_model = spec.get("transition_model", {})
if transition_model.get("next_action_id") != NEXT_ACTION_ID:
    fail("config/sfjm.yaml: next_action_id incorreto")
if transition_model.get("state_source") != "github_live":
    fail("config/sfjm.yaml: estado de lifecycle deve ser resolvido live")
if transition_model.get("versioned_state") != "policy_not_volatile_snapshot":
    fail("config/sfjm.yaml: documentos versionados não devem armazenar snapshot volátil")
if transition_model.get("gate_evidence") != "head_bound_external_evidence":
    fail("config/sfjm.yaml: evidência dos gates deve ser vinculada ao head")
if transition_model.get("authorization_evidence") != "exact_head_bound_external_evidence":
    fail("config/sfjm.yaml: evidência de autorização deve ser vinculada ao head exato")
if transition_model.get("execute_only_first_applicable_transition") is not True:
    fail("config/sfjm.yaml: apenas a primeira transição aplicável pode ser executada")
if transition_model.get("transitions") != EXPECTED_TRANSITIONS:
    fail(
        "config/sfjm.yaml: máquina de transição divergente; "
        f"esperada={EXPECTED_TRANSITIONS}; encontrada={transition_model.get('transitions')}"
    )

for invariant in (
    "live_state_must_be_resolved_not_versioned_as_snapshot",
    "same_head_gate_progression_requires_no_intermediate_commit",
    "metadata_only_ready_transition_does_not_invalidate_head_bound_gates",
    "authorization_presence_advances_transition",
    "durable_records_not_rewritten_for_same_head_lifecycle",
):
    if spec.get("invariants", {}).get(invariant) is not True:
        fail(f"config/sfjm.yaml: invariante de lifecycle ausente: {invariant}")

for relative_path in NEXT_ACTION_DOCUMENTS:
    observed_action_id = extract_next_action_id(read(relative_path), relative_path)
    if observed_action_id and observed_action_id != NEXT_ACTION_ID:
        fail(
            f"{relative_path}: Next action ID divergente; "
            f"esperado={NEXT_ACTION_ID}; encontrado={observed_action_id}"
        )

blocked_text = read("docs/BLOCKED_ACTIONS.md")
if "não atualizar os registros versionados apenas por conclusão de gate" not in blocked_text.lower():
    fail("docs/BLOCKED_ACTIONS.md: regra antíloop de desbloqueio ausente")
if "Atualizar este documento e `docs/NEXT_SAFE_ACTION.md`" in blocked_text:
    fail("docs/BLOCKED_ACTIONS.md: reescrita incondicional de lifecycle ainda presente")

bootstrap_order = extract_numbered_paths(
    read("bootstrap/BOOTSTRAP_CANONICO.md"),
    "## Ordem mínima de leitura",
    "bootstrap/BOOTSTRAP_CANONICO.md",
)
expected_bootstrap_order = EXPECTED_READ_ORDER[1:]
if bootstrap_order != expected_bootstrap_order:
    fail(
        "bootstrap/BOOTSTRAP_CANONICO.md: ordem publicada diverge do manifesto; "
        f"esperada={expected_bootstrap_order}; encontrada={bootstrap_order}"
    )

handoff_order = extract_numbered_paths(
    read("handoffs/CURRENT.md"),
    "## Ordem de continuidade",
    "handoffs/CURRENT.md",
)
if handoff_order != EXPECTED_READ_ORDER:
    fail(
        "handoffs/CURRENT.md: ordem publicada diverge do manifesto; "
        f"esperada={EXPECTED_READ_ORDER}; encontrada={handoff_order}"
    )

copy_path = ROOT / UPSTREAM_LOCAL_COPY
evidence_path = ROOT / UPSTREAM_EVIDENCE
if not copy_path.is_file():
    fail(f"{UPSTREAM_LOCAL_COPY}: cópia upstream ausente")
if not evidence_path.is_file():
    fail(f"{UPSTREAM_EVIDENCE}: evidência upstream ausente")

protocol_bytes = None
if copy_path.is_file():
    try:
        encoded = "".join(copy_path.read_text(encoding="utf-8").split())
        protocol_bytes = gzip.decompress(base64.b64decode(encoded, validate=True))
        observed_blob = git_blob_sha(protocol_bytes)
        if observed_blob != UPSTREAM_BLOB:
            fail(
                f"{UPSTREAM_LOCAL_COPY}: Git blob SHA divergente; "
                f"esperado={UPSTREAM_BLOB}; encontrado={observed_blob}"
            )
        if len(protocol_bytes) != UPSTREAM_SIZE:
            fail(
                f"{UPSTREAM_LOCAL_COPY}: tamanho divergente; "
                f"esperado={UPSTREAM_SIZE}; encontrado={len(protocol_bytes)}"
            )
    except Exception as exc:
        fail(f"{UPSTREAM_LOCAL_COPY}: cópia upstream inválida: {exc}")

if evidence_path.is_file():
    evidence = evidence_path.read_text(encoding="utf-8")
    for label, expected in EXPECTED_EVIDENCE_FIELDS.items():
        observed = extract_backticked_evidence_field(evidence, label)
        if observed is not None and observed != expected:
            fail(
                f"{UPSTREAM_EVIDENCE}: campo {label} divergente; "
                f"esperado={expected}; encontrado={observed}"
            )
    size_matches = re.findall(
        r"(?m)^- Tamanho do conteúdo decodificado: `(\d+)` bytes UTF-8\s*$",
        evidence,
    )
    if len(size_matches) != 1:
        fail(f"{UPSTREAM_EVIDENCE}: campo canônico de tamanho ausente ou duplicado")
    elif int(size_matches[0]) != UPSTREAM_SIZE:
        fail(
            f"{UPSTREAM_EVIDENCE}: tamanho declarado divergente; "
            f"esperado={UPSTREAM_SIZE}; encontrado={size_matches[0]}"
        )

if errors:
    print("VALIDATION FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(
    "VALIDATION PASSED: framework canônico preservado; "
    "SFJM operacional com ordem estrita, diagnósticos preservados, "
    "transições autorizadas sem looping e evidência upstream por campos exatos."
)
