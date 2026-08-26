# Handoff Atual — Ecossistema de Blogs, Sites, Portais e SEO

- Status: continuidade operacional baseada em estado live
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Specialist model: SES shared specialists + Project Adapter + project-local adoption
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Objetivo operacional

Retomada entre conversas e especialistas com fonte, revisões, lacunas, bloqueios, autorizações e transições explícitas, sem depender de identidades GPT numeradas para novo roteamento.

## Estado confirmado

1. A arquitetura canônica de especialistas pertence ao SES e usa `CANONICAL_NAME + ARCHETYPE_ID`.
2. Este projeto adota especialistas por `ROLE -> ARCHETYPE_ID` em `config/specialists.yaml` e via Project Adapter SES.
3. `config/gpts.yaml` e seus Builders/skills/tests permanecem apenas como continuidade/história e exceções project-local explicitadas.
4. A Action GitHub project-local permanece `READ_ONLY`.
5. O gate documental é `documentation_audit` / `documentation-auditor`, head-bound.
6. O gate de lifecycle é governança project-local SFJM, head+base-bound.
7. Ready e merge são separados e exigem head/base atuais e autorizações separadas.
8. Local SEO e Authority & Digital PR permanecem TARGET no SES; não podem ser tratados como archetypes ativos/adotados antes da certificação/registro.
9. Monetização permanece capability project-local sem replacement SES canônico neste momento.
10. SES registra MoreNumTegra com `ADOPTED_VIA_CROSS_PROJECT_SERVICE` para `seo_strategy`, `technical_seo`, `content_semantic_seo`, `seo_analytics_growth` e `paid_search_sem`, tendo este projeto como provider, sem transferência de código, arquitetura, UX/UI, release, spend/publication ou autoridade de produção.
11. O repo `wagnerjfjunior/MoreNumTegra` permanece fonte canônica da implementação do ativo.
12. `moreemumtegra.com.br` permanece `USER_REPORTED_PURCHASED`; ownership, DNS e conexão de produção não estão verificados por este registro.

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` canônica project-local | aprovada | governança |
| Specialist identity SES | canônica | SES Canonical Specialist Framework |
| Specialist adoption project-local | migração proposta | `config/specialists.yaml` |
| Legacy GPT registry | continuidade/história | `config/gpts.yaml` |
| SFJM operacional | aprovado | Product Authority |
| Tabela e manifesto autoritativos | aprovado | `NEXT_SAFE_ACTION` e `sfjm.yaml` |
| Estado volátil não versionado | aprovado | política SFJM |
| MoreNumTegra Search service | decisão SES vigente; continuidade project-local candidata até integração desta PR | SES current adoption matrix + `docs/assets/morenumtegra-seo-handoff.md` |
| Implementação MoreNumTegra | permanece no repo consumidor | `wagnerjfjunior/MoreNumTegra` |

## Entregas duráveis

Framework local legado preservado como evidência, estrutura SFJM, evidência upstream, máquina de lifecycle, validador, testes adversariais, migração SES project-local e handoff SEO candidato do MoreNumTegra.

## Trabalho em andamento

Concluir a normalização consumer-side para SES sem apagar história nem declarar Builder retirement; integrar o handoff MoreNumTegra usando somente roles/archetypes canônicos; calcular lifecycle live pela máquina e não declarar snapshot neste arquivo.

## Lacunas

Builder live, inventário completo de ativos, ambientes, métricas e produção precisam de revalidação específica. Builders legados só podem ser aposentados individualmente após equivalência, runtime proof e autorização. Local SEO e Authority/Digital PR aguardam elegibilidade SES. O handoff MoreNumTegra não prova provider runtime execution, ownership/DNS nem tracking ativo.

## Riscos ativos

| Risco | Controle |
|---|---|
| Nomenclatura GPT numerada voltar ao roteamento | `config/specialists.yaml` + testes de regressão |
| PR antiga reintroduzir taxonomia legada | reconciliar/encerrar PRs superseded e portar conteúdo útil para branches SES-aligned |
| Gate ou autorização de outra revisão | exigir head/base exatos |
| Merge ref confundido com head | checkout explícito do head |
| Gate não passante avançar | transições de parada |
| Estado terminal sem ação | transições merged/closed |
| SES adoption confundida com Builder retirement | gate separado por Builder |
| Handoff SEO confundido com autorização de implementação | fronteira de autoridade explícita por projeto |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Ações bloqueadas

Mutações sem autorização, gate não passante, merge sem autorização, Builder retirement sem equivalência/autorização, deploy, produção, DNS, analytics, campanhas e SFJM experimental.

## Ordem de continuidade

1. `bootstrap/BOOTSTRAP_CANONICO.md`
2. `handoffs/CURRENT.md`
3. `docs/PROJECT_STATUS.md`
4. `docs/NEXT_SAFE_ACTION.md`
5. `docs/BLOCKED_ACTIONS.md`
6. `config/project.yaml`
7. `config/specialists.yaml`

## Prompt curto

> Resolva projeto e role via SES/Adapter, reconstrua o contexto project-local, resolva PR/head/base/workflow/gates/autorizações/review live e execute somente a primeira transição segura.
