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

`main` aprovada é a fonte de verdade project-local. Estado de PR, head, base, workflow, gates, autorizações, reviews, threads e pós-merge é resolvido live.

A arquitetura universal de especialistas pertence ao SES. Para identidade, domínio, lifecycle de specialist e nomenclatura, usar o `CANONICAL_SPECIALIST_FRAMEWORK` do SES e o Project Adapter aplicável. Para adoção project-local, usar `config/specialists.yaml`.

Divergência material, `BLOCK` ou `INCONCLUSIVE` exige parada. Informação ausente não é inferida.

## Ordem mínima de leitura

1. `handoffs/CURRENT.md`
2. `docs/PROJECT_STATUS.md`
3. `docs/NEXT_SAFE_ACTION.md`
4. `docs/BLOCKED_ACTIONS.md`
5. `config/project.yaml`
6. `config/specialists.yaml`

Quando identidade/migração de especialista for material, resolver também SES live e ler o Project Adapter, o archetype exato e o ledger de certificação aplicável. `config/gpts.yaml`, `docs/gpts/`, `.agents/skills/`, `config/builder/` e `tests/gpts/` são fontes legadas de continuidade/evidência e só devem ser lidas quando a tarefa exigir compatibilidade, histórico ou retirement.

## Estado confirmado

1. Novo roteamento usa `ROLE -> ARCHETYPE_ID` via SES/Project Adapter e `config/specialists.yaml`.
2. `config/gpts.yaml` permanece preservado como registry legado, sem autoridade de novo roteamento.
3. A Action GitHub project-local inicial é `READ_ONLY`.
4. Escrita direta em `main` é proibida.
5. O gate documental é `documentation_audit` / `documentation-auditor` e é head-bound.
6. O gate de lifecycle pertence à governança SFJM project-local e é head+base-bound; não existe archetype fictício para substituir a antiga identidade de lifecycle.
7. Ready e merge exigem autorizações separadas para head e base.
8. O SFJM é operacional, sem scoring ou benchmark experimental.
9. Builders legados não são aposentados por adoção SES; retirement exige equivalência, testes e autorização explícita.

## Lacunas

Builder live, ativos, domínios, métricas, tráfego, receita e produção exigem verificação específica. Local SEO e Authority & Digital PR ainda não são roles SES adotáveis neste projeto enquanto permanecerem TARGET/certification pending no framework SES. Monetização permanece exceção project-local até existir replacement SES canônico.

## Autorizações

Leitura e gates `READ_ONLY` são permitidos quando forem a primeira transição aplicável. Correção, Ready, merge, Builder, retirement de Builder, deploy, publicação, domínio, DNS, campanha e compromissos exigem autorização explícita.

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Ações bloqueadas

Consulte `docs/BLOCKED_ACTIONS.md`. Ausência na lista não autoriza.

## Retomada

1. Resolver PR, head e base live.
2. Ler a ordem mínima.
3. Resolver role/archetype no SES quando houver trabalho de especialista.
4. Confirmar workflow no head exato.
5. Separar fatos e lacunas.
6. Calcular a primeira transição.
7. Parar diante de drift, gate não passante, review pendente ou falta de autoridade.

## Atualização

Atualizar somente por mudança durável de fonte, política, ordem, máquina, autoridade, specialist adoption ou bloqueio material; nunca por mero avanço de lifecycle.
