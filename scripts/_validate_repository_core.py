from pathlib import Path
import hashlib
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

EXPECTED_NAMES = {
    "gpt0": "GPT0 — SEO - Auditor documental",
    "gpt1": "GPT1 — SEO - Arquiteto do ecossistema",
    "gpt2": "GPT2 — SEO - Pesquisa de mercado e palavras-chave",
    "gpt3": "GPT3 — SEO técnico",
    "gpt4": "GPT4 — SEO - GitHub, lifecycle e publicação",
    "gpt5": "GPT5 — SEO - Conteúdo e autoridade temática",
    "gpt6": "GPT6 — SEO - Link building e digital PR, DA e DR",
    "gpt7": "GPT7 — SEO - Monetização",
    "gpt8": "GPT8 — SEO - Analytics e crescimento",
}
EXPECTED_VERDICTS = ["PASS", "PASS_WITH_RESIDUAL_RISK", "BLOCK", "INCONCLUSIVE"]
CONTRACT_SECTIONS = [
    "## Missão", "## Escopo autorizado", "## Escopo proibido",
    "## Entradas obrigatórias", "## Ferramentas permitidas",
    "## Ferramentas proibidas", "## Procedimento",
    "## Evidências obrigatórias", "## Formato de saída",
    "## Vereditos e critérios", "## Política de mutação",
    "## Dados ausentes e acesso insuficiente",
    "## Política contra overclaim", "## Handoffs",
    "## Registros canônicos",
]
SKILL_SECTIONS = [
    "## Quando usar", "## Quando não usar", "## Pré-condições",
    "## Entradas", "## Procedimento", "## Validações",
    "## Condições de parada", "## Saída", "## Restrições",
    "## Handoff", "## Referências canônicas",
]
SFJM_DOCUMENTS = {
    "bootstrap": "bootstrap/BOOTSTRAP_CANONICO.md",
    "current_handoff": "handoffs/CURRENT.md",
    "project_status": "docs/PROJECT_STATUS.md",
    "next_safe_action": "docs/NEXT_SAFE_ACTION.md",
    "blocked_actions": "docs/BLOCKED_ACTIONS.md",
    "continuity_policy": "docs/governance/sfjm-continuity-policy.md",
}
SFJM_READ_ORDER = [
    "bootstrap/BOOTSTRAP_CANONICO.md",
    "handoffs/CURRENT.md",
    "docs/PROJECT_STATUS.md",
    "docs/NEXT_SAFE_ACTION.md",
    "docs/BLOCKED_ACTIONS.md",
    "config/project.yaml",
    "config/gpts.yaml",
]
SFJM_TRUE_INVARIANTS = {
    "exactly_one_authoritative_next_safe_action",
    "summaries_are_derived",
    "material_divergence_requires_stop",
    "missing_information_must_not_be_inferred",
    "authorization_does_not_propagate",
    "direct_main_writes_forbidden",
    "ready_and_merge_require_separate_authorizations",
    "head_drift_invalidates_gates",
    "evidence_must_identify_source_and_revision",
}


def fail(message):
    errors.append(message)


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: leitura falhou: {exc}")
        return ""


def load(path):
    try:
        return yaml.safe_load(read(path)) or {}
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: YAML inválido: {exc}")
        return {}


def require_file(relative_path):
    path = ROOT / relative_path
    if not path.is_file():
        fail(f"Arquivo obrigatório ausente: {relative_path}")
    return path


project = load(ROOT / "config/project.yaml")
if project.get("metadata", {}).get("id") != "blogs-sites-portais-seo":
    fail("ID técnico incorreto")
if project.get("metadata", {}).get("name") != "Ecossistema de Blogs, Sites, Portais e SEO":
    fail("Nome público incorreto")
project_spec = project.get("spec", {})
if project_spec.get("canonical_repository") != "wagnerjfjunior/Blogs-sites-portais-seo":
    fail("Repositório canônico incorreto")
if project_spec.get("actions", {}).get("mutation_actions_enabled") is not False:
    fail("Actions mutáveis devem permanecer desabilitadas")
project_policies = project_spec.get("policies", {})
if project_policies.get("missing_information_must_not_be_inferred") is not True:
    fail("Política de não inferência ausente")
if project_policies.get("exactly_one_authoritative_next_safe_action") is not True:
    fail("Política de próxima ação única ausente")
if project_policies.get("next_safe_action_path") != "docs/NEXT_SAFE_ACTION.md":
    fail("Caminho autoritativo da próxima ação incorreto")
project_sfjm = project_spec.get("sfjm", {})
expected_project_sfjm = {"manifest": "config/sfjm.yaml", **SFJM_DOCUMENTS}
for key, expected in expected_project_sfjm.items():
    if project_sfjm.get(key) != expected:
        fail(f"config/project.yaml: referência SFJM incorreta para {key}")

registry = load(ROOT / "config/gpts.yaml")
if registry.get("spec", {}).get("verdicts") != EXPECTED_VERDICTS:
    fail("Taxonomia de vereditos incorreta")
agents = registry.get("spec", {}).get("agents", [])
if len(agents) != 9:
    fail(f"Esperados 9 GPTs; encontrados {len(agents)}")

ids, slugs, ext_ids, urls = set(), set(), set(), set()
for agent in agents:
    aid = agent.get("id")
    if aid in ids:
        fail(f"ID duplicado: {aid}")
    ids.add(aid)
    if agent.get("name") != EXPECTED_NAMES.get(aid):
        fail(f"{aid}: nome público incorreto")
    slug = agent.get("slug")
    if slug in slugs:
        fail(f"Slug duplicado: {slug}")
    slugs.add(slug)
    ext = agent.get("external_gpt_id")
    url = agent.get("external_gpt_url")
    if not re.fullmatch(r"g-[0-9a-f]{32}", ext or ""):
        fail(f"{aid}: external_gpt_id inválido")
    if ext in ext_ids:
        fail(f"{aid}: external_gpt_id duplicado")
    ext_ids.add(ext)
    if not url or ext not in url:
        fail(f"{aid}: external_gpt_url não corresponde ao ID")
    if url in urls:
        fail(f"{aid}: external_gpt_url duplicada")
    urls.add(url)
    if agent.get("visibility") != "private" or agent.get("audience") != "owner_only":
        fail(f"{aid}: privacidade declarada incorreta")
    for key in ("skill", "canonical_document", "builder_manifest", "builder_instructions", "acceptance_tests"):
        value = agent.get(key)
        if not value or not (ROOT / value).is_file():
            fail(f"{aid}: arquivo ausente para {key}: {value}")

    contract_path = ROOT / agent.get("canonical_document", "")
    contract = read(contract_path)
    for section in CONTRACT_SECTIONS:
        if section not in contract:
            fail(f"{aid}: contrato sem seção {section}")

    skill_path = ROOT / agent.get("skill", "")
    skill_text = read(skill_path)
    if not re.match(r"\A---\n.*?\n---\n", skill_text, re.S):
        fail(f"{aid}: frontmatter da skill inválido")
    else:
        skill_data = yaml.safe_load(skill_text.split("---", 2)[1]) or {}
        if skill_data.get("name") != slug:
            fail(f"{aid}: name da skill não corresponde ao slug")
    for section in SKILL_SECTIONS:
        if section not in skill_text:
            fail(f"{aid}: skill sem seção {section}")

    builder_path = ROOT / agent.get("builder_manifest", "")
    builder = load(builder_path)
    spec = builder.get("spec", {})
    if spec.get("sharing_level") != "owner_only":
        fail(f"{aid}: sharing_level do Builder incorreto")
    if spec.get("action_profile") != "github_read_only":
        fail(f"{aid}: action_profile incorreto")
    instructions_file = spec.get("instructions_file")
    if instructions_file != agent.get("builder_instructions"):
        fail(f"{aid}: Instructions divergentes entre registro e manifesto")
    if instructions_file and (ROOT / instructions_file).is_file():
        digest = hashlib.sha256((ROOT / instructions_file).read_bytes()).hexdigest()
        if digest != spec.get("instructions_sha256"):
            fail(f"{aid}: hash das Instructions divergente")

    tests = load(ROOT / agent.get("acceptance_tests", ""))
    cases = tests.get("spec", {}).get("cases", [])
    if len(cases) < 8:
        fail(f"{aid}: suíte de aceitação incompleta")
    case_ids = {case.get("id") for case in cases}
    required_cases = {
        "identity", "authorized-task", "forbidden-task", "missing-evidence",
        "overclaim", "mutation", "handoff", "source-version",
    }
    if not required_cases.issubset(case_ids):
        fail(f"{aid}: casos obrigatórios ausentes")

action_path = ROOT / "config/actions/github-read-only.openapi.yaml"
action = load(action_path)
if action.get("openapi") != "3.1.0":
    fail("OpenAPI deve ser 3.1.0")
servers = action.get("servers", [])
if servers != [{"url": "https://api.github.com", "description": "GitHub REST API"}]:
    fail("Servidor da Action incorreto")
operation_ids = set()
for path, operations in action.get("paths", {}).items():
    if "/repos/wagnerjfjunior/Blogs-sites-portais-seo" not in path and path != "/user":
        fail(f"Path fora do repositório autorizado: {path}")
    for method, operation in operations.items():
        if method.lower() != "get":
            fail(f"Método mutável encontrado: {method.upper()} {path}")
        if operation.get("x-openai-isConsequential") is not False:
            fail(f"Operação não marcada como não consequencial: {path}")
        operation_id = operation.get("operationId")
        if not operation_id or operation_id in operation_ids:
            fail(f"operationId ausente ou duplicado: {operation_id}")
        operation_ids.add(operation_id)

sfjm = load(ROOT / "config/sfjm.yaml")
if sfjm.get("kind") != "SFJMContinuity":
    fail("config/sfjm.yaml: kind incorreto")
if sfjm.get("metadata", {}).get("project_id") != "blogs-sites-portais-seo":
    fail("config/sfjm.yaml: project_id incorreto")
if sfjm.get("metadata", {}).get("mode") != "operational":
    fail("config/sfjm.yaml: somente o modo operacional é permitido")
sfjm_spec = sfjm.get("spec", {})
upstream = sfjm_spec.get("upstream", {})
if upstream.get("repository") != "wagnerjfjunior/StopJuniorMode":
    fail("config/sfjm.yaml: repositório upstream incorreto")
if upstream.get("ref") != "d03d477c3b329aa973a38ec4e949c249fa017929":
    fail("config/sfjm.yaml: revisão upstream não congelada")
if upstream.get("protocol_path") != "docs/CANONICAL_BOOTSTRAP_PROTOCOL.md":
    fail("config/sfjm.yaml: caminho do protocolo incorreto")
if upstream.get("protocol_blob_sha") != "7befd02533aad6c2df5544c7307e4a66dce28844":
    fail("config/sfjm.yaml: blob do protocolo incorreto")
canonical = sfjm_spec.get("canonical_source", {})
if canonical.get("repository") != "wagnerjfjunior/Blogs-sites-portais-seo":
    fail("config/sfjm.yaml: fonte canônica incorreta")
if canonical.get("branch") != "main":
    fail("config/sfjm.yaml: branch canônica incorreta")
if sfjm_spec.get("documents") != SFJM_DOCUMENTS:
    fail("config/sfjm.yaml: mapa de documentos SFJM incorreto")
if sfjm_spec.get("read_order") != SFJM_READ_ORDER:
    fail("config/sfjm.yaml: ordem mínima de leitura incorreta")
for name in SFJM_TRUE_INVARIANTS:
    if sfjm_spec.get("invariants", {}).get(name) is not True:
        fail(f"config/sfjm.yaml: invariante ausente ou falsa: {name}")
if sfjm_spec.get("invariants", {}).get("next_safe_action_authority") != "docs/NEXT_SAFE_ACTION.md":
    fail("config/sfjm.yaml: autoridade da próxima ação incorreta")
required_exclusions = {
    "experimental_scoring", "benchmark_adjudication", "synthetic_scenarios",
    "autonomous_external_mutation", "automatic_ready", "automatic_merge",
    "automatic_builder_update",
}
if not required_exclusions.issubset(set(sfjm_spec.get("excluded_capabilities", []))):
    fail("config/sfjm.yaml: exclusões operacionais incompletas")

for relative_path in ["config/sfjm.yaml", *SFJM_DOCUMENTS.values()]:
    require_file(relative_path)
require_file("docs/decisions/ADR-0002-adopt-sfjm-operational-bootstrap.md")

bootstrap_text = read(ROOT / SFJM_DOCUMENTS["bootstrap"])
handoff_text = read(ROOT / SFJM_DOCUMENTS["current_handoff"])
status_text = read(ROOT / SFJM_DOCUMENTS["project_status"])
next_text = read(ROOT / SFJM_DOCUMENTS["next_safe_action"])
blocked_text = read(ROOT / SFJM_DOCUMENTS["blocked_actions"])
policy_text = read(ROOT / SFJM_DOCUMENTS["continuity_policy"])

required_headings = {
    SFJM_DOCUMENTS["bootstrap"]: ["## Regra de canonicalidade", "## Ordem mínima de leitura", "## Próxima ação segura", "## Retomada"],
    SFJM_DOCUMENTS["current_handoff"]: ["## Estado confirmado", "## Lacunas", "## Riscos ativos", "## Próxima ação segura"],
    SFJM_DOCUMENTS["project_status"]: ["## Estado por frente", "## Decisões necessárias", "## Riscos", "## Próxima ação segura"],
    SFJM_DOCUMENTS["next_safe_action"]: ["## 1. Ação", "## 4. Pré-condições", "## 7. Autorização", "## 10. Condições de parada"],
    SFJM_DOCUMENTS["blocked_actions"]: ["## 1. Bloqueios ativos", "## 2. Ações que sempre exigem autorização explícita", "## 6. Procedimento para desbloqueio"],
    SFJM_DOCUMENTS["continuity_policy"]: ["## 2. Registros obrigatórios", "## 3. Invariantes", "## 4. Ordem de retomada", "## 7. Conflitos"],
}
texts_by_path = {
    SFJM_DOCUMENTS["bootstrap"]: bootstrap_text,
    SFJM_DOCUMENTS["current_handoff"]: handoff_text,
    SFJM_DOCUMENTS["project_status"]: status_text,
    SFJM_DOCUMENTS["next_safe_action"]: next_text,
    SFJM_DOCUMENTS["blocked_actions"]: blocked_text,
    SFJM_DOCUMENTS["continuity_policy"]: policy_text,
}
for relative_path, headings in required_headings.items():
    for heading in headings:
        if heading not in texts_by_path[relative_path]:
            fail(f"{relative_path}: seção obrigatória ausente: {heading}")

for relative_path, text in {
    SFJM_DOCUMENTS["bootstrap"]: bootstrap_text,
    SFJM_DOCUMENTS["current_handoff"]: handoff_text,
    SFJM_DOCUMENTS["project_status"]: status_text,
}.items():
    if "docs/NEXT_SAFE_ACTION.md" not in text:
        fail(f"{relative_path}: referência à próxima ação autoritativa ausente")

marker = "Este é o registro atual autoritativo da única próxima ação segura do projeto."
marker_count = sum(marker in text for text in texts_by_path.values())
if marker_count != 1 or marker not in next_text:
    fail("SFJM: deve existir exatamente um marcador de próxima ação autoritativa")
if next_text.count("## 1. Ação") != 1:
    fail("docs/NEXT_SAFE_ACTION.md: deve conter exatamente uma seção de ação")
if "ausência nesta lista não constitui autorização" not in blocked_text.lower():
    fail("docs/BLOCKED_ACTIONS.md: regra de não autorização por ausência não encontrada")
if "divergência material" not in policy_text.lower() or "parada" not in policy_text.lower():
    fail("Política SFJM: regra de conflito incompleta")
if "scoring" not in policy_text.lower() or "experimental" not in policy_text.lower():
    fail("Política SFJM: fronteira experimental não declarada")

for required_reference in (
    "bootstrap/BOOTSTRAP_CANONICO.md",
    "docs/NEXT_SAFE_ACTION.md",
    "config/sfjm.yaml",
):
    if required_reference not in read(ROOT / "README.md"):
        fail(f"README.md: referência SFJM ausente: {required_reference}")
if "bootstrap/BOOTSTRAP_CANONICO.md" not in read(ROOT / "AGENTS.md"):
    fail("AGENTS.md: ponto de entrada SFJM ausente")

for path in ROOT.rglob("*"):
    if ".git" in path.parts:
        continue
    if path.is_file():
        rel = path.relative_to(ROOT).as_posix()
        text = read(path)
        lower = text.lower()
        demo_token = "pet" + "store"
        if demo_token in lower or ("swagger " + demo_token) in lower:
            fail(f"Schema de demonstração encontrado em {rel}")
        example_repo = "wagnerjfjunior/" + "fecha.ai"
        if example_repo in lower:
            fail(f"Referência ao repositório de exemplo encontrada em {rel}")

required_governance = [
    "docs/governance/canonical-governance.md",
    "docs/governance/authorization-matrix.md",
    "docs/governance/lifecycle-policy.md",
    "docs/governance/tooling-policy.md",
    "docs/governance/builder-provisioning-policy.md",
    "docs/governance/sfjm-continuity-policy.md",
]
for item in required_governance:
    require_file(item)

if errors:
    print("VALIDATION FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(
    "VALIDATION PASSED: "
    "9 GPTs, 9 contratos, 9 skills, 9 manifests Builder, "
    "9 Instructions, 9 suítes de aceitação, Action GitHub READ_ONLY, "
    "governança e SFJM operacional com próxima ação única."
)
