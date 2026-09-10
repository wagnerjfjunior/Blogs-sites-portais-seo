import json
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RESF = ROOT / "docs" / "frameworks" / "resf"
V1 = RESF / "v1"

ALLOWED_LIFECYCLE = {
    "EXPERIMENTAL", "CANDIDATE", "RECOMMENDED", "STABLE",
    "DEPRECATED", "SUPERSEDED", "ARCHIVED",
}
ALLOWED_PATTERN_QUALIFICATIONS = {
    "PROVEN", "PROMISING", "PAGE_SPECIFIC",
    "SUPERSEDED", "CONTRADICTED", "UNVALIDATED",
}


def load_json_yaml(path):
    return json.loads(path.read_text(encoding="utf-8"))


class RESFFrameworkTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            RESF / "README.md",
            RESF / "CURRENT.md",
            RESF / "GOVERNANCE.md",
            RESF / "VERSIONING.md",
            RESF / "CHANGELOG.md",
            RESF / "CONSUMPTION_GUIDE.md",
            RESF / "AI_INSTRUCTIONS.md",
            V1 / "MANIFEST.yaml",
            V1 / "FRAMEWORK.md",
            V1 / "MODULE_REGISTRY.yaml",
            V1 / "PATTERN_REGISTRY.yaml",
            V1 / "ANTI_PATTERN_REGISTRY.yaml",
            V1 / "CONTRACT_REGISTRY.yaml",
            V1 / "PLAYBOOK_REGISTRY.yaml",
            V1 / "EVIDENCE_REGISTRY.yaml",
            V1 / "LIMITATION_REGISTRY.yaml",
            V1 / "PROMOTION_CRITERIA.md",
            V1 / "RECONCILIATION_MATRIX.md",
        ]
        for path in required:
            self.assertTrue(path.exists(), str(path))

    def test_registries_parse_and_ids_are_unique(self):
        specs = [
            ("MODULE_REGISTRY.yaml", "modules"),
            ("PATTERN_REGISTRY.yaml", "patterns"),
            ("ANTI_PATTERN_REGISTRY.yaml", "anti_patterns"),
            ("CONTRACT_REGISTRY.yaml", "contracts"),
            ("PLAYBOOK_REGISTRY.yaml", "playbooks"),
            ("EVIDENCE_REGISTRY.yaml", "evidence"),
            ("LIMITATION_REGISTRY.yaml", "limitations"),
        ]
        for filename, key in specs:
            data = load_json_yaml(V1 / filename)
            records = data[key]
            ids = [item["id"] for item in records]
            self.assertEqual(len(ids), len(set(ids)), filename)

    def test_module_contract_and_pattern_references_resolve(self):
        modules = load_json_yaml(V1 / "MODULE_REGISTRY.yaml")["modules"]
        contracts = {x["id"] for x in load_json_yaml(V1 / "CONTRACT_REGISTRY.yaml")["contracts"]}
        patterns = {x["id"] for x in load_json_yaml(V1 / "PATTERN_REGISTRY.yaml")["patterns"]}
        anti_patterns = {x["id"] for x in load_json_yaml(V1 / "ANTI_PATTERN_REGISTRY.yaml")["anti_patterns"]}
        module_ids = {x["id"] for x in modules}
        for module in modules:
            self.assertTrue(set(module["required_contracts"]) <= contracts, module["id"])
            self.assertTrue(set(module["optional_contracts"]) <= contracts, module["id"])
            self.assertTrue(set(module["patterns"]) <= patterns, module["id"])
            self.assertTrue(set(module["anti_patterns"]) <= anti_patterns, module["id"])
            self.assertTrue(set(module["prerequisites"]) <= module_ids, module["id"])

    def test_module_records_include_canonical_operational_fields(self):
        modules = load_json_yaml(V1 / "MODULE_REGISTRY.yaml")["modules"]
        required = {
            "applicability", "prerequisites", "inputs", "outputs",
            "required_contracts", "optional_contracts", "patterns", "anti_patterns",
            "evidence_requirements", "responsible_specialist_capability",
            "validation_procedure", "consumer_override_policy", "limitations",
        }
        for module in modules:
            self.assertTrue(required <= set(module), module["id"])
            self.assertEqual(
                module["responsible_specialist_capability"],
                module["responsible_capability"],
                module["id"],
            )
            self.assertEqual(module["limitations"], module["known_limitations"], module["id"])

    def test_module_schema_requires_canonical_operational_fields(self):
        schema = json.loads((RESF / "schemas" / "module-record.schema.json").read_text(encoding="utf-8"))
        required = set(schema["required"])
        self.assertIn("responsible_specialist_capability", required)
        self.assertIn("limitations", required)
        self.assertNotIn("responsible_capability", required)
        self.assertNotIn("known_limitations", required)

    def test_playbook_references_resolve(self):
        modules = {x["id"] for x in load_json_yaml(V1 / "MODULE_REGISTRY.yaml")["modules"]}
        contracts = {x["id"] for x in load_json_yaml(V1 / "CONTRACT_REGISTRY.yaml")["contracts"]}
        for playbook in load_json_yaml(V1 / "PLAYBOOK_REGISTRY.yaml")["playbooks"]:
            self.assertTrue(set(playbook["modules"]) <= modules, playbook["id"])
            self.assertTrue(set(playbook["contracts"]) <= contracts, playbook["id"])

    def test_lifecycle_and_pattern_qualification(self):
        manifest = load_json_yaml(V1 / "MANIFEST.yaml")
        self.assertEqual(manifest["metadata"]["lifecycle_status"], "CANDIDATE")
        self.assertEqual(set(manifest["spec"]["lifecycle"]["allowed_states"]), ALLOWED_LIFECYCLE)
        for module in load_json_yaml(V1 / "MODULE_REGISTRY.yaml")["modules"]:
            self.assertIn(module["lifecycle"], ALLOWED_LIFECYCLE)
        for pattern in load_json_yaml(V1 / "PATTERN_REGISTRY.yaml")["patterns"]:
            self.assertIn(pattern["qualification"], ALLOWED_PATTERN_QUALIFICATIONS)

    def test_existing_provider_pattern_ids_are_preserved(self):
        current = load_json_yaml(V1 / "PATTERN_REGISTRY.yaml")
        ids = {x["id"] for x in current["patterns"]}
        baseline = (ROOT / "docs" / "frameworks" / "resf" / "v1" / "PATTERN_REGISTRY.md").read_text(encoding="utf-8")
        # Compatibility view points to machine authority; provider ID preservation is
        # additionally tested through representative IDs from each legacy category.
        for expected in [
            "PAT-INT-001", "PAT-IA-001", "PAT-SEO-001", "PAT-CONTENT-001",
            "PAT-SCHEMA-001", "PAT-LINK-001", "PAT-UX-001", "PAT-CONV-001",
            "PAT-LEAD-001", "PAT-SCORE-001", "PAT-TRK-001", "PAT-ATTR-001",
            "PAT-CONSENT-001", "PAT-PAID-001", "PAT-QA-001", "PAT-GOV-001",
        ]:
            self.assertIn(expected, ids)
        self.assertIn("PATTERN_REGISTRY.yaml", baseline)

    def test_legacy_provider_pattern_evidence_is_preserved(self):
        patterns = load_json_yaml(V1 / "PATTERN_REGISTRY.yaml")["patterns"]
        legacy = [
            item for item in patterns
            if item.get("provenance", {}).get("ref")
            == "193c5c3245019b99d3a3070b3e485f48796e7e37"
        ]
        self.assertEqual(len(legacy), 44)
        for item in legacy:
            self.assertTrue(item.get("source_evidence"), item["id"])

    def test_legacy_anti_pattern_ids_are_resolvable(self):
        anti = load_json_yaml(V1 / "ANTI_PATTERN_REGISTRY.yaml")
        legacy = {x["id"] for x in anti["legacy_provider_records"]}
        expected_ids = {
            "AP-INT-001", "AP-IA-001",
            "AP-SEO-001", "AP-SEO-002", "AP-SEO-003", "AP-CONTENT-001",
            "AP-SCHEMA-001", "AP-SCHEMA-002", "AP-SCHEMA-003", "AP-LINK-001",
            "AP-UX-001", "AP-UX-002", "AP-UX-003", "AP-CONV-001", "AP-LEAD-001",
            "AP-SCORE-001", "AP-SCORE-002",
            "AP-TRK-001", "AP-TRK-002", "AP-TRK-003",
            "AP-ATTR-001", "AP-ATTR-002", "AP-PAID-001",
            "AP-CONSENT-001", "AP-CONSENT-002", "AP-QA-001", "AP-QA-002",
        }
        self.assertEqual(expected_ids, legacy)

    def test_adoption_template_requires_immutable_provider_ref(self):
        template = yaml.safe_load((RESF / "templates" / "CONSUMER_ADOPTION_MANIFEST.template.yaml").read_text(encoding="utf-8"))
        provider_ref = template["framework"]["provider_ref"]
        self.assertNotEqual(provider_ref, "main")
        self.assertEqual(provider_ref, "REQUIRED_IMMUTABLE_SHA")
        schema = json.loads((RESF / "schemas" / "adoption-manifest.schema.json").read_text(encoding="utf-8"))
        pattern = schema["properties"]["framework"]["properties"]["provider_ref"]["pattern"]
        self.assertTrue(re.fullmatch(pattern, provider_ref))
        self.assertFalse(re.fullmatch(pattern, "main"))

    def test_all_templates_parse(self):
        templates = list((RESF / "templates").glob("*.yaml"))
        self.assertGreaterEqual(len(templates), 10)
        for path in templates:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertIsInstance(value, dict, path.name)

    def test_record_schemas_exist_and_parse(self):
        names = {
            "adoption-manifest.schema.json",
            "module-record.schema.json",
            "pattern-record.schema.json",
            "contract-record.schema.json",
            "evidence-record.schema.json",
            "result-record.schema.json",
        }
        for name in names:
            schema = json.loads((RESF / "schemas" / name).read_text(encoding="utf-8"))
            self.assertEqual(schema["type"], "object")

    def test_no_performance_guarantees(self):
        manifest = load_json_yaml(V1 / "MANIFEST.yaml")
        non_claims = manifest["spec"]["non_claims"]
        for key in ["guarantees_ranking", "guarantees_traffic", "guarantees_leads", "guarantees_revenue"]:
            self.assertIs(non_claims[key], False)

    def test_consumer_facts_are_not_in_generic_core(self):
        generic = "\n".join([
            (V1 / "MODULE_REGISTRY.yaml").read_text(encoding="utf-8"),
            (V1 / "CONTRACT_REGISTRY.yaml").read_text(encoding="utf-8"),
            (V1 / "PLAYBOOK_REGISTRY.yaml").read_text(encoding="utf-8"),
        ]).lower()
        for forbidden in ["capri", "zen", "epic", "vista_milano", "jordanacyrela.com.br"]:
            self.assertNotIn(forbidden, generic)

    def test_capri_is_reference_not_causal_template(self):
        evidence = load_json_yaml(V1 / "EVIDENCE_REGISTRY.yaml")["evidence"]
        capri = next(x for x in evidence if x["id"] == "EVD-003")
        self.assertEqual(capri["classification"], "CAPRI_HIGH_VALUE_REFERENCE_IMPLEMENTATION")
        self.assertEqual(capri["causality"], "NOT_ESTABLISHED")
        manifest = load_json_yaml(V1 / "MANIFEST.yaml")
        self.assertFalse(manifest["spec"]["principles"]["reference_implementation_is_universal_template"])
        self.assertFalse(manifest["spec"]["principles"]["observed_result_proves_causality"])

    def test_bootstrap_and_framework_index_discover_resf(self):
        bootstrap = (ROOT / "bootstrap" / "BOOTSTRAP_CANONICO.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "frameworks" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("docs/frameworks/resf/README.md", bootstrap)
        self.assertIn("docs/frameworks/resf/AI_INSTRUCTIONS.md", bootstrap)
        self.assertIn("docs/frameworks/resf/README.md", index)
        self.assertIn("docs/frameworks/resf/AI_INSTRUCTIONS.md", index)

    def test_backward_compatible_human_paths_are_aliases(self):
        pattern_md = (V1 / "PATTERN_REGISTRY.md").read_text(encoding="utf-8")
        anti_md = (V1 / "ANTI_PATTERN_REGISTRY.md").read_text(encoding="utf-8")
        limitations_md = (V1 / "KNOWN_LIMITATIONS.md").read_text(encoding="utf-8")
        self.assertIn("PATTERN_REGISTRY.yaml", pattern_md)
        self.assertIn("ANTI_PATTERN_REGISTRY.yaml", anti_md)
        self.assertIn("LIMITATION_REGISTRY.yaml", limitations_md)


if __name__ == "__main__":
    unittest.main()
