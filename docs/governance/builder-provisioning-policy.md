# Política de provisioning do Builder

## Fonte

As Instructions do Builder são projeções dos contratos canônicos. Não podem introduzir regras novas ou contraditórias.

## Ordem por GPT

1. Confirmar ID e URL externos.
2. Confirmar compartilhamento `Apenas para mim`.
3. Remover schemas de demonstração.
4. Inserir as Instructions canônicas.
5. Configurar a Action `github_read_only`.
6. Configurar autenticação sem registrar o token.
7. Salvar a versão.
8. Executar a suíte de aceitação.
9. Registrar data, fonte e resultado.

## Evidência mínima

- GPT e URL;
- commit-fonte;
- hash das Instructions;
- Action configurada;
- compartilhamento observado;
- testes executados;
- resultado;
- limitações.

## Rollback

Restaurar a versão anterior do Builder e registrar a divergência. O GitHub continua sendo a fonte de reconstrução.
