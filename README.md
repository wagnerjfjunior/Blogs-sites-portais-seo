# Ecossistema de Blogs, Sites, Portais e SEO

- **ID técnico:** `blogs-sites-portais-seo`
- **Repositório canônico:** `wagnerjfjunior/Blogs-sites-portais-seo`
- **Visibilidade:** privado
- **Specialist model:** SES shared specialists + Project Adapter + project-local adoption
- **Action GitHub project-local:** somente leitura
- **Branch principal:** `main`

O repositório é a fonte canônica da verdade project-local: estratégia, ativos, regras, SFJM, bloqueios, evidências e autoridade. A arquitetura universal de especialistas pertence ao `wagnerjfjunior/Specialist-Engineering-System`.

## Ponto de entrada

Comece por `bootstrap/BOOTSTRAP_CANONICO.md`. A máquina autoritativa está em `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml`.

Head, base, estado da PR, workflow, gates, autorizações, reviews, threads e verificação pós-merge são resolvidos live. Documentos versionados armazenam regras duráveis, não snapshots.

## Especialistas

Novo trabalho usa `ROLE -> ARCHETYPE_ID` por meio do SES Project Adapter e de `config/specialists.yaml`.

O antigo registry `config/gpts.yaml`, os manifests `config/builder/gpt*.yaml`, Instructions/contratos em `docs/gpts/`, skills e suites `tests/gpts/` permanecem preservados como continuidade/história e para retirement controlado. Não são mais a taxonomia canônica de novo roteamento.

## Estrutura

- `config/project.yaml`: identidade e políticas.
- `config/specialists.yaml`: adoção project-local de specialists SES e exceções legadas.
- `config/gpts.yaml`: registry legado preservado, sem autoridade de novo roteamento.
- `config/sfjm.yaml`: manifesto e transições SFJM.
- `bootstrap/BOOTSTRAP_CANONICO.md`: entrada e ordem.
- `handoffs/CURRENT.md`: contexto durável.
- `docs/PROJECT_STATUS.md`: estado estrutural.
- `docs/NEXT_SAFE_ACTION.md`: tabela autoritativa.
- `docs/BLOCKED_ACTIONS.md`: bloqueios estruturais.
- `docs/migrations/`: migração SES e Builder legado.
- `docs/evidence/`: evidências canônicas.
- `tests/test_sfjm_validation.py`: testes adversariais SFJM.
- `tests/test_ses_specialist_migration.py`: regressão da migração SES.
- `docs/governance/`: políticas.
- `scripts/validate_repository.py`: validador determinístico.

## Regras essenciais

1. Mudanças por branch e PR.
2. Workflow valida o head exato da PR.
3. `documentation_audit` é head-bound; lifecycle governance é head+base-bound.
4. Somente gates passando permitem Ready ou merge.
5. Ready e merge têm autorizações separadas para head e base.
6. Estados merged e closed continuam calculáveis.
7. A Action project-local permanece `READ_ONLY`.
8. Informação ausente não é inferida.
9. Divergência material exige parada.
10. Estado volátil não é snapshot versionado.
11. `CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED`.
12. Legacy Builder retirement é separado da adoção SES.

## Validação

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_builder_action.py
```
