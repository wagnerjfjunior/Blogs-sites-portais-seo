# Handoff Atual — Ecossistema de Blogs, Sites, Portais e SEO

- Status: continuidade operacional baseada em estado live
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Specialist model: SES shared specialists + Project Adapter + project-local adoption
- Portfolio strategy: `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md`
- Portfolio registry: `config/assets.yaml`
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Objetivo operacional

Construir e operar um ecossistema de ativos digitais com papéis explícitos, Search/SEM coordenados, autoridade e monetização sustentáveis, mantendo cada projeto corretamente posicionado antes de implementação para evitar canibalização e retrabalho.

A continuidade entre conversas/especialistas deve reconstruir não apenas lifecycle, mas também a tese do portfólio e o placement de cada ativo.

## Estado confirmado

1. A arquitetura canônica de especialistas pertence ao SES e usa `CANONICAL_NAME + ARCHETYPE_ID`.
2. Este projeto adota especialistas por `ROLE -> ARCHETYPE_ID` em `config/specialists.yaml` e via Project Adapter SES.
3. `config/gpts.yaml` e seus Builders/skills/tests permanecem apenas como continuidade/história e exceções project-local explicitadas.
4. A Action GitHub project-local permanece `READ_ONLY`.
5. O gate documental é `documentation_audit` / `documentation-auditor`, head-bound.
6. O gate de lifecycle é governança project-local SFJM, head+base-bound.
7. Ready e merge são separados e exigem head/base atuais e autorizações separadas.
8. Local SEO e Authority & Digital PR permanecem TARGET no SES; não podem ser tratados como archetypes ativos/adotados antes da certificação/registro.
9. Monetização permanece capability project-local sem replacement SES canônico neste momento.
10. MoreNumTegra mantém as cinco capabilities Search `ADOPTED`; a execução project-local delega essas tarefas a este projeto como provider.
11. O repo `wagnerjfjunior/MoreNumTegra` permanece fonte canônica da implementação e da autoridade do ativo.
12. MoreNumTegra é o ativo `P0` do ciclo atual, classificado no portfolio candidate como `COMMERCIAL_CONVERSION_HUB`.
13. Novos projetos/domínios devem passar por portfolio-fit antes de implementação.
14. O handoff `wagnerjfjunior/MoreNumTegra/handoffs/SEARCH_PROVIDER_HANDOFF_2026-08-28.md` foi consumido e recebeu uma recomendação provider versionada nesta PR.

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` canônica project-local | aprovada | governança |
| Specialist identity SES | canônica | SES Canonical Specialist Framework |
| Specialist adoption project-local | integrado em `main` pela PR #7 | `config/specialists.yaml` + merge `a2ef316933861a3aaffbee81fb8b73b76e2fd315` |
| Legacy GPT registry | continuidade/história | `config/gpts.yaml` |
| SFJM operacional | aprovado | Product Authority |
| Tabela e manifesto autoritativos | aprovado | `NEXT_SAFE_ACTION` e `sfjm.yaml` |
| Estado volátil não versionado | aprovado | política SFJM |
| Estratégia mestra do ecossistema | candidata nesta PR | `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md` |
| Portfolio registry | candidato nesta PR | `config/assets.yaml` |
| MoreNumTegra Search service | decisão SES vigente; handoff local candidato nesta PR | SES adoption matrix + handoff local |
| MoreNumTegra placement | `P0 / COMMERCIAL_CONVERSION_HUB` candidato | portfolio registry |
| Provider Search recommendation | produzida nesta PR | `docs/assets/morenumtegra-search-provider-recommendation-2026-08-28.md` |
| Implementação MoreNumTegra | permanece no repo consumidor | `wagnerjfjunior/MoreNumTegra` |

## Entregas duráveis desta rodada

- estratégia mestra do ecossistema, incluindo domínio/asset intake e regra anti-retrabalho;
- registry de ativos com MoreNumTegra como primeira prioridade operacional;
- recomendação Search versionada para canonical, `www`, metadata, robots, sitemap, Search Console, JSON-LD, arquitetura, conteúdo, mensuração e SEM;
- atualização do bootstrap/status/handoff para tornar objetivo e placement reconstruíveis sem depender da conversa.

## MoreNumTegra — resultado devolvido pelo provider

Consumer main observado na entrada do provider:

```text
wagnerjfjunior/MoreNumTegra@b4cdbc1ac0be9a98112cb74a378571b64cf16e7f
```

Prioridade recomendada:

```text
P0 canonicalidade / hostname / metadata / robots / sitemap / Search Console
-> P1 JSON-LD / social metadata / rendering / CWV / IA / internal linking / measurement
-> P2 SEM após conversion+tracking+budget gates
-> Authority/Digital PR somente após elegibilidade/adoption SES
```

A superfície geral de web-fetch do provider não conseguiu recuperar a produção nesta execução. Claims HTTP/live são portanto atribuídas ao handoff consumer datado e devem ser rechecadas antes da aceitação da implementação.

## MoreNumTegra — Prêmio Master Imobiliário 2026

Novo provider result:

`docs/assets/morenumtegra-master-imobiliario-2026-search-guidance-2026-08-29.md`

Evidência externa confirmada em 2026-08-29:

- Tegra / RIIO by Piero Lissoni — Prêmio Master Imobiliário 2026, categoria `Profissional – Soluções Arquitetônicas`;
- Caminhos da Lapa / Helbor | Toledo Ferrari | Tegra — categoria `Empreendimento – Qualificação Urbana`.

Boundary Search:

- usar o prêmio como prova institucional/masterplan;
- não afirmar que cada condomínio individual ganhou o prêmio;
- badge recomendado deve explicitar `masterplan premiado` ou relação equivalente;
- fonte SECOVI-SP deve ser visível no bloco institucional;
- implementação visual e lifecycle permanecem no MoreNumTegra.

Consumer implementation observed for this provider result:

`wagnerjfjunior/MoreNumTegra PR #32 @ 38a8c20de236c9fda75b0b57236df94592803c1a`

O provider não mutou o consumer.

## Trabalho em andamento

Validar e integrar esta PR sem transferir autoridade ao provider. Após integração, MoreNumTegra deve adjudicar o provider result e decidir o escopo P0 de implementação no próprio lifecycle.

## Lacunas

- independent HTTP fetch da produção pelo provider nesta execução;
- Search Console e sitemap não comprovados;
- tracking/GA4/GSC data não comprovados;
- keyword exports brutos referenciados historicamente ainda não são evidência versionada no repositório;
- Local SEO e Authority & Digital PR aguardam lifecycle SES;
- Builder live/retirement continua gate separado.

## Riscos ativos

| Risco | Controle |
|---|---|
| novo projeto virar domínio sem tese | `config/assets.yaml` + estratégia mestra |
| MoreNumTegra ser confundido com o ecossistema inteiro | primary role/priority explícitos |
| nomenclatura GPT numerada voltar ao roteamento | `config/specialists.yaml` + testes de regressão |
| provider assumir autoridade do consumer | fronteira cross-project explícita |
| páginas/facetas em escala gerarem thin/duplicate content | URL indexável somente com tese e conteúdo próprio |
| gate ou autorização de outra revisão | exigir head/base exatos |
| SES adoption confundida com Builder retirement | gate separado por Builder |
| Authority/Digital PR ser antecipado | fail closed até role SES elegível/adotada |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver PR/head/base/workflow/gates live e executar somente a primeira transição aplicável.

## Ações bloqueadas

Sem autorização específica: merge, Builder retirement, mutação no MoreNumTegra, DNS, deploy, produção, Search Console via DNS, tracking, campanhas/spend e novos domínios.

## Ordem de continuidade

1. `bootstrap/BOOTSTRAP_CANONICO.md`
2. `handoffs/CURRENT.md`
3. `docs/PROJECT_STATUS.md`
4. `docs/NEXT_SAFE_ACTION.md`
5. `docs/BLOCKED_ACTIONS.md`
6. `config/project.yaml`
7. `config/specialists.yaml`

Quando portfolio/placement for material, ler também:

- `docs/strategy/ECOSYSTEM_MASTER_STRATEGY.md`;
- `config/assets.yaml`.

Quando MoreNumTegra Search for material, resolver o consumer live e ler o handoff/provider result vigente.

## Prompt curto

> Reconstrua SFJM + portfolio strategy + asset registry. Se a tarefa envolver MoreNumTegra, resolva consumer e provider live, consuma o handoff Search vigente, preserve a fronteira de autoridade e execute somente a primeira transição segura.
