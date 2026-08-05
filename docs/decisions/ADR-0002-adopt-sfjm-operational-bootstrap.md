# ADR-0002 — Adoção do bootstrap operacional SFJM

- Status: aceito
- Data: 2026-08-05
- Autoridade: Wagner

## Contexto

O framework dos nove GPTs foi mergeado pela PR #1, mas a continuidade do projeto ainda dependia de conversas e de interpretação do estado. O validador inicial também rejeitava artefatos SFJM porque o tema estava fora do escopo da primeira PR.

O projeto precisa permitir retomada segura por novas conversas e especialistas sem reconstrução manual do histórico e sem transformar intenção em autorização.

## Decisão

Adotar a camada operacional de continuidade definida pelo Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`, ancorado em:

- revisão `d03d477c3b329aa973a38ec4e949c249fa017929`;
- documento `docs/CANONICAL_BOOTSTRAP_PROTOCOL.md`;
- blob `7befd02533aad6c2df5544c7307e4a66dce28844`.

A adoção inclui:

- `bootstrap/BOOTSTRAP_CANONICO.md`;
- `handoffs/CURRENT.md`;
- `docs/PROJECT_STATUS.md`;
- `docs/NEXT_SAFE_ACTION.md`;
- `docs/BLOCKED_ACTIONS.md`;
- `config/sfjm.yaml`;
- política local de continuidade;
- validação determinística das invariantes.

## Fronteiras

Esta decisão não autoriza:

- scoring ou adjudicação experimental;
- cenários sintéticos;
- mutações externas autônomas;
- Ready ou merge automáticos;
- alteração automática do Builder;
- deploy ou publicação.

O SFJM operacional complementa o framework GPT existente; não substitui contratos, skills, Instructions, testes ou lifecycle.

## Consequências

- `docs/NEXT_SAFE_ACTION.md` passa a ser o único registro autoritativo da próxima ação segura.
- Bootstrap, handoff e status contêm apenas resumos derivados.
- Divergência material bloqueia execução até reconciliação.
- Novas conversas devem começar pela ordem mínima de leitura.
- Mudanças de estado exigem atualização dos registros aplicáveis.
- O validador deixa de proibir SFJM e passa a exigir sua estrutura e coerência.

## Alternativas rejeitadas

1. Depender do histórico das conversas: não é verificável nem portátil.
2. Manter apenas um arquivo genérico de handoff: não separa status, próxima ação e bloqueios.
3. Criar uma máquina experimental completa de scoring: excede o objetivo operacional atual.
