# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Política: lifecycle resolvido live, sem snapshot volátil
- Specialist model: SES shared specialists + Project Adapter + `config/specialists.yaml`
- Portfolio strategy: `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md`
- Portfolio registry: `config/assets.yaml`
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Resultado pretendido

Ecossistema profissional de ativos digitais com papéis claros, audiência própria, autoridade temática, aquisição orgânica/paga, leads, monetização e valor comercial sustentável. Novos projetos devem ser encaixados por tese e evidência antes de domínio/implementação para evitar retrabalho, canibalização e redes artificiais de links.

## Estado por frente

| Frente | Estado durável | Evidência | Próximo marco live | Bloqueio |
|---|---|---|---|---|
| Specialist framework | SES canônico | SES `CANONICAL_SPECIALIST_FRAMEWORK` | consumir via Adapter | nenhum de identidade conhecido |
| Project specialist adoption | integrado em `main` | `config/specialists.yaml` + PR #7 merged | consumir por ROLE -> ARCHETYPE_ID | nenhum blocker de identidade conhecido |
| Portfolio strategy | candidato nesta PR | `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md` | validar/integrar | ainda não em `main` |
| Portfolio registry | candidato nesta PR | `config/assets.yaml` | validar/integrar | ainda não em `main` |
| Legacy GPT0–GPT8 assets | preservados como continuidade/história | `config/gpts.yaml`, Builder/skills/tests | retirement por Builder quando elegível | equivalência/autorização ausentes |
| Documentation gate | SES role definido | `documentation_audit -> documentation-auditor` | aplicar no head exato | gate não passante para |
| Lifecycle gate | SFJM project governance | `config/sfjm.yaml` | aplicar head+base | não há archetype substituto |
| Action READ_ONLY | concluída | schema OpenAPI | preservar durante legado | mutações desabilitadas |
| Lifecycle | definido | governança | aplicar máquina | gates não passantes param |
| MoreNumTegra | ativo `P0` / `COMMERCIAL_CONVERSION_HUB` candidato nesta PR | registry + handoff + provider recommendation | concluir gate e devolver resultado ao consumer | implementação permanece no consumer |
| Caminhos da Lapa Tegra | `CREATE_NEW_ASSET_CANDIDATE`; `EDITORIAL_AUTHORITY_PROPERTY` + `LOCAL_DISCOVERY_PROPERTY` | registry + placement ADR + lifecycle contract | aceitar placement e depois definir consumer repo/RESF adoption/IA | sem implementação/runtime autorizada |
| Real-estate lifecycle ownership | contrato candidato | Architecture + Content/Semantic SEO rechecks `PASS_WITH_RESIDUAL_RISK` | Product Authority acceptance | commercial-closure predicate ainda precisa regra |
| Search provider result | produzido nesta PR | `docs/assets/morenumtegra-search-provider-recommendation-2026-08-28.md` | consumer adjudicar P0 | provider não tem mutation authority no consumer |

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

## MoreNumTegra — estado Search atual

O handoff consumer `handoffs/SEARCH_PROVIDER_HANDOFF_2026-08-28.md` foi consumido contra `wagnerjfjunior/MoreNumTegra@b4cdbc1ac0be9a98112cb74a378571b64cf16e7f`.

A recomendação provider candidata define como P0:

- canonical raiz `https://moretegra.com.br/`;
- tratamento consistente do `www`, preferindo 301/308 real quando viável;
- title/meta description finais;
- robots/indexabilidade da Green;
- sitemap;
- Search Console por gate próprio;
- separação Vercel `noindex`;
- smoke HTTP/canonical pós-publicação.

P1 inclui JSON-LD conservador, OG/Twitter, rendered-content validation, CWV baseline, arquitetura de páginas e internal linking. P2 inclui SEM após tracking/conversion/spend gates e Authority/Digital PR apenas quando a role SES se tornar elegível/adotada.

A superfície de web-fetch independente do provider não conseguiu recuperar `https://moretegra.com.br/` nesta execução; por isso claims HTTP/live permanecem vinculados ao handoff consumer datado e exigem recheck antes da aceitação de implementação.

## Placement de ativos

Todo novo projeto deve entrar primeiro em `config/assets.yaml` e ser classificado antes de domínio/arquitetura material.

Resultados permitidos de intake:

- `ATTACH_TO_EXISTING_ASSET`;
- `CREATE_NEW_ASSET_CANDIDATE`;
- `CREATE_CAMPAIGN_SURFACE`;
- `DEFER_INSUFFICIENT_THESIS`;
- `REJECT_MANIPULATIVE_OR_REDUNDANT`.

MoreNumTegra é a prioridade operacional atual, mas não é sinônimo do ecossistema inteiro. A arquitetura deve continuar apta a receber propriedades editoriais, locais, comparadores, diretórios/data products e campanhas quando houver tese independente.

### Caminhos da Lapa Tegra

`caminhosdalapategra.com.br` passa a ser registrado como candidato de ativo irmão do MoreNumTegra, com tese independente e durável:

- `EDITORIAL_AUTHORITY_PROPERTY` como papel primário;
- `LOCAL_DISCOVERY_PROPERTY` como papel secundário;
- foco em Caminhos da Lapa como complexo/microbairro, evolução e entidades constituintes;
- MoreNumTegra preserva current commercial intent enquanto houver comercialização governada;
- o site oficial/institucional externo é fonte de evidência, não ativo do portfólio;
- lifecycle Search/runtime segue `docs/governance/REAL_ESTATE_ASSET_LIFECYCLE_OWNERSHIP_CONTRACT.md`;
- RESF atual: `AVAILABLE_NOT_ADOPTED`.

A criação de páginas, migração de conteúdo, redirect, noindex, canonical, DNS, tracking ou deploy não é autorizada por este placement.

## Decisões necessárias

| Decisão | Autoridade | Condição |
|---|---|---|
| Documentation audit | SES Documentation Auditor | workflow verde no head |
| Lifecycle gate | SFJM project governance | documentation audit passando, head/base atuais |
| Ready | Wagner | gates passando e autorização head/base |
| Merge | Wagner | review atual, gates passando e autorização posterior head/base |
| Implementar recomendação Search no MoreNumTegra | MoreNumTegra Product Authority | adjudicação do provider result + escopo exato |
| Aceitar placement do Caminhos da Lapa Tegra | Wagner / Product Authority | registry + ADR + lifecycle contract revisados |
| Criar consumer repo / implementar Caminhos | Wagner / Product Authority | placement aceito + consumer lifecycle + escopo explícito |
| Adotar RESF no Caminhos | Caminhos Product Authority | manifesto seletivo pinando provider commit |
| Search Console / DNS verification | MoreNumTegra Product Authority | gate próprio |
| Analytics/tracking | MoreNumTegra Product Authority | consent/privacy + measurement gate |
| SEM spend/publication | MoreNumTegra Product Authority | conversion/tracking + budget authorization |
| Builder retirement | Wagner | equivalência, testes/runtime proof e replacement elegível por Builder |

## Dependências e bloqueios

Mudança de head invalida gates/autorizações vinculados ao head. Mudança só da base invalida lifecycle gate e autorizações de transição. `BLOCK` e `INCONCLUSIVE` impedem Ready/merge.

Mudança de portfólio ou novo projeto não autoriza automaticamente novo domínio, backlinks, deploy, tracking ou spend.

## Riscos

| Risco | Mitigação |
|---|---|
| snapshot obsoleto | resolver live |
| taxonomia legada voltar a ser authority | `config/specialists.yaml` é novo routing locator |
| projeto novo virar domínio sem tese | portfolio-fit obrigatório antes de implementação |
| canibalização entre propriedades | mapear público/intenção/canonical role antes da criação |
| rede própria degradar para PBN | cada ativo exige valor próprio; links editoriais/contextuais apenas |
| MoreNumTegra dominar arquitetura do ecossistema | tratá-lo como `P0 COMMERCIAL_CONVERSION_HUB`, não como modelo único |
| Caminhos duplicar current commercial intent | durable/context role + active commercial owner separados |
| domínio independente parecer oficial | declarar boundary e usar official source apenas como evidência externa |
| estado comercial disparar mudança técnica automática | lifecycle transition != runtime/Search mutation |
| provider assumir autoridade do consumer | handoff + boundaries explícitos |
| HTTP/canonical sobreafirmado | recheck live antes da aceitação |
| Local/Authority target tratados como certificados | fail closed até registry/certification SES |
| monetização sem replacement | manter exceção project-local explícita |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live da PR e executar somente a primeira transição aplicável da máquina de lifecycle.

## Fora do escopo sem autorização específica

Builder externo live, retirement, mutação no MoreNumTegra, DNS, deploy, publicação, produção, tracking, Search Console via DNS, campanhas/spend e aquisição de novos domínios.

## Atualização

Somente por mudança durável de política, estrutura, specialist adoption, estratégia, portfolio placement, máquina, risco, bloqueio ou escopo; não por mero gate, metadata, autorização ou estado terminal.
