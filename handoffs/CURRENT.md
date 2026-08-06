# Handoff Atual — Ecossistema de Blogs, Sites, Portais e SEO

- Status: continuidade operacional baseada em estado live
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Adoção SFJM: PR #2, estado resolvido live
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Objetivo operacional

Retomada entre conversas e especialistas com fonte, revisões, lacunas, bloqueios, autorizações e transições explícitas.

## Estado confirmado

1. Framework GPT0–GPT8 introduzido pela PR #1.
2. Nove GPTs privados.
3. Action GitHub `READ_ONLY`.
4. PR #2 rastreia a adoção SFJM; estado, head, base e workflow são live.
5. GPT0 é head-bound; GPT4 é head+base-bound.
6. Ready e merge são separados e exigem head/base.
7. Estados closed e merged possuem transições.

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` canônica | aprovada | governança |
| SFJM operacional | aprovado para PR #2 | Product Authority |
| Tabela e manifesto autoritativos | aprovado | `NEXT_SAFE_ACTION` e `sfjm.yaml` |
| Estado volátil não versionado | aprovado | política SFJM |

## Entregas duráveis

Framework, estrutura SFJM, evidência upstream, máquina de lifecycle, validador e testes adversariais.

## Trabalho em andamento

Calcular live pela máquina. Não declarar snapshot neste arquivo.

## Lacunas

Builder, inventário de ativos, ambientes, métricas e produção não foram revalidados.

## Riscos ativos

| Risco | Controle |
|---|---|
| Gate ou autorização de outra revisão | exigir head/base exatos |
| Merge ref confundido com head | checkout explícito do head |
| Gate não passante avançar | transições de parada |
| Estado terminal sem ação | transições merged/closed |
| Divergência tabela/manifesto | comparação determinística |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Ações bloqueadas

Mutações sem autorização, gate não passante, merge sem autorização, Builder, deploy, produção e SFJM experimental.

## Ordem de continuidade

1. `bootstrap/BOOTSTRAP_CANONICO.md`
2. `handoffs/CURRENT.md`
3. `docs/PROJECT_STATUS.md`
4. `docs/NEXT_SAFE_ACTION.md`
5. `docs/BLOCKED_ACTIONS.md`
6. `config/project.yaml`
7. `config/gpts.yaml`

## Prompt curto

> Resolva PR, head, base, workflow, gates, autorizações e review live; confirme tabela/manifesto; execute somente a primeira transição.
