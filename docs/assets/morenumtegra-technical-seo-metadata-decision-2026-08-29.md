# MoreNumTegra — Technical SEO Metadata Decision — 2026-08-29

## Status

`PROVIDER_TECHNICAL_SEO_DECISION / PREVIEW_APPROVED_WITH_RESIDUAL_RISK / NO_CONSUMER_MUTATION_AUTHORITY`

## 1. Target

Consumer:

`wagnerjfjunior/MoreNumTegra`

Observed PR:

`#32`

Observed consumer head before this provider record:

`287793959a1da8667f042b8177d4476ad43e6821`

Commercial canonical target:

`https://moretegra.com.br/`

## 2. Scope approved by Product Authority

The owner explicitly approved the package shown in-chat after the implementation summary:

- stable commercial title;
- stable commercial meta description;
- canonical target;
- Open Graph metadata;
- Twitter metadata;
- conservative JSON-LD `WebSite + WebPage`;
- award copy;
- two Nova Vivere conversion cards on the same home;
- Nova Vivere 105 m² cash-offer card;
- no outbound SECOVI CTA.

This approval does not authorize merge or Green publication.

## 3. Title and description

Keep the homepage centered on the primary commercial intent, not on the award.

Title:

`Apartamentos Tegra em São Paulo | More em um Tegra`

Description:

`Compare empreendimentos Tegra em São Paulo por região, estágio e faixa de valor. Veja lançamentos, prontos para morar e opções no premiado Caminhos da Lapa.`

Reason:

- preserves core entity + geo + commercial intent;
- uses the award as supporting authority rather than replacing the page topic;
- avoids volatile unit price in stable homepage metadata.

## 4. Canonical via JavaScript

Current Green composition does not provide a separately versioned head artifact in the GitHub-to-Green copy workflow.

Google Search Central currently documents that canonicalization can occur before and after rendering and specifically recommends that JavaScript-generated canonical signals remain consistent with the original HTML; when an original canonical cannot be set, leaving it absent before JavaScript is preferable to creating conflicting signals.

Official source:

`https://developers.google.com/search/docs/crawling-indexing/canonicalization`

Google Search documentation update notes also record the JavaScript canonicalization clarification:

`https://developers.google.com/search/updates`

### Decision

Allow JS to create/update:

`<link rel="canonical" href="https://moretegra.com.br/">`

only under these conditions:

1. no conflicting canonical exists in the initial commercial Green HTML;
2. Vercel Preview may contain the same commercial canonical while remaining `noindex,nofollow`;
3. no JavaScript path may rewrite the canonical to a Vercel hostname;
4. post-Green smoke must inspect the rendered head when access allows.

### Residual risk

`PASS_WITH_RESIDUAL_RISK`

Static-server canonical remains preferable when Green exposes a reliable head/canonical capability. Client-side canonical is accepted here as the practical current transport, not as a universal preference.

`JS_CANONICAL_ACCEPTED != STATIC_CANONICAL_PROVEN`

## 5. Open Graph and Twitter

Approved as social/discovery metadata.

These fields are not treated as Google ranking factors and do not replace title/meta/canonical.

Approved:

- `og:type=website`;
- `og:url`;
- `og:title`;
- `og:description`;
- `og:locale`;
- `og:site_name`;
- `twitter:card`;
- `twitter:title`;
- `twitter:description`.

No image claim is added until a durable approved social image exists.

## 6. JSON-LD

Approved conservative graph:

- `WebSite`;
- `WebPage`.

Google supports structured data generated with JavaScript, but structured data presence does not guarantee rich results.

Official Google documentation includes JavaScript-generated structured data in the supported implementation flow:

`https://developers.google.com/search/docs/appearance/structured-data/education-qa`

The cited page is schema-specific but points to Google's supported JavaScript generation guidance. The general invariant remains:

`VALID_SCHEMA != RICH_RESULT_GRANTED`

### Explicitly not approved in this package

- award schema invented from unsupported types;
- `AggregateRating`;
- self-authored `Review`;
- `Product`/price schema for volatile homepage unit offers;
- artificial organization facts not present in visible/reliable sources.

## 7. Vercel boundary

Vercel is homologation, not commercial origin.

It must remain:

`noindex,nofollow`

A commercial canonical pointing to `https://moretegra.com.br/` does not authorize Vercel indexation.

`NOINDEX_VERCEL + COMMERCIAL_CANONICAL != VERCEL_INDEXABLE`

## 8. Cash-offer metadata boundary

Nova Vivere unit 708 / R$ 1.129.900 is a conversion claim, not stable homepage metadata.

Do not place the volatile unit price in:

- homepage `<title>`;
- homepage meta description;
- canonical;
- WebSite/WebPage JSON-LD.

Keep it visible in the card with unit/condition disclaimer and evidence path.

## 9. Verdict

`PASS_WITH_RESIDUAL_RISK`

Passing scope:

- Search metadata package for PR #32 Preview/lifecycle progression;
- award semantics/copy;
- Nova Vivere two-card home strategy;
- JS canonical under the conditions above;
- OG/Twitter;
- WebSite/WebPage JSON-LD.

Residual risks:

1. client-side canonical is weaker operationally than a proven static/head implementation;
2. Green rendered-head smoke has not yet occurred;
3. Nova Vivere unit 708 availability/condition is volatile and must be reconfirmed before Green.

This decision does not authorize Ready, merge, Vercel Production promotion or Green publication.
