# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Política: lifecycle resolvido live, sem snapshot volátil
- Adoção SFJM: PR #2
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Resultado pretendido

Ecossistema com nove GPTs, governança versionada, continuidade baseada em revisões verificáveis e portfólio de ativos SEO gerenciados sem absorver indevidamente a autoridade de implementação dos projetos consumidores.

## Estado por frente

| Frente | Estado durável | Evidência | Próximo marco live | Bloqueio |
|---|---|---|---|---|
| Framework GPT0–GPT8 | concluído | PR #1 | manter sincronismo | Builder não revalidado |
| Action READ_ONLY | concluída | schema OpenAPI | preservar | mutações desabilitadas |
| Lifecycle | definido | governança | aplicar máquina | gates não passantes param |
| Adoção SFJM | PR #2 | PR e branch | calcular transição | merge exige autorização |
| Ativos SEO | iniciado | `docs/assets/morenumtegra-seo-handoff.md` | executar arquitetura/pesquisa do primeiro ativo após integração | inventário geral ainda incompleto |
| MoreNumTegra | ativo consumidor registrado para governança SEO | handoff do ativo + repo consumidor | GPT1/GPT2 em modo read-only | implementação permanece no repo consumidor |
| Domínios | inventário parcial | `moreemumtegra.com.br` como `USER_REPORTED_PURCHASED` | verificar ownership/DNS somente em gate próprio | ownership e DNS não verificados |
| Produção | bloqueada | restrições | planejar | ambiente não aprovado pelo ecossistema |

## Marcos

Framework, kit SFJM, âncora upstream, máquina de lifecycle e testes adversariais são duráveis. O handoff do MoreNumTegra inicia o inventário de ativos SEO sem transformar este repositório em monorepo de produtos.

Gate, Ready, merge e pós-merge continuam estado live.

## Decisões vigentes

| Decisão | Estado | Fonte |
|---|---|---|
| `main` canônica | aprovada | governança |
| SFJM operacional | aprovado para PR #2 | Product Authority |
| MoreNumTegra como ativo SEO gerenciado | candidato até merge do handoff | `docs/assets/morenumtegra-seo-handoff.md` |
| código/release do MoreNumTegra permanece externo | preservado | repo consumidor `wagnerjfjunior/MoreNumTegra` |
| novos domínios exigem tese própria | definido no handoff | política do ativo |
| backlinks manipulativos/PBN não são estratégia autorizada | definido no handoff e contratos GPT6 | política de links |

## Decisões necessárias

| Decisão | Autoridade | Condição |
|---|---|---|
| GPT0 | GPT0 | workflow verde no head |
| GPT4 | GPT4 | GPT0 passando, head/base atuais |
| Ready | Wagner | gates passando e autorização head/base |
| Merge | Wagner | review atual, gates passando e autorização posterior head/base |
| Builder | Wagner | escopo por GPT |
| novos domínios | Wagner | tese, público, proposta de valor, owner e papel no portfólio |
| mutação no MoreNumTegra | autoridade do projeto consumidor | lifecycle e autorização próprios do ativo |

## Dependências e bloqueios

Mudança de head invalida todos os gates/autorizações. Mudança só da base invalida GPT4 e autorizações de transição. `BLOCK` e `INCONCLUSIVE` impedem Ready/merge.

O handoff SEO não propaga autorização para DNS, Green Sales, Vercel, analytics, Ads ou alterações no repositório consumidor.

## Riscos

| Risco | Mitigação |
|---|---|
| Snapshot obsoleto | resolver live |
| Merge ref validado como head | checkout explícito |
| Tabela divergente | comparação determinística |
| Estado terminal sem ação | transições terminal |
| Review material | rechecagem antes do merge |
| GitHub–Builder divergente | verificar individualmente |
| confundir governança SEO com ownership de implementação | manter fronteira explícita por ativo |
| tratar domínio reportado como DNS/ownership verificado | usar estados de evidência separados |
| comprar domínios por volume sem tese | GPT1 antes de aquisição |
| rede própria de backlinks degradar para PBN | política GPT6 de link earning/digital PR |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Fora do escopo sem autorização específica

Builder, alteração de domínio/DNS/hospedagem, deploy, produção, campanhas, aquisição de novos domínios, compra de backlinks, tracking/analytics e qualquer mutação em projetos consumidores.

Pesquisa, arquitetura e planejamento SEO read-only podem ser executados dentro dos contratos dos GPTs quando o contexto e a autoridade do ativo estiverem resolvidos.

## Atualização

Somente por mudança durável de política, estrutura, máquina, risco, bloqueio, escopo ou inventário de ativos; não por gate, metadata, autorização ou estado terminal.
