# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Política: lifecycle resolvido live, sem snapshot volátil
- Specialist model: SES shared specialists + Project Adapter + `config/specialists.yaml`
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Resultado pretendido

Ecossistema digital com especialistas compartilhados pelo SES, governança versionada, adoção explícita por projeto, portfólio de ativos SEO gerenciados e continuidade baseada em revisões verificáveis, bloqueios e máquina segura.

## Estado por frente

| Frente | Estado durável | Evidência | Próximo marco live | Bloqueio |
|---|---|---|---|---|
| Specialist framework | SES canônico | SES `CANONICAL_SPECIALIST_FRAMEWORK` | consumir via Adapter | nenhum de identidade |
| Project specialist adoption | migração V1 em PR | `config/specialists.yaml` | validar e integrar | PRs antigas podem reintroduzir drift |
| Legacy GPT0–GPT8 assets | preservados como continuidade/história | `config/gpts.yaml`, Builder/skills/tests | retirement por Builder quando elegível | equivalência/autorização ausentes |
| Documentation gate | SES role definido | `documentation_audit -> documentation-auditor` | aplicar no head exato | gate não passante para |
| Lifecycle gate | SFJM project governance | `config/sfjm.yaml` | aplicar head+base | não há archetype substituto |
| Action READ_ONLY | concluída | schema OpenAPI | preservar durante legado | mutações desabilitadas |
| Lifecycle | definido | governança | aplicar máquina | gates não passantes param |
| Ativos SEO | iniciado | `docs/assets/morenumtegra-seo-handoff.md` | integrar handoff e iniciar baseline read-only | inventário geral ainda incompleto |
| MoreNumTegra | Search consumer via cross-project service | SES adoption matrix + handoff + repo consumidor | executar somente as cinco roles Search provider após contexto/handoff válidos | architecture/UX/implementação/autoridade continuam no repo consumidor |
| Domínios | inventário parcial | `moreemumtegra.com.br` como `USER_REPORTED_PURCHASED` | verificar ownership/DNS somente em gate próprio | ownership e DNS não verificados |
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

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` canônica | aprovada | governança |
| Specialist identity SES | canônica | SES Canonical Specialist Framework |
| Specialist adoption project-local | migração proposta | `config/specialists.yaml` |
| Legacy GPT registry | continuidade/história | `config/gpts.yaml` |
| MoreNumTegra Search service | decisão SES vigente; registro local candidato até integração | SES current adoption matrix + `docs/assets/morenumtegra-seo-handoff.md` |
| Código/release do MoreNumTegra permanece externo | preservado | `wagnerjfjunior/MoreNumTegra` |
| Novos domínios exigem tese própria | definido no handoff | política do ativo |
| Backlinks manipulativos/PBN não são estratégia autorizada | definido | política de autoridade |

## Decisões necessárias

| Decisão | Autoridade | Condição |
|---|---|---|
| Documentation audit | SES Documentation Auditor | workflow verde no head |
| Lifecycle gate | SFJM project governance | documentation audit passando, head/base atuais |
| Ready | Wagner | gates passando e autorização head/base |
| Merge | Wagner | review atual, gates passando e autorização posterior head/base |
| Builder retirement | Wagner | equivalência, testes/runtime proof e replacement elegível por Builder |
| Builder externo change | Wagner | escopo/fingerprint/revalidação específicos |
| Novo domínio | Wagner | tese, público, proposta de valor, owner, papel no portfólio e análise de canibalização |
| Mutação no MoreNumTegra | autoridade do projeto consumidor | lifecycle e autorização próprios do ativo |

## Dependências e bloqueios

Mudança de head invalida todos os gates/autorizações. Mudança só da base invalida lifecycle gate e autorizações de transição. `BLOCK` e `INCONCLUSIVE` impedem Ready/merge.

PRs abertas anteriores à migração devem ser reconciliadas se puderem reintroduzir nomenclatura operacional GPT numerada. O handoff SEO não propaga autorização para DNS, Green Sales, Vercel, analytics, Ads ou alterações no repositório consumidor.

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
| Governança SEO confundida com ownership de implementação | manter fronteira explícita por ativo |
| Domínio reportado tratado como DNS/ownership verificado | separar estados de evidência |
| Comprar domínios por volume sem tese | `architecture` + `seo_strategy` antes de aquisição |
| Rede própria de backlinks degradar para PBN | proibir finalidade primária de manipulação de autoridade |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Fora do escopo

Builder externo live, retirement sem gate, domínios/DNS, hospedagem, deploy, produção, campanhas, compra de backlinks, tracking/analytics sem gate e qualquer mutação em projeto consumidor.

Pesquisa, estratégia, Technical SEO, Content/Semantic SEO, Search Analytics e Paid Search read-only podem ser executados pelo provider quando o contexto e a autoridade do ativo estiverem resolvidos. Architecture e UX/UI permanecem roles diretas do MoreNumTegra e recebem handoffs quando necessário.

## Atualização

Somente por mudança durável de política, estrutura, specialist adoption, máquina, risco, bloqueio, escopo ou inventário de ativos; não por gate, metadata, autorização ou estado terminal.
