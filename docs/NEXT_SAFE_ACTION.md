# Próxima Ação Segura — Ecossistema de Blogs, Sites, Portais e SEO

> Este é o registro atual autoritativo da única próxima ação segura do projeto.

- Next action ID: `resolve-live-lifecycle-transition-v1`
- Fonte de estado: GitHub live, resolvido no início de cada execução
- Função versionada: política e máquina de transição, não snapshot volátil da PR
- Autoridade material: Wagner

Resumos no bootstrap, handoff e status são derivados. A sincronização é validada pelo mesmo `Next action ID`.

## 1. Ação

Resolver o estado live do repositório, da PR aplicável, do head, da base, dos checks, dos gates, das reviews e das threads; em seguida, executar somente a primeira transição aplicável da máquina abaixo.

Não editar documentos apenas para registrar a passagem de GPT0 para GPT4, Draft para Ready ou Ready para merge. Essas transições não alteram o head e são comprovadas por evidência externa vinculada ao head exato.

## 2. Máquina de transição

| Prioridade | Condição live | Única ação permitida |
|---:|---|---|
| 0 | head/base drift ou finding material não resolvido | parar e reconciliar somente sob autorização explícita |
| 1 | workflow canônico do head exato ausente, incompleto ou sem sucesso | aguardar ou reexecutar somente se autorizado |
| 2 | workflow verde e nenhum gate GPT0 elegível no head | executar GPT0 `READ_ONLY` |
| 3 | GPT0 elegível com `PASS` ou `PASS_WITH_RESIDUAL_RISK` e nenhum GPT4 elegível | executar GPT4 `READ_ONLY` |
| 4 | gates atuais e PR em Draft | exigir autorização explícita de Ready para o head exato |
| 5 | PR Ready e estado de review mudou | adjudicar findings materiais antes do merge |
| 6 | PR Ready, gates atuais e nenhuma thread material pendente | exigir autorização explícita de merge para o head exato |
| 7 | autorização de merge corresponde ao head exato | fazer merge e verificar `main` sem propagar autoridade |

## 3. Regra antíloop

- GPT0 e GPT4 devem usar o mesmo head congelado.
- A progressão GPT0 → GPT4 → Ready não exige commit intermediário.
- Mudança de metadata da PR não invalida gates vinculados ao mesmo head.
- Somente correção material que altere arquivos ou head reinicia workflow, GPT0 e GPT4.
- Finding não material deve ser classificado como risco residual ou backlog, sem nova rodada corretiva nesta PR.

## 4. Pré-condições

- resolver `main`, PR, base e head live;
- confirmar que o head permaneceu estável durante a etapa;
- usar somente gates que identifiquem o mesmo head exato;
- verificar workflow, reviews e threads mais recentes;
- confirmar autorização específica antes de qualquer mutação.

## 5. Resultado verificável

Cada transição deve produzir evidência contendo:

- repositório, PR, base, branch e head exatos;
- estado live relevante;
- checks ou gates aplicáveis;
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
- Ready: exige autorização humana separada e vinculada ao head.
- Merge: exige autorização humana posterior, separada e vinculada ao head.
- Builder, deploy e produção: permanecem fora de escopo até autorização própria.

## 8. Evidência dos gates

O resultado de GPT0 ou GPT4 é estado de execução externo e deve:

- identificar o head exato;
- registrar o veredito e as evidências;
- permanecer reutilizável enquanto o head não mudar;
- não exigir commit apenas para avançar ao gate seguinte.

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
- um gate estiver vinculado a outro head;
- surgir finding material não resolvido;
- reviews ou threads não puderem ser lidas;
- faltar autorização para a transição mutável aplicável;
- houver divergência de `Next action ID` entre os documentos.

## 11. Atualização deste registro

Atualizar somente quando mudar a política, a máquina de transição, a autoridade, o escopo ou um bloqueio material. Não atualizar por simples mudança de status da PR ou conclusão de um gate no mesmo head.
