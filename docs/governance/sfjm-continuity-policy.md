# Política de Continuidade Operacional SFJM

## 1. Finalidade

Esta política aplica ao projeto o Protocolo Operacional de Bootstrap Canônico do repositório `wagnerjfjunior/StopJuniorMode`.

Âncora de origem:

- repositório: `wagnerjfjunior/StopJuniorMode`
- revisão: `d03d477c3b329aa973a38ec4e949c249fa017929`
- documento: `docs/CANONICAL_BOOTSTRAP_PROTOCOL.md`
- blob: `7befd02533aad6c2df5544c7307e4a66dce28844`

A adoção é operacional. Não inclui scoring, benchmark, cenário sintético ou avaliação experimental.

## 2. Registros obrigatórios

| Registro | Caminho | Função |
|---|---|---|
| Bootstrap | `bootstrap/BOOTSTRAP_CANONICO.md` | ponto de entrada e ordem mínima de leitura |
| Handoff atual | `handoffs/CURRENT.md` | contexto operacional estável para continuidade |
| Status | `docs/PROJECT_STATUS.md` | frentes, riscos e decisões estáveis |
| Próxima ação | `docs/NEXT_SAFE_ACTION.md` | máquina autoritativa para calcular a próxima transição live |
| Bloqueios | `docs/BLOCKED_ACTIONS.md` | restrições estruturais e autorizações necessárias |
| Manifesto | `config/sfjm.yaml` | caminhos, invariantes e transições legíveis por máquina |

Os registros versionados armazenam política, estrutura, fatos canônicos duráveis e regras de transição. Eles não devem funcionar como snapshot de head, Draft/Ready, checks, reviews, gates ou autorizações correntes.

## 3. Invariantes

1. A branch `main` aprovada é a fonte canônica.
2. Revisão, head, base, checks, reviews, threads e autorizações devem ser resolvidos live antes de agir.
3. Fato, decisão, proposta, hipótese e lacuna permanecem separados.
4. Informação ausente não pode ser preenchida por plausibilidade.
5. Deve existir exatamente uma próxima ação segura autoritativa.
6. Bootstrap, handoff, status, bloqueios e próxima ação devem compartilhar o mesmo `Next action ID`.
7. Divergência material exige parada e reconciliação.
8. Autorização não se propaga entre preparação, revisão, Ready, merge, Builder, deploy e publicação.
9. Mudança de head invalida gates e autorizações anteriores vinculadas a outro head.
10. Progressão GPT0 → GPT4 → Ready no mesmo head não exige commit intermediário.
11. Alteração apenas de metadata da PR não invalida gates vinculados ao mesmo head.
12. A ausência de autorização seleciona a transição de solicitação; sua presença seleciona a transição de execução correspondente.
13. Bloqueios devem ser visíveis no repositório; resultados de execução e autorizações permanecem como evidência externa vinculada ao head.

## 4. Ordem de retomada

1. Confirmar repositório, branch, PR, base e revisão live.
2. Ler `bootstrap/BOOTSTRAP_CANONICO.md`.
3. Seguir a ordem mínima definida no bootstrap.
4. Apresentar no máximo oito fatos confirmados.
5. Declarar lacunas e limitações de acesso.
6. Ler o `Next action ID` e a máquina em `docs/NEXT_SAFE_ACTION.md`.
7. Resolver gates e autorizações vinculados ao head exato.
8. Comparar a primeira transição aplicável com `docs/BLOCKED_ACTIONS.md`.
9. Executar somente essa transição.

## 5. Evidência de execução

Gates, checks, reviews, Ready, merge e autorizações são fatos de execução externos. A evidência válida deve registrar:

- fonte consultada;
- timestamp ou estado live;
- base e head exatos;
- veredito, autorização ou transição;
- findings materiais;
- mutações autorizadas.

A evidência permanece elegível enquanto o head não mudar. Não é necessário criar commit apenas para registrar a passagem de um gate ou autorização à etapa seguinte.

## 6. Atualização dos registros

Atualizar os registros versionados quando mudar:

- fonte canônica ou protocolo upstream;
- política, máquina de transição ou `Next action ID`;
- escopo, autoridade ou fronteira de um especialista;
- decisão durável, risco estrutural ou bloqueio material;
- estrutura obrigatória dos registros.

Não atualizar apenas porque:

- GPT0 ou GPT4 terminou no mesmo head;
- a PR mudou de Draft para Ready;
- uma autorização foi concedida ou consumida no mesmo head;
- um check ou review atualizou sem alterar arquivos;
- a etapa calculada pela máquina avançou.

## 7. Conflitos

Se o `Next action ID`, a ordem de leitura ou uma regra material divergir entre manifesto, próxima ação, bootstrap, handoff, status ou bloqueios:

1. interromper a execução;
2. usar `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml` para identificar a intenção autoritativa;
3. reconciliar no fluxo normal de branch e PR;
4. repetir gates somente se a correção alterar arquivos ou head.

## 8. Critério antíloop

Novo ciclo corretivo só é obrigatório quando o finding for válido, material, aplicável ao head atual e exigir mudança de arquivo. Sugestões cosméticas, melhorias futuras e riscos não bloqueadores devem ser registrados como risco residual ou backlog.

## 9. Limites

Esta política não garante reprodução de raciocínio oculto ou memória integral. Ela reduz regressão de contexto ao tornar explícitos fonte, estado resolvido live, restrições, evidências e transições.
