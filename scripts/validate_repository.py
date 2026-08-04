from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(message):
    errors.append(message)

def load(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: YAML inválido: {exc}")
        return {}

project = load(ROOT / "config/project.yaml")
if project.get("metadata", {}).get("id") != "blogs-sites-portais-seo":
    fail("ID técnico incorreto")
if project.get("metadata", {}).get("name") != "Ecossistema de Blogs, Sites, Portais e SEO":
    fail("Nome público incorreto")
sfjm = project.get("spec", {}).get("sfjm", {})
if sfjm.get("status") != "deferred" or sfjm.get("authorized") is not False:
    fail("SFJM deve permanecer adiado e não autorizado")

registry = load(ROOT / "config/gpts.yaml")
agents = registry.get("spec", {}).get("agents", [])
if len(agents) != 9:
    fail(f"Esperados 9 GPTs; encontrados {len(agents)}")

for agent in agents:
    if agent.get("visibility") != "private" or agent.get("audience") != "owner_only":
        fail(f"{agent.get('id')}: privacidade incorreta")
    for key in ("skill", "canonical_document"):
        path = ROOT / agent[key]
        if not path.is_file():
            fail(f"Arquivo ausente: {agent[key]}")
    skill = ROOT / agent["skill"]
    if skill.is_file() and not re.match(r"\A---\n.*?\n---\n", skill.read_text(encoding="utf-8"), re.S):
        fail(f"{agent['id']}: frontmatter da skill inválido")

for forbidden in ("sfjm", "SFJM.md", "config/sfjm.yaml"):
    if (ROOT / forbidden).exists():
        fail(f"SFJM fora de escopo encontrado: {forbidden}")

if errors:
    print("VALIDATION FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("VALIDATION PASSED: 9 GPTs, 9 skills, 9 contratos canônicos; SFJM ausente.")
