from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SFJMValidationAdversarialTests(unittest.TestCase):
    def copy_repository(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        destination = Path(temp.name) / "repo"
        shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        return destination

    def run_validator(self, repo):
        return subprocess.run(
            [sys.executable, "scripts/validate_repository.py"],
            cwd=repo,
            text=True,
            capture_output=True,
            check=False,
        )

    def mutate(self, relative_path, old, new):
        repo = self.copy_repository()
        path = repo / relative_path
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture ausente: {old}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return self.run_validator(repo)

    def test_canonical_repository_passes(self):
        result = self.run_validator(self.copy_repository())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_project_without_specialist_adoption(self):
        result = self.mutate("config/project.yaml", "specialist_adoption: config/specialists.yaml", "specialist_adoption: config/gpts.yaml")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("specialist_adoption incorreto", result.stdout)

    def test_rejects_legacy_registry_as_routing_authority(self):
        result = self.mutate("config/specialists.yaml", "routing_authority: false", "routing_authority: true")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("legacy registry", result.stdout)

    def test_rejects_fuzzy_replacement_of_technical_seo(self):
        result = self.mutate("config/specialists.yaml", "archetype_id: technical-seo-specialist", "archetype_id: seo-specialist")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mapa adotado divergente", result.stdout)

    def test_requires_documentation_auditor_gate(self):
        result = self.mutate("config/sfjm.yaml", "archetype_id: documentation-auditor", "archetype_id: gpt0")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("documentary gate", result.stdout)

    def test_requires_project_local_lifecycle_gate(self):
        result = self.mutate("config/sfjm.yaml", "owner: PROJECT_SFJM_GOVERNANCE", "owner: gpt4")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("lifecycle gate", result.stdout)

    def test_rejects_manifest_transition_drift(self):
        result = self.mutate(
            "config/sfjm.yaml",
            "current_lifecycle_governance_gate_verdict_is_block",
            "current_lifecycle_gate_is_current",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("máquina de transição divergente", result.stdout)

    def test_rejects_published_transition_drift(self):
        result = self.mutate(
            "docs/NEXT_SAFE_ACTION.md",
            "`report_lifecycle_complete_without_mutation`",
            "`perform_unversioned_extra_action`",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tabela publicada diverge", result.stdout)

    def test_requires_exact_pr_head_checkout(self):
        result = self.mutate(
            ".github/workflows/validate-agent-framework.yml",
            "ref: ${{ github.event.pull_request.head.sha }}",
            "ref: ${{ github.sha }}",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ref do checkout PR incorreto", result.stdout)

    def test_builder_external_mutation_is_fail_closed(self):
        result = self.mutate(
            "config/specialists.yaml",
            "external_builder_mutation_in_this_migration: false",
            "external_builder_mutation_in_this_migration: true",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Builder externo", result.stdout)

    def test_legacy_ids_remain_addressable(self):
        result = self.mutate("config/gpts.yaml", "- id: gpt8", "- id: removed-gpt8")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("artefatos legados", result.stdout)

    def test_bootstrap_order_uses_specialists_not_legacy_registry(self):
        result = self.mutate(
            "bootstrap/BOOTSTRAP_CANONICO.md",
            "6. `config/specialists.yaml`",
            "6. `config/gpts.yaml`",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("bootstrap: ordem mínima divergente", result.stdout)

    def test_ignores_generated_python_bytecode(self):
        repo = self.copy_repository()
        cache = repo / "tests/__pycache__"
        cache.mkdir(parents=True)
        (cache / "synthetic.cpython-312.pyc").write_bytes(b"\x00\xff\x00generated-bytecode")
        result = self.run_validator(repo)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
