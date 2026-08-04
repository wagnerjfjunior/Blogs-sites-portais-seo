# Política de ferramentas

## GitHub
O acesso operacional dos GPTs ocorre por Action OpenAPI. O perfil inicial é `github-read-only`, usa somente `GET`, servidor `api.github.com` e paths fixos para o repositório canônico.

## Builder
Compartilhamento esperado: `owner_only` / “Apenas para mim”. Petstore não é integração operacional e deve ser substituído pelo schema canônico.

## Credenciais
Tokens, chaves e segredos nunca entram no Git. Use credencial fine-grained, limitada ao repositório e às permissões de leitura necessárias.

## Mutações
Nenhuma mutação GitHub está exposta no schema inicial. Um perfil futuro de lifecycle exige PR separada e autorização explícita.
