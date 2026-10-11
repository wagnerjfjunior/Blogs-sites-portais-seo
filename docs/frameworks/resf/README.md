# RESF — Real Estate Search Framework

Canonical provider: `wagnerjfjunior/Blogs-sites-portais-seo`.
Current selectable version: `RESF v1 — Search-to-Lead`.
Lifecycle: `CANDIDATE`.

RESF is the provider-local, reusable real-estate Search-to-Lead framework. It standardizes controllable work across demand, intent, product truth, architecture, content, SEO, schema/GEO/AEO, UX/mobile/performance, conversion, tracking, lead/CRM handoff, consent, paid media, QA and measurement. It does not guarantee ranking, traffic, leads or revenue.

## Authority boundary

`FRAMEWORK != TRUTH`
`FRAMEWORK != PROJECT AUTHORITY`
`REFERENCE IMPLEMENTATION != UNIVERSAL TEMPLATE`
`OBSERVED RESULT != PROVEN CAUSALITY`
`ADOPTION != IMPLEMENTATION != DEPLOYMENT != VALIDATION`

Provider authority is limited to framework definitions and provider-local lifecycle. Every consumer retains product facts, brand, content, code, CMS, domain, DNS, deploy, analytics, CRM, campaigns, consent, risk and release authority.

## Human consumption

1. Confirm the project domain is real estate.
2. Read `CURRENT.md` and the selected version manifest.
3. Read `CONSUMPTION_GUIDE.md`.
4. Resolve the consumer repository and its immutable adoption manifest.
5. Load only adopted modules, contracts, patterns, anti-patterns and limitations.
6. Produce and validate artifacts in the consumer repository.

## AI consumption

Agents must start at `AI_INSTRUCTIONS.md`. Missing adoption means `AVAILABLE_NOT_ADOPTED`; missing consumer facts blocks factual implementation; missing runtime evidence forbids `CURRENT`, `DEPLOYED` or `VALIDATED` claims.

## Canonical registries

- `v1/MODULE_REGISTRY.yaml`
- `v1/CONTRACT_REGISTRY.yaml`
- `v1/PATTERN_REGISTRY.yaml`
- `v1/ANTI_PATTERN_REGISTRY.yaml`
- `v1/PLAYBOOK_REGISTRY.yaml`
- `v1/EVIDENCE_REGISTRY.yaml`
- `v1/LIMITATION_REGISTRY.yaml`

Legacy Markdown registries remain compatibility/navigation aliases only. Machine-readable YAML registries above are canonical.

## Evidence base

Initial origin: `ProjetosCyrela@193c5c3245019b99d3a3070b3e485f48796e7e37/docs/architecture/resf-v1-origin/`.
Current operationalization source consumed for this version reconciliation: `ProjetosCyrela@60a8af63a94b86542c52f992d76bb5df1ca4ea2e`.
Capri remains a high-value reference implementation with observed Google visibility and Gemini citation; causality is not established. Vista Milano is a controlled preview application, not production validation.

## Candidate — Exact-project JSON-LD validation (2026-10-11)

- `v1/EXACT_PROJECT_JSONLD_GRAPH_PROFILE_V1_2026-10-11.md` — **candidate**, factual graph architecture, field-level validation, and consumer-observed Google Rich Results 6 valid items / Schema.org 0 errors and 0 warnings for the Bem Moema pilot; not a universal six-item guarantee.
- `templates/EXACT_PROJECT_JSONLD_INTAKE.template.yaml` — question-based facts intake before generating any exact-project JSON-LD.
- `v1/EVIDENCE_REGISTRY.yaml` entry `EVD-005` — captures provenance, exact consumer SHA and limitations.

**Do not treat this candidate as C07/C17 promotion or automatic adoption of `RESF-SCHEMA`.** The consumer remains authoritative for facts, deployment, validation and module adoption.

## Padrão Único RESF de construção de páginas de empreendimentos — requisitos 01 a 04

Entrada canônica proposta: `v1/EXACT_PROJECT_PAGE_BUILD_STANDARD_V1_2026-10-11.md`.

1. **Item 01 — JSON-LD:** `v1/EXACT_PROJECT_JSONLD_GRAPH_PROFILE_V1_2026-10-11.md`; estrutura factual do grafo, conexões, teste Schema.org e Google Rich Results com evidência Bem Moema + Ampère Brooklin.
2. **Item 02 — Imagens para busca/SERP:** `v1/EXACT_PROJECT_SERP_IMAGE_OWNERSHIP_V1_2026-10-11.md`; coerência entre hero, `og:image`, `twitter:image`, `WebPage.image`, `primaryImageOfPage`, dois `ImageObject` e prioridade do hero. A SERP não garante miniatura escolhida.
3. **Item 03 — FAQ estratégico de SEO:** `v1/EXACT_PROJECT_SEO_FAQ_INTENT_V1_2026-10-11.md`; seleção de perguntas por intenção de busca, respostas reais e úteis, HTML visível, paridade literal com `FAQPage`. Ária tem 12 perguntas estruturadas como referência editorial; Ampère FAQ 6→12 está em PR de consumidor #387 **Draft**, sem publicação/homologação Google pós-mudança. Não impor 12 como mínimo universal.
4. **Requisito 04 — UX/CSS formulário e footer:** `v1/EXACT_PROJECT_FORM_FOOTER_UX_V1_2026-10-11.md`; referência Ária Higienópolis para cartão branco, inputs e botão amarelo mobile-first, footer escuro, identidade e campos legais. Ampère tem implementação proposta em PR de consumidor #388 **Draft**; preservar Form 46, tracking e dados comerciais.

**Fase candidata:** estes quatro requisitos do mesmo padrão ainda dependem de revisão, gates, merge do provider e adoção explícita pelo consumer. Não criam obrigação retroativa nem autorizam mudanças fora de cada escopo aprovado.
