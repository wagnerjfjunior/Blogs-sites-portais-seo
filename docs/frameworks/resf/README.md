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

## Padrão único RESF de construção de páginas de empreendimentos — requisitos 01 a 06

**Estado documental:** publicado na `main` do provider via PR #23, merge SHA `f9b6bfb1f92f49aa9e49a47f9b1c7e3157beeccf`. **Piloto integrado:** Ampère Brooklin / MoreNumTegra PRs #388 e #389; production `READY` no SHA `b6497954e45d77cf37dd639dbea3c18bd29a4040`. Isso não representa promoção geral do ciclo RESF v1 nem adoção automática em outros projetos.

**[Ler o padrão único](v1/EXACT_PROJECT_PAGE_BUILD_STANDARD_V1_2026-10-11.md)** · **[Handoff completo do release e da conversa](v1/RESF_EXACT_PROJECT_RELEASE_CLOSURE_2026-10-11.md)**.

| Requisito | Documento e função |
|---|---|
| 01 — JSON-LD | [Perfil factual](v1/EXACT_PROJECT_JSONLD_GRAPH_PROFILE_V1_2026-10-11.md) — entidades, fatos, propriedades compatíveis e teste |
| 02 — Imagens principais de busca | [Ownership SERP](v1/EXACT_PROJECT_SERP_IMAGE_OWNERSHIP_V1_2026-10-11.md) — hero, OG/Twitter, imagens e JSON-LD |
| 03 — FAQ SEO | [Perguntas por intenção](v1/EXACT_PROJECT_SEO_FAQ_INTENT_V1_2026-10-11.md) — HTML visível e `FAQPage` literal |
| 04 — Formulário/footer | [UX/CSS de conversão](v1/EXACT_PROJECT_FORM_FOOTER_UX_V1_2026-10-11.md) — referência Ária, Form 46 governado |
| 05 — Hero/facts | [Abertura de quatro quadros](v1/EXACT_PROJECT_HERO_FACTS_UX_V1_2026-10-11.md) — sem dados duplicados |
| 06 — SEO editorial/copy/local | [Conteúdo comercial](v1/EXACT_PROJECT_SEO_COMMERCIAL_COPY_V1_2026-10-11.md) — busca, marca, visita, negociação, imagens do bairro e link regional |

**Reconciliado:** PR #387 de FAQ encerrada **sem merge**; seu objetivo foi absorvido pela versão final de 12 FAQs na PR #389 mergeada. A PR #388 e a #389 também foram mergeadas. CI do consumidor: 9/9 e 10/10, respectivamente. A Vercel confirmou READY no domínio comercial. A validação externa de imagens, teste manual mobile/formulário, Rich Results/Schema.org e observação GSC **após** o novo release não foram novamente comprovados aqui.

**Retomada:** começar pelo [handoff](v1/RESF_EXACT_PROJECT_RELEASE_CLOSURE_2026-10-11.md), depois resolver novamente fatos live, branch e governança do consumidor. Nunca reutilizar preços ou atributos do Ampère na próxima página nem concluir por contagem de palavras que haverá ranking.
