from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SFJMValidationAdversarialTests(unittest.TestCase):
    def copy_repository(self):
        temp = tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup)
        destination = Path(temp.name) / "repo"
        shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        return destination
    def run_validator(self, repo):
        return subprocess.run([sys.executable, "scripts/validate_repository.py"], cwd=repo, text=True, capture_output=True, check=False)
    def mutate(self, relative_path, old, new):
        repo = self.copy_repository(); path = repo / relative_path
        path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
        return self.run_validator(repo)
    def test_canonical_repository_passes(self):
        result = self.run_validator(self.copy_repository()); self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
    def test_persistent_agent_rules_present(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Não atualize registros por conclusão de gate", text)
        self.assertIn("merge só aceita autorização concedida depois de Ready", text)
        self.assertIn("tentativa mais recente do workflow canônico", text)
    def test_rejects_malformed_numbered_item(self):
        result = self.mutate("bootstrap/BOOTSTRAP_CANONICO.md", "6. `config/gpts.yaml`\n", "6. `config/gpts.yaml`\n7. README.md\n")
        self.assertNotEqual(result.returncode, 0); self.assertIn("item numerado malformado", result.stdout)
    def test_replays_core_diagnostics(self):
        result = self.mutate("config/project.yaml", "id: blogs-sites-portais-seo", "id: invalid-project-id")
        self.assertNotEqual(result.returncode, 0); self.assertIn("ID técnico incorreto", result.stdout)
    def test_rejects_action_id_drift(self):
        result = self.mutate("handoffs/CURRENT.md", "resolve-live-lifecycle-transition-v1", "stale-transition-id")
        self.assertNotEqual(result.returncode, 0); self.assertIn("Next action ID divergente", result.stdout)
    def test_rejects_summary_drift(self):
        result = self.mutate("handoffs/CURRENT.md", "- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.", "- Resumo derivado: executar GPT4 imediatamente.")
        self.assertNotEqual(result.returncode, 0); self.assertIn("resumo derivado divergente", result.stdout)
    def test_rejects_manifest_transition_drift(self):
        result = self.mutate("config/sfjm.yaml", "current_gpt4_gate_verdict_is_block", "current_gpt4_gate_is_current")
        self.assertNotEqual(result.returncode, 0); self.assertIn("máquina de transição divergente", result.stdout)
    def test_rejects_published_table_drift(self):
        result = self.mutate("docs/NEXT_SAFE_ACTION.md", "`report_lifecycle_complete_without_mutation`", "`perform_unversioned_extra_action`")
        self.assertNotEqual(result.returncode, 0); self.assertIn("tabela publicada diverge", result.stdout)
    def test_requires_latest_workflow_attempt(self):
        result = self.mutate("config/sfjm.yaml", "latest_canonical_workflow_attempt_for_exact_head_is_completed_success", "exact_head_has_any_completed_successful_workflow")
        self.assertNotEqual(result.returncode, 0); self.assertIn("máquina de transição divergente", result.stdout)
    def test_rejects_inverted_pr_checkout_condition(self):
        result = self.mutate(".github/workflows/validate-agent-framework.yml", "if: ${{ github.event_name == 'pull_request' }}", "if: ${{ github.event_name != 'pull_request' }}")
        self.assertNotEqual(result.returncode, 0); self.assertIn("condição do checkout PR incorreta", result.stdout)
    def test_rejects_wrong_pr_checkout_ref(self):
        result = self.mutate(".github/workflows/validate-agent-framework.yml", "ref: ${{ github.event.pull_request.head.sha }}", "ref: ${{ github.sha }}")
        self.assertNotEqual(result.returncode, 0); self.assertIn("ref do checkout PR incorreto", result.stdout)
    def test_requires_terminal_transition(self):
        result = self.mutate("config/sfjm.yaml", "pull_request_is_closed_and_not_merged", "pull_request_is_closed")
        self.assertNotEqual(result.returncode, 0); self.assertIn("máquina de transição divergente", result.stdout)
    def test_requires_passing_gate_condition(self):
        result = self.mutate("config/sfjm.yaml", "current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_draft", "gates_are_current_pull_request_is_draft")
        self.assertNotEqual(result.returncode, 0); self.assertIn("máquina de transição divergente", result.stdout)
    def test_requires_post_ready_merge_authorization(self):
        result = self.mutate("config/sfjm.yaml", "post_ready_exact_head_and_base_merge_authorization_is_present", "exact_head_and_base_merge_authorization_is_present")
        self.assertNotEqual(result.returncode, 0); self.assertIn("máquina de transição divergente", result.stdout)
    def test_rejects_volatile_adr_rewrite_rule(self):
        result = self.mutate("docs/decisions/ADR-0002-adopt-sfjm-operational-bootstrap.md", "Gates, autorizações, Draft/Ready, reviews, merge e pós-merge são evidências externas", "Mudanças de estado exigem atualização dos registros aplicáveis")
        self.assertNotEqual(result.returncode, 0); self.assertIn("ADR-0002", result.stdout)
    def test_ignores_generated_python_bytecode(self):
        repo = self.copy_repository(); cache = repo / "tests/__pycache__"; cache.mkdir(parents=True)
        (cache / "synthetic.cpython-312.pyc").write_bytes(b"\x00\xff\x00generated-bytecode")
        result = self.run_validator(repo); self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
    def test_requires_base_bound_lifecycle_evidence(self):
        result = self.mutate("config/sfjm.yaml", "exact_head_and_base_bound_external_evidence", "exact_head_bound_external_evidence")
        self.assertNotEqual(result.returncode, 0); self.assertIn("transition_model incorreto", result.stdout)
    def test_rejects_contradictory_evidence_field(self):
        result = self.mutate("docs/evidence/sfjm-upstream-anchor.md", "- Git blob SHA observado: `7befd02533aad6c2df5544c7307e4a66dce28844`", "- Git blob SHA observado: `0000000000000000000000000000000000000000`")
        self.assertNotEqual(result.returncode, 0); self.assertIn("campo Git blob SHA observado divergente", result.stdout)
    def test_rejects_duplicate_evidence_field(self):
        repo = self.copy_repository(); path = repo / "docs/evidence/sfjm-upstream-anchor.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n- Git blob SHA observado: incorrect\n", encoding="utf-8")
        result = self.run_validator(repo); self.assertNotEqual(result.returncode, 0); self.assertIn("campo ausente ou duplicado", result.stdout)

if __name__ == "__main__": unittest.main()
