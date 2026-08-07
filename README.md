# Ecossistema de Blogs, Sites, Portais e SEO

- **ID técnico:** `blogs-sites-portais-seo`
- **Repositório canônico:** `wagnerjfjunior/Blogs-sites-portais-seo`
- **Visibilidade:** privado
- **GPTs:** nove, compartilhamento `owner_only`
- **Action GitHub:** somente leitura
- **Branch principal:** `main`

O repositório é a fonte canônica de identidade, contratos, skills, Builder, testes, governança, Actions, evidências e continuidade operacional.

## Ponto de entrada

Comece por `bootstrap/BOOTSTRAP_CANONICO.md`. A máquina autoritativa está em `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml`.

Head, base, estado da PR, workflow, gates, autorizações, reviews, threads e verificação pós-merge são resolvidos live. Documentos versionados armazenam regras duráveis, não snapshots.

## Estrutura

- `config/project.yaml`: identidade e políticas.
- `config/gpts.yaml`: nove GPTs.
- `config/sfjm.yaml`: manifesto e transições SFJM.
- `bootstrap/BOOTSTRAP_CANONICO.md`: entrada e ordem.
- `handoffs/CURRENT.md`: contexto durável.
- `docs/PROJECT_STATUS.md`: estado estrutural.
- `docs/NEXT_SAFE_ACTION.md`: tabela autoritativa.
- `docs/BLOCKED_ACTIONS.md`: bloqueios estruturais.
- `docs/evidence/`: evidências canônicas.
- `tests/test_sfjm_validation.py`: testes adversariais.
- `docs/governance/`: políticas.
- `scripts/validate_repository.py`: validador determinístico.

## Regras essenciais

1. Mudanças por branch e PR.
2. Workflow valida o head exato da PR.
3. GPT0 é head-bound; GPT4 é head+base-bound.
4. Somente gates passando permitem Ready ou merge.
5. Ready e merge têm autorizações separadas para head e base.
6. Estados merged e closed continuam calculáveis.
7. A Action dos GPTs permanece `READ_ONLY`.
8. Informação ausente não é inferida.
9. Divergência material exige parada.
10. Estado volátil não é snapshot versionado.

## Validação

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_builder_action.py
```
