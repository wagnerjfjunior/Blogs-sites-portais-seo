# Política de lifecycle

## Fluxo padrão

1. Implementação consolidada em branch.
2. Validação local e testes adversariais.
3. Workflow canônico no head corretivo.
4. Revisão automática ou humana do head corretivo.
5. Adjudicação e correção de todos os findings materiais válidos.
6. Resolução das threads corrigidas.
7. Congelamento do head final somente quando não houver correção previsível pendente.
8. Gate GPT0 documental no head congelado.
9. Gate GPT4 de lifecycle no mesmo head, sem commit intermediário.
10. Autorização humana de Ready, quando aplicável.
11. Conferência curta de head, checks, reviews e threads após Ready.
12. Autorização humana separada de merge.
13. Merge protegido pelo head exato e verificação pós-merge de `main`.

## Estado live e registros versionados

O lifecycle corrente é resolvido no GitHub. Documentos versionados definem a máquina e as regras, mas não devem congelar como fatos atuais:

- head ou base corrente;
- Draft ou Ready;
- check mais recente;
- gate que acabou de terminar;
- quantidade atual de reviews ou threads.

A passagem GPT0 → GPT4 → Ready no mesmo head é mudança de estado externo, não mudança documental.

## Regras de revalidação

- Head mudou: repetir workflow, GPT0 e GPT4.
- Arquivos mudaram: repetir workflow, GPT0 e GPT4.
- Apenas a base mudou: repetir GPT4 e avaliar impacto no diff.
- Check reexecutado no mesmo head: validar a execução mais recente.
- Metadata da PR mudou sem alteração de head: gates do mesmo head permanecem válidos.
- Review ficou stale: obter nova decisão aplicável.
- Finding material após Ready: corrigir em novo head e repetir os gates.
- Finding não material: registrar risco residual ou backlog sem reiniciar a PR.

## Elegibilidade de gates

Um gate é elegível quando identifica:

- repositório e PR;
- base e head exatos;
- escopo analisado;
- evidências consultadas;
- veredito oficial;
- ausência de mutação não autorizada.

GPT0 e GPT4 podem ser executados sequencialmente no mesmo head. Não se deve alterar `NEXT_SAFE_ACTION`, handoff ou status apenas para autorizar o gate seguinte.

## Estados de decisão

- `PASS`: escopo integralmente atendido.
- `PASS_WITH_RESIDUAL_RISK`: sem bloqueio, com limitação explicitada.
- `BLOCK`: evidência disponível demonstra não conformidade.
- `INCONCLUSIVE`: acesso ou evidência insuficiente.

Não usar resultado condicional para encobrir correção obrigatória.

## Critério antíloop

Antes de alterar novamente o head, confirmar que o finding é simultaneamente válido, material, aplicável e bloqueador. Consolidar todos os findings conhecidos em uma única rodada antes de recongelar o head.

## Autorizações

- Leitura e gates `READ_ONLY` não autorizam mutação.
- Ready exige autorização específica para o head exato.
- Merge exige autorização posterior e separada.
- Merge não autoriza Builder, deploy, publicação ou produção.
