# RESF v1 — Candidate Pattern Registry

Status: `CANDIDATE`
Source provenance: `wagnerjfjunior/ProjetosCyrela@193c5c3245019b99d3a3070b3e485f48796e7e37/docs/architecture/resf-v1-origin/03_REUSABLE_PATTERNS_AND_ANTI_PATTERNS.md`

Framework qualification values in this registry are restricted to:

`PROVEN`, `PROMISING`, `PAGE_SPECIFIC`, `SUPERSEDED`, `CONTRADICTED`, `UNVALIDATED`.

Any additional context appears only as `source_evidence` and does not create a new qualification state.

## Intelligence
- `PAT-INT-001` Search demand before architecture — `PROVEN`. source_evidence: established across source planning and later search-performance analysis.
- `PAT-INT-002` Search term != configured keyword — `PROVEN`. source_evidence: demonstrated by paid-search leakage/failure evidence.

## Information architecture
- `PAT-IA-001` One dominant intent, one canonical owner — `PROVEN`. source_evidence: repeated cannibalization/ownership findings.
- `PAT-IA-002` Product/guide separation when intent materially differs — `PROVEN`. source_evidence: ZEN/product-guide architecture evidence.
- `PAT-IA-003` Multi-path decision architecture — `PROMISING`. source_evidence: approved design direction; not independently outcome-validated.

## SEO
- `PAT-SEO-001` Preserve performing canonical continuity where feasible — `PROMISING`. source_evidence: Capri continuity is supportive but not causal proof.
- `PAT-SEO-002` Technical SEO is an enabling layer, not a ranking guarantee — `PROVEN`. source_evidence: EPIC technical-score versus SERP outcome contrast.
- `PAT-SEO-003` Content completeness over arbitrary word counts — `PROMISING`. source_evidence: strongly supported design principle; no isolated causal test.

## Content
- `PAT-CONTENT-001` Editorial + semantic + commercial completeness — `PROMISING`. source_evidence: Capri benchmark plus comparative source evidence.
- `PAT-CONTENT-002` Match communication to product/page archetype — `PROMISING`. source_evidence: approved architecture across Signature/high-standard cases.

## Schema
- `PAT-SCHEMA-001` Schema is factual representation — `PROVEN`. source_evidence: repeated schema-governance decisions and failure prevention.
- `PAT-SCHEMA-002` One canonical FAQPage emitter when applicable — `PROVEN`. source_evidence: duplicate FAQPage failure evidence.
- `PAT-SCHEMA-003` Stable entity @id when useful — `PROVEN`. source_evidence: established technical pattern; ranking causality not claimed.

## Linking
- `PAT-LINK-001` Link by semantic relationship, journey, intent adjacency, territory and archetype — `PROMISING`. source_evidence: supported architecture rule; no isolated outcome proof.
- `PAT-LINK-002` Hub ↔ relevant product reciprocity — `PROMISING`. source_evidence: approved architecture direction.

## UX
- `PAT-UX-001` Independent real mobile validation — `PROVEN`. source_evidence: repeated mobile defect/failure evidence.
- `PAT-UX-002` Regression-safe patching — `PROVEN`. source_evidence: Capri patch-chain learning.
- `PAT-UX-003` Inspect actual DOM before selector/CSS remediation — `PROVEN`. source_evidence: exact-selector failure diagnosis.

## Conversion
- `PAT-CONV-001` One dominant business conversion action per page — `PROMISING`. source_evidence: strongly supported by page/funnel design work.
- `PAT-CONV-002` CTA language follows intent/archetype — `PROMISING`. source_evidence: approved page-archetype strategy.
- `PAT-CONV-003` Minimize form friction unless complexity creates measurable value — `PROMISING`. source_evidence: source-project form-friction learning; universal effect not isolated.
- `PAT-CONV-004` Native platform form — `PAGE_SPECIFIC`. source_evidence: local Capri/Guia decision; explicitly non-universal.

## Lead
- `PAT-LEAD-001` Lead must represent a real business event — `PROVEN`. source_evidence: tracking/thank-you-page contradiction and correction history.
- `PAT-LEAD-002` Explicit lead identity/semantics contract — `PROMISING`. source_evidence: required-for-maturity design conclusion.
- `PAT-SCORE-001` Context + engagement + intent scoring model — `PROMISING`. source_evidence: model exists, but historical thresholds/classifications conflict and are not portable.

## Tracking
- `PAT-TRK-001` One logical event should use one stable event identity across destinations — `PROMISING`. source_evidence: desired invariant is coherent, but the source implementation/result is `CONTRADICTED` by later event_id observations and therefore is not treated as proven implementation evidence.
- `PAT-TRK-002` Destination allowlists — `PROVEN`. source_evidence: demonstrated by broad-trigger failure/remediation evidence.
- `PAT-TRK-003` End-to-end payload validation — `PROVEN`. source_evidence: HTTP-200-versus-semantic-correctness findings.
- `PAT-TRK-004` Product/page/funnel dimensions on relevant events — `PROMISING`. source_evidence: approved measurement-contract direction.

## Attribution
- `PAT-ATTR-001` Identifier persistence across the required business boundary — `PROMISING`. source_evidence: required principle; persistence was not fully proven in CRM runtime.
- `PAT-ATTR-002` One explicit conversion owner per business outcome — `PROMISING`. source_evidence: duplicate-conversion architecture risk identified; closed-loop outcome remains unvalidated.

## Consent
- `PAT-CONSENT-001` Consent UI != consent enforcement — `PROVEN`. source_evidence: platform/UI state was insufficient to establish destination gating.
- `PAT-CONSENT-002` Destination-specific consent matrix — `PROMISING`. source_evidence: required-for-maturity design direction; full enforcement not validated.

## Paid Search (`RESF-PAID`)
- `PAT-PAID-001` Search-term governance — `PROVEN`. source_evidence: demonstrated by Capri paid-search leakage/failure evidence.
- `PAT-PAID-002` Qualified conversion over CTR-only optimization — `PROVEN`. source_evidence: high CTR with zero reported leads demonstrated metric insufficiency.

## QA
- `PAT-QA-001` Preserve DESIGNED / IMPLEMENTED / DEPLOYED / VALIDATED — `PROVEN`. source_evidence: repeated historical-state ambiguity required this distinction.
- `PAT-QA-002` Validate CMS/source -> rendered output -> DOM/HEAD -> crawler — `PROVEN`. source_evidence: Green/rendered-output discrepancies.
- `PAT-QA-003` Regression protocol after material change — `PROVEN`. source_evidence: repeated patch-chain regressions.
- `PAT-QA-004` Timestamp validation — `PROVEN`. source_evidence: explicit governance decision to distinguish time-bounded validation from current truth.

## Governance
- `PAT-GOV-001` Framework is selectable, not truth — `PROVEN`. source_evidence: explicitly approved governance invariant.
- `PAT-GOV-002` Framework is versioned — `PROVEN`. source_evidence: explicitly approved governance invariant.
- `PAT-GOV-003` Module-level adoption and overrides — `PROVEN`. source_evidence: explicitly approved governance invariant.
- `PAT-GOV-004` Preserve provenance — `PROVEN`. source_evidence: explicitly approved governance invariant.
- `PAT-GOV-005` Preserve superseded knowledge — `PROVEN`. source_evidence: explicitly approved governance invariant.

This registry is a Candidate index. Each pattern still requires a full provider-local record before promotion beyond Candidate.