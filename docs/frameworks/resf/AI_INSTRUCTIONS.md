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
15a. For dedicated real-estate project/entity pages where RESF-QA is adopted, load C17 and perform an exact-project readiness/parity check before describing the page as release-ready.
15b. A consumer-approved Local Live Sync may be used as branch-level validation evidence when hosted Preview is unavailable, prohibited, rate-limited or intentionally avoided, provided the exact consumer branch/head SHA is recorded and Production-only claims are not inferred.
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


## Exact-project readiness algorithm

When the consumer is building a dedicated project/entity page and adopts RESF-QA:

1. Load `C17 — Exact Project Page Readiness Contract`.
2. Resolve the consumer-owned reference family, if any.
3. Build an independent fact pack; never copy product facts from the reference page.
4. Build a parity matrix for recurring adopted capabilities such as conversion actions, location handoff, commercial truth surface, consent/preference controls, schema graph, internal linking and media/performance behavior.
5. Mark every recurring capability `PRESENT`, `NOT_APPLICABLE`, `BLOCKED_BY_MISSING_FACT` or `MISSING`.
6. Do not call the page release-ready while an adopted required capability is `MISSING`.
7. Do not invent price, unit, address, postal code, coordinates, stage, amenity, availability or structured Offer data to satisfy readiness.
8. Validate consent persistence and a reopen/change path when the consumer exposes persistent consent UI.
9. Validate local structured data connectivity and postal/geo completeness only when those facts are governed.
10. Preserve consumer release authority.


## Local validation transport

RESF does not require a hosted Preview as the only valid pre-release review surface. When the consumer explicitly governs a Local Live Sync workflow, it may be used for eligible branch-level visual, mobile, interaction, DOM/schema and non-production smoke evidence.

Required semantics:

- GitHub/consumer canonical repository remains source of truth;
- exact branch and immutable head SHA must be known;
- local sync must consume repository content rather than a manually reconstructed copy;
- local evidence must be labelled LOCAL;
- local validation must not be reported as DEPLOYED or Production VALIDATED;
- Production-domain, CRM, analytics, DNS, indexation, CDN and performance gates remain separate when required by the consumer;
- local validation does not transfer merge, publish or deploy authority.
