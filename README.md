# Ecossistema de Blogs, Sites, Portais e SEO

- **ID técnico:** `blogs-sites-portais-seo`
- **Repositório canônico:** `wagnerjfjunior/Blogs-sites-portais-seo`
- **Visibilidade do repositório:** privado
- **Compartilhamento dos GPTs:** `Apenas para mim` / `owner_only`
- **Integração GitHub:** Action OpenAPI somente leitura
- **Branch principal:** `main`

Este repositório é a fonte canônica de identidade, contratos, skills, instruções do Builder, testes, governança, Actions e evidências do projeto.

## Estrutura canônica

- `config/project.yaml`: identidade e políticas do projeto.
- `config/gpts.yaml`: registro dos nove GPTs.
- `docs/gpts/`: contratos e instruções do Builder.
- `.agents/skills/`: skills operacionais.
- `config/builder/`: manifestos de provisioning.
- `config/actions/`: schemas OpenAPI.
- `tests/gpts/`: casos de aceitação.
- `docs/governance/`: políticas de lifecycle, autorização, ferramentas e Builder.
- `scripts/validate_repository.py`: validação determinística.

## Regras essenciais

1. Toda mudança canônica ocorre por branch e Pull Request.
2. O head auditado deve permanecer congelado entre os gates.
3. Ready e merge exigem autorizações humanas separadas.
4. A Action inicial dos nove GPTs é estritamente `READ_ONLY`.
5. Nenhum token, segredo ou credencial é versionado.
6. Conteúdo patrocinado e links pagos devem ser identificados adequadamente.
7. Métricas como DA e DR são auxiliares de terceiros, não métricas do Google.

## Validação

```bash
python scripts/validate_repository.py
```
