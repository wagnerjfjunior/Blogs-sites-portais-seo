# MoreNumTegra -> RESF v1 Consumer Evidence Intake

Date: `2026-09-23`

Provider project: `blogs-sites-portais-seo`

Framework: `RESF — Real Estate Search Framework v1 / Search-to-Lead`

Provider lifecycle: `CANDIDATE`

Intake status: `CONSUMER_EVIDENCE_INTAKE / CLASSIFICATION_ONLY / NO_FRAMEWORK_PROMOTION`

## 1. Purpose

Receive a provenance-preserving consumer evidence packet from MoreNumTegra after execution of its Search-to-Lead QA/release/observability sequence.

This intake does not mutate MoreNumTegra, does not promote RESF lifecycle, does not automatically create a pattern, and does not convert consumer-specific facts into universal framework truth.

## 2. Immutable source

Consumer:

```text
project = morenumtegra
repository = wagnerjfjunior/MoreNumTegra
canonical source revision = e6fc4fee3a375afc45988d456220891cbe11cb15
effective Production runtime SHA = 124b620855175a583c528733462d6d0f4f44cd41
Production tree SHA = b40b9afb5b834b0fc0abdd32d3486f82198d0e9e
Production deployment = dpl_9xYzKZnnVM8qAKDEgnBNXCUvPv7C
canonical host = https://www.moretegra.com.br/
```

Provider base at intake creation:

```text
repository = wagnerjfjunior/Blogs-sites-portais-seo
main = 7a61aa036d677015ee4540ca8c5dc9a41f0165d4
RESF lifecycle = CANDIDATE
```

## 3. Consumer evidence package

Primary aggregate registry:

`wagnerjfjunior/MoreNumTegra@e6fc4fee3a375afc45988d456220891cbe11cb15:docs/observability/MNT_M7_12_RESULT_PROVENANCE_REGISTRY_2026-09-23.md`

Supporting evidence:

- `docs/qa/MNT_M7_02_PRODUCT_TRUTH_READJUDICATION_2026-09-22.md`
- `docs/qa/MNT_M7_03_INDEPENDENT_MOBILE_QA_2026-09-23.md`
- `docs/qa/MNT_M7_04_TRACKING_LEAD_E2E_QA_2026-09-23.md`
- `docs/qa/MNT_M7_05_REGRESSION_SUITE_2026-09-23.md`
- `docs/qa/MNT_M7_06_P0_P1_RELEASE_ADJUDICATION_2026-09-23.md`
- `docs/qa/MNT_M7_07_VERCEL_PRODUCTION_HOMOLOGATION_2026-09-23.md`
- `docs/qa/MNT_M7_08_GREEN_PUBLICATION_READJUDICATION_2026-09-23.md`
- `docs/qa/MNT_M7_09_PRODUCTION_SMOKE_2026-09-23.md`
- `docs/observability/MNT_M7_10_POST_RELEASE_MEASUREMENT_2026-09-23.md`
- `docs/observability/MNT_M7_11_GSC_GA4_ADS_OBSERVATION_WINDOW_2026-09-23.md`

All paths above are relative to the immutable MoreNumTegra source revision unless otherwise noted.

## 4. Observed consumer results

### QA / release

```text
P0 = 0
P1 = 0
P2 = 2
P3 = 0
```

Retained P2 consumer residuals:

1. CAPIITOLO client-side editorial composition.
2. Search favicon eligibility residual.

Mobile/touch evidence:

```text
viewport = 393x852
hasTouch = true
browsers = Chromium + Firefox + WebKit
result = 27 PASS / 0 FAIL
physical-device proof = NOT_OBSERVED
```

The tested PR head and Production merge shared the exact Git tree `b40b9afb5b834b0fc0abdd32d3486f82198d0e9e`.

### Tracking / lead

Consumer composite evidence preserved:

```text
Form46 / Green real handoff proof = EXISTING
GTM source = mnt_lead_success
GA4 destination = generate_lead
current live GA4 generate_lead = OBSERVED
synthetic real lead for final M7 QA = NOT_CREATED
```

Critical lead/measurement source blobs were unchanged from the earlier accepted E2E runtime to the current Production runtime.

### Publication topology

Consumer ADR-006 changed the canonical web-publication topology:

```text
Vercel = commercial web Production
www.moretegra.com.br = canonical host
Green/GDigital = Form46 backend / CRM
legacy Green web surface = fallback/noncanonical
```

Therefore the historical consumer WBS task named "Controlled Green publication" was accepted by explicit architecture supersession rather than by creating an artificial Green web publication.

This is a consumer lifecycle adjudication, not a provider-wide rule.

### Post-release observability

The current Production deployment became READY on 2026-09-22 at approximately 15:16 BRT.

GA4 had unambiguous later Home observations at 18h and 19h.

The consumer explicitly separated:

```text
OBSERVED POST-RELEASE TRAFFIC
!=
RELEASE CAUSED TRAFFIC
```

No ranking/traffic/lead causal claim was made.

### Paid media

Google Ads implementation remained intentionally frozen.

Read-only observation of the designated future account for the current available seven-day window returned zero rows.

Consumer disposition:

```text
M6-07 external paid implementation = DEFERRED / FROZEN
M6-08 paid conversion QA = DEFERRED / DEPENDS_ON_M6-07
Ads spend used for RESF closure = R$ 0
```

The consumer did not manufacture paid-media activity to make the planning percentage reach 100%.

## 5. Classification

### EVIDENCE — supports existing RESF contract behavior

#### C15 Release Contract

The consumer produced direct evidence for:

- technical/content QA;
- mobile/touch QA;
- tracking/lead QA;
- regression QA;
- explicit P0=0/P1=0 adjudication;
- separate publication authority.

Classification:

`CONSUMER_EVIDENCE_SUPPORTS_EXISTING_CONTRACT`

No change to C15 is requested by this intake.

#### C16 Post-release Measurement Contract

The consumer produced timestamped post-release observations and explicitly kept observed result separate from causal claim.

Classification:

`CONSUMER_EVIDENCE_SUPPORTS_EXISTING_CONTRACT`

This intake itself fulfills the consumer-to-provider evidence handoff leg of the learning loop. It does not complete a provider lifecycle decision.

### PATTERN CANDIDATE — exact-tree evidence reuse

Observed consumer behavior:

```text
PR HEAD TREE == PRODUCTION MERGE TREE
-> exact-tree QA evidence remains applicable to the deployed file tree
-> merge-commit identity difference alone does not require artificial duplicate runtime mutation
```

Candidate classification:

`PATTERN_CANDIDATE / NEEDS_CONTROLLED_REVALIDATION`

Limitation: tree equality does not prove environment/provider parity, configuration parity or current external-system state. Runtime/provider observations remain separately required.

### PATTERN CANDIDATE — superseded publication target

Observed consumer behavior:

A historical release task named for a previous production platform was adjudicated against a newer accepted architecture rather than executed literally.

Candidate classification:

`GOVERNANCE_PATTERN_CANDIDATE / NEEDS_CONTROLLED_REVALIDATION`

Boundary:

```text
HISTORICAL TASK LABEL
!=
AUTHORITY TO RECREATE SUPERSEDED TOPOLOGY
```

This does not mean any planned task can be skipped by convenience; a current accepted architecture decision and explicit adjudication are required.

### PATTERN CANDIDATE — composite lead QA without duplicate synthetic lead

Observed consumer behavior:

A prior real downstream lead proof, unchanged critical lead/measurement source blobs, current exact-tree CTA/Form regression, and current destination-event observation were combined without generating another real CRM lead solely for QA.

Candidate classification:

`PATTERN_CANDIDATE / NEEDS_CONTROLLED_REVALIDATION`

Boundary:

This approach is admissible only when identity/equivalence of the relevant runtime contract is proven. It is not a blanket substitute for real end-to-end testing after material lead-path changes.

### CONSUMER-SPECIFIC DECISION — paid implementation deferred

MoreNumTegra chose to close its non-paid sequence while M6-07/M6-08 remain deferred.

Classification:

`CONSUMER_LIFECYCLE_DECISION / NOT_UNIVERSAL_FRAMEWORK_RULE`

No framework claim is made that paid media is optional for every consumer.

## 6. Limitations

This evidence does not establish:

- physical-device mobile PASS;
- SEO ranking causality;
- traffic causality;
- lead/revenue causality;
- paid campaign performance;
- M6-07 or M6-08 completion;
- universal applicability of Vercel/Green topology;
- universal permission to reuse exact-tree evidence;
- automatic RESF promotion from CANDIDATE.

Search Console observations are sparse and time-lagged.

GA4 event-count equality is not treated as a joined user funnel.

## 7. Conflicts

No material conflict with current C15 or C16 was identified in this bounded intake.

Potential future pattern candidates above require provider-side controlled revalidation before any registry promotion.

## 8. Authority boundary

```text
PROVIDER INTAKE != CONSUMER MUTATION
EVIDENCE INTAKE != PATTERN PROMOTION
PATTERN CANDIDATE != PROVEN PATTERN
CONSUMER RESULT != UNIVERSAL CAUSAL CLAIM
```

MoreNumTegra retains authority over its product, facts, runtime, release, analytics, CRM, budget and campaigns.

The provider retains authority over RESF lifecycle and framework registries subject to its own governance.

## 9. Human decision represented

Product Authority authorized the MoreNumTegra non-paid RESF sequence through provider evidence intake while paid implementation remains frozen.

This file records the intake only.

It does not represent a decision to:

- promote RESF lifecycle;
- edit current pattern/contract registries;
- activate paid media;
- mutate MoreNumTegra;
- publish anything externally.

## 10. Intake disposition

```text
INTAKE = READY_FOR_PROVIDER_DOCUMENTATION/LIFECYCLE_GATES
C15 SUPPORT = YES
C16 SUPPORT = YES
PATTERN CANDIDATES = 3
FRAMEWORK REGISTRY MUTATION = NO
FRAMEWORK LIFECYCLE PROMOTION = NO
CONSUMER MUTATION = NO
```
