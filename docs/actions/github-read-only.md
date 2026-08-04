# Action GitHub READ_ONLY

## Finalidade

Permitir que GPT0 a GPT8 consultem o repositório privado `wagnerjfjunior/Blogs-sites-portais-seo` diretamente pela API REST do GitHub.

## Segurança

- servidor fixo `https://api.github.com`;
- paths fixos no repositório;
- apenas métodos `GET`;
- operações marcadas como não consequenciais;
- token fine-grained com permissões mínimas;
- nenhum token versionado.

## Configuração no Builder

1. Remover schemas de demonstração.
2. Colar `config/actions/github-read-only.openapi.yaml`.
3. Configurar autenticação por Bearer token.
4. Testar `/user`.
5. Testar repositório, arquivo por SHA, PR, checks e workflow.
6. Confirmar compartilhamento `Apenas para mim`.

## Limitações

A API REST de comentários de review não oferece, isoladamente, toda a semântica GraphQL de resolução de threads. Quando a decisão depender de `isResolved`, registrar a limitação ou usar evidência adicional autorizada.

## Proibição

Não adicionar `POST`, `PUT`, `PATCH` ou `DELETE` a este schema.
