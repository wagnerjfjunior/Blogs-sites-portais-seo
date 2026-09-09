# RESF — Deterministic AI Instructions

These instructions govern AI consumption of the provider framework. They do not authorize mutations.

## Resolution algorithm

1. Resolve provider `wagnerjfjunior/Blogs-sites-portais-seo@main` live.
2. Read `docs/frameworks/resf/CURRENT.md`.
3. Read the selected version `MANIFEST.yaml`.
4. Identify the consumer project and repository.
5. Resolve the consumer `main` live.
6. Locate the consumer RESF adoption manifest.
7. Confirm the domain and applicability.
8. Load only adopted modules.
9. Load each adopted module's required contracts.
10. Consult canonical patterns, anti-patterns, evidence and limitations.
11. Keep provider facts and consumer facts separate.
12. Require governed evidence for missing consumer facts.
13. Produce artifacts in the consumer, not the provider, unless provider mutation is separately authorized.
14. Validate artifacts against schemas/contracts.
15. Preserve implementation states: `DESIGNED`, `IMPLEMENTED`, `DEPLOYED`, `VALIDATED`.
16. Respect consumer lifecycle, release gates and authorization.
17. Never assume a reference implementation is a template.
18. Never treat an observed result as causal proof.
19. Never promote the framework automatically.
20. Never modify provider or consumer without explicit authority.

## Routing

```text
IF project.domain != real_estate
THEN RESF = NOT_APPLICABLE

IF consumer_adoption_manifest == MISSING
THEN RESF = AVAILABLE_NOT_ADOPTED

IF adoption.mode == SELECTIVE
THEN load only adoption.modules

IF required consumer facts == MISSING
THEN BLOCK_FACTUAL_IMPLEMENTATION

IF current runtime evidence == MISSING
THEN do not claim CURRENT, DEPLOYED or VALIDATED
```

## Evidence semantics

`DOCUMENTED != IMPLEMENTED`
`IMPLEMENTED != DEPLOYED`
`DEPLOYED != VALIDATED`
`VALIDATED_AT_TIME_T != CURRENTLY_VALID`

Capri is a high-value reference implementation with observed Google visibility and Gemini citation. Causality is not established. Vista Milano is evidence of controlled preview adoption, not production validation.

## Mutation boundary

Provider framework work does not transfer authority over consumer facts, code, deploy, DNS, analytics, CRM, campaigns, budget, consent or release.
