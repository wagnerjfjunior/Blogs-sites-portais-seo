# Migração de especialistas para SES — V1

## Status

`MIGRATION_CANDIDATE / PR_ONLY / NO_LEGACY_BUILDER_RETIREMENT`

## Âncoras

- Projeto consumidor: `wagnerjfjunior/Blogs-sites-portais-seo`
- Base da migração: `main@8c7f3380582b9c2f2997600c746e9054978ff64d`
- SES framework observado: `wagnerjfjunior/Specialist-Engineering-System@e61598ced19e0e846b85d369e692943fee4e3487`
- Framework: `docs/architecture/CANONICAL_SPECIALIST_FRAMEWORK.md`
- Política: `docs/migrations/LEGACY_SPECIALIST_IDENTITY_MIGRATION_PLAN.md`
- Autoridade de preparação desta PR: Wagner

## Objetivo

Migrar o roteamento novo do projeto da taxonomia local GPT0–GPT8 para o modelo SES compartilhado `ROLE -> ARCHETYPE_ID`, preservando história, contratos, Builder IDs, URLs, skills, testes e evidências legadas até gates explícitos de equivalência e retirement.

```text
LEGACY_LABEL != CANONICAL_IDENTITY
MIGRATION != HISTORY_REWRITE
ADOPTION != LEGACY_BUILDER_RETIREMENT
RENAME != BEHAVIORAL_EQUIVALENCE
RETROACTIVE_PASS = NO
```

## Fonte de roteamento após a migração

`config/specialists.yaml` passa a ser a fonte project-local para adoção e boundaries de especialistas SES.

`config/gpts.yaml` permanece preservado como registry de continuidade/história e deixa de ser autoridade para novo roteamento.

## De/para e equivalência

| Legado | Função histórica | Role SES / destino | Equivalência | Estado de Builder legado |
|---|---|---|---|---|
| `gpt0` | auditoria documental | `documentation_audit -> documentation-auditor` | PARTIAL | preservar; retirement não autorizado |
| `gpt1` | arquitetura do ecossistema | `architecture -> software-systems-architect` + overlap `seo_strategy` | PARTIAL/OVERLAPPING | preservar; retirement não autorizado |
| `gpt2` | mercado/keywords | `seo_strategy` + `content_semantic_seo` | OVERLAPPING | preservar; retirement não autorizado |
| `gpt3` | SEO técnico | `technical_seo -> technical-seo-specialist` | PARTIAL | preservar; retirement não autorizado |
| `gpt4` | GitHub/lifecycle/publicação | `PROJECT_SFJM_GOVERNANCE` | NO_EQUIVALENT | preservar evidência; retirement exige gate próprio |
| `gpt5` | conteúdo/topical authority | `content_semantic_seo -> content-semantic-seo-specialist` | PARTIAL | preservar; retirement não autorizado |
| `gpt6` | authority/link/Digital PR | TARGET SES ainda não adotável | NOT_DETERMINED | continuidade somente até certificação/adoption |
| `gpt7` | monetização | projeto-local; sem archetype SES canônico | NO_EQUIVALENT | exceção ativa project-local |
| `gpt8` | analytics/growth | `seo_analytics_growth -> seo-analytics-growth-specialist` | PARTIAL | preservar; retirement não autorizado |

## Novos especialistas sem legado local equivalente

O projeto já pode adotar via SES, sem criar GPT project-local duplicado:

- `ux_ui -> ux-ui-app-specialist`;
- `application_security -> application-security-assurance-specialist`;
- `paid_search_sem -> paid-search-sem-specialist`.

`backend_data` permanece explicitamente não adotado até necessidade material.

## Search domain

A coordenação de Search passa a usar os nomes canônicos:

- SES — SEO Strategy & Governance Specialist;
- SES — Technical SEO Specialist;
- SES — Content & Semantic SEO Specialist;
- SES — SEO Analytics & Growth Specialist;
- SES — Paid Search & SEM Specialist.

Local SEO e Authority & Digital PR permanecem TARGET no SES e não devem ser representados como archetypes ativos/certificados/adotados antes dos respectivos gates.

GEO permanece capacidade transversal, não um especialista isolado.

## Lifecycle project-local

A máquina SFJM deixa de depender de nomes GPT numerados:

- gate documental: `documentation_audit`, executado pelo `documentation-auditor`, head-bound;
- gate de lifecycle: `PROJECT_SFJM_GOVERNANCE`, head+base-bound;
- Ready e merge continuam decisões separadas;
- nenhuma autorização se propaga.

O antigo `gpt4` não recebe um archetype fictício. Sua função de lifecycle é absorvida pela governança project-local/SFJM; seus artefatos históricos permanecem preservados até eventual retirement autorizado.

## Builder

Esta PR atualiza a governança do Builder, mas **não altera os Custom GPTs externos** e não declara equivalência runtime.

Todos os manifests em `config/builder/gpt*.yaml`, Instructions em `docs/gpts/*-builder-instructions.md`, contratos, skills e suites `tests/gpts/` permanecem addressable como evidência histórica/project-local.

O plano detalhado de Builder está em `docs/migrations/LEGACY_BUILDER_MIGRATION_PLAN.md`.

## PRs concorrentes observadas na base

Na preparação desta migração foram observadas PRs abertas que ainda usam o modelo legado:

- PR #5 — adoção SES anterior que preserva GPT0–GPT8 como modelo operacional;
- PR #6 — handoff MoreNumTegra contendo responsabilidades por GPT1/GPT2/GPT3/GPT5/GPT6/GPT8;
- PR #4 — evidência histórica de Builder GPT0.

Esta PR não fecha nem reescreve essas PRs automaticamente. Antes de merge, qualquer PR concorrente que possa reintroduzir nomenclatura operacional antiga deve ser reconciliada/rebaseada ou explicitamente supersedida.

## Companion change no SES

Após a integração consumer-side, o SES Project Adapter `projects/blogs-sites-portais-seo/PROJECT_ADAPTER.md` precisa de atualização coordenada para:

- usar `config/specialists.yaml` como project-local specialist adoption locator;
- remover `config/gpts.yaml` como fonte de novo roteamento;
- manter `config/gpts.yaml` apenas como legacy continuity/history locator;
- refletir lifecycle project-local sem `GPT4` como identidade canônica;
- preservar regras de retirement do SES.

Essa alteração pertence ao repositório SES e deve ocorrer em PR separada para manter a autoridade de cada repositório.

## Critérios de conclusão da migração

A migração de identidade consumer-side está pronta para merge somente se:

1. `config/specialists.yaml` for validado;
2. bootstrap, handoff, status, SFJM, bloqueios e próxima ação usarem roles canônicas;
3. validator e testes rejeitarem regressão para roteamento GPT numerado;
4. os assets legados permanecerem addressable;
5. nenhum Builder externo for declarado migrado sem prova;
6. a PR #5/#6 for reconciliada para não reintroduzir drift;
7. gates e autorizações do head/base exatos forem satisfeitos.

Builder retirement permanece uma fase posterior e separada.
