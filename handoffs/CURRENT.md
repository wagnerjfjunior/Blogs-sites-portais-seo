# Handoff Atual — Ecossistema de Blogs, Sites, Portais e SEO

- Status: continuidade operacional baseada em estado live
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Adoção SFJM: PR #2, estado resolvido live
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Objetivo operacional

Retomada entre conversas e especialistas com fonte, revisões, lacunas, bloqueios, autorizações, transições explícitas e inventário de ativos SEO sem absorver a autoridade operacional dos projetos consumidores.

## Estado confirmado

1. Framework GPT0–GPT8 introduzido pela PR #1.
2. Nove GPTs privados.
3. Action GitHub `READ_ONLY`.
4. PR #2 rastreia a adoção SFJM; estado, head, base e workflow são live.
5. GPT0 é head-bound; GPT4 é head+base-bound.
6. Ready e merge são separados e exigem head/base.
7. Estados closed e merged possuem transições.
8. O MoreNumTegra foi selecionado pelo Product Authority como primeiro ativo para handoff de governança SEO ao ecossistema; a integração canônica depende do merge da PR correspondente.

## Ativo SEO inicial — MoreNumTegra

Registro candidato:

```text
ASSET_ID: morenumtegra
IMPLEMENTATION_REPOSITORY: wagnerjfjunior/MoreNumTegra
DOMAIN: moreemumtegra.com.br
DOMAIN_STATUS: USER_REPORTED_PURCHASED
DOMAIN_OWNERSHIP_VERIFIED: false
DNS_VERIFIED: false
CODE_MOVED_TO_ECOSYSTEM: false
```

O ecossistema recebe estratégia de portfólio, pesquisa, clusters, conteúdo, SEO técnico, autoridade e mensuração quando autorizada.

O repositório `wagnerjfjunior/MoreNumTegra` continua autoridade para código, release, Vercel, Green Sales e demais mutações do produto.

Fonte detalhada do handoff:

`docs/assets/morenumtegra-seo-handoff.md`

## Evidência de keyword research do ativo

Dois exports foram fornecidos pelo owner em 2026-08-26 e permanecem fora do repositório nesta etapa:

- `Keyword Stats 2026-08-26 at 15_23_07_cyrela_google_e_parceiros.csv` — período `1 de agosto de 2025 - 31 de julho de 2026`, 2.182 linhas de keywords;
- `Keyword Stats 2026-08-26 at 15_22_21Tegra_parceiros.csv` — mesmo período, 1.937 linhas de keywords.

Tratar como `USER_PROVIDED_KEYWORD_EXPORT`. Não inventar volume, CPC, concorrência ou dificuldade e não ocultar limitações da fonte.

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` canônica | aprovada | governança |
| SFJM operacional | aprovado para PR #2 | Product Authority |
| Tabela e manifesto autoritativos | aprovado | `NEXT_SAFE_ACTION` e `sfjm.yaml` |
| Estado volátil não versionado | aprovado | política SFJM |
| MoreNumTegra permanece repo consumidor autônomo | aprovado no escopo do handoff | Product Authority + handoff candidato |
| estratégia SEO do MoreNumTegra é gerida pelo ecossistema após integração | candidato até merge | `docs/assets/morenumtegra-seo-handoff.md` |
| novos domínios não são comprados apenas por volume de keyword | candidato até merge | handoff do ativo |
| backlinks seguem link earning/digital PR, sem PBN | candidato até merge | handoff + contrato GPT6 |

## Entregas duráveis

Framework, estrutura SFJM, evidência upstream, máquina de lifecycle, validador e testes adversariais. Após merge do handoff, o inventário de ativos passa a incluir MoreNumTegra como primeiro ativo SEO gerenciado.

## Trabalho em andamento

Calcular lifecycle live pela máquina. Não declarar snapshot neste arquivo.

No fluxo SEO, após integração do handoff, a sequência recomendada é:

```text
GPT1 arquitetura do ecossistema
-> GPT2 keyword mapping e clusters
-> GPT5 arquitetura editorial/internal linking
-> GPT3 contrato técnico SEO
-> GPT6 autoridade/digital PR quando houver ativos publicáveis
-> GPT8 mensuração somente após gate próprio
```

## Lacunas

- inventário geral de ativos ainda incompleto;
- ownership e DNS de `moreemumtegra.com.br` não verificados;
- Builder, ambientes, métricas e produção do ecossistema não foram revalidados;
- analytics/Search Console do MoreNumTegra não são presumidos;
- arquivos brutos de keyword research não estão versionados neste repositório.

## Riscos ativos

| Risco | Controle |
|---|---|
| Gate ou autorização de outra revisão | exigir head/base exatos |
| Merge ref confundido com head | checkout explícito do head |
| Gate não passante avançar | transições de parada |
| Estado terminal sem ação | transições merged/closed |
| Divergência tabela/manifesto | comparação determinística |
| governança SEO ser confundida com autorização no repo consumidor | fronteira de autoridade documentada por ativo |
| domínio reportado ser confundido com DNS live | estados de verificação separados |
| expansão para múltiplos domínios gerar redundância/PBN | GPT1 antes de domínio e GPT6 para política de links |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Ações bloqueadas

Mutações sem autorização, gate não passante, merge sem autorização, Builder, deploy, produção, DNS, aquisição de domínio, tracking e ações externas não autorizadas.

## Ordem de continuidade

1. `bootstrap/BOOTSTRAP_CANONICO.md`
2. `handoffs/CURRENT.md`
3. `docs/PROJECT_STATUS.md`
4. `docs/NEXT_SAFE_ACTION.md`
5. `docs/BLOCKED_ACTIONS.md`
6. `config/project.yaml`
7. `config/gpts.yaml`

## Prompt curto

> Resolva o lifecycle live. Para SEO de portfólio, trate MoreNumTegra como ativo consumidor governado pelo handoff em `docs/assets/morenumtegra-seo-handoff.md`, sem propagar autoridade para código, Green, Vercel, DNS ou analytics.
