# Política de lifecycle

## Fluxo padrão

1. Implementação consolidada em branch.
2. Validação local e testes adversariais.
3. Workflow no head exato da PR.
4. Revisão automática ou humana do head.
5. Adjudicação e correção de findings materiais.
6. Resolução das threads corrigidas.
7. Congelamento do head final.
8. GPT0 documental no head congelado.
9. GPT4 no mesmo head e na base atual.
10. `BLOCK` ou `INCONCLUSIVE`: parar e remediar evidência ou conteúdo.
11. Gates passando e PR Draft: solicitar ou executar Ready conforme autorização.
12. PR Ready: revalidar reviews e threads.
13. Solicitar autorização de merge somente depois de Ready.
14. Executar merge apenas com autorização posterior e separada.
15. Verificar merge commit e `main`.
16. Em retomadas posteriores, reportar estado terminal sem mutação.

## Estado live e registros versionados

Lifecycle é resolvido no GitHub. Documentos não congelam head, base, Draft/Ready, check, gate, autorização, review ou thread atuais.

## Regras de revalidação

- Head mudou: repetir workflow, GPT0, GPT4 e obter novas autorizações.
- Apenas a base mudou: repetir GPT4, avaliar o diff e obter novas autorizações de Ready/merge; GPT0 pode ser reutilizado se o head não mudou.
- Check reexecutado no mesmo head: usar a execução mais recente.
- Metadata mudou sem alterar head/base: evidências permanecem válidas.
- Review ficou stale ou mudou após Ready: reavaliar antes do merge.
- Finding material: corrigir em novo head e repetir gates invalidados.
- Finding não material: risco residual ou backlog.

## Elegibilidade

GPT0 identifica repositório, PR, head, escopo, evidências e veredito.

GPT4 identifica repositório, PR, head, base, checks, reviews, threads, mergeabilidade e veredito.

Autorização de Ready identifica transição, repositório, PR, head, base, exclusões e autoridade concedente.

Autorização de merge contém os mesmos campos e evidência de que foi concedida depois da transição Ready. Autorização antecipada ou conjunta é inelegível.

Somente `PASS` e `PASS_WITH_RESIDUAL_RISK` são vereditos de passagem. `BLOCK` e `INCONCLUSIVE` nunca permitem Ready ou merge.

## Workflow

Em evento `pull_request`, `actions/checkout` usa explicitamente `github.event.pull_request.head.sha`. O merge ref sintético não é evidência do head exato.

A validação é executada antes e depois dos testes adversariais. Bytecode e caches gerados não podem alterar o resultado.

## Estados terminais

- PR merged sem verificação: verificar merge commit e `main`.
- PR merged com verificação: reportar lifecycle concluído sem mutação.
- PR closed sem merge: reportar o estado e exigir decisão explícita para reabrir ou abandonar.

## Critério antíloop

Antes de alterar o head, confirmar finding válido, material, aplicável e bloqueador. Consolidar findings conhecidos antes de recongelar.

## Autorizações

Leitura e gates `READ_ONLY` não autorizam mutação. Ready e merge são separados e sequenciais. Merge não autoriza Builder, deploy, publicação ou produção.
