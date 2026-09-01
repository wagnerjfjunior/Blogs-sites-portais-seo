# RESF v1 — Search-to-Lead

Status: `CANDIDATE`
Provider: `blogs-sites-portais-seo`
Initial evidence source: `projetos-cyrela`

## Definition

RESF v1 — Search-to-Lead is a versioned, modular, selectable, evidence-oriented real-estate framework for designing and governing the chain between search demand, intent architecture, content, discovery, experience, conversion, measurement and lead generation.

It does not prescribe a specific brand, CMS or commercial implementation and does not claim to guarantee ranking, leads or revenue.

## Governance invariants

`FRAMEWORK != TRUTH`

`FRAMEWORK != PROJECT AUTHORITY`

`FRAMEWORK != MANDATORY STANDARD`

`FRAMEWORK != PERMANENT BEST PRACTICE`

`FRAMEWORK = VERSIONED + SELECTABLE + COMPOSABLE STRATEGY`

`RECOMMENDED_AT_TIME_T != RECOMMENDED_AT_TIME_T+1`

## Evidence origin

The initial Candidate was derived from a curated canonical reconstruction in `wagnerjfjunior/ProjetosCyrela`, not from a generic best-practice checklist.

The immutable source revision for this Candidate intake is:

`wagnerjfjunior/ProjetosCyrela@193c5c3245019b99d3a3070b3e485f48796e7e37`

Source package path at that revision:

`docs/architecture/resf-v1-origin/`

Human workflow context at intake time: branch `sfjm/bootstrap-legacy-recovery-v1`, PR `#1`.

The provider must preserve provenance and must not copy consumer-specific facts or IDs into universal rules.

## Core system chain

`SEARCH DEMAND -> SEARCH INTENT -> SERP -> INFORMATION ARCHITECTURE -> PAGE ARCHETYPE -> CONTENT -> TECHNICAL SEO / SCHEMA / GEO-AEO -> UX / MOBILE / PERFORMANCE -> CTA -> FORM / WHATSAPP -> LEAD VALIDATION -> TRACKING -> CRM -> ATTRIBUTION -> ADS OPTIMIZATION`

The Candidate is deliberately named **Search-to-Lead** because the initial source evidence does not establish a complete Search-to-Revenue closed loop.

## Modules

- `RESF-INTELLIGENCE`
- `RESF-IA`
- `RESF-SEO`
- `RESF-CONTENT`
- `RESF-SCHEMA`
- `RESF-LINKING`
- `RESF-UX`
- `RESF-CONVERSION`
- `RESF-TRACKING`
- `RESF-LEAD`
- `RESF-ATTRIBUTION`
- `RESF-CONSENT`
- `RESF-PAID`
- `RESF-QA`

Modules may be adopted, partially adopted, overridden, deferred or rejected by a consumer project. Adoption is never implicit.

## Consumer authority

Consumer projects retain authority over product facts, commercial data, credentials, repository/code, CMS, deploy, DNS, analytics accounts, CRM, campaign publication, budget, risk acceptance and adoption decisions.

`PROVIDER_SPECIALIST_WORK != CONSUMER_PROJECT_MUTATION`

## Candidate rules with strongest source support

The initial Candidate gives strongest weight to:

- observed search demand before architecture;
- one materially distinct dominant intent with a canonical owner;
- guide/product separation when intent materially differs;
- preserving performing canonical continuity where feasible;
- technical SEO as an enabling layer, not a ranking guarantee;
- factual schema only, with canonical emitter ownership;
- internal linking by semantic relationship and journey rather than quota;
- independent mobile validation and regression-safe changes;
- one real business definition for lead semantics;
- an explicit logical-event identity contract for deduplication, while treating the source implementation outcome as contradicted until revalidated;
- destination allowlists and end-to-end tracking validation;
- explicit conversion ownership;
- attribution identifier persistence where closed-loop questions require it;
- consent UI/enforcement separation;
- search-term governance and qualified-conversion optimization for paid search;
- explicit `DESIGNED / IMPLEMENTED / DEPLOYED / VALIDATED` states;
- timestamped validation and preserved provenance.

## Benchmark governance

The source project's Capri case is a reference implementation and empirical benchmark, not a universal template or proof of ranking causality. ZEN and EPIC contribute independent evidence around intent architecture, schema/FAQ failure, page archetypes, technical SEO versus SERP outcome and mobile/implementation QA.

## Pattern qualification

Framework patterns use only these qualification states:

`PROVEN`, `PROMISING`, `PAGE_SPECIFIC`, `SUPERSEDED`, `CONTRADICTED`, `UNVALIDATED`.

Source-project evidence uses a separate evidence taxonomy. Pattern records may therefore carry a framework qualification plus a distinct `source_evidence` note; source evidence must not be silently collapsed into framework qualification.

## Lifecycle

Allowed framework lifecycle states are:

`EXPERIMENTAL`, `CANDIDATE`, `RECOMMENDED`, `STABLE`, `DEPRECATED`, `SUPERSEDED`, `ARCHIVED`.

This PR introduces only `CANDIDATE`. No automatic promotion to `RECOMMENDED` is authorized.

## Promotion requirement

At minimum, promotion beyond Candidate should require reviewed pattern and anti-pattern registries, formal contracts, provenance, explicit limitations, a validated consumer adoption model, at least one controlled application/revalidation and no unclassified critical contradiction.
