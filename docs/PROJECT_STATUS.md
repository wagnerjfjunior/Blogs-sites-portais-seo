# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Política: lifecycle resolvido live, sem snapshot volátil
- Specialist model: SES shared specialists + Project Adapter + `config/specialists.yaml`
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Resultado pretendido

Ecossistema digital com especialistas compartilhados pelo SES, governança versionada, adoção explícita por projeto e continuidade baseada em revisões verificáveis, bloqueios e máquina segura.

## Estado por frente

| Frente | Estado durável | Evidência | Próximo marco live | Bloqueio |
|---|---|---|---|---|
| Specialist framework | SES canônico | SES `CANONICAL_SPECIALIST_FRAMEWORK` | consumir via Adapter | nenhum de identidade |
| Project specialist adoption | integrado em `main` | `config/specialists.yaml` + PR #7 merged | consumir por ROLE -> ARCHETYPE_ID | nenhum blocker de identidade conhecido |
| Legacy GPT0–GPT8 assets | preservados como continuidade/história | `config/gpts.yaml`, Builder/skills/tests | retirement por Builder quando elegível | equivalência/autorização ausentes |
| Documentation gate | SES role definido | `documentation_audit -> documentation-auditor` | aplicar no head exato | gate não passante para |
| Lifecycle gate | SFJM project governance | `config/sfjm.yaml` | aplicar head+base | não há archetype substituto |
| Action READ_ONLY | concluída | schema OpenAPI | preservar durante legado | mutações desabilitadas |
| Lifecycle | definido | governança | aplicar máquina | gates não passantes param |
| Ativos SEO | handoff MoreNumTegra candidato nesta PR | `docs/assets/morenumtegra-seo-handoff.md` | validar e integrar | inventário geral ainda incompleto |
| MoreNumTegra | Search consumer via provider project-local | SES current adoption matrix + MoreNumTegra/Blogs adapters + handoff | executar somente após contexto/handoff válidos | implementação/autoridade permanecem no consumidor |
| Produção | bloqueada | restrições | planejar | ambiente não aprovado |

## Portfolio SES adotado

Ativos/adotados para este projeto:

- `documentation_audit -> documentation-auditor`;
- `architecture -> software-systems-architect`;
- `ux_ui -> ux-ui-app-specialist`;
- `application_security -> application-security-assurance-specialist`;
- `seo_strategy -> seo-strategy-governance-specialist`;
- `technical_seo -> technical-seo-specialist`;
- `content_semantic_seo -> content-semantic-seo-specialist`;
- `seo_analytics_growth -> seo-analytics-growth-specialist`;
- `paid_search_sem -> paid-search-sem-specialist`.

Explicitamente não adotado: `backend_data`.

Ainda não adotáveis como archetype SES atual: Local SEO e Authority & Digital PR, enquanto permanecerem TARGET/certification pending/not registered. Authority/Digital PR mantém continuidade local controlada; monetização permanece exceção project-local sem equivalente SES canônico.

## MoreNumTegra Search service

O SES central registra MoreNumTegra com as cinco capabilities Search como `ADOPTED`, usando metadata project-local de execução delegada ao provider `blogs-sites-portais-seo`:

- `seo_strategy`;
- `technical_seo`;
- `content_semantic_seo`;
- `seo_analytics_growth`;
- `paid_search_sem`.

Este projeto atua como Search Center of Expertise/provider. MoreNumTegra preserva Product Authority, architecture/UX ownership, repository/implementation, deploy, budget, campaign publication e risk acceptance. Local SEO e Authority & Digital PR continuam future intent/TARGET enquanto não houver elegibilidade SES + ativação explícita.

```text
PROVIDER_SPECIALIST_WORK != CONSUMER_PROJECT_MUTATION
PROJECT_LOCAL_CROSS_PROJECT_SERVICE != PROJECT_OWNERSHIP_TRANSFER
```

## Decisões necessárias

| Decisão | Autoridade | Condição |
|---|---|---|
| Documentation audit | SES Documentation Auditor | workflow verde no head |
| Lifecycle gate | SFJM project governance | documentation audit passando, head/base atuais |
| Ready | Wagner | gates passando e autorização head/base |
| Merge | Wagner | review atual, gates passando e autorização posterior head/base |
| Builder retirement | Wagner | equivalência, testes/runtime proof e replacement elegível por Builder |
| Builder externo change | Wagner | escopo/fingerprint/revalidação específicos |

## Dependências e bloqueios

Mudança de head invalida todos os gates/autorizações. Mudança só da base invalida lifecycle gate e autorizações de transição. `BLOCK` e `INCONCLUSIVE` impedem Ready/merge.

PRs abertas anteriores à migração devem ser reconciliadas se puderem reintroduzir nomenclatura operacional GPT numerada.

## Riscos

| Risco | Mitigação |
|---|---|
| Snapshot obsoleto | resolver live |
| Merge ref validado como head | checkout explícito |
| Taxonomia legada voltar a ser authority | `config/specialists.yaml` é novo routing locator |
| Builder SES confundido com Builder legado | preservar fingerprints/evidência e retirement separado |
| Local/Authority target tratados como certificados | fail closed até registry/certification SES |
| Monetização sem replacement | manter exceção project-local explícita |
| GitHub–Builder divergência | verificar individualmente |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Fora do escopo

Builder externo live, retirement sem gate, domínios, DNS, hospedagem, deploy, produção, SEO operacional e avaliação experimental.

## Atualização

Somente por mudança durável de política, estrutura, specialist adoption, máquina, risco, bloqueio ou escopo; não por gate, metadata, autorização ou estado terminal.
