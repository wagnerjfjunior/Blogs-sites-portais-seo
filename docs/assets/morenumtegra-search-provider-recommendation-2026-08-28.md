# Search Provider Recommendation — MoreNumTegra — 2026-08-28

## Status

`PROVIDER_RESULT_CANDIDATE / READ_ONLY / NO_CONSUMER_MUTATION_AUTHORITY`

## 1. Provenance

Consumer / Product Authority: `wagnerjfjunior/MoreNumTegra`

Search provider: `wagnerjfjunior/Blogs-sites-portais-seo`

Consumer live main observed for this provider work:

```text
wagnerjfjunior/MoreNumTegra@b4cdbc1ac0be9a98112cb74a378571b64cf16e7f
```

Primary project-local input:

`handoffs/SEARCH_PROVIDER_HANDOFF_2026-08-28.md`

Consumer handoff records production as `https://moretegra.com.br` and describes live observations made on 2026-08-28, including HTTPS, HTTP->HTTPS, functional `www -> root` navigation, 21 rendered developments, Green Form 46, missing/uncertain Search metadata and page-level `www` redirection.

Provider also inspected exact repository source on the consumer main, including:

- `src-greenn/blocks/01-html-inicial.html`;
- `src-greenn/blocks/02-html-pos-form.html`;
- `src-greenn/blocks/03-footer.html`;
- `src-greenn/moretegra.js` / CSS inventory;
- project-local Search handoff and current lifecycle/boundary evidence.

### Live-access limitation

The provider's general web-fetch surface could not independently retrieve `https://moretegra.com.br/` in this execution. Therefore:

```text
CONSUMER_LIVE_HANDOFF_OBSERVED != PROVIDER_INDEPENDENT_HTTP_FETCH
```

The recommendations below are grounded in the consumer's dated live evidence plus exact repository final-state evidence. HTTP-specific claims such as the current `www` status code must be rechecked immediately before implementation/acceptance when a live HTTP-capable surface is available.

## 2. Executive decision

MoreNumTegra should be treated as the current `P0` commercial Search asset of the ecosystem and as a `COMMERCIAL_CONVERSION_HUB`, not as a temporary landing page.

The immediate Search objective is to make the current production technically unambiguous and indexable before expanding surface area.

Recommended order:

```text
P0 TECHNICAL INDEXABILITY / CANONICALITY
-> P0 METADATA / SEARCH IDENTITY
-> P0 SITEMAP + SEARCH CONSOLE
-> P1 STRUCTURED DATA
-> P1 INFORMATION ARCHITECTURE
-> P1 CONTENT / INTERNAL LINKING
-> P1 MEASUREMENT
-> P2 SEM
-> P2 AUTHORITY / DIGITAL PR WHEN SES ROLE IS ELIGIBLE
```

Do not create additional domains or hundreds of SEO pages before the canonical commercial hub is stable.

## 3. Findings

| ID | Severity | Finding | Evidence class | Decision |
|---|---|---|---|---|
| MT-SEO-001 | HIGH | explicit root canonical was not identified in the consumer's live observation | CONSUMER_LIVE_HANDOFF | add canonical for the commercial root |
| MT-SEO-002 | HIGH | `www` currently navigates to root but the handoff did not prove HTTP 301/308; HAR observed HTTP 200 before page-level navigation | CONSUMER_LIVE_HANDOFF | prefer server/edge 301/308; canonical is mitigation, not equivalent |
| MT-SEO-003 | HIGH | title/meta description are absent, generic or insufficient in Green live observation | CONSUMER_LIVE_HANDOFF | define final commercial metadata |
| MT-SEO-004 | MEDIUM | Open Graph incomplete and Twitter metadata not identified | CONSUMER_LIVE_HANDOFF | implement social metadata consistently |
| MT-SEO-005 | HIGH | JSON-LD was not identified | CONSUMER_LIVE_HANDOFF | add conservative factual schema in phases |
| MT-SEO-006 | HIGH | sitemap/Search Console state is not established | MISSING_EVIDENCE | create sitemap and Search Console gate |
| MT-SEO-007 | HIGH | Vercel is homologation and should not become competing indexed origin | PROJECT_BOUNDARY | preserve noindex on homologation |
| MT-SEO-008 | MEDIUM | current site is a single commercial hub with useful regions/stages/FAQ, but no durable URL architecture for entity/project/region demand | REPO_FINAL_STATE | expand progressively using justified pages, not filter-index explosion |
| MT-SEO-009 | MEDIUM | Search measurement is not proven active | PROJECT_BOUNDARY / MISSING_EVIDENCE | activate GSC/GA4 only through explicit measurement gate |
| MT-SEO-010 | MEDIUM | SEM is eligible as a specialist capability but no spend/publication is authorized | AUTHORITY_BOUNDARY | design only; campaigns/spend require separate authorization |

## 4. Canonical and hostname recommendation

### Primary commercial canonical

Use:

```html
<link rel="canonical" href="https://moretegra.com.br/">
```

The non-`www` HTTPS root should be the canonical commercial origin unless a later product/domain decision explicitly changes it.

### `www`

Preferred target state:

```text
https://www.moretegra.com.br/*
-> HTTP 301 or 308
-> https://moretegra.com.br/*
```

If Green cannot implement a proper HTTP redirect immediately, retain the functional page-level navigation only as an operational fallback and ensure the root canonical is emitted on any alternate representation. This mitigates duplication but does not prove equivalent redirect semantics.

### HTTP

Preserve HTTP -> HTTPS redirect behavior already reported by the consumer handoff.

## 5. Final metadata recommendation

### Title

Recommended homepage title:

```text
Apartamentos Tegra em São Paulo | More em um Tegra
```

Rationale:

- primary commercial entity/category first;
- geographic qualifier;
- project/brand proposition retained;
- avoids stuffing stage/region variants into the homepage title.

### Meta description

Recommended:

```text
Compare empreendimentos Tegra em São Paulo por região, estágio e faixa de valor. Veja lançamentos, imóveis em construção e prontos para morar e fale com a Tegra Vendas.
```

The commercial team must validate the wording before publication, especially any phrase that could imply official institutional ownership beyond the current visible disclosure.

### Open Graph

Recommended minimum:

```html
<meta property="og:type" content="website">
<meta property="og:url" content="https://moretegra.com.br/">
<meta property="og:title" content="Apartamentos Tegra em São Paulo | More em um Tegra">
<meta property="og:description" content="Compare empreendimentos Tegra em São Paulo por região, estágio e faixa de valor e encontre o projeto que combina com o seu momento.">
<meta property="og:image" content="ABSOLUTE_APPROVED_SOCIAL_IMAGE_URL">
<meta property="og:locale" content="pt_BR">
```

Do not invent an image URL. Use only an approved stable production asset.

### Twitter/X

If social sharing support is desired:

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Apartamentos Tegra em São Paulo | More em um Tegra">
<meta name="twitter:description" content="Compare empreendimentos Tegra em São Paulo por região, estágio e faixa de valor.">
<meta name="twitter:image" content="ABSOLUTE_APPROVED_SOCIAL_IMAGE_URL">
```

No `twitter:site` should be declared unless an actual authorized account is established.

## 6. Robots and indexation

### Green production

Target posture for the commercial root:

```html
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
```

Only apply after canonical/metadata are correct and the product authority confirms that commercial production should enter organic indexing.

### Vercel homologation

Preserve:

```text
noindex, nofollow
```

The Vercel hostname is a validation environment, not a second organic Search origin.

## 7. Sitemap

### Initial phase

If only the homepage is intentionally indexable, publish a minimal valid sitemap containing only canonical indexable URLs.

Example target:

```text
https://moretegra.com.br/sitemap.xml
```

Do not include:

- Vercel URLs;
- `www` duplicates;
- anchors/filter states;
- URLs not intended to be indexed;
- future project/region pages before they actually exist.

### Expansion phase

As durable pages are created, sitemap should be generated/maintained from the canonical URL inventory and separated by type only when volume justifies it.

## 8. Search Console

Preferred:

1. Domain Property for `moretegra.com.br` if DNS verification is authorized and operationally safe;
2. URL-prefix property `https://moretegra.com.br/` as a bounded alternative/initial step when DNS verification is not yet authorized;
3. submit sitemap;
4. inspect canonical root;
5. monitor indexing, query coverage and duplicate/canonical signals;
6. do not infer success from property verification alone.

`SEARCH_CONSOLE_VERIFIED != INDEXED`

`INDEXED != RANKING`

DNS verification remains a separate MoreNumTegra gate.

## 9. JSON-LD recommendation

Use structured data conservatively and only for visible/factual content.

### Phase 1 — recommended

`WebSite` + `WebPage` describing the commercial site/page.

Conceptual graph:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://moretegra.com.br/#website",
      "url": "https://moretegra.com.br/",
      "name": "More em um Tegra",
      "inLanguage": "pt-BR"
    },
    {
      "@type": "WebPage",
      "@id": "https://moretegra.com.br/#webpage",
      "url": "https://moretegra.com.br/",
      "name": "Apartamentos Tegra em São Paulo | More em um Tegra",
      "isPartOf": {"@id": "https://moretegra.com.br/#website"},
      "inLanguage": "pt-BR"
    }
  ]
}
```

Do not add an `Organization`/official-corporate claim unless the factual/legal publisher relationship is explicitly established by MoreNumTegra.

### Phase 2 — conditional

`ItemList` becomes valuable when each development has a stable canonical detail URL. Before that, avoid fabricating URL/entity relationships solely for schema.

### FAQPage

The current source contains visible FAQ content, so `FAQPage` can be syntactically/factually supportable if the final Green output preserves those questions and answers. However it should be treated as semantic markup, not as a guaranteed Google rich-result strategy.

Do not mark hidden or invented FAQs.

## 10. Information architecture

### Current role

Homepage = broad commercial hub for Tegra residential inventory in São Paulo.

### Recommended expansion model

```text
/
├── /empreendimentos/{slug}/
├── /regioes/{bairro-ou-regiao}/
├── /imoveis/{lancamentos|em-construcao|prontos}/
├── /comparar/{tema}/             [only with genuine editorial value]
└── /guias/{tema}/                [only with search/user thesis]
```

This is a target information model, not an implementation mandate.

### Development pages

Create a page only when the project can sustain:

- factual/current property data;
- unique copy and useful decision support;
- canonical URL;
- internal links;
- update ownership;
- lead path;
- no material duplicate/thin-content risk.

### Region pages

Create only when there is real regional search intent and enough useful local/contextual information. Do not mass-produce neighborhood pages from a template with trivial substitutions.

### Stage pages

Launch/em-construction/ready pages may be useful indexable collections if they have stable URLs, unique copy and real inventory. Current JavaScript filters should not automatically create indexable faceted combinations.

## 11. Internal linking

Recommended hierarchy:

```text
HOME
-> region hubs
-> stage hubs
-> development pages
-> relevant guides/comparisons
-> commercial CTA
```

Every indexable support page should have a clear path back to the commercial conversion surface.

Avoid orphan pages and avoid excessive exact-match anchors.

## 12. Content and semantic strategy

The current source already supports important entity/intention seeds:

- Tegra;
- São Paulo;
- launches / under construction / ready to move;
- zones and neighborhoods;
- payment/negotiation process;
- project comparison;
- current FAQ.

Priority content clusters should be selected from real demand evidence and mapped to one canonical page each.

Useful families to evaluate:

- branded project queries;
- Tegra + neighborhood/region;
- Tegra + stage;
- comparison/decision queries;
- buying process/negotiation questions;
- high-intent residential queries where MoreNumTegra has a factual inventory answer.

Do not infer volumes without a source.

The historical keyword exports referenced by this project should be versioned or re-ingested with provenance before quantitative prioritization is treated as reproducible.

## 13. Technical SEO priorities

### P0 before initial indexation push

- canonical root;
- `www` redirect decision;
- title/meta description;
- robots/indexability decision;
- sitemap;
- Search Console gate;
- verify no accidental Vercel indexation;
- preserve one H1 and semantic structure already present;
- validate HTTP status/canonical after Green publication.

### P1

- JSON-LD;
- OG/Twitter;
- image alt/size/loading audit;
- Core Web Vitals field/lab evidence when tooling is available;
- JS/rendering audit for the dynamically rendered project grid;
- stable URL design for project/region/stage pages;
- 404/redirect handling as URL surface grows.

### Rendering risk

The development grid is populated by JavaScript. Before relying on project-card text as indexable content, verify rendered HTML accessibility to major crawlers and confirm that key commercial content remains present without requiring fragile interaction.

`CLIENT_RENDERED != RELIABLY_INDEXED`

## 14. Organic measurement

Minimum measurement contract after authorization:

- GSC impressions/clicks/queries/pages;
- index coverage/canonical issues;
- organic landing sessions in GA4;
- form and WhatsApp conversion definitions;
- lead-origin integrity;
- branded vs non-branded segmentation when possible;
- region/project/stage page cohorts after URL expansion.

Do not activate or alter tracking without MoreNumTegra consent/privacy and measurement authorization.

## 15. SEM recommendation

SEM is recommended as a later controlled acquisition layer because MoreNumTegra is a commercial conversion hub with high-intent inventory.

Start only after:

- conversion definition is agreed;
- tracking gate is satisfied;
- landing/canonical production is stable;
- budget and campaign publication are separately authorized.

Initial design candidates:

- branded Tegra/project search;
- high-intent project-name terms;
- region + apartment intent when inventory aligns;
- controlled competitor/conquest evaluation only after legal/brand/landing relevance review;
- negatives and search-term review from the beginning.

No campaign, bid, budget or spend is authorized by this provider result.

## 16. Authority and backlinks

Authority & Digital PR is still a TARGET SES role, not an active adopted provider role in the current framework.

Current recommendation is policy-level only:

- earn links through useful inventory/data/content;
- partnerships/editorial references only when legitimate;
- no PBN;
- no network of domains whose primary purpose is linking to MoreNumTegra;
- no paid links intended to manipulate rankings.

When the SES role becomes active/adopted, perform a dedicated authority strategy.

## 17. Files / surfaces MoreNumTegra will likely need to change

Implementation should be decided in MoreNumTegra, but expected targets include:

- Green page head/settings or the production surface that controls title/meta/canonical/OG/schema;
- `src-greenn/blocks/01-html-inicial.html` if structured/semantic body adjustments are needed;
- Vercel/production robots controls;
- sitemap asset/generation mechanism;
- future canonical route files for project/region/stage pages;
- project documentation for Search Console/analytics configuration and proof.

Do not assume the body block can control Green's `<head>`; that dependency must be confirmed by the consumer before implementation.

## 18. Green-specific dependencies

Need confirmation from MoreNumTegra/Green during implementation planning:

1. where `<title>`, meta tags, canonical and head scripts can be configured;
2. whether Green supports true 301/308 for the `www` hostname;
3. whether `/robots.txt` and `/sitemap.xml` can be controlled directly;
4. how arbitrary JSON-LD can be injected safely;
5. whether stable subpaths/pages can be created for future SEO architecture;
6. whether page settings alter social metadata independently.

If Green cannot satisfy a material technical requirement, return the constraint to MoreNumTegra Architecture/Product Authority rather than introducing a new platform unilaterally.

## 19. Mandatory initial-indexation set vs later evolution

### Mandatory / P0

- final canonical root;
- hostname consistency;
- unique title/meta description;
- explicit indexability decision;
- sitemap;
- Search Console property + sitemap submission when authorized;
- Vercel noindex separation;
- post-publication HTTP/canonical smoke.

### Strongly recommended / P1

- JSON-LD WebSite/WebPage;
- OG/Twitter;
- rendered-content validation;
- CWV baseline;
- project/region/stage URL architecture design;
- internal-link map;
- measurement plan.

### Later / P2

- SEM campaigns after conversion/spend gates;
- broader editorial clusters after demand analysis;
- Authority/Digital PR after SES eligibility/adoption;
- additional ecosystem properties only after portfolio-fit review.

## 20. Handoff back to MoreNumTegra

This document is the provider result requested by `handoffs/SEARCH_PROVIDER_HANDOFF_2026-08-28.md`.

Required next consumer action:

```text
MORENUMTEGRA
-> review/adjudicate this provider result
-> decide P0 implementation scope
-> authorize exact repository/product changes
-> branch + PR
-> Vercel Preview
-> Search validation
-> merge
-> Vercel Production
-> Green Sales
-> production HTTP/Search smoke
```

No consumer mutation, DNS change, Search Console setup, analytics activation, campaign publication or spend was executed by the provider.
