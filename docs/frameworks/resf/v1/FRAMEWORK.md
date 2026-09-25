# RESF v1 — Search-to-Lead

Status: `CANDIDATE`  
Provider: `blogs-sites-portais-seo`

RESF v1 is the selectable, versioned real-estate framework for governing:

`DEMAND -> INTENT -> PRODUCT TRUTH -> IA -> PAGE/CONTENT -> SEO/SCHEMA/GEO-AEO -> UX/PERFORMANCE -> CONVERSION -> TRACKING -> VALID LEAD -> CRM HANDOFF -> ATTRIBUTION BOUNDARY -> QA -> MEASUREMENT -> LEARNING`

Canonical machine definitions live in the registries referenced by `MANIFEST.yaml`. The human entrypoint is `../README.md`; deterministic agent instructions are in `../AI_INSTRUCTIONS.md`.

## Core invariants

`FRAMEWORK != TRUTH`  
`FRAMEWORK != PROJECT AUTHORITY`  
`FRAMEWORK != MANDATORY STANDARD`  
`REFERENCE IMPLEMENTATION != UNIVERSAL TEMPLATE`  
`OBSERVED RESULT != PROVEN CAUSALITY`  
`ADOPTION != IMPLEMENTATION`  
`IMPLEMENTATION != DEPLOYMENT`  
`DEPLOYMENT != VALIDATION`  
`VALIDATED_AT_TIME_T != CURRENTLY_VALID`

## Authority boundary

The provider owns only framework definitions and provider-local lifecycle. A consumer owns its product facts, commercial claims, brand, code, CMS, domain, DNS, deployments, analytics, CRM, campaigns, budget, consent/risk and release decisions.

An override is a consumer decision. It does not mutate the provider framework.

## Evidence boundary

The initial origin package is preserved at:

`wagnerjfjunior/ProjetosCyrela@193c5c3245019b99d3a3070b3e485f48796e7e37/docs/architecture/resf-v1-origin/`

The operational knowledge layer used for this reconciliation is pinned at:

`wagnerjfjunior/ProjetosCyrela@60a8af63a94b86542c52f992d76bb5df1ca4ea2e`

Capri is a high-value reference implementation with observed Google visibility and observed Gemini citation. Those observations do not establish causal contribution by RESF or any isolated pattern.

Vista Milano is a controlled preview application of RESF concepts. It is not production validation and does not satisfy the full promotion gate.

## Lifecycle

Allowed states are `EXPERIMENTAL`, `CANDIDATE`, `RECOMMENDED`, `STABLE`, `DEPRECATED`, `SUPERSEDED`, `ARCHIVED`.

This version remains `CANDIDATE`. Documentation completeness, Capri visibility or a preview application do not authorize promotion.


## Audience readiness boundary

For consumers that adopt `RESF-TRACKING`, audience readiness is a measurement/classification capability, not a platform asset requirement.

```text
AUDIENCE_READY != AUDIENCE_CREATED
AUDIENCE_CREATED != AUDIENCE_MEMBERSHIP
AUDIENCE_MEMBERSHIP != AUDIENCE_ACTIVATED
AUDIENCE_MEMBERSHIP != ACQUISITION_ATTRIBUTION
```

A conforming implementation uses a stable, governed, consumer-owned classifier and governed non-PII semantic page/event context so intended page/entity classes can be segmented without page-specific tracking rework. The provider does not prescribe GA4, a URL namespace, a membership window, a universal audience catalog, or automatic creation of page-specific audiences.

Audience creation, membership windows, platform configuration, activation and archival remain consumer-owned. Consent/privacy requirements remain controlling. Post-release evidence must distinguish documented configuration from current runtime/platform proof.

## Scope boundary

v1 ends at Search-to-Lead. A future Search-to-Revenue version requires separate lifecycle and evidence for CRM opportunity/sale feedback, revenue attribution and applicable offline-conversion loops.
