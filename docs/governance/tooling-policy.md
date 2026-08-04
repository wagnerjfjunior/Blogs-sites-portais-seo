# Política de ferramentas

## GitHub

O acesso dos GPTs ao GitHub ocorre por Action OpenAPI direcionada a `https://api.github.com`.

## Perfil inicial

`github_read_only`:

- repositório fixo `wagnerjfjunior/Blogs-sites-portais-seo`;
- somente métodos `GET`;
- `x-openai-isConsequential: false`;
- token fine-grained restrito ao repositório;
- nenhum segredo no repositório;
- nenhuma operação genérica sobre outros repositórios.

## Permissões mínimas do token

- Metadata: Read
- Contents: Read
- Pull requests: Read
- Actions: Read
- Checks: Read

A disponibilidade exata depende dos endpoints e do modelo de token usado.

## Builder

- Compartilhamento: `Apenas para mim`.
- Schemas de demonstração não autorizados: proibidos.
- Apps e plugins não fazem parte da arquitetura definida.
- A Action READ_ONLY pode usar permissão persistente somente após validar domínio, token, paths e ausência de mutações.

## Mutações

Uma futura Action mutável será separada, exclusiva do GPT4 e deverá exigir confirmação humana. Não faz parte do perfil inicial.
