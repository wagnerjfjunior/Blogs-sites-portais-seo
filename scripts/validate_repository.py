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
UPSTREAM_REPOSITORY = "wagnerjfjunior/StopJuniorMode"
UPSTREAM_REF = "d03d477c3b329aa973a38ec4e949c249fa017929"
UPSTREAM_PATH = "docs/CANONICAL_BOOTSTRAP_PROTOCOL.md"
UPSTREAM_BLOB = "7befd02533aad6c2df5544c7307e4a66dce28844"
UPSTREAM_LOCAL_COPY = "docs/references/sfjm/CANONICAL_BOOTSTRAP_PROTOCOL.md.gz.b64"
UPSTREAM_EVIDENCE = "docs/evidence/sfjm-upstream-anchor.md"
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

    paths = []
    for line in match.group("body").splitlines():
        item = re.match(r"^\s*\d+\.\s+`([^`]+)`\s*$", line)
        if item:
            paths.append(item.group(1))

    if not paths:
        fail(f"{relative_path}: nenhuma entrada numerada encontrada em {heading}")
    if len(paths) != len(set(paths)):
        fail(f"{relative_path}: ordem contém entradas duplicadas")
    return paths


def git_blob_sha(data):
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


if not CORE.is_file():
    print("VALIDATION FAILED")
    print("- scripts/_validate_repository_core.py: validador-base ausente")
    sys.exit(1)

with contextlib.redirect_stdout(io.StringIO()):
    runpy.run_path(str(CORE), run_name="__main__")

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
    except Exception as exc:
        fail(f"{UPSTREAM_LOCAL_COPY}: cópia upstream inválida: {exc}")

if evidence_path.is_file():
    evidence = evidence_path.read_text(encoding="utf-8")
    for expected in (
        UPSTREAM_REPOSITORY,
        UPSTREAM_REF,
        UPSTREAM_PATH,
        UPSTREAM_BLOB,
        UPSTREAM_LOCAL_COPY,
    ):
        if expected not in evidence:
            fail(f"{UPSTREAM_EVIDENCE}: evidência incompleta: {expected}")

if errors:
    print("VALIDATION FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(
    "VALIDATION PASSED: framework canônico preservado; "
    "SFJM operacional com ordem sincronizada, próxima ação única "
    "e âncora upstream localmente verificável."
)
