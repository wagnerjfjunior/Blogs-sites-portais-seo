# Handoff Atual — Ecossistema de Blogs, Sites, Portais e SEO

- Status: continuidade operacional baseada em estado live
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Adoção SFJM: rastreada pela PR #2; resolver estado live
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Objetivo operacional

Permitir retomada entre conversas e especialistas com fonte, estado resolvido live, lacunas, bloqueios, autorização e máquina de transição explícitos.

## Estado confirmado

1. O framework GPT0–GPT8 foi introduzido pela PR #1.
2. O projeto contém nove GPTs especializados e privados.
3. A Action GitHub dos GPTs permanece `READ_ONLY`.
4. A PR #2 é o registro de adoção do SFJM operacional; Draft/Ready, base, head, checks e autorizações devem ser consultados live.
5. `docs/NEXT_SAFE_ACTION.md` é a autoridade para calcular a próxima transição.
6. GPT0, GPT4, Ready e merge são etapas separadas.
7. GPT0 e GPT4 podem avançar no mesmo head sem commit intermediário.

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` é a fonte canônica | aprovada | `docs/governance/canonical-governance.md` |
| Adotar SFJM operacional | aprovada para a PR #2 | Product Authority |
| Máquina live é autoritativa | aprovada | `config/sfjm.yaml` e `docs/NEXT_SAFE_ACTION.md` |
| Ready e merge são separados | aprovada | `docs/governance/lifecycle-policy.md` |
| Estado volátil não é snapshot versionado | aprovada | `docs/governance/sfjm-continuity-policy.md` |

## Entregas duráveis

- Framework GPT0–GPT8 e governança base.
- Estrutura operacional SFJM na PR #2.
- Evidência upstream e cópia imutável do protocolo.
- Validador de ordem, blob, máquina de transição, evidência e `Next action ID`.
- Testes adversariais de malformed list, diagnóstico, resumos, autorização e evidência.

## Trabalho em andamento

O estágio atual não é declarado neste arquivo. Deve ser calculado pela máquina com base no estado live da PR, do head, do workflow, dos gates, das autorizações, das reviews e das threads.

## Lacunas

- Builder não foi revalidado nesta etapa.
- Não há inventário canônico de domínios, ambientes, métricas ou produção.
- Proteção de branch deve ser consultada live quando afetar lifecycle.
- Evidência de gates e autorizações depende do head exato observado.

## Riscos ativos

| Risco | Impacto | Controle |
|---|---|---|
| Reutilizar gate ou autorização de outro head | decisão inválida | exigir head exato na evidência |
| Estado versionado ficar obsoleto | retomada incorreta | resolver estado live |
| Divergência entre resumos | ação conflitante | validar resumo estruturado e `Next action ID` |
| Finding material após Ready | merge inseguro | rechecagem obrigatória de reviews |
| Escrita direta em `main` | perda de gates | branch e PR |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

Não alterar este handoff apenas para registrar GPT0, GPT4, Ready ou autorização no mesmo head.

## Ações bloqueadas

- qualquer mutação sem autorização específica;
- Ready sem autorização vinculada ao head;
- merge sem autorização posterior e separada;
- Builder, deploy, publicação e produção sem escopo próprio;
- scoring, benchmark, cenário sintético ou avaliação experimental do SFJM.

## Ordem de continuidade

1. `bootstrap/BOOTSTRAP_CANONICO.md`
2. `handoffs/CURRENT.md`
3. `docs/PROJECT_STATUS.md`
4. `docs/NEXT_SAFE_ACTION.md`
5. `docs/BLOCKED_ACTIONS.md`
6. `config/project.yaml`
7. `config/gpts.yaml`

## Prompt curto de retomada

> Resolva `main`, PR, base e head live; leia a ordem de continuidade; confirme o `Next action ID`; identifique a primeira transição aplicável; não infira estado ausente nem execute transição mutável sem autorização específica.
