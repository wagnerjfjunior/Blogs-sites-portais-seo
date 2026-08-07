# Bootstrap Canônico — Ecossistema de Blogs, Sites, Portais e SEO

## Identificação

- Projeto: Ecossistema de Blogs, Sites, Portais e SEO
- ID: `blogs-sites-portais-seo`
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Revisão: resolver head e base live antes de agir
- Autoridade: Wagner
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Regra de canonicalidade

`main` aprovada é a fonte de verdade. Estado de PR, head, base, workflow, gates, autorizações, reviews, threads e pós-merge é resolvido live.

Divergência material, `BLOCK` ou `INCONCLUSIVE` exige parada. Informação ausente não é inferida.

## Ordem mínima de leitura

1. `handoffs/CURRENT.md`
2. `docs/PROJECT_STATUS.md`
3. `docs/NEXT_SAFE_ACTION.md`
4. `docs/BLOCKED_ACTIONS.md`
5. `config/project.yaml`
6. `config/gpts.yaml`

Para um GPT específico, leia também contrato, skill, Instructions, manifesto e testes.

## Estado confirmado

1. O projeto possui GPT0 a GPT8, totalizando nove GPTs privados.
2. A Action GitHub inicial é `READ_ONLY`.
3. Escrita direta em `main` é proibida.
4. GPT0 é vinculado ao head; GPT4 ao head e à base.
5. Ready e merge exigem autorizações separadas para head e base.
6. O SFJM é operacional, sem scoring ou benchmark experimental.
7. Adoção do SFJM é rastreada pela PR #2, cujo estado deve ser resolvido live.

## Lacunas

Builder, ativos, domínios, métricas, tráfego, receita e produção exigem verificação específica.

## Autorizações

Leitura, GPT0 e GPT4 `READ_ONLY` são permitidos quando forem a primeira transição. Correção, Ready, merge, Builder, deploy, publicação, domínio, DNS, campanha e compromissos exigem autorização explícita.

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Ações bloqueadas

Consulte `docs/BLOCKED_ACTIONS.md`. Ausência na lista não autoriza.

## Retomada

1. Resolver PR, head e base live.
2. Ler a ordem mínima.
3. Confirmar workflow no head exato.
4. Separar fatos e lacunas.
5. Calcular a primeira transição.
6. Parar diante de drift, gate não passante, review pendente ou falta de autoridade.

## Atualização

Atualizar somente por mudança durável de fonte, política, ordem, máquina, autoridade ou bloqueio material; nunca por mero avanço de lifecycle.
