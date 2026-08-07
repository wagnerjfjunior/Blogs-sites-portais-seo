# Próxima Ação Segura — Ecossistema de Blogs, Sites, Portais e SEO

> Este é o registro atual autoritativo da única próxima ação segura do projeto.

- Next action ID: `resolve-live-lifecycle-transition-v1`
- Fonte de estado: GitHub live, resolvido no início de cada execução
- Função versionada: política e máquina de transição, não snapshot volátil da PR
- Autoridade material: Wagner

Resumos no bootstrap, handoff, status e bloqueios são derivados. A tabela abaixo é comparada deterministicamente ao manifesto.

## 1. Ação

Resolver o estado live do repositório, da PR, do head, da base, da tentativa mais recente do workflow canônico, dos gates, das autorizações, da ordem temporal Ready/merge, das reviews, das threads e de eventual verificação pós-merge; em seguida, executar somente a primeira transição aplicável.

Uma execução verde antiga não prevalece sobre tentativa mais recente falha, cancelada, pendente ou em andamento no mesmo head.

## 2. Máquina de transição

| Prioridade | ID | Condição (`when`) | Ação (`action`) |
|---:|---|---|---|
| 0 | `verify_merged_main` | `pull_request_is_merged_and_main_verification_is_absent` | `verify_merge_commit_and_main_then_record_external_evidence` |
| 1 | `report_completed_lifecycle` | `pull_request_is_merged_and_main_verification_is_present` | `report_lifecycle_complete_without_mutation` |
| 2 | `report_closed_unmerged` | `pull_request_is_closed_and_not_merged` | `report_closed_unmerged_and_require_explicit_reopen_or_abandon_decision` |
| 3 | `stop_on_drift_or_material_finding` | `open_pull_request_has_head_or_base_drift_or_material_unresolved_finding` | `stop_and_reconcile_under_explicit_authorization` |
| 4 | `require_successful_workflow` | `latest_canonical_workflow_attempt_for_exact_head_is_not_completed_success` | `wait_or_rerun_only_if_authorized` |
| 5 | `run_gpt0_read_only` | `latest_canonical_workflow_attempt_for_exact_head_is_completed_success_and_no_current_gpt0_gate` | `execute_documentary_gate_without_mutation` |
| 6 | `stop_on_gpt0_block` | `current_gpt0_gate_verdict_is_block` | `stop_and_require_material_remediation_authorization` |
| 7 | `stop_on_gpt0_inconclusive` | `current_gpt0_gate_verdict_is_inconclusive` | `stop_and_require_missing_evidence_or_access` |
| 8 | `run_gpt4_read_only` | `current_gpt0_gate_verdict_is_passing_and_no_current_gpt4_gate` | `execute_lifecycle_gate_without_mutation` |
| 9 | `stop_on_gpt4_block` | `current_gpt4_gate_verdict_is_block` | `stop_and_require_material_remediation_authorization` |
| 10 | `stop_on_gpt4_inconclusive` | `current_gpt4_gate_verdict_is_inconclusive` | `stop_and_require_missing_evidence_or_access` |
| 11 | `require_ready_authorization` | `current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_draft_and_exact_head_and_base_ready_authorization_is_absent` | `require_explicit_ready_authorization_for_exact_head_and_base` |
| 12 | `execute_ready_transition` | `current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_draft_and_exact_head_and_base_ready_authorization_is_present` | `mark_pull_request_ready_only` |
| 13 | `recheck_ready_reviews` | `current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_ready_and_review_state_changed_since_latest_eligible_gate_or_recheck` | `adjudicate_material_findings_before_merge` |
| 14 | `require_merge_authorization` | `current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_ready_review_state_is_current_no_material_threads_remain_and_post_ready_exact_head_and_base_merge_authorization_is_absent` | `require_explicit_post_ready_merge_authorization_for_exact_head_and_base` |
| 15 | `execute_merge_and_verify_main` | `current_gpt0_and_gpt4_gate_verdicts_are_passing_pull_request_is_ready_review_state_is_current_no_material_threads_remain_and_post_ready_exact_head_and_base_merge_authorization_is_present` | `merge_exact_head_then_verify_merge_commit_and_main_without_propagating_authority` |

`passing` significa exclusivamente `PASS` ou `PASS_WITH_RESIDUAL_RISK`. `BLOCK` e `INCONCLUSIVE` selecionam transições de parada e nunca autorizam Ready ou merge.

## 3. Regra antíloop

- A tentativa mais recente do workflow canônico para o head exato é a única autoridade de CI.
- GPT0 permanece elegível enquanto o head não mudar.
- GPT4 permanece elegível enquanto head e base não mudarem.
- Ready e merge exigem autorizações separadas vinculadas ao head e à base observados.
- A autorização de merge somente é elegível quando concedida depois da transição Ready.
- Autorização antecipada ou conjunta de merge não pode ser reutilizada após Ready.
- A progressão GPT0 → GPT4 → Ready não exige commit intermediário.
- Mudança apenas de metadata da PR não invalida gates vinculados às mesmas revisões.
- Somente correção material que altere arquivos ou head reinicia workflow e GPT0.
- Mudança somente da base exige nova avaliação GPT4 e invalida autorizações de transição anteriores.
- Finding não material deve ser risco residual ou backlog, sem nova rodada corretiva.

## 4. Pré-condições

- resolver `main`, PR, base e head live;
- selecionar a tentativa mais recente do workflow canônico para o head exato;
- confirmar `status: completed` e `conclusion: success` nessa tentativa;
- confirmar por estrutura YAML que o workflow faz checkout do head exato da PR;
- usar apenas GPT0 vinculado ao head atual;
- usar apenas GPT4 vinculado ao head e à base atuais;
- resolver autorizações live e exigir correspondência com head, base e ordem temporal;
- verificar review completa, threads e mergeabilidade;
- confirmar autorização específica antes de qualquer mutação.

## 5. Resultado verificável

Cada transição deve produzir evidência contendo repositório, PR, base, branch, head, ID e número da tentativa mais recente do workflow, status, conclusion, gates, vereditos, autorizações, ordem verificável, findings, mutações e, quando aplicável, merge commit e novo `main`.

## 6. Limites explícitos

Resolução live e gates `READ_ONLY` não autorizam correção, Ready, merge, Builder, deploy, publicação, produção, atividade SEO ou propagação de autoridade.

## 7. Autorização

- GPT0 e GPT4 `READ_ONLY`: permitidos quando forem a primeira transição aplicável.
- Correção material: exige escopo explícito.
- Ready ausente: solicitar autorização para head e base exatos.
- Ready autorizada: executar somente Draft → Ready.
- Merge ausente: solicitar autorização posterior e separada depois de Ready para head e base exatos.
- Merge autorizado antes ou junto de Ready: inelegível para merge.
- Merge autorizado depois de Ready: executar somente o merge do head exato e verificar merge commit e `main`.
- Builder, deploy e produção permanecem fora de escopo.

## 8. Evidência dos gates e autorizações

- CI é vinculada ao head e à tentativa mais recente.
- GPT0 é vinculado ao head auditado.
- GPT4 é vinculado ao head e à base avaliados.
- Autorização de Ready é vinculada ao head e à base observados.
- Autorização de merge é vinculada ao head e à base e deve ser posterior ao Ready.
- Mudança de head invalida gates e autorizações anteriores.
- Mudança somente de base invalida GPT4 e autorizações de transição, mas não exige repetir GPT0 se o head não mudou.
- Verificação pós-merge é vinculada ao merge commit e ao novo `main`.

## 9. Verificação de conclusão

A etapa está concluída quando a primeira transição foi executada, não houve ação posterior automática, a tentativa mais recente de CI e as revisões permaneceram estáveis e o próximo estado continua calculável.

## 10. Condições de parada

Pare diante de drift, tentativa mais recente de workflow diferente de `completed/success`, semântica YAML divergente, gate ou autorização de outra revisão, autorização de merge não posterior ao Ready, `BLOCK`, `INCONCLUSIVE`, finding material, review incompleta, thread material, falta de autoridade ou divergência entre tabela e manifesto.

## 11. Atualização deste registro

Atualizar somente quando mudar política, máquina, autoridade, escopo ou bloqueio material. Não atualizar por simples conclusão de gate, mudança de metadata, autorização ou estado terminal já representado pela máquina.
