# Provider Input Evidence — MoreNumTegra Search — 2026-08-28

## Status

`READ_ONLY / CROSS_PROJECT_PROVIDER_INPUT / REVISION_BOUND`

## Target

Provider project:

`wagnerjfjunior/Blogs-sites-portais-seo`

Consumer project:

`wagnerjfjunior/MoreNumTegra`

Consumer main resolved for this provider result:

```text
b4cdbc1ac0be9a98112cb74a378571b64cf16e7f
```

## Material consumer sources

### Search provider handoff

```text
path: handoffs/SEARCH_PROVIDER_HANDOFF_2026-08-28.md
blob: 65cf29f8a39c830fe60a0d01d16eae33555bab5a
coverage: INTEGRAL_READ
```

Material facts supplied by the consumer:

- commercial production: `https://moretegra.com.br`;
- homologation: `https://morenumtegra.vercel.app/`;
- state at handoff: `GREEN_COMMERCIAL_V1_FUNCTIONALLY_HOMOLOGATED`;
- root HTTPS and HTTP->HTTPS reported functional;
- `www` reported HTTPS-valid and navigating to root via page-level redirect, without proof of HTTP 301/308;
- 21 developments reported rendered;
- Search preliminaries reported missing/uncertain canonical, JSON-LD, final title/meta, OG/Twitter;
- provider requested to return versioned recommendation for canonical, metadata, robots, sitemap, Search Console, JSON-LD, architecture, content, authority, measurement and SEM;
- no consumer mutation authority transferred.

### Green body source

```text
path: src-greenn/blocks/01-html-inicial.html
blob: 2006b4b086b10623f3ec847be417f9c301a957af
coverage: PARTIAL_READ_FOR_FILE / MATERIAL_SECTIONS_READ
```

Material source observations:

- visible single H1: `Encontre o Tegra que combina com o seu momento.`;
- commercial portfolio framing for São Paulo;
- current visible count = 21 developments;
- stages: launches, under construction, ready to move;
- zone and price filters;
- visible negotiation guidance;
- visible region content;
- visible FAQ;
- disclosure that the page is commercial Tegra Vendas-oriented and does not replace the institutional corporate Tegra site.

The provider did not use this source to claim `<head>` production state because the body block does not itself prove Green head/settings output.

## Provider independent web fetch

The provider attempted independent web retrieval of:

- `https://moretegra.com.br/`;
- exact-domain web search.

The retrieval surface returned no usable production page in this execution. This is recorded as:

```text
PROVIDER_HTTP_FETCH: UNAVAILABLE_IN_EXECUTION
CONSUMER_LIVE_HANDOFF: AVAILABLE
```

Therefore HTTP status, redirect and actual production-head acceptance must be rechecked before implementation acceptance.

## Evidence semantics

```text
CONSUMER_LIVE_HANDOFF_OBSERVED != PROVIDER_INDEPENDENT_HTTP_FETCH
REPOSITORY_BODY_SOURCE != PRODUCTION_HEAD_OUTPUT
RECOMMENDATION != IMPLEMENTATION
IMPLEMENTATION != PRODUCTION_VALIDATION
```

## Dependent provider result

`docs/assets/morenumtegra-search-provider-recommendation-2026-08-28.md`

## Invalidation events

Re-resolve consumer evidence when any of these occur:

- MoreNumTegra main changes materially for Search;
- Green page/head/domain configuration changes;
- canonical/robots/sitemap are implemented;
- Search Console/analytics are activated;
- production hostname/redirect behavior changes;
- project URL architecture expands.
