# MoreNumTegra — Search Guidance — Prêmio Master Imobiliário 2026

## Status

`PROVIDER_SEARCH_GUIDANCE / CROSS_PROJECT / NO_CONSUMER_MUTATION_AUTHORITY`

## 1. Scope

This document records the Search/SEO interpretation of the 2026 Prêmio Master Imobiliário recognition for use by MoreNumTegra.

Consumer / Product Authority:

`wagnerjfjunior/MoreNumTegra`

Search provider:

`wagnerjfjunior/Blogs-sites-portais-seo`

Consumer implementation observed for this assessment:

- PR #32 — `feat: destacar Prêmio Master Imobiliário 2026`
- base: `4202356b6199fef720919eb639168aa4158ae3d8`
- head observed: `38a8c20de236c9fda75b0b57236df94592803c1a`
- implementation surfaces: `src-greenn/blocks/01-html-inicial.html`, `src-greenn/moretegra.css`, `src-greenn/moretegra.js`

PR lifecycle state is volatile and must be resolved live. This document does not authorize consumer mutation, Ready, merge, Vercel Production or Green publication.

## 2. Authoritative factual evidence

Primary external source:

SECOVI-SP — Conheça os vencedores do Prêmio Master Imobiliário 2026  
https://secovi.com.br/conheca-os-vencedores-do-premio-master-imobiliario-2026/

Observed on 2026-08-29:

1. `Profissional – Soluções Arquitetônicas`
   - Empresa: Tegra
   - Case: `RIIO BY PIERO LISONI - O Rio com alma italiana`
   - Localização: Rio de Janeiro/RJ

2. `Empreendimento – Qualificação Urbana`
   - Empresas: `Helbor | Toledo Ferrari | Tegra`
   - Case: `Caminhos da Lapa: redesenhando um bairro`
   - Localização: São Paulo/SP

The second recognition is for the Caminhos da Lapa case/masterplan, not proof that each condominium/phase individually won a separate award.

## 3. Product/masterplan relationship evidence

Official Tegra pages support a relationship between current MoreNumTegra catalog entries and the Caminhos da Lapa complex:

- Nova Vivere: official Tegra page describes it as a new address/project of the `complexo Caminhos da Lapa`.
  - https://www.tegraincorporadora.com.br/sp/sao-paulo/oeste/lapa/novavivere
- Garden Design: official Tegra page describes it as a project of the `complexo Caminhos da Lapa`.
  - https://www.tegraincorporadora.com.br/sp/sao-paulo/oeste/lapa/gardendesignprivateparkresidence
- Caminhos da Lapa Elo Duo: the official product name and legal text explicitly associate it with Caminhos da Lapa.
  - https://www.tegraincorporadora.com.br/sp/sao-paulo/oeste/lapa/caminhos-da-lapa-elo-duo
- Reserva Caminhos da Lapa: official Tegra product naming supports the relationship.
  - https://www.tegraincorporadora.com.br/sp/sao-paulo/oeste/lapa/reserva-caminhos-da-lapa

Therefore, MoreNumTegra may factually communicate that these projects are part of the award-winning Caminhos da Lapa masterplan/complex, provided the wording does not state or imply that each individual project independently received the 2026 award.

## 4. Search copy decision

### Institutional block

Recommended primary heading:

`Tegra recebe dois reconhecimentos no Prêmio Master Imobiliário 2026`

Recommended supporting copy:

`Em 2026, o Prêmio Master Imobiliário reconheceu a Tegra em Soluções Arquitetônicas pelo RIIO by Piero Lissoni e premiou o case Caminhos da Lapa, desenvolvido por Helbor, Toledo Ferrari e Tegra, na categoria Qualificação Urbana.`

Why:

- uses the exact award/category entities;
- separates the Tegra-only RIIO recognition from the joint Caminhos da Lapa recognition;
- improves factual extractability for Search/AEO/GEO;
- avoids implying that every Tegra development won an award.

### Award cards

Prefer exact labels over generic marketing abstractions:

- `RIIO BY PIERO LISONI — Soluções Arquitetônicas`
- `Caminhos da Lapa — Qualificação Urbana`

The visible text `Excelência em arquitetura` is acceptable as marketing copy but should not replace the official category name if Search citability is the goal.

## 5. Badge / card rule

For projects that are part of Caminhos da Lapa, the short badge should not read simply:

`PROJETO PREMIADO`

because that can reasonably be interpreted as an individual award for the specific condominium.

Preferred short variants:

- `MASTERPLAN PREMIADO`
- `CAMINHOS DA LAPA · MASTER 2026`
- `PARTE DO MASTERPLAN PREMIADO`

Preferred accessible/expanded label:

`Parte do masterplan Caminhos da Lapa, vencedor do Prêmio Master Imobiliário 2026 na categoria Qualificação Urbana.`

This preserves the commercial value of the visual badge while keeping the claim aligned to the source.

## 6. Source/provenance recommendation

The institutional award block should include a visible editorial citation to the official SECOVI-SP source.

Recommended anchor:

`Fonte: SECOVI-SP — Prêmio Master Imobiliário 2026`

This is not a link-building tactic and should not be treated as a ranking guarantee. Its purpose is factual provenance, trust and extractability.

At the consumer head observed for this assessment, the award block did not contain a visible SECOVI URL in the final HTML source inspected.

## 7. Consumer PR #32 reconciliation finding

Observed inconsistency:

- PR #32 body states that the corner badge applies to Nova Vivere, Caminhos da Lapa Elo Duo and Reserva Caminhos da Lapa;
- the exact JavaScript head observed also applies the award badge to Garden Design.

The Garden Design relationship itself is supported by the official Tegra page, so this is not a factual blocker by itself.

However:

`PR_DESCRIPTION != IMPLEMENTATION_DIFF`

The consumer should reconcile the PR description with the actual four-card implementation before lifecycle completion.

## 8. SEO / AEO / GEO use

The award should be treated as a new factual entity relationship:

`Tegra -> Prêmio Master Imobiliário 2026 -> RIIO by Piero Lissoni -> Soluções Arquitetônicas`

and:

`Caminhos da Lapa -> Prêmio Master Imobiliário 2026 -> Qualificação Urbana -> Helbor + Toledo Ferrari + Tegra`

For future stable Caminhos da Lapa/project pages, this evidence can support:

- concise factual award sections;
- entity disambiguation;
- provenance links;
- internal linking between the masterplan and its component developments;
- answerable FAQ/content only where useful to users;
- structured data only when a suitable schema type and visible factual content are present.

Do not create artificial award schema, reviews or ratings.

## 9. Homepage vs future project pages

Homepage role:

- institutional proof of Tegra recognition;
- concise summary;
- direct relationship to Caminhos da Lapa inventory.

Future project/detail page role:

- explain that the specific project is part of the Caminhos da Lapa masterplan;
- reference the masterplan award precisely;
- avoid saying the individual tower/project won unless a source proves that exact claim.

This distinction supports BOFU product pages without contaminating product-level factual accuracy.

## 10. Ownership boundary

### MoreNumTegra / Product Authority owns

- visual design;
- badge geometry/color/placement;
- catalog eligibility implementation;
- HTML/CSS/JS;
- Vercel Preview;
- publication lifecycle;
- Green publication;
- final commercial risk acceptance.

### Search provider owns

- factual Search wording recommendation;
- semantic precision;
- source/provenance requirement;
- SEO/AEO/GEO interpretation;
- future information-architecture and structured-data recommendation;
- validation that Search claims do not overstate the evidence.

`SEARCH_GUIDANCE != CONSUMER_IMPLEMENTATION_AUTHORITY`

## 11. Provider verdict on the observed basic implementation

`PASS_WITH_REQUIRED_COPY_RECONCILIATION_BEFORE_PUBLICATION`

The concept is valid and the source evidence is strong.

Before Green publication, Search recommends:

1. change the short per-project badge away from `PROJETO PREMIADO` to a masterplan-specific claim;
2. expose the official category names in visible copy;
3. add a visible SECOVI-SP source link;
4. reconcile PR #32 body with the four projects actually carrying the badge.

No consumer mutation was performed by the provider.
