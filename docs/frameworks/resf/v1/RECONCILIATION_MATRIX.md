# RESF v1 — Provider × ProjetosCyrela Reconciliation

Provider baseline: `Blogs-sites-portais-seo@92eb39a00a6299d32cd8fb884582ab2685308a94`
Source baseline: `ProjetosCyrela@60a8af63a94b86542c52f992d76bb5df1ca4ea2e`

## Previous provider state

The provider already had the v1 Candidate manifest, framework narrative, Markdown pattern/anti-pattern indexes, known limitations, framework discovery index and the original ProjetosCyrela intake. It did not yet expose a complete machine-readable operational package for selective consumer use.

## Source operational layer

The current ProjetosCyrela knowledge layer contains 17 local modules, 13 contracts, 20 patterns, 16 anti-patterns, 3 playbooks, 18 evidence gaps, two observed Capri results and a Vista Milano preview implementation manifest.

Only portable abstractions and immutable provenance are reconciled here. Product facts and source-project runtime details remain in the consumer.

## Module mapping

| Source module | Provider outcome | Status |
|---|---|---|
| M01 FACTS_CLAIM_REGISTRY | RESF-PRODUCT-TRUTH | RENAMED |
| M02 MARKET_INTENT_INPUT | RESF-INTELLIGENCE | RENAMED |
| M03 SEARCH_CONTRACT | RESF-SEARCH-CONTRACT | RENAMED |
| M04 PAGE_CONTRACT | RESF-IA + Page Contract | SPLIT |
| M05 ENTITY_SCHEMA_CONTRACT | RESF-SCHEMA | RENAMED |
| M06 CONTENT_ARCHITECTURE | RESF-CONTENT + RESF-GEO-AEO | SPLIT |
| M07 UX_CRO_ARCHITECTURE | RESF-UX + RESF-CONVERSION | SPLIT |
| M08 PERFORMANCE_BUDGET | RESF-PERFORMANCE | RENAMED |
| M09 TRACKING_CONTRACT | RESF-TRACKING | RENAMED |
| M10 FORM_CRM_CONTRACT | RESF-LEAD + RESF-CRM | SPLIT |
| M11 PAID_MEDIA_CONTRACT | RESF-PAID + RESF-ATTRIBUTION | SPLIT |
| M12 PRIVACY_CONSENT_GATE | RESF-CONSENT | RENAMED |
| M13 BUILD_PREVIEW | QA/release process | MERGED |
| M14 QA_REGRESSION_RELEASE | RESF-QA | RENAMED |
| M15 POST_RELEASE_MEASUREMENT | RESF-OBSERVABILITY | RENAMED |
| M16 GEO_AI_OBSERVATION | GEO-AEO + OBSERVABILITY | MERGED |
| M17 HEATMAP_SESSION_REPLAY | no core module | DEFERRED: EVIDENCE_MISSING |
| Provider SEO / LINKING | RESF-SEO / RESF-LINKING | EXISTING |

The provider exposes 20 explicit modules.

## Contracts and playbooks

The source 13-contract model is normalized to 16 provider contracts by separating market intelligence, information architecture and internal linking concerns. Three source playbooks are normalized to nine provider playbooks composed from modules and contracts.

## Duplication policy

YAML files are the single machine-readable registries. Existing Markdown registry paths remain compatibility views. Raw recovery material stays in ProjetosCyrela. `CURRENT.md` is only a version pointer.

## Evidence boundary

Capri: `HIGH_VALUE_REFERENCE_IMPLEMENTATION + OBSERVED_GOOGLE_VISIBILITY + OBSERVED_GEMINI_CITATION + CAUSALITY_NOT_ESTABLISHED`.

Vista Milano: `CONTROLLED_PREVIEW_APPLICATION + PRODUCTION_NOT_PROVEN + REVALIDATION_PARTIAL`.

Neither permits lifecycle promotion.

## Gaps

Search-to-Revenue, closed-loop CRM/offline attribution, current dedup, current consent enforcement, heatmap/session-replay evidence and full production/revalidation evidence remain incomplete.

## Result

The provider now has deterministic human/AI entrypoints, one registry per type, schemas/templates, selective immutable-SHA adoption and backward-compatible discovery paths while remaining `CANDIDATE`.
