# Próxima Ação Segura — Ecossistema de Blogs, Sites, Portais e SEO

> Este é o registro atual autoritativo da única próxima ação segura do projeto.

- Next action ID: `resolve-live-lifecycle-transition-v1`
- Fonte de estado: GitHub live, resolvido no início de cada execução
- Função versionada: política e máquina de transição, não snapshot volátil da PR
- Autoridade material: Wagner

Resumos no bootstrap, handoff, status e bloqueios são derivados. A sincronização é validada pelo mesmo `Next action ID`.

## 1. Ação

Resolver o estado live do repositório, da PR aplicável, do head, da base, dos checks, dos gates, das autorizações, das reviews e das threads; em seguida, executar somente a primeira transição aplicável da máquina abaixo.

Não editar documentos apenas para registrar a passagem de GPT0 para GPT4, Draft para Ready ou Ready para merge. Essas transições não alteram o head e são comprovadas por evidência externa vinculada ao head exato.

## 2. Máquina de transição

| Prioridade | Condição live | Única ação permitida |
|---:|---|---|
| 0 | head/base drift ou finding material não resolvido | parar e reconciliar somente sob autorização explícita |
| 1 | workflow canônico do head exato ausente, incompleto ou sem sucesso | aguardar ou reexecutar somente se autorizado |
| 2 | workflow verde e nenhum gate GPT0 elegível no head | executar GPT0 `READ_ONLY` |
| 3 | GPT0 elegível com `PASS` ou `PASS_WITH_RESIDUAL_RISK` e nenhum GPT4 elegível | executar GPT4 `READ_ONLY` |
| 4 | gates atuais, PR Draft e autorização de Ready para o head exato ausente | exigir autorização explícita de Ready |
| 5 | gates atuais, PR Draft e autorização de Ready para o head exato presente | marcar somente a PR como Ready |
| 6 | PR Ready e estado de review mudou desde o gate ou a última rechecagem | adjudicar findings materiais antes do merge |
| 7 | PR Ready, gates atuais, nenhuma thread material e autorização de merge ausente | exigir autorização explícita de merge |
| 8 | PR Ready, gates atuais, nenhuma thread material e autorização de merge presente | fazer merge do head exato e verificar `main` |

## 3. Regra antíloop

- GPT0 e GPT4 devem usar o mesmo head congelado.
- A progressão GPT0 → GPT4 → Ready não exige commit intermediário.
- A presença de autorização válida avança da etapa de solicitação para a execução correspondente.
- Mudança de metadata da PR não invalida gates vinculados ao mesmo head.
- Somente correção material que altere arquivos ou head reinicia workflow, GPT0 e GPT4.
- Finding não material deve ser classificado como risco residual ou backlog, sem nova rodada corretiva nesta PR.

## 4. Pré-condições

- resolver `main`, PR, base e head live;
- confirmar que o head permaneceu estável durante a etapa;
- usar somente gates que identifiquem o mesmo head exato;
- resolver autorizações live e exigir correspondência com o head exato;
- verificar workflow, reviews e threads mais recentes;
- confirmar autorização específica antes de qualquer mutação.

## 5. Resultado verificável

Cada transição deve produzir evidência contendo:

- repositório, PR, base, branch e head exatos;
- estado live relevante;
- checks ou gates aplicáveis;
- autorização ausente ou presente e seu escopo;
- findings materiais e sua situação;
- mutações executadas, se autorizadas;
- próxima transição calculada sem atualizar documentos por mero avanço de lifecycle.

## 6. Limites explícitos

A resolução live e os gates `READ_ONLY` não autorizam:

- correção de arquivos;
- Ready;
- merge;
- Builder;
- deploy, publicação ou produção;
- atividade SEO;
- propagação de uma autorização para etapa posterior.

## 7. Autorização

- GPT0 e GPT4 `READ_ONLY`: permitidos quando forem a primeira transição aplicável.
- Correção material: exige escopo explícito.
- Ready ausente: solicitar autorização específica para o head exato.
- Ready autorizada: executar somente a transição Draft → Ready.
- Merge ausente: solicitar autorização posterior e separada para o head exato.
- Merge autorizado: executar somente o merge do head exato e verificar `main`.
- Builder, deploy e produção: permanecem fora de escopo até autorização própria.

## 8. Evidência dos gates e autorizações

O resultado de GPT0, GPT4 ou uma autorização é estado de execução externo e deve:

- identificar o head exato;
- registrar veredito ou escopo autorizado;
- permanecer reutilizável enquanto o head não mudar;
- não exigir commit apenas para avançar à transição seguinte.

## 9. Verificação de conclusão

A etapa está concluída quando:

- a primeira transição aplicável foi executada integralmente;
- não houve ação posterior automática;
- o head não mudou sem revalidação;
- qualquer mutação respeitou autorização específica;
- o próximo estado pode ser novamente calculado por esta mesma máquina.

## 10. Condições de parada

Pare se:

- o head ou a base mudar de forma material;
- o workflow não pertencer ao head exato;
- um gate ou autorização estiver vinculado a outro head;
- surgir finding material não resolvido;
- reviews ou threads não puderem ser lidas;
- faltar autorização para a transição mutável aplicável;
- houver divergência de `Next action ID` entre os documentos.

## 11. Atualização deste registro

Atualizar somente quando mudar a política, a máquina de transição, a autoridade, o escopo ou um bloqueio material. Não atualizar por simples mudança de status da PR, conclusão de gate ou consumo de uma autorização no mesmo head.
