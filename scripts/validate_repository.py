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
        return yaml.safe_load(read(path))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: YAML inválido: {exc}")
        return {}

project = load(ROOT / "config/project.yaml")
if project.get("metadata", {}).get("id") != "blogs-sites-portais-seo":
    fail("ID técnico incorreto")
if project.get("metadata", {}).get("name") != "Ecossistema de Blogs, Sites, Portais e SEO":
    fail("Nome público incorreto")
if project.get("spec", {}).get("canonical_repository") != "wagnerjfjunior/Blogs-sites-portais-seo":
    fail("Repositório canônico incorreto")
if project.get("spec", {}).get("actions", {}).get("mutation_actions_enabled") is not False:
    fail("Actions mutáveis devem permanecer desabilitadas")

registry = load(ROOT / "config/gpts.yaml")
if registry.get("spec", {}).get("verdicts") != EXPECTED_VERDICTS:
    fail("Taxonomia de vereditos incorreta")
agents = registry.get("spec", {}).get("agents", [])
if len(agents) != 9:
    fail(f"Esperados 9 GPTs; encontrados {len(agents)}")

ids, slugs, ext_ids, urls, operation_paths = set(), set(), set(), set(), []
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
    skill_data = yaml.safe_load(skill_text.split("---", 2)[1])
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
    required_cases = {"identity","authorized-task","forbidden-task","missing-evidence","overclaim","mutation","handoff","source-version"}
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
    for method, op in operations.items():
        if method.lower() != "get":
            fail(f"Método mutável encontrado: {method.upper()} {path}")
        if op.get("x-openai-isConsequential") is not False:
            fail(f"Operação não marcada como não consequencial: {path}")
        operation_id = op.get("operationId")
        if not operation_id or operation_id in operation_ids:
            fail(f"operationId ausente ou duplicado: {operation_id}")
        operation_ids.add(operation_id)

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
        if rel in {"SFJM.md", "config/sfjm.yaml"} or rel.startswith("sfjm/"):
            fail(f"Artefato fora de escopo encontrado: {rel}")

required_governance = [
    "docs/governance/canonical-governance.md",
    "docs/governance/authorization-matrix.md",
    "docs/governance/lifecycle-policy.md",
    "docs/governance/tooling-policy.md",
    "docs/governance/builder-provisioning-policy.md",
]
for item in required_governance:
    if not (ROOT / item).is_file():
        fail(f"Documento de governança ausente: {item}")

if errors:
    print("VALIDATION FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(
    "VALIDATION PASSED: "
    "9 GPTs, 9 contratos, 9 skills, 9 manifests Builder, "
    "9 Instructions, 9 suítes de aceitação, Action GitHub READ_ONLY e governança."
)
