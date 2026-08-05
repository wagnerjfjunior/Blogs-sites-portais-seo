from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
ACTION_PATH = ROOT / "config/actions/github-read-only.openapi.yaml"
AUTHORIZED_REPOSITORY = "/repos/wagnerjfjunior/Blogs-sites-portais-seo"
errors = []


def fail(message):
    errors.append(message)


def contains_key(value, target):
    if isinstance(value, dict):
        return target in value or any(contains_key(item, target) for item in value.values())
    if isinstance(value, list):
        return any(contains_key(item, target) for item in value)
    return False


try:
    action = yaml.safe_load(ACTION_PATH.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"BUILDER ACTION VALIDATION FAILED\n- YAML inválido: {exc}")
    sys.exit(1)

if action.get("openapi") != "3.1.0":
    fail("OpenAPI deve ser 3.1.0")

if action.get("servers") != [{"url": "https://api.github.com", "description": "GitHub REST API"}]:
    fail("Servidor deve ser exclusivamente https://api.github.com")

components = action.get("components")
if components is not None:
    if not isinstance(components, dict):
        fail("components deve ser um objeto")
    elif not isinstance(components.get("schemas"), dict):
        fail("components.schemas deve ser um objeto quando components existir")

if contains_key(action, "$ref"):
    fail("O schema do Builder não deve usar $ref; parâmetros e respostas devem ser inline")

paths = action.get("paths")
if not isinstance(paths, dict) or not paths:
    fail("paths deve ser um objeto não vazio")
else:
    operation_ids = set()
    for path, methods in paths.items():
        if path != "/user" and AUTHORIZED_REPOSITORY not in path:
            fail(f"Path fora do repositório autorizado: {path}")
        if not isinstance(methods, dict):
            fail(f"Path sem objeto de operações: {path}")
            continue

        for method, operation in methods.items():
            if method.lower() != "get":
                fail(f"Método mutável encontrado: {method.upper()} {path}")
                continue
            if not isinstance(operation, dict):
                fail(f"Operação inválida: {method.upper()} {path}")
                continue

            operation_id = operation.get("operationId")
            if not isinstance(operation_id, str) or not operation_id:
                fail(f"operationId ausente em {path}")
            elif operation_id in operation_ids:
                fail(f"operationId duplicado: {operation_id}")
            else:
                operation_ids.add(operation_id)

            if operation.get("x-openai-isConsequential") is not False:
                fail(f"Operação não marcada como não consequencial: {operation_id}")

            parameters = operation.get("parameters", [])
            if not isinstance(parameters, list):
                fail(f"{operation_id}: parameters deve ser uma lista")
            else:
                for index, parameter in enumerate(parameters):
                    if not isinstance(parameter, dict):
                        fail(f"{operation_id}: parâmetro {index} não é um objeto")
                        continue
                    if not isinstance(parameter.get("name"), str):
                        fail(f"{operation_id}: parâmetro {index} sem name string")
                    if parameter.get("in") not in {"path", "query", "header", "cookie"}:
                        fail(f"{operation_id}: parâmetro {index} com in inválido")
                    if not isinstance(parameter.get("schema"), dict):
                        fail(f"{operation_id}: parâmetro {index} sem schema objeto")

            responses = operation.get("responses")
            if not isinstance(responses, dict) or not responses:
                fail(f"{operation_id}: responses deve ser um objeto não vazio")

text = ACTION_PATH.read_text(encoding="utf-8").lower()
demo_schema = "pet" + "store"
example_repository = "wagnerjfjunior/" + "fecha.ai"
if demo_schema in text or example_repository in text:
    fail("Schema de demonstração ou repositório incorreto encontrado")

if errors:
    print("BUILDER ACTION VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("BUILDER ACTION VALIDATION PASSED: parâmetros e respostas inline, sem $ref, somente GET e repositório fixo.")
