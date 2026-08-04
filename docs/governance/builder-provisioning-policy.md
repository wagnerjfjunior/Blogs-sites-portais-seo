# Política de provisioning do Builder

Para cada GPT, configure nome, descrição, Instructions, Knowledge necessário, Action, compartilhamento e recursos conforme o manifest versionado.

A Action deve usar `config/actions/github-read-only.openapi.yaml`. O compartilhamento deve permanecer “Apenas para mim”. Não registrar tokens, screenshots sensíveis ou segredos.

Antes de concluir, execute a suíte de aceitação do GPT e registre resultado, versão das Instructions e data. Divergência entre Builder e repositório é drift de configuração.
