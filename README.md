# Ecossistema de Blogs, Sites, Portais e SEO

- **ID técnico:** `blogs-sites-portais-seo`
- **Repositório canônico:** `wagnerjfjunior/Blogs-sites-portais-seo`
- **Visibilidade:** privado
- **Audiência dos GPTs:** `owner_only`

Este repositório é a fonte canônica dos contratos, skills, configurações do Builder, schemas de Actions, testes e decisões do projeto.

## Bootstrap
Cobre GPT0 a GPT8, documentação canônica, Action GitHub somente leitura, configuração declarativa do Builder e testes de aceitação.

## Regras essenciais
1. Mudanças canônicas ocorrem por branch e Pull Request.
2. O head auditado permanece congelado durante os gates.
3. Ready e merge exigem autorizações humanas distintas.
4. A configuração real do Builder deve corresponder aos manifests e às instruções versionadas.
5. Nenhum segredo é armazenado no repositório.
6. SFJM permanece fora de escopo e não pode ser criado nesta etapa.

Execute `python scripts/validate_repository.py` antes de solicitar auditoria ou lifecycle.
