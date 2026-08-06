# ADR-0002 — Adoção do bootstrap operacional SFJM

- Status: aceito
- Data: 2026-08-05
- Autoridade: Wagner

## Contexto

O framework dos nove GPTs foi mergeado pela PR #1, mas a continuidade do projeto ainda dependia de conversas e de interpretação do estado. O projeto precisa permitir retomada segura por novas conversas e especialistas sem reconstrução manual do histórico e sem transformar intenção em autorização.

## Decisão

Adotar a camada operacional de continuidade definida pelo Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`, ancorado em:

- revisão `d03d477c3b329aa973a38ec4e949c249fa017929`;
- documento `docs/CANONICAL_BOOTSTRAP_PROTOCOL.md`;
- blob `7befd02533aad6c2df5544c7307e4a66dce28844`.

A adoção inclui bootstrap, handoff, status, máquina de próxima ação, bloqueios, manifesto, política local e validação determinística das invariantes.

## Fronteiras

Esta decisão não autoriza scoring experimental, cenários sintéticos, mutações externas autônomas, Ready ou merge automáticos, alteração automática do Builder, deploy ou publicação.

O SFJM operacional complementa o framework GPT existente; não substitui contratos, skills, Instructions, testes ou lifecycle.

## Consequências

- `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml` formam a máquina autoritativa de transições.
- Bootstrap, handoff e status contêm resumos derivados validados.
- Divergência material bloqueia execução até reconciliação.
- Novas conversas começam pela ordem mínima de leitura.
- Gates, autorizações, Draft/Ready, reviews, merge e pós-merge são evidências externas e não exigem reescrita de registros por mero avanço de lifecycle.
- Registros versionados são atualizados somente quando mudar política, estrutura, autoridade, bloqueio material ou evidência canônica durável.
- A autorização de merge deve ser posterior e separada da transição Ready.
- O validador exige estrutura, coerência, idempotência e exclusão de artefatos binários gerados.

## Alternativas rejeitadas

1. Depender do histórico das conversas: não é verificável nem portátil.
2. Manter apenas um arquivo genérico de handoff: não separa status, próxima ação e bloqueios.
3. Criar uma máquina experimental completa de scoring: excede o objetivo operacional atual.
