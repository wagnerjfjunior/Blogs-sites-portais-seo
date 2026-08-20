from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


class SESAdoptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.adoption = yaml.safe_load((ROOT / "config/ses.yaml").read_text(encoding="utf-8"))
        cls.project = yaml.safe_load((ROOT / "config/project.yaml").read_text(encoding="utf-8"))
        cls.gpts = yaml.safe_load((ROOT / "config/gpts.yaml").read_text(encoding="utf-8"))

    def test_project_points_to_adoption_manifest(self):
        self.assertEqual("config/ses.yaml", self.project["spec"]["ses"]["adoption_manifest"])
        self.assertEqual("blogs-sites-portais-seo", self.project["spec"]["ses"]["gateway_project_id"])

    def test_exact_five_horizontal_roles_are_adopted(self):
        observed = {
            item["role"]: item["archetype_id"]
            for item in self.adoption["spec"]["adopted_roles"]
            if item["status"] == "adopted"
        }
        expected = {
            "documentation_audit": "documentation-auditor",
            "architecture": "software-systems-architect",
            "ux_ui": "ux-ui-app-specialist",
            "backend_data": "backend-data-platform-specialist",
            "application_security": "application-security-assurance-specialist",
        }
        self.assertEqual(expected, observed)

    def test_gateway_never_authorizes_mutation(self):
        self.assertFalse(self.adoption["spec"]["gateway"]["mutation_authorized"])
        self.assertTrue(self.adoption["spec"]["invariants"]["routable_does_not_authorize_mutation"])

    def test_legacy_project_specialists_are_preserved(self):
        local_ids = [agent["id"] for agent in self.gpts["spec"]["agents"]]
        adopted_local_ids = self.adoption["spec"]["project_local_specialists"]["ids"]
        self.assertEqual([f"gpt{i}" for i in range(9)], local_ids)
        self.assertEqual(local_ids, adopted_local_ids)
        self.assertTrue(self.adoption["spec"]["project_local_specialists"]["preserved"])
        self.assertTrue(
            self.adoption["spec"]["project_local_specialists"]["retirement_requires_explicit_validation_and_authorization"]
        )

    def test_overlap_boundaries_are_explicit(self):
        boundaries = {item["role"]: item["boundary"] for item in self.adoption["spec"]["adopted_roles"]}
        self.assertIn("Does not replace GPT0", boundaries["documentation_audit"])
        self.assertIn("Does not replace GPT1", boundaries["architecture"])
        self.assertIn("Does not replace GPT8", boundaries["backend_data"])
        self.assertIn("Does not replace GPT4", boundaries["application_security"])

    def test_exact_matching_and_no_semantic_translation(self):
        invariants = self.adoption["spec"]["invariants"]
        self.assertTrue(invariants["gateway_role_matching_is_exact"])
        self.assertTrue(invariants["semantic_or_fuzzy_role_translation_is_forbidden"])


if __name__ == "__main__":
    unittest.main()
