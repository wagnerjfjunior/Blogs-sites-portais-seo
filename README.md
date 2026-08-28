# Ecossistema de Blogs, Sites, Portais e SEO/SEM

- **ID técnico:** `blogs-sites-portais-seo`
- **Repositório canônico:** `wagnerjfjunior/Blogs-sites-portais-seo`
- **Visibilidade:** privado
- **Specialist model:** SES shared specialists + Project Adapter + project-local adoption
- **Action GitHub project-local:** somente leitura
- **Branch principal:** `main`

Este repositório é a fonte canônica project-local para estratégia, portfolio placement, ativos, Search/SEM, SFJM, bloqueios, evidências e autoridade. A arquitetura universal de especialistas pertence ao `wagnerjfjunior/Specialist-Engineering-System`.

## Objetivo principal

Construir uma rede sustentável de ativos digitais independentes — sites, blogs, portais, diretórios, ferramentas e domínios temáticos — com audiência, autoridade, descoberta orgânica/paga, leads, monetização e valor comercial próprio.

Cada nova propriedade deve ser encaixada no ecossistema antes de implementação. Um novo projeto não significa automaticamente um novo domínio.

```text
PORTFOLIO_FIT_BEFORE_IMPLEMENTATION
NEW_PROJECT != NEW_DOMAIN
KEYWORD_VOLUME != DOMAIN_JUSTIFICATION
```

A estratégia mestra está em `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md` e o registry de ativos em `config/assets.yaml`.

## Prioridade atual — MoreNumTegra

`MoreNumTegra` é o ativo `P0` do ciclo atual e ocupa o papel primário de `COMMERCIAL_CONVERSION_HUB`.

```text
Consumer / Product Authority:
wagnerjfjunior/MoreNumTegra

Commercial production:
https://moretegra.com.br/

Search Center of Expertise / provider:
wagnerjfjunior/Blogs-sites-portais-seo
```

Este projeto responde por Search nas roles atuais:

- `seo_strategy`;
- `technical_seo`;
- `content_semantic_seo`;
- `seo_analytics_growth`;
- `paid_search_sem`.

MoreNumTegra mantém autoridade sobre produto, arquitetura/UX do consumer, código, deploy, Green/Vercel, DNS, publicação, orçamento/spend e risco.

O handoff e a recomendação Search vigentes estão em:

- `docs/assets/morenumtegra-seo-handoff.md`;
- `docs/assets/morenumtegra-search-provider-recommendation-2026-08-28.md`.

## Ponto de entrada

Comece por `bootstrap/BOOTSTRAP_CANONICO.md`. A máquina autoritativa está em `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml`.

Head, base, estado da PR, workflow, gates, autorizações, reviews, threads e verificação pós-merge são resolvidos live. Documentos versionados armazenam regras duráveis, não snapshots.

## Especialistas

Novo trabalho usa `ROLE -> ARCHETYPE_ID` por meio do SES Project Adapter e de `config/specialists.yaml`.

O antigo registry `config/gpts.yaml`, os manifests `config/builder/gpt*.yaml`, Instructions/contratos em `docs/gpts/`, skills e suites `tests/gpts/` permanecem preservados como continuidade/história e para retirement controlado. Não são mais a taxonomia canônica de novo roteamento.

## Estrutura

- `config/project.yaml`: identidade, políticas e locators da estratégia/portfolio.
- `config/specialists.yaml`: adoção project-local de specialists SES e relações de serviço.
- `config/assets.yaml`: registry e placement dos ativos digitais.
- `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md`: tese e arquitetura mestra do ecossistema.
- `config/gpts.yaml`: registry legado preservado, sem autoridade de novo roteamento.
- `config/sfjm.yaml`: manifesto e transições SFJM.
- `bootstrap/BOOTSTRAP_CANONICO.md`: entrada e ordem.
- `handoffs/CURRENT.md`: contexto durável.
- `docs/PROJECT_STATUS.md`: estado estrutural.
- `docs/NEXT_SAFE_ACTION.md`: tabela autoritativa.
- `docs/BLOCKED_ACTIONS.md`: bloqueios estruturais.
- `docs/assets/`: handoffs e recomendações por ativo.
- `docs/migrations/`: migração SES e Builder legado.
- `docs/evidence/`: evidências canônicas.
- `docs/governance/`: políticas.
- `scripts/validate_repository.py`: validador determinístico.

## Regras essenciais

1. Mudanças por branch e PR.
2. Novo ativo/domínio passa por portfolio-fit antes de implementação.
3. Workflow valida o head exato da PR.
4. `documentation_audit` é head-bound; lifecycle governance é head+base-bound.
5. Somente gates passando permitem Ready ou merge.
6. Ready e merge têm autorizações separadas para head e base.
7. A Action project-local permanece `READ_ONLY`.
8. Informação ausente não é inferida.
9. Divergência material exige parada.
10. `CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED`.
11. Provider Search não recebe autoridade de mutação do consumer.
12. Legacy Builder retirement é separado da adoção SES.
13. PBN, rede artificial de links e domínios sem valor próprio não fazem parte da estratégia.

## Validação

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_builder_action.py
```
