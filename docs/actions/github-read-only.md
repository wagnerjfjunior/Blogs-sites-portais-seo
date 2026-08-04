# Action GitHub READ_ONLY

Schema: `config/actions/github-read-only.openapi.yaml`.

## Finalidade
Permitir aos nove GPTs consultar exclusivamente `wagnerjfjunior/Blogs-sites-portais-seo` pela API REST do GitHub.

## Autenticação
Configurar no Builder como Bearer usando token fine-grained limitado ao repositório e às permissões de leitura necessárias. Nunca versionar o token.

## Garantias
O schema contém somente `GET`, servidor `https://api.github.com`, paths fixos e `x-openai-isConsequential: false`. Respostas truncadas, paginadas ou incompletas não comprovam cobertura integral.

## Builder
Remover o Petstore, importar este schema e manter compartilhamento “Apenas para mim”. “Sempre permitir” só é aceitável enquanto o schema permanecer estritamente somente leitura.
