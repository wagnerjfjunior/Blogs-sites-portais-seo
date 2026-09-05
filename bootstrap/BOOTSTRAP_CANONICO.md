# Bootstrap Canônico — Ecossistema de Blogs, Sites, Portais e SEO

## Identificação

- Projeto: Ecossistema de Blogs, Sites, Portais e SEO
- ID: `blogs-sites-portais-seo`
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Revisão: resolver head e base live antes de agir
- Autoridade: Wagner
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Objetivo principal

Construir e operar um ecossistema profissional de ativos digitais independentes — sites, blogs, portais, diretórios, ferramentas e domínios temáticos — com audiência, autoridade, aquisição orgânica/paga, leads, receita e valor comercial sustentável.

Cada nova propriedade deve ser posicionada no portfólio antes de implementação para evitar duplicação, canibalização, retrabalho e redes artificiais de links.

Fontes duráveis para esse objetivo:

- estratégia mestra: `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md`;
- inventário/placement de ativos: `config/assets.yaml`;
- pesquisa e lacunas de evidência: `docs/research/SEARCH_RESEARCH_LEDGER.md`.

`NEW_PROJECT != NEW_DOMAIN`

`PORTFOLIO_FIT_BEFORE_IMPLEMENTATION`

`KEYWORD_VOLUME != DOMAIN_JUSTIFICATION`

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

Quando posicionamento de novo projeto/domínio, arquitetura de portfólio ou estratégia do ecossistema for material, ler também `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md`, `config/assets.yaml` e, quando pesquisa anterior influenciar a decisão, `docs/research/SEARCH_RESEARCH_LEDGER.md`.

Quando identidade/migração de especialista, consulta manual ou serviço cross-project for material, resolver também SES live e ler `projects/SPECIALIST_ADOPTION_MATRIX_CURRENT.md` -> versão corrente, o Project Adapter do projeto consumidor/provider, o archetype exato, o ledger de certificação aplicável e `core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md`. `config/gpts.yaml`, `docs/gpts/`, `.agents/skills/`, `config/builder/` e `tests/gpts/` são fontes legadas de continuidade/evidência e só devem ser lidas quando a tarefa exigir compatibilidade, histórico ou retirement.

Quando a tarefa envolver MoreNumTegra Search, resolver `wagnerjfjunior/MoreNumTegra` live e consumir o handoff project-local vigente antes de emitir recomendação.

## Estado confirmado

1. Novo roteamento usa `ROLE -> ARCHETYPE_ID` via SES/Project Adapter e `config/specialists.yaml`; em handoff manual, o destino humano usa obrigatoriamente o `CANONICAL_NAME` do archetype SES, nunca o label GPT legacy.
2. `config/gpts.yaml` permanece preservado como registry legado, sem autoridade de novo roteamento.
3. A Action GitHub project-local inicial é `READ_ONLY`.
4. Escrita direta em `main` é proibida.
5. O gate documental é `documentation_audit` / `documentation-auditor` e é head-bound.
6. O gate de lifecycle pertence à governança SFJM project-local e é head+base-bound; não existe archetype fictício para substituir a antiga identidade de lifecycle.
7. Ready e merge exigem autorizações separadas para head e base.
8. O SFJM é operacional, sem scoring ou benchmark experimental.
9. Builders legados não são aposentados por adoção SES; retirement exige equivalência, testes e autorização explícita.
10. Este projeto é o Search Center of Expertise / provider de `morenumtegra` para `seo_strategy`, `technical_seo`, `content_semantic_seo`, `seo_analytics_growth` e `paid_search_sem`, sem adquirir autoridade sobre produto, código, deploy, orçamento, publicação ou risco do MoreNumTegra.
11. MoreNumTegra é o ativo `P0` do ciclo atual e deve ser posicionado como `COMMERCIAL_CONVERSION_HUB`, sem ser confundido com a totalidade do ecossistema.
12. Novos projetos devem passar pelo portfolio registry e pela tese de placement antes de receber domínio, arquitetura Search ou relacionamento de links.
13. Pesquisa histórica/conversacional só pode influenciar decisão como evidência classificada; fatos atuais exigem revalidação quando a fonte estiver ausente ou stale.

## Lacunas

Builder live, métricas, tráfego, receita e produção exigem verificação específica. O modo project-local cross-project não cria um novo status universal de adoção e não é prova de execução runtime; cada tarefa MoreNumTegra exige contexto live e handoff com provenance de ambos os projetos. Local SEO e Authority & Digital PR ainda não são roles SES adotáveis neste projeto enquanto permanecerem TARGET/certification pending no framework SES. Monetização permanece exceção project-local até existir replacement SES canônico.

## Autorizações

Leitura e gates `READ_ONLY` são permitidos quando forem a primeira transição aplicável. Correção, Ready, merge, Builder, retirement de Builder, deploy, publicação, domínio, DNS, campanha e compromissos exigem autorização explícita.

O provider Search pode auditar e recomendar sobre MoreNumTegra quando o handoff estiver válido; isso não autoriza mutação no consumer.

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Ações bloqueadas

Consulte `docs/BLOCKED_ACTIONS.md`. Ausência na lista não autoriza.

## Retomada

1. Resolver PR, head e base live.
2. Ler a ordem mínima.
3. Resolver strategy/portfolio registry quando placement de ativos for material.
4. Resolver research ledger quando pesquisa histórica puder alterar a decisão.
5. Resolver role/archetype no SES quando houver trabalho de especialista e renderizar `SPECIALIST_TARGET_NAME = ARCHETYPE_REGISTRY.CANONICAL_NAME` para qualquer handoff manual.
6. Para MoreNumTegra, resolver consumer main + handoff Search live.
7. Confirmar workflow no head exato.
8. Separar fatos e lacunas.
9. Calcular a primeira transição.
10. Parar diante de drift, gate não passante, review pendente ou falta de autoridade.

## Atualização

Atualizar somente por mudança durável de fonte, política, ordem, máquina, autoridade, specialist adoption, estratégia, pesquisa canônica ou placement de portfólio; nunca por mero avanço de lifecycle.
