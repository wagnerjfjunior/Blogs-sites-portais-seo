from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SFJMValidationAdversarialTests(unittest.TestCase):
    def copy_repository(self):
        temporary = tempfile.TemporaryDirectory()
        destination = Path(temporary.name) / "repo"
        shutil.copytree(
            ROOT,
            destination,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        self.addCleanup(temporary.cleanup)
        return destination

    def run_validator(self, repository):
        return subprocess.run(
            [sys.executable, "scripts/validate_repository.py"],
            cwd=repository,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_canonical_repository_passes(self):
        result = self.run_validator(self.copy_repository())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_malformed_numbered_read_order_item(self):
        repository = self.copy_repository()
        path = repository / "bootstrap/BOOTSTRAP_CANONICO.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "6. `config/gpts.yaml`\n",
            "6. `config/gpts.yaml`\n7. README.md\n",
            1,
        )
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(repository)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("item numerado malformado", result.stdout)

    def test_replays_core_validator_diagnostics(self):
        repository = self.copy_repository()
        path = repository / "config/project.yaml"
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "id: blogs-sites-portais-seo",
            "id: invalid-project-id",
            1,
        )
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(repository)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ID técnico incorreto", result.stdout)

    def test_rejects_divergent_derived_next_action_id(self):
        repository = self.copy_repository()
        path = repository / "handoffs/CURRENT.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "resolve-live-lifecycle-transition-v1",
            "stale-transition-id",
            1,
        )
        path.write_text(text, encoding="utf-8")

        result = self.run_validator(repository)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Next action ID divergente", result.stdout)


if __name__ == "__main__":
    unittest.main()
