# Handoff SEO — MoreNumTegra

- Status: `CANDIDATE_ON_MAIN_BASED_PR`
- Data: `2026-08-26`
- Ecossistema receptor: `blogs-sites-portais-seo`
- Ativo: `morenumtegra`
- Owner / Product Authority: Wagner
- Implementação canônica do ativo: `wagnerjfjunior/MoreNumTegra`
- Regra de revisão: resolver `main` live do ecossistema e do ativo antes de qualquer decisão material

## 1. Decisão de handoff

O **Ecossistema de Blogs, Sites, Portais e SEO** passa a atuar como Search Center of Expertise / specialist-service provider do MoreNumTegra para as roles Search explicitamente registradas no SES. MoreNumTegra permanece Product Authority.

Este handoff não move o código do MoreNumTegra para este repositório e não transfere autoridade de implementação, release ou produção.

```text
SEARCH STRATEGY / TECHNICAL SEO / CONTENT-SEMANTIC SEO / SEARCH ANALYTICS / PAID SEARCH
-> wagnerjfjunior/Blogs-sites-portais-seo

PRODUCT / ARCHITECTURE / UX-UI / CODE / RELEASE / VERCEL / GREEN SALES / SPEND-PUBLICATION AUTHORITY
-> wagnerjfjunior/MoreNumTegra
```

O MoreNumTegra permanece projeto consumidor autônomo, com bootstrap, baselines, lifecycle, bloqueios e fonte canônica próprios.

## 2. Estado do ativo observado no handoff

Estado observado em `2026-08-26`:

```text
REPOSITORY: wagnerjfjunior/MoreNumTegra
BRANCH: main
OBSERVED_MAIN_SHA: 3207c7bfe25de6d1636663096b01b98e2733686a
```

Esse SHA é evidência temporal do handoff. Sempre resolver `main` live antes de trabalho material.

Estado conhecido pelo bootstrap do ativo:

- HTML5 + CSS + JavaScript vanilla;
- Vercel como homologação pública;
- Green Sales como produção comercial V1;
- Vercel `noindex, nofollow` até decisão específica;
- Form 46 nativo Green Sales como captação V1;
- catálogo com 19 empreendimentos, sujeito a revalidação factual/comercial antes da Green;
- analytics, GTM, GA4, Meta Pixel, DNS e integrações externas permanecem gates separados.

## 3. Domínio

```text
DOMAIN: moreemumtegra.com.br
STATUS: USER_REPORTED_PURCHASED
OWNERSHIP_VERIFIED: false
DNS_VERIFIED: false
PRODUCTION_CONNECTED: false
```

O domínio pode ser considerado no planejamento, mas este registro não autoriza DNS, nameservers, publicação, remoção de `noindex`, Search Console ou analytics.

## 4. Evidência de pesquisa fornecida pelo owner

Foram fornecidos em `2026-08-26` dois exports de pesquisa de palavras-chave, não versionados neste repositório:

1. `Keyword Stats 2026-08-26 at 15_23_07_cyrela_google_e_parceiros.csv`
   - período declarado: `1 de agosto de 2025 - 31 de julho de 2026`;
   - 2.182 linhas de keywords, excluindo título/período/cabeçalho.
2. `Keyword Stats 2026-08-26 at 15_22_21Tegra_parceiros.csv`
   - período declarado: `1 de agosto de 2025 - 31 de julho de 2026`;
   - 1.937 linhas de keywords, excluindo título/período/cabeçalho.

```text
SOURCE_CLASS: USER_PROVIDED_KEYWORD_EXPORT
RAW_FILES_IN_REPOSITORY: false
METRICS_MUST_NOT_BE_INVENTED: true
VOLUMES_MUST_BE_INTERPRETED_WITH_TOOL_LIMITATIONS: true
```

Qualquer número derivado desses arquivos deve registrar fonte, data, período e limitações da ferramenta.

## 5. Responsabilidades via SES

Novo roteamento usa somente `ROLE -> ARCHETYPE_ID`, conforme `config/specialists.yaml`, SES `projects/SPECIALIST_ADOPTION_MATRIX_CURRENT.md` e os Project Adapters aplicáveis. Para MoreNumTegra, as cinco roles abaixo permanecem `ADOPTED`; a execução usa metadata project-local `EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE` com `SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo`.

### `seo_strategy -> seo-strategy-governance-specialist`

Responsável por Search Market Intelligence, diagnóstico de SERP/mercado, macro keyword strategy, concorrência, priorização, SEO/GEO governance e coordenação dos especialistas Search.

### `content_semantic_seo -> content-semantic-seo-specialist`

Responsável por intent mapping, entidades, topical coverage, clusters editoriais, on-page, internal linking, answerability, citability e conteúdo-side GEO.

### `technical_seo -> technical-seo-specialist`

Responsável por crawl/indexação, canonicalização, robots/sitemap, rendering, structured data, performance/Core Web Vitals e requisitos técnicos de lançamento do domínio comercial.

### `seo_analytics_growth -> seo-analytics-growth-specialist`

Responsável por GSC/GA4, integridade de KPIs, conversões, limites de atribuição, experimentação e análise de crescimento orgânico. Fica condicionado ao gate específico de mensuração; não presumir tracking configurado.

### `paid_search_sem -> paid-search-sem-specialist`

Responsável por estratégia/análise de Paid Search e overlap SEO/SEM quando explicitamente solicitado. Não autoriza spend, campanhas ou publicação.

### Handoffs fora do provider Search

`architecture -> software-systems-architect` e `ux_ui -> ux-ui-app-specialist` permanecem roles diretas do MoreNumTegra. O projeto Blogs pode devolver findings/recomendações a essas roles, mas não as executa como parte deste serviço cross-project sem uma decisão posterior explícita.

### Targets ainda não adotáveis

`Local SEO` e `Authority & Digital PR` permanecem `TARGET / CERTIFICATION_PENDING / NOT_YET_REGISTERED` no SES e não devem ser tratados como archetypes ativos/adotados.

Enquanto `authority-digital-pr-specialist` não estiver elegível/adotado, a capability histórica de autoridade externa permanece continuidade controlada e não deve receber novo roteamento SES fictício.

## 6. Política para novos domínios e autoridade

A compra de domínio adicional exige antes da recomendação:

1. tese própria;
2. público/intenção próprios;
3. proposta de valor própria;
4. owner definido;
5. papel no portfólio;
6. justificativa de por que uma URL no domínio existente não resolve melhor;
7. risco de canibalização/duplicação;
8. plano de conteúdo e manutenção;
9. política de links compatível com diretrizes de busca.

`KEYWORD_VOLUME != DOMAIN_JUSTIFICATION`.

Não criar rede de domínios com finalidade principal de gerar backlinks ao MoreNumTegra. Não autorizar PBN, compra de links para manipulação de ranking ou troca excessiva de links.

## 7. Fronteira de autoridade

Este handoff autoriza governança e análise SEO dentro do Ecossistema. Não autoriza mutação em:

- `wagnerjfjunior/MoreNumTegra`;
- Green Sales;
- Vercel;
- domínio/DNS;
- Search Console;
- GA4/GTM/Meta Pixel;
- campanhas Ads;
- aquisição de novos domínios;
- contratação/compra de backlinks.

Implementações propostas pelo ecossistema retornam ao projeto consumidor e seguem o lifecycle/authority do MoreNumTegra.

## 8. Próxima etapa SEO após integração deste handoff

Em modo read-only:

```text
seo_strategy
-> content_semantic_seo
-> technical_seo
-> seo_analytics_growth quando houver gate de mensuração
-> paid_search_sem quando explicitamente aplicável
```

`architecture` e `ux_ui` são handoffs de volta ao MoreNumTegra quando necessários. Local SEO e Authority/Digital PR entram somente após elegibilidade SES + ativação/adopção explícita posterior.

## 9. Critério de sucesso do handoff

O handoff está completo quando:

- o ecossistema reconhece MoreNumTegra como ativo SEO gerenciado;
- o repo `MoreNumTegra` permanece fonte canônica da implementação;
- domínio mantém status de evidência correto, sem presumir DNS;
- fontes de keyword research permanecem rastreáveis;
- responsabilidades são expressas por roles/archetypes SES canônicos;
- nenhuma autoridade de produção ou mutação é propagada implicitamente;
- architecture/UX do MoreNumTegra não são apropriados pelo provider Search.
