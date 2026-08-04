from pathlib import Path
import hashlib, re, yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_NAME = "Ecossistema de Blogs, Sites, Portais e SEO"
EXPECTED_ID = "blogs-sites-portais-seo"
EXPECTED_REPO = "wagnerjfjunior/Blogs-sites-portais-seo"
VERDICTS = ["PASS", "PASS_WITH_RESIDUAL_RISK", "BLOCK", "INCONCLUSIVE"]

def load(path):
    p = ROOT / path
    assert p.is_file(), f"missing: {path}"
    return yaml.safe_load(p.read_text(encoding="utf-8"))

project = load("config/project.yaml")
registry = load("config/gpts.yaml")
assert project["metadata"]["id"] == EXPECTED_ID
assert project["metadata"]["public_name"] == EXPECTED_NAME
assert project["metadata"]["repository"] == EXPECTED_REPO
assert project["spec"]["verdicts"] == VERDICTS
agents = registry["spec"]["agents"]
assert len(agents) == 9
assert [a["id"] for a in agents] == [f"gpt{i}" for i in range(9)]
assert len({a["slug"] for a in agents}) == 9
assert len({a["external_gpt_id"] for a in agents}) == 9
assert len({a["external_gpt_url"] for a in agents}) == 9

for a in agents:
    assert re.fullmatch(r"g-[0-9a-f]{32}", a["external_gpt_id"])
    assert a["external_gpt_id"] in a["external_gpt_url"]
    for key in ["skill", "canonical_document", "builder_manifest", "builder_instructions", "acceptance_suite"]:
        assert (ROOT / a[key]).is_file(), f"missing reference: {a[key]}"
    manifest = load(a["builder_manifest"])
    instructions = (ROOT / a["builder_instructions"]).read_text(encoding="utf-8").strip()
    assert manifest["spec"]["instructions_sha256"] == hashlib.sha256(instructions.encode()).hexdigest()
    assert manifest["spec"]["sharing_level"] == "owner_only"
    assert len(load(a["acceptance_suite"])["cases"]) >= 6
    contract = (ROOT / a["canonical_document"]).read_text(encoding="utf-8")
    skill = (ROOT / a["skill"]).read_text(encoding="utf-8")
    for section in ["Ferramentas permitidas", "Política de evidências", "Política de mutação", "Vereditos", "Handoff"]:
        assert section in contract, f"{a['id']} contract missing {section}"
    for section in ["Quando usar", "Quando não usar", "Pré-condições", "Condições de parada", "Handoff"]:
        assert section in skill, f"{a['id']} skill missing {section}"

action = load("config/actions/github-read-only.openapi.yaml")
assert action["openapi"] == "3.1.0"
assert action["servers"] == [{"url": "https://api.github.com", "description": "GitHub REST API"}]
assert len(action["paths"]) >= 20
for path, item in action["paths"].items():
    assert EXPECTED_REPO in path or path == "/user", path
    assert set(item) == {"get"}, f"non-GET method: {path}"
    assert item["get"]["x-openai-isConsequential"] is False

action_text = (ROOT / "config/actions/github-read-only.openapi.yaml").read_text(encoding="utf-8").lower()
assert "petstore.swagger.io" not in action_text
for forbidden in ["sfjm", "SFJM.md", "config/sfjm.yaml"]:
    assert not (ROOT / forbidden).exists(), forbidden

print("VALIDATION PASSED: 9 GPTs; contracts, skills, Builder manifests, Instructions, tests and READ_ONLY Action coherent; SFJM absent.")
