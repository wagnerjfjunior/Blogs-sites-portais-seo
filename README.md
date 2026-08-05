# Ecossistema de Blogs, Sites, Portais e SEO

- **ID técnico:** `blogs-sites-portais-seo`
- **Repositório canônico:** `wagnerjfjunior/Blogs-sites-portais-seo`
- **Visibilidade do repositório:** privado
- **Compartilhamento dos GPTs:** `Apenas para mim` / `owner_only`
- **Integração GitHub:** Action OpenAPI somente leitura
- **Branch principal:** `main`

Este repositório é a fonte canônica de identidade, contratos, skills, instruções do Builder, testes, governança, Actions, evidências e continuidade operacional do projeto.

## Ponto de entrada operacional

Toda nova conversa, retomada ou transferência deve começar por:

```text
bootstrap/BOOTSTRAP_CANONICO.md
```

A ordem mínima de leitura é definida nesse arquivo. A única próxima ação segura autoritativa reside em:

```text
docs/NEXT_SAFE_ACTION.md
```

Resumos em outros documentos são derivados e não autorizam execução.

## Estrutura canônica

- `config/project.yaml`: identidade e políticas do projeto.
- `config/gpts.yaml`: registro dos nove GPTs.
- `config/sfjm.yaml`: manifesto de continuidade operacional SFJM.
- `bootstrap/BOOTSTRAP_CANONICO.md`: entrada e ordem de retomada.
- `handoffs/CURRENT.md`: handoff atual do projeto.
- `docs/PROJECT_STATUS.md`: status consolidado.
- `docs/NEXT_SAFE_ACTION.md`: única próxima ação segura autoritativa.
- `docs/BLOCKED_ACTIONS.md`: ações bloqueadas e condições de liberação.
- `docs/gpts/`: contratos e instruções do Builder.
- `.agents/skills/`: skills operacionais.
- `config/builder/`: manifestos de provisioning.
- `config/actions/`: schemas OpenAPI.
- `tests/gpts/`: casos de aceitação.
- `docs/governance/`: políticas de lifecycle, autorização, ferramentas, Builder e SFJM.
- `scripts/validate_repository.py`: validação determinística.

## SFJM operacional

O projeto adota o Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`, ancorado na revisão registrada em `config/sfjm.yaml`.

A adoção cobre continuidade entre conversas, fonte canônica, estado verificável, lacunas, bloqueios, autorização e menor próxima ação segura. Não inclui scoring, benchmark, cenários sintéticos ou adjudicação experimental.

## Regras essenciais

1. Toda mudança canônica ocorre por branch e Pull Request.
2. O head auditado deve permanecer congelado entre os gates.
3. Ready e merge exigem autorizações humanas separadas.
4. A Action inicial dos nove GPTs é estritamente `READ_ONLY`.
5. Nenhum token, segredo ou credencial é versionado.
6. Conteúdo patrocinado e links pagos devem ser identificados adequadamente.
7. Métricas como DA e DR são auxiliares de terceiros, não métricas do Google.
8. Informação ausente não pode ser inferida.
9. Deve existir exatamente uma próxima ação segura autoritativa.
10. Divergência material entre registros de continuidade exige parada e reconciliação.

## Validação

```bash
python scripts/validate_repository.py
python scripts/validate_builder_action.py
```
