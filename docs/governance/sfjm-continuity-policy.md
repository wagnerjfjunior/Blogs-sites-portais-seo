# Política de Continuidade Operacional SFJM

## 1. Finalidade

Esta política aplica ao projeto o Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`.

Âncora: repositório `wagnerjfjunior/StopJuniorMode`, revisão `d03d477c3b329aa973a38ec4e949c249fa017929`, documento `docs/CANONICAL_BOOTSTRAP_PROTOCOL.md`, blob `7befd02533aad6c2df5544c7307e4a66dce28844`.

A adoção é operacional. Não inclui scoring, benchmark, cenário sintético ou avaliação experimental.

## 2. Registros obrigatórios

| Registro | Caminho | Função |
|---|---|---|
| Bootstrap | `bootstrap/BOOTSTRAP_CANONICO.md` | entrada e ordem mínima |
| Handoff | `handoffs/CURRENT.md` | contexto operacional durável |
| Status | `docs/PROJECT_STATUS.md` | frentes, riscos e decisões duráveis |
| Próxima ação | `docs/NEXT_SAFE_ACTION.md` | tabela autoritativa de transições |
| Bloqueios | `docs/BLOCKED_ACTIONS.md` | restrições estruturais |
| Manifesto | `config/sfjm.yaml` | máquina legível por software |

Registros versionados não são snapshot de head, base, Draft/Ready, checks, gates, autorizações, reviews ou threads.

## 3. Invariantes

1. `main` aprovada é a fonte canônica.
2. PR, head, base, tentativa mais recente do workflow, gates, autorizações, reviews e threads são resolvidos live.
3. Fato, decisão, proposta, hipótese e lacuna permanecem separados.
4. Informação ausente não é preenchida por plausibilidade.
5. Existe uma única máquina autoritativa.
6. Tabela publicada e manifesto devem corresponder exatamente.
7. Resumos derivados usam o mesmo `Next action ID` e texto estruturado.
8. `BLOCK` e `INCONCLUSIVE` sempre selecionam parada.
9. Autorização não se propaga entre etapas.
10. Mudança de head invalida todos os gates e autorizações anteriores.
11. Mudança somente de base invalida GPT4 e autorizações de Ready/merge.
12. Autorização de merge precisa ser concedida depois da transição Ready.
13. A tentativa mais recente do workflow para o head exato é a única autoridade de CI.
14. GPT0 → GPT4 → Ready no mesmo head não exige commit intermediário.
15. Estados merged e closed permanecem calculáveis.
16. Workflow de PR valida o head da PR, não o merge ref sintético.
17. A semântica dos passos do workflow é validada estruturalmente.
18. Validações repetidas ignoram caches e bytecode Python gerados.

## 4. Ordem de retomada

1. Confirmar repositório, PR, branch, head e base live.
2. Ler o bootstrap e seguir sua ordem.
3. Declarar fatos e lacunas.
4. Confirmar tabela e manifesto.
5. Resolver a tentativa mais recente do workflow, gates, autorizações, sequência Ready/merge e review.
6. Executar somente a primeira transição aplicável.

## 5. Evidência de execução

- CI elegível identifica ID, número, head, status e conclusion da tentativa mais recente.
- GPT0 permanece elegível apenas enquanto o head auditado não mudar.
- GPT4 permanece elegível apenas enquanto head e base avaliados não mudarem.
- Autorização de Ready permanece elegível apenas para head e base declarados.
- Autorização de merge permanece elegível apenas para head/base declarados e quando concedida depois do Ready.
- Verificação pós-merge identifica merge commit e novo `main`.

Não criar commit apenas para registrar a passagem a uma etapa seguinte.

## 6. Atualização dos registros

Atualizar somente por mudança durável de fonte, política, máquina, `Next action ID`, autoridade, estrutura, risco ou bloqueio material.

Não atualizar apenas porque gate, check, autorização, Draft/Ready ou estado terminal mudou sem alteração da política versionada.

## 7. Conflitos

Divergência de ordem, resumo, tabela, manifesto, tentativa de workflow ou regra material exige parada, reconciliação por branch/PR e repetição apenas dos gates invalidados.

## 8. Critério antíloop

Novo ciclo corretivo exige finding simultaneamente válido, material, aplicável e dependente de mudança de arquivo. Melhoria não bloqueadora vira risco residual ou backlog.

## 9. Limites

A política não reproduz raciocínio oculto ou memória integral; ela torna explícitos fonte, revisões, evidências, restrições e transições.
