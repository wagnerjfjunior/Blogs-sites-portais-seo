from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]


class SESSpecialistMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.adoption = yaml.safe_load((ROOT / "config/specialists.yaml").read_text(encoding="utf-8"))
        cls.project = yaml.safe_load((ROOT / "config/project.yaml").read_text(encoding="utf-8"))
        cls.sfjm = yaml.safe_load((ROOT / "config/sfjm.yaml").read_text(encoding="utf-8"))

    def test_canonical_adoption_locator(self):
        self.assertEqual("config/specialists.yaml", self.project["spec"]["specialist_adoption"])
        self.assertEqual("config/gpts.yaml", self.project["spec"]["legacy_gpt_registry"])

    def test_required_search_roles(self):
        roles = {
            item["role"]: item["archetype_id"]
            for item in self.adoption["spec"]["adopted_roles"]
        }
        self.assertEqual("seo-strategy-governance-specialist", roles["seo_strategy"])
        self.assertEqual("technical-seo-specialist", roles["technical_seo"])
        self.assertEqual("content-semantic-seo-specialist", roles["content_semantic_seo"])
        self.assertEqual("seo-analytics-growth-specialist", roles["seo_analytics_growth"])
        self.assertEqual("paid-search-sem-specialist", roles["paid_search_sem"])

    def test_architecture_is_software_systems_architect(self):
        roles = {
            item["role"]: item["archetype_id"]
            for item in self.adoption["spec"]["adopted_roles"]
        }
        self.assertEqual("software-systems-architect", roles["architecture"])

    def test_targets_are_not_claimed_as_adopted(self):
        targets = {item["role"]: item for item in self.adoption["spec"]["target_roles_not_yet_adoptable"]}
        self.assertIn("local_seo", targets)
        self.assertIn("authority_digital_pr", targets)
        adopted = {item["role"] for item in self.adoption["spec"]["adopted_roles"]}
        self.assertNotIn("local_seo", adopted)
        self.assertNotIn("authority_digital_pr", adopted)

    def test_monetization_stays_explicit_local_exception(self):
        exceptions = {item["role"]: item for item in self.adoption["spec"]["project_local_exceptions"]}
        self.assertEqual("PROJECT_LOCAL_ACTIVE_EXCEPTION_NO_SES_EQUIVALENT", exceptions["monetization"]["status"])
        self.assertEqual("NOT_ELIGIBLE_NO_CANONICAL_REPLACEMENT", exceptions["monetization"]["retirement_status"])

    def test_builder_retirement_is_not_automatic(self):
        policy = self.adoption["spec"]["builder_policy"]
        self.assertFalse(policy["external_builder_mutation_in_this_migration"])
        self.assertTrue(policy["builder_retirement_requires_equivalence_tests"])
        self.assertTrue(policy["builder_retirement_requires_explicit_authorization"])

    def test_lifecycle_is_not_routed_to_legacy_gpt(self):
        roles = self.sfjm["spec"]["roles"]
        self.assertEqual("documentation-auditor", roles["documentary_gate"]["archetype_id"])
        self.assertEqual("PROJECT_SFJM_GOVERNANCE", roles["lifecycle_gate"]["owner"])
        self.assertIsNone(roles["lifecycle_gate"]["specialist_archetype_id"])


if __name__ == "__main__":
    unittest.main()
