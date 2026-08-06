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

A ordem mínima de leitura é definida nesse arquivo. A máquina autoritativa da próxima transição reside em:

```text
docs/NEXT_SAFE_ACTION.md
config/sfjm.yaml
```

Head, base, Draft/Ready, checks, gates, autorizações, reviews e threads devem ser resolvidos live no GitHub. Resumos em outros documentos são derivados e não autorizam execução.

## Estrutura canônica

- `config/project.yaml`: identidade e políticas do projeto.
- `config/gpts.yaml`: registro dos nove GPTs.
- `config/sfjm.yaml`: manifesto de continuidade e transições SFJM.
- `bootstrap/BOOTSTRAP_CANONICO.md`: entrada e ordem de retomada.
- `handoffs/CURRENT.md`: contexto operacional durável.
- `docs/PROJECT_STATUS.md`: status estrutural consolidado.
- `docs/NEXT_SAFE_ACTION.md`: máquina autoritativa da próxima transição.
- `docs/BLOCKED_ACTIONS.md`: bloqueios estruturais e autorizações exigidas.
- `docs/gpts/`: contratos e instruções do Builder.
- `.agents/skills/`: skills operacionais.
- `config/builder/`: manifestos de provisioning.
- `config/actions/`: schemas OpenAPI.
- `tests/gpts/`: casos de aceitação.
- `tests/test_sfjm_validation.py`: testes negativos e adversariais do SFJM.
- `docs/governance/`: políticas de lifecycle, autorização, ferramentas, Builder e SFJM.
- `scripts/validate_repository.py`: validação determinística.

## SFJM operacional

O projeto adota o Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`, ancorado na revisão registrada em `config/sfjm.yaml`.

A adoção cobre continuidade entre conversas, fonte canônica, estado verificável, lacunas, bloqueios, autorização e menor próxima ação segura. Não inclui scoring, benchmark, cenários sintéticos ou adjudicação experimental.

## Regras essenciais

1. Toda mudança canônica ocorre por branch e Pull Request.
2. O head auditado deve permanecer congelado entre os gates.
3. GPT0 e GPT4 avançam no mesmo head sem commit intermediário.
4. Ready e merge exigem autorizações humanas separadas e vinculadas ao head exato.
5. A presença de autorização válida seleciona a execução da transição correspondente.
6. A Action inicial dos nove GPTs é estritamente `READ_ONLY`.
7. Nenhum token, segredo ou credencial é versionado.
8. Conteúdo patrocinado e links pagos devem ser identificados adequadamente.
9. Métricas como DA e DR são auxiliares de terceiros, não métricas do Google.
10. Informação ausente não pode ser inferida.
11. Divergência material entre registros de continuidade exige parada e reconciliação.
12. Estado volátil não deve ser gravado como snapshot em documentos duráveis.

## Validação

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_builder_action.py
```
