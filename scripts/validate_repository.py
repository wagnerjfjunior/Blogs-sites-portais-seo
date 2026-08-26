from pathlib import Path
import hashlib
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
TEST_COMMAND = 'python -m unittest discover -s tests -p "test_*.py"'
READ_ORDER = [
    "bootstrap/BOOTSTRAP_CANONICO.md",
    "handoffs/CURRENT.md",
    "docs/PROJECT_STATUS.md",
    "docs/NEXT_SAFE_ACTION.md",
    "docs/BLOCKED_ACTIONS.md",
    "config/project.yaml",
    "config/specialists.yaml",
]
TRANSITIONS = [
    {"id": "verify_merged_main", "when": "pull_request_is_merged_and_main_verification_is_absent", "action": "verify_merge_commit_and_main_then_record_external_evidence"},
    {"id": "report_completed_lifecycle", "when": "pull_request_is_merged_and_main_verification_is_present", "action": "report_lifecycle_complete_without_mutation"},
    {"id": "report_closed_unmerged", "when": "pull_request_is_closed_and_not_merged", "action": "report_closed_unmerged_and_require_explicit_reopen_or_abandon_decision"},
    {"id": "stop_on_drift_or_material_finding", "when": "open_pull_request_has_head_or_base_drift_or_material_unresolved_finding", "action": "stop_and_reconcile_under_explicit_authorization"},
    {"id": "require_successful_workflow", "when": "latest_canonical_workflow_attempt_for_exact_head_is_not_completed_success", "action": "wait_or_rerun_only_if_authorized"},
    {"id": "run_documentation_audit_read_only", "when": "latest_canonical_workflow_attempt_for_exact_head_is_completed_success_and_no_current_documentation_audit_gate", "action": "execute_documentary_gate_without_mutation"},
    {"id": "stop_on_documentation_audit_block", "when": "current_documentation_audit_gate_verdict_is_block", "action": "stop_and_require_material_remediation_authorization"},
    {"id": "stop_on_documentation_audit_inconclusive", "when": "current_documentation_audit_gate_verdict_is_inconclusive", "action": "stop_and_require_missing_evidence_or_access"},
    {"id": "run_lifecycle_governance_read_only", "when": "current_documentation_audit_gate_verdict_is_passing_and_no_current_lifecycle_governance_gate", "action": "execute_lifecycle_gate_without_mutation"},
    {"id": "stop_on_lifecycle_governance_block", "when": "current_lifecycle_governance_gate_verdict_is_block", "action": "stop_and_require_material_remediation_authorization"},
    {"id": "stop_on_lifecycle_governance_inconclusive", "when": "current_lifecycle_governance_gate_verdict_is_inconclusive", "action": "stop_and_require_missing_evidence_or_access"},
    {"id": "require_ready_authorization", "when": "current_documentation_and_lifecycle_gates_are_passing_pull_request_is_draft_and_exact_head_and_base_ready_authorization_is_absent", "action": "require_explicit_ready_authorization_for_exact_head_and_base"},
    {"id": "execute_ready_transition", "when": "current_documentation_and_lifecycle_gates_are_passing_pull_request_is_draft_and_exact_head_and_base_ready_authorization_is_present", "action": "mark_pull_request_ready_only"},
    {"id": "recheck_ready_reviews", "when": "current_documentation_and_lifecycle_gates_are_passing_pull_request_is_ready_and_review_state_changed_since_latest_eligible_gate_or_recheck", "action": "adjudicate_material_findings_before_merge"},
    {"id": "require_merge_authorization", "when": "current_documentation_and_lifecycle_gates_are_passing_pull_request_is_ready_review_state_is_current_no_material_threads_remain_and_post_ready_exact_head_and_base_merge_authorization_is_absent", "action": "require_explicit_post_ready_merge_authorization_for_exact_head_and_base"},
    {"id": "execute_merge_and_verify_main", "when": "current_documentation_and_lifecycle_gates_are_passing_pull_request_is_ready_review_state_is_current_no_material_threads_remain_and_post_ready_exact_head_and_base_merge_authorization_is_present", "action": "merge_exact_head_then_verify_merge_commit_and_main_without_propagating_authority"},
]
EXPECTED_ADOPTED = {
    "documentation_audit": "documentation-auditor",
    "architecture": "software-systems-architect",
    "ux_ui": "ux-ui-app-specialist",
    "application_security": "application-security-assurance-specialist",
    "seo_strategy": "seo-strategy-governance-specialist",
    "technical_seo": "technical-seo-specialist",
    "content_semantic_seo": "content-semantic-seo-specialist",
    "seo_analytics_growth": "seo-analytics-growth-specialist",
    "paid_search_sem": "paid-search-sem-specialist",
}
errors = []


def fail(message):
    errors.append(message)


def load(path):
    try:
        return yaml.safe_load((ROOT / path).read_text(encoding="utf-8")) or {}
    except Exception as exc:
        fail(f"{path}: leitura/YAML falhou: {exc}")
        return {}


def read(path):
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"{path}: leitura falhou: {exc}")
        return ""


def require_file(path, context):
    if not path or not (ROOT / path).is_file():
        fail(f"{context}: arquivo legado ausente: {path}")
        return False
    return True


def numbered_paths(text, heading, path):
    match = re.search(rf"(?ms)^{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s|\Z)", text)
    if not match:
        fail(f"{path}: seção ausente: {heading}")
        return []
    result = []
    for line in match.group("body").splitlines():
        item = re.match(r"^\s*\d+\.\s+`([^`]+)`\s*$", line)
        if item:
            result.append(item.group(1))
        elif re.match(r"^\s*\d+\.\s+", line):
            fail(f"{path}: item numerado malformado: {line.strip()}")
    return result


def table_transitions(text):
    result = []
    for line in text.splitlines():
        row = re.fullmatch(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", line.strip())
        if row:
            result.append({"id": row.group(1), "when": row.group(2), "action": row.group(3)})
    return result


project = load("config/project.yaml")
if project.get("metadata", {}).get("id") != "blogs-sites-portais-seo":
    fail("ID técnico incorreto")
spec = project.get("spec", {})
if spec.get("specialist_adoption") != "config/specialists.yaml":
    fail("config/project.yaml: specialist_adoption incorreto")
if spec.get("legacy_gpt_registry") != "config/gpts.yaml":
    fail("config/project.yaml: legacy_gpt_registry ausente")
if spec.get("actions", {}).get("mutation_actions_enabled") is not False:
    fail("Actions mutáveis devem permanecer desabilitadas")
if spec.get("policies", {}).get("new_specialist_routing_uses_role_to_archetype") is not True:
    fail("política ROLE -> ARCHETYPE_ID ausente")
if spec.get("policies", {}).get("legacy_gpt_labels_are_continuity_only") is not True:
    fail("política de identidade legada ausente")

adoption = load("config/specialists.yaml")
observed = {
    item.get("role"): item.get("archetype_id")
    for item in adoption.get("spec", {}).get("adopted_roles", [])
    if item.get("adoption_status") == "ADOPTED"
}
if observed != EXPECTED_ADOPTED:
    fail(f"config/specialists.yaml: mapa adotado divergente: {observed}")
legacy = adoption.get("spec", {}).get("legacy_registry", {})
if legacy.get("path") != "config/gpts.yaml" or legacy.get("routing_authority") is not False:
    fail("config/specialists.yaml: legacy registry não está fail-closed para routing")
builder_policy = adoption.get("spec", {}).get("builder_policy", {})
if builder_policy.get("external_builder_mutation_in_this_migration") is not False:
    fail("config/specialists.yaml: Builder externo não pode ser alterado por esta migração")
if builder_policy.get("status_manifest") != "config/builder/legacy-status.yaml":
    fail("config/specialists.yaml: status manifest de Builder legado ausente")

legacy_registry = load("config/gpts.yaml")
legacy_agents = legacy_registry.get("spec", {}).get("agents", [])
legacy_ids = [item.get("id") for item in legacy_agents]
if legacy_ids != [f"gpt{i}" for i in range(9)]:
    fail("config/gpts.yaml: artefatos legados devem permanecer addressable")

# Preserve integrity of legacy Builder evidence without making it current routing authority.
for agent in legacy_agents:
    aid = agent.get("id", "unknown")
    for key in ("skill", "canonical_document", "builder_manifest", "builder_instructions", "acceptance_tests"):
        require_file(agent.get(key), f"{aid}/{key}")
    ext_id = agent.get("external_gpt_id")
    ext_url = agent.get("external_gpt_url")
    if not re.fullmatch(r"g-[0-9a-f]{32}", ext_id or ""):
        fail(f"{aid}: external_gpt_id legado inválido")
    if not ext_url or ext_id not in ext_url:
        fail(f"{aid}: external_gpt_url legado não corresponde ao ID")
    manifest_path = agent.get("builder_manifest")
    if manifest_path and (ROOT / manifest_path).is_file():
        manifest = load(manifest_path)
        m_spec = manifest.get("spec", {})
        if m_spec.get("external_gpt_id") != ext_id or m_spec.get("external_gpt_url") != ext_url:
            fail(f"{aid}: Builder manifest diverge do registry legado")
        if m_spec.get("action_profile") != "github_read_only":
            fail(f"{aid}: Builder legado perdeu action_profile READ_ONLY")
        if m_spec.get("instructions_file") != agent.get("builder_instructions"):
            fail(f"{aid}: Instructions divergentes entre registry e Builder manifest")
        instructions = m_spec.get("instructions_file")
        if instructions and (ROOT / instructions).is_file():
            digest = hashlib.sha256((ROOT / instructions).read_bytes()).hexdigest()
            if digest != m_spec.get("instructions_sha256"):
                fail(f"{aid}: hash das Instructions legadas divergente")

legacy_builder_status = load("config/builder/legacy-status.yaml")
if legacy_builder_status.get("spec", {}).get("external_mutation_executed") is not False:
    fail("config/builder/legacy-status.yaml: não pode declarar mutação externa executada")
status_ids = [item.get("legacy_id") for item in legacy_builder_status.get("spec", {}).get("builders", [])]
if status_ids != [f"gpt{i}" for i in range(9)]:
    fail("config/builder/legacy-status.yaml: cobertura dos Builders legados incompleta")

sfjm = load("config/sfjm.yaml")
sfjm_spec = sfjm.get("spec", {})
if sfjm_spec.get("read_order") != READ_ORDER:
    fail("config/sfjm.yaml: ordem mínima divergente")
if sfjm_spec.get("transition_model", {}).get("transitions") != TRANSITIONS:
    fail("config/sfjm.yaml: máquina de transição divergente")
roles = sfjm_spec.get("roles", {})
if roles.get("documentary_gate", {}).get("archetype_id") != "documentation-auditor":
    fail("config/sfjm.yaml: documentary gate não usa Documentation Auditor")
if roles.get("lifecycle_gate", {}).get("owner") != "PROJECT_SFJM_GOVERNANCE":
    fail("config/sfjm.yaml: lifecycle gate deve permanecer project-local")
if roles.get("specialist_adoption") != "config/specialists.yaml":
    fail("config/sfjm.yaml: specialist adoption locator incorreto")

bootstrap = read("bootstrap/BOOTSTRAP_CANONICO.md")
handoff = read("handoffs/CURRENT.md")
if numbered_paths(bootstrap, "## Ordem mínima de leitura", "bootstrap/BOOTSTRAP_CANONICO.md") != READ_ORDER[1:]:
    fail("bootstrap: ordem mínima divergente")
if numbered_paths(handoff, "## Ordem de continuidade", "handoffs/CURRENT.md") != READ_ORDER:
    fail("handoff: ordem de continuidade divergente")
if table_transitions(read("docs/NEXT_SAFE_ACTION.md")) != TRANSITIONS:
    fail("docs/NEXT_SAFE_ACTION.md: tabela publicada diverge do manifesto")

for path in ["README.md", "AGENTS.md", "bootstrap/BOOTSTRAP_CANONICO.md", "handoffs/CURRENT.md", "docs/PROJECT_STATUS.md"]:
    text = read(path)
    if "config/specialists.yaml" not in text:
        fail(f"{path}: referência a config/specialists.yaml ausente")

workflow = load(".github/workflows/validate-agent-framework.yml")
steps = workflow.get("jobs", {}).get("validate", {}).get("steps", [])
by_name = {item.get("name"): item for item in steps if isinstance(item, dict)}
pr_checkout = by_name.get("Checkout exact pull request head", {})
if pr_checkout.get("with", {}).get("ref") != "${{ github.event.pull_request.head.sha }}":
    fail("workflow: ref do checkout PR incorreto")
if by_name.get("Validate canonical framework", {}).get("run") != "python scripts/validate_repository.py":
    fail("workflow: validador canônico incorreto")
if by_name.get("Run SFJM adversarial tests", {}).get("run") != TEST_COMMAND:
    fail("workflow: comando de testes incorreto")
if by_name.get("Validate legacy Builder Action compatibility", {}).get("run") != "python scripts/validate_builder_action.py":
    fail("workflow: validação de Builder legado ausente")

builder_plan = read("docs/migrations/LEGACY_BUILDER_MIGRATION_PLAN.md")
for required in [
    "ADOPTION != BUILDER_RETIREMENT",
    "RENAME != BEHAVIORAL_EQUIVALENCE",
    "NO_EXTERNAL_BUILDER_MUTATION_IN_THIS_PR",
]:
    if required not in builder_plan:
        fail(f"Builder migration plan: invariante ausente: {required}")

if errors:
    print("VALIDATION FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("VALIDATION PASSED: SES role/archetype adoption, SFJM lifecycle, legacy Builder integrity and migration boundaries are coherent.")
