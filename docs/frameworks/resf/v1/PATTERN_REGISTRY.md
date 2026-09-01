# RESF v1 — Candidate Pattern Registry

Status: `CANDIDATE`
Source provenance: `wagnerjfjunior/ProjetosCyrela/docs/architecture/resf-v1-origin/03_REUSABLE_PATTERNS_AND_ANTI_PATTERNS.md`

## Intelligence
- `PAT-INT-001` Search demand before architecture — `PROVEN`.
- `PAT-INT-002` Search term != configured keyword — `PROVEN BY FAILURE`.

## Information architecture
- `PAT-IA-001` One dominant intent, one canonical owner — `PROVEN`.
- `PAT-IA-002` Product/guide separation when intent materially differs — `PROVEN`.
- `PAT-IA-003` Multi-path decision architecture — `PROMISING`.

## SEO
- `PAT-SEO-001` Preserve performing canonical continuity where feasible — `PROVEN/PROMISING`.
- `PAT-SEO-002` Technical SEO is an enabling layer, not a ranking guarantee — `PROVEN`.
- `PAT-SEO-003` Content completeness over arbitrary word counts — `PROMISING/STRONGLY_SUPPORTED`.

## Content
- `PAT-CONTENT-001` Editorial + semantic + commercial completeness — `PROMISING`.
- `PAT-CONTENT-002` Match communication to product/page archetype — `PROMISING`.

## Schema
- `PAT-SCHEMA-001` Schema is factual representation — `PROVEN`.
- `PAT-SCHEMA-002` One canonical FAQPage emitter when applicable — `PROVEN BY FAILURE`.
- `PAT-SCHEMA-003` Stable entity @id when useful — `PROVEN`.

## Linking
- `PAT-LINK-001` Link by semantic relationship, journey, intent adjacency, territory and archetype — `PROVEN/PROMISING`.
- `PAT-LINK-002` Hub ↔ relevant product reciprocity — `PROMISING`.

## UX
- `PAT-UX-001` Independent real mobile validation — `PROVEN BY FAILURE`.
- `PAT-UX-002` Regression-safe patching — `PROVEN`.
- `PAT-UX-003` Inspect actual DOM before selector/CSS remediation — `PROVEN BY FAILURE`.

## Conversion
- `PAT-CONV-001` One dominant business conversion action per page — `PROMISING/STRONGLY_SUPPORTED`.
- `PAT-CONV-002` CTA language follows intent/archetype — `PROMISING`.
- `PAT-CONV-003` Minimize form friction unless complexity creates measurable value — `PROVEN PRINCIPLE`.
- `PAT-CONV-004` Native platform form — `PAGE_SPECIFIC`, not universal.

## Lead
- `PAT-LEAD-001` Lead must represent a real business event — `PROVEN`.
- `PAT-LEAD-002` Explicit lead identity/semantics contract — `PROMISING/REQUIRED_FOR_MATURITY`.
- `PAT-SCORE-001` Context + engagement + intent scoring model — `PROMISING`; thresholds not portable.

## Tracking
- `PAT-TRK-001` One logical event, one event_id — `PROVEN`.
- `PAT-TRK-002` Destination allowlists — `PROVEN BY FAILURE`.
- `PAT-TRK-003` End-to-end payload validation — `PROVEN`.
- `PAT-TRK-004` Product/page/funnel dimensions on relevant events — `PROMISING`.

## Attribution
- `PAT-ATTR-001` Identifier persistence across required business boundary — `PROVEN PRINCIPLE`.
- `PAT-ATTR-002` One explicit conversion owner per business outcome — `PROVEN BY RISK`.

## Consent
- `PAT-CONSENT-001` Consent UI != consent enforcement — `PROVEN PRINCIPLE`.
- `PAT-CONSENT-002` Destination-specific consent matrix — `PROMISING/REQUIRED`.

## Paid Search
- `PAT-PAID-001` Search-term governance — `PROVEN BY FAILURE`.
- `PAT-PAID-002` Qualified conversion over CTR-only optimization — `PROVEN`.

## QA
- `PAT-QA-001` Preserve DESIGNED / IMPLEMENTED / DEPLOYED / VALIDATED — `PROVEN`.
- `PAT-QA-002` Validate CMS/source -> rendered output -> DOM/HEAD -> crawler — `PROVEN`.
- `PAT-QA-003` Regression protocol after material change — `PROVEN`.
- `PAT-QA-004` Timestamp validation — `PROVEN GOVERNANCE`.

## Governance
- `PAT-GOV-001` Framework is selectable, not truth — `APPROVED GOVERNANCE`.
- `PAT-GOV-002` Framework is versioned — `APPROVED GOVERNANCE`.
- `PAT-GOV-003` Module-level adoption and overrides — `APPROVED GOVERNANCE`.
- `PAT-GOV-004` Preserve provenance — `APPROVED GOVERNANCE`.
- `PAT-GOV-005` Preserve superseded knowledge — `APPROVED GOVERNANCE`.

This registry is a Candidate index. Each pattern still requires a full provider-local record before promotion beyond Candidate.