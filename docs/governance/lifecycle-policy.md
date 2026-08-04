# Política de lifecycle

## Fluxo padrão

1. Implementação em branch.
2. Validação local completa.
3. Commit corretivo consolidado.
4. Congelamento do head.
5. Gate GPT0 documental.
6. Gate GPT4 de lifecycle.
7. Autorização humana de Ready.
8. Conferência curta de head, checks, reviews e threads.
9. Autorização humana separada de merge.
10. Merge e verificação pós-merge.

## Regras de revalidação

- Head mudou: repetir GPT0 e GPT4.
- Arquivos mudaram: repetir GPT0 e GPT4.
- Apenas a base mudou: repetir GPT4 e avaliar impacto no diff.
- Check reexecutado no mesmo head: validar a execução mais recente.
- Review ficou stale: obter nova decisão aplicável.

## Estados de decisão

- `PASS`: escopo integralmente atendido.
- `PASS_WITH_RESIDUAL_RISK`: sem bloqueio, com limitação explicitada.
- `BLOCK`: evidência disponível demonstra não conformidade.
- `INCONCLUSIVE`: acesso ou evidência insuficiente.

Não usar resultado condicional para encobrir correção obrigatória.
