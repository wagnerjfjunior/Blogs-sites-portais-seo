# Política de Continuidade Operacional SFJM

## 1. Finalidade

Esta política aplica ao projeto o Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`.

Âncora de origem:

- repositório: `wagnerjfjunior/StopJuniorMode`
- revisão: `d03d477c3b329aa973a38ec4e949c249fa017929`
- documento: `docs/CANONICAL_BOOTSTRAP_PROTOCOL.md`
- blob: `7befd02533aad6c2df5544c7307e4a66dce28844`

A adoção é operacional e universal. Não inclui avaliação experimental, scoring, benchmark, cenário sintético ou adjudicação.

## 2. Registros obrigatórios

| Registro | Caminho | Função |
|---|---|---|
| Bootstrap | `bootstrap/BOOTSTRAP_CANONICO.md` | ponto de entrada e ordem mínima de leitura |
| Handoff atual | `handoffs/CURRENT.md` | estado necessário para continuidade |
| Status | `docs/PROJECT_STATUS.md` | visão consolidada de frentes, riscos e decisões |
| Próxima ação | `docs/NEXT_SAFE_ACTION.md` | única próxima ação segura autoritativa |
| Bloqueios | `docs/BLOCKED_ACTIONS.md` | restrições, dependências e autorizações |
| Manifesto | `config/sfjm.yaml` | caminhos e invariantes legíveis por máquina |

## 3. Invariantes

1. A branch `main` aprovada é a fonte canônica.
2. A revisão live deve ser resolvida antes de qualquer ação material.
3. Fato, decisão, proposta, hipótese e lacuna devem permanecer separados.
4. Informação ausente não pode ser preenchida por plausibilidade.
5. Deve existir exatamente uma próxima ação segura autoritativa.
6. Resumos da próxima ação são derivados e não autorizam execução.
7. Divergência material exige parada e reconciliação.
8. Autorização não se propaga entre preparação, revisão, Ready, merge, Builder, deploy e publicação.
9. Mudança de head invalida gates anteriores.
10. Bloqueios devem ser visíveis no repositório, não apenas em conversas.

## 4. Ordem de retomada

1. Confirmar repositório, branch e revisão live.
2. Ler `bootstrap/BOOTSTRAP_CANONICO.md`.
3. Seguir a ordem mínima definida no bootstrap.
4. Apresentar no máximo oito fatos confirmados.
5. Declarar lacunas e limitações de acesso.
6. Identificar a ação autoritativa em `docs/NEXT_SAFE_ACTION.md`.
7. Comparar a ação com `docs/BLOCKED_ACTIONS.md` e a autorização vigente.
8. Executar somente o menor escopo seguro autorizado.

## 5. Responsabilidades

| Papel | Responsabilidade |
|---|---|
| Wagner | Product Authority e autorizações materiais |
| GPT0 | gate documental independente e sem implementação |
| GPT4 | gate de lifecycle, drift, checks, reviews e elegibilidade |
| GPT1–GPT8 | trabalho dentro da especialidade e handoff explícito |
| Orquestrador | resolver contexto, direcionar especialista e preservar separação de funções |

## 6. Atualização dos registros

Atualizar os registros quando mudar:

- revisão ou fonte canônica;
- fase, marco, decisão, risco ou bloqueio;
- autorização vigente;
- evidência relevante;
- próxima ação segura;
- escopo de um especialista;
- estado externo que tenha sido verificado.

Preferir substituir estado obsoleto a acumular narrativas indefinidas. O histórico Git preserva auditoria.

## 7. Conflitos

Se `docs/NEXT_SAFE_ACTION.md` divergir de bootstrap, handoff ou status:

1. o registro autoritativo identifica a ação pretendida;
2. a execução permanece interrompida;
3. os documentos devem ser reconciliados no fluxo normal de branch e PR;
4. nenhum resumo substitui silenciosamente o registro autoritativo.

## 8. Limites

Esta política não garante reprodução de raciocínio oculto ou memória integral. Ela reduz regressão de contexto ao tornar explícitos fonte, estado, restrições, evidências e próximo passo.
