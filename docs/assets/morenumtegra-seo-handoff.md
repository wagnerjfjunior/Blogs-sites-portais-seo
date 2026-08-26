# Handoff SEO — MoreNumTegra

- Status: `CANDIDATE_IN_PR`
- Data: `2026-08-26`
- Ecossistema receptor: `blogs-sites-portais-seo`
- Ativo: `morenumtegra`
- Owner / Product Authority: Wagner
- Implementação canônica do ativo: `wagnerjfjunior/MoreNumTegra`
- Regra de revisão: resolver `main` live do ecossistema e do ativo antes de qualquer decisão material

## 1. Decisão de handoff

A estratégia SEO do MoreNumTegra passa a ser governada pelo **Ecossistema de Blogs, Sites, Portais e SEO**.

Este handoff **não move o código** do MoreNumTegra para este repositório e **não transfere autoridade de implementação, release ou produção**.

Preservar:

```text
SEO PORTFOLIO / RESEARCH / CLUSTERS / CONTENT / AUTHORITY
-> wagnerjfjunior/Blogs-sites-portais-seo

PRODUCT CODE / RELEASE / VERCEL / GREEN SALES
-> wagnerjfjunior/MoreNumTegra
```

O `MoreNumTegra` permanece um projeto consumidor autônomo, com seu próprio bootstrap, baselines, lifecycle, bloqueios e fonte canônica.

## 2. Estado do ativo observado no handoff

Estado live observado em `2026-08-26`:

```text
REPOSITORY: wagnerjfjunior/MoreNumTegra
BRANCH: main
OBSERVED_MAIN_SHA: 3207c7bfe25de6d1636663096b01b98e2733686a
```

Esse SHA é evidência temporal do handoff e **não deve ser congelado** como referência futura. Sempre resolver `main` live antes de trabalho material.

Estado de produto conhecido pelo bootstrap do ativo:

- HTML5 + CSS + JavaScript vanilla;
- Vercel como homologação pública;
- Green Sales como produção comercial V1;
- Vercel `noindex, nofollow` até decisão específica;
- Form 46 nativo Green Sales como captação V1;
- catálogo atual com 19 empreendimentos, sujeito à revalidação factual/comercial antes da Green;
- analytics, GTM, GA4, Meta Pixel, DNS e integrações externas permanecem gates separados.

## 3. Domínio

```text
DOMAIN: moreemumtegra.com.br
STATUS: USER_REPORTED_PURCHASED
OWNERSHIP_VERIFIED: false
DNS_VERIFIED: false
PRODUCTION_CONNECTED: false
```

O domínio é tratado como intenção comercial confirmada pelo owner para planejamento de arquitetura SEO.

Este registro **não autoriza**:

- alteração de DNS;
- alteração de nameservers;
- conexão com Green/Vercel;
- remoção do `noindex` da homologação;
- publicação/indexação orgânica;
- configuração de Search Console ou analytics.

## 4. Evidência de pesquisa fornecida pelo owner

Foram fornecidos em `2026-08-26` dois exports de pesquisa de palavras-chave, não versionados neste repositório:

1. `Keyword Stats 2026-08-26 at 15_23_07_cyrela_google_e_parceiros.csv`
   - período declarado no arquivo: `1 de agosto de 2025 - 31 de julho de 2026`;
   - 2.182 linhas de keywords, excluindo título/período/cabeçalho.

2. `Keyword Stats 2026-08-26 at 15_22_21Tegra_parceiros.csv`
   - período declarado no arquivo: `1 de agosto de 2025 - 31 de julho de 2026`;
   - 1.937 linhas de keywords, excluindo título/período/cabeçalho.

Classificação da evidência:

```text
SOURCE_CLASS: USER_PROVIDED_KEYWORD_EXPORT
RAW_FILES_IN_REPOSITORY: false
METRICS_MUST_NOT_BE_INVENTED: true
VOLUMES_MUST_BE_INTERPRETED_WITH_TOOL_LIMITATIONS: true
```

Qualquer número derivado desses arquivos deve registrar fonte, data, período e limitações da ferramenta.

## 5. Responsabilidades SEO no ecossistema

### GPT1 — SEO - Arquiteto do ecossistema

Responsável por:

- posição do MoreNumTegra no portfólio;
- arquitetura de domínio/propriedades;
- tese para eventual aquisição de novos domínios;
- dependências entre ativos;
- ADR e roadmap de portfólio.

### GPT2 — SEO - Pesquisa de mercado e palavras-chave

Responsável por:

- processar os exports Tegra/Cyrela;
- mapear demanda, intenção, entidades e concorrência;
- criar clusters e priorização;
- separar branded, non-branded, bairro/região, estágio e empreendimento;
- registrar limitações dos dados.

### GPT3 — SEO técnico

Responsável por:

- rastreamento/indexação;
- canonicalização;
- robots/sitemap;
- structured data;
- performance e Core Web Vitals;
- requisitos técnicos de lançamento do domínio comercial.

### GPT5 — SEO - Conteúdo e autoridade temática

Responsável por:

- arquitetura editorial;
- páginas/landing pages justificadas por intenção;
- clusters e links internos;
- briefings e manutenção de conteúdo;
- prevenção de thin/duplicate content.

### GPT6 — SEO - Link building e digital PR

Responsável por:

- link earning;
- digital PR;
- avaliação de prospects e relevância;
- política de backlinks.

Não usar PBN, compra de links para manipular ranking, troca excessiva de links ou múltiplos domínios sem valor próprio apenas para redirecionar autoridade.

### GPT8 — SEO - Analytics e crescimento

Fica posterior ao gate específico de analytics/mensuração. Não presumir GA4, Search Console, conversões ou tracking configurados.

## 6. Política para novos domínios

A compra de um domínio adicional exige, antes da recomendação:

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

Não criar rede de domínios apenas para gerar backlinks ao MoreNumTegra.

## 7. Fronteira de autoridade

Este handoff autoriza somente a **governança estratégica SEO** dentro do Ecossistema.

Não autoriza mutação em:

- `wagnerjfjunior/MoreNumTegra`;
- Green Sales;
- Vercel Production/Preview;
- domínio/DNS;
- Search Console;
- GA4/GTM/Meta Pixel;
- campanhas Ads;
- FECH.AI/n8n/Make;
- aquisição de novos domínios;
- contratação/compra de backlinks.

Implementações propostas pelo ecossistema retornam ao projeto consumidor e seguem o lifecycle/authority do MoreNumTegra.

## 8. Próxima etapa SEO recomendada após integração deste handoff

Executar, em modo read-only e com evidência versionada quando apropriado:

```text
GPT1 — arquitetura do ativo no ecossistema
-> GPT2 — keyword mapping Tegra x Cyrela + clusters
-> GPT5 — arquitetura editorial / internal linking
-> GPT3 — contrato técnico SEO para o domínio de produção
-> GPT6 — autoridade externa / digital PR quando houver ativos publicáveis
-> GPT8 — mensuração somente após gate próprio
```

A ordem pode ser ajustada quando houver evidência material, mas novos domínios e backlinks não devem preceder a tese de arquitetura e o keyword mapping.

## 9. Critério de sucesso do handoff

O handoff está completo quando:

- o ecossistema reconhece MoreNumTegra como ativo SEO gerenciado;
- o repo `MoreNumTegra` permanece fonte canônica de implementação;
- domínio é registrado com status de evidência correto, sem presumir DNS;
- fontes de keyword research ficam rastreáveis;
- responsabilidades GPT1/GPT2/GPT3/GPT5/GPT6/GPT8 ficam explícitas;
- nenhuma autoridade de produção ou mutação é propagada implicitamente.
