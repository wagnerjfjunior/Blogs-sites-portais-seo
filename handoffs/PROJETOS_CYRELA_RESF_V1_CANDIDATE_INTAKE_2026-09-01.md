# Handoff Intake — Projetos Cyrela -> RESF v1 Candidate

Date: `2026-09-01`
Provider project: `blogs-sites-portais-seo`
Source project: `projetos-cyrela`
Framework: `RESF — Real Estate Search Framework`
Version: `v1`
Variant: `Search-to-Lead`
Requested lifecycle: `CANDIDATE`

## Purpose

Receive a curated, provenance-preserving framework candidate extracted from the canonical legacy reconstruction in `wagnerjfjunior/ProjetosCyrela`.

This handoff does not transfer authority over the source project and does not authorize consumer mutation.

## Source package

Canonical source repository:

`wagnerjfjunior/ProjetosCyrela`

Immutable source revision used for this intake:

`193c5c3245019b99d3a3070b3e485f48796e7e37`

Source branch/PR context at handoff preparation:

- branch: `sfjm/bootstrap-legacy-recovery-v1`
- PR: `#1`
- source commit: `193c5c3245019b99d3a3070b3e485f48796e7e37`
- source package path: `docs/architecture/resf-v1-origin/`

Expected source artifacts at that exact revision:

1. `01_CROSS_DISCIPLINE_CANONICAL_SYNTHESIS.md`
2. `02_CAPRI_ZEN_EPIC_COMPARATIVE_EVIDENCE_MATRIX.md`
3. `03_REUSABLE_PATTERNS_AND_ANTI_PATTERNS.md`
4. `04_RESF_V1_CANDIDATE_HANDOFF_SPEC.md`
5. `05_CONSISTENCY_CHECK_AND_PROVIDER_HANDOFF.md`

The source project's historical recovery packets remain canonical there and should not be copied wholesale into this provider.

## Intake result in this PR

The provider-side candidate materializes:

- `docs/frameworks/resf/v1/MANIFEST.yaml`
- `docs/frameworks/resf/v1/FRAMEWORK.md`
- `docs/frameworks/resf/v1/PATTERN_REGISTRY.md`
- `docs/frameworks/resf/v1/ANTI_PATTERN_REGISTRY.md`
- `docs/frameworks/resf/v1/KNOWN_LIMITATIONS.md`

The durable provider discovery pointer is `docs/PROJECT_STATUS.md`, which links to the RESF Candidate manifest.

These files are provider-local candidate abstractions, not consumer implementation instructions.

## Authority boundary

`FRAMEWORK != PROJECT AUTHORITY`

`PROVIDER_SPECIALIST_WORK != CONSUMER_PROJECT_MUTATION`

`CONSUMER_ADOPTION != AUTOMATIC`

The provider may review, version and publish framework definitions subject to its own governance. Each consumer retains facts, implementation, deploy, DNS, CMS, analytics, CRM, budget, campaign publication and risk authority.

## Evidence boundary

The intake preserves these distinctions:

`DOCUMENTED != IMPLEMENTED`

`IMPLEMENTED != DEPLOYED`

`DEPLOYED != VALIDATED`

`VALIDATED_AT_TIME_T != CURRENTLY_VALID`

`CORRECTION_APPLIED != PROBLEM_RESOLVED`

The framework Candidate must not upgrade historical source evidence into current-live consumer truth.

## Candidate limitations

The initial evidence does not establish:

- complete Search-to-Revenue closed-loop attribution;
- offline-conversion feedback;
- universal scoring thresholds;
- current cross-destination consent enforcement;
- AI citation/discovery effectiveness;
- ranking causality from Capri, ZEN, EPIC or any isolated tactic.

The tracking identity design is also explicitly separated from source runtime proof: one logical-event identity is retained only as a Candidate design invariant, while later source `event_id` observations remain contradicted implementation evidence until revalidated.

These limitations are intentionally preserved.

## Provider adjudication requested

The provider should evaluate only whether this body is coherent enough to exist as a `CANDIDATE` selectable framework. It should not automatically promote to `RECOMMENDED` or `STABLE`.

Future promotion should require provider-local review, pattern-record completion, provenance checks, contract formalization and controlled consumer revalidation.

## Explicit non-actions

This intake does not authorize:

- merge without a current post-review authorization;
- external publication;
- mutation of Projetos Cyrela;
- mutation of MoreNumTegra or any other consumer;
- DNS/deploy/tracking/campaign changes;
- lifecycle promotion beyond `CANDIDATE`.
