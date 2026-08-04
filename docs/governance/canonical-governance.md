# Governança canônica

## Fonte de verdade
GitHub é a fonte canônica. Builder, prompts e testes apontam para arquivos versionados neste repositório.

## Cadeia de mudança
`branch → PR Draft → validação local → head congelado → GPT0 → GPT4 → autorização Ready → Ready → conferência final → autorização merge → merge`.

A conferência final não repete auditorias quando o head permanece idêntico.

## Independência
O autor não audita a própria alteração. GPT0 audita documentação; GPT4 valida lifecycle. Nenhum deles autoriza Ready ou merge.

## Evidência
Toda conclusão deve indicar objeto, referência exata, data e limitação. Conteúdo truncado ou inacessível não comprova leitura integral.

## Builder
Manifests e Instructions são projeções dos contratos canônicos. A configuração real deve ser validada no Builder sem registrar segredos.

## SFJM
SFJM está fora de escopo. A ausência é uma restrição obrigatória deste bootstrap.
