# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Política: lifecycle resolvido live, sem snapshot volátil
- Adoção SFJM: PR #2
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Resultado pretendido

Ecossistema com nove GPTs, governança versionada e continuidade baseada em revisões verificáveis, bloqueios e máquina segura.

## Estado por frente

| Frente | Estado durável | Evidência | Próximo marco live | Bloqueio |
|---|---|---|---|---|
| Framework GPT0–GPT8 | concluído | PR #1 | manter sincronismo | Builder não revalidado |
| Action READ_ONLY | concluída | schema OpenAPI | preservar | mutações desabilitadas |
| Lifecycle | definido | governança | aplicar máquina | gates não passantes param |
| Adoção SFJM | PR #2 | PR e branch | calcular transição | merge exige autorização |
| Ativos | não iniciado | registro ausente | definir inventário | dados ausentes |
| Produção | bloqueada | restrições | planejar | ambiente não aprovado |

## Marcos

Framework, kit SFJM, âncora upstream, máquina de lifecycle e testes adversariais são duráveis. Gate, Ready, merge e pós-merge são estado live.

## Decisões necessárias

| Decisão | Autoridade | Condição |
|---|---|---|
| GPT0 | GPT0 | workflow verde no head |
| GPT4 | GPT4 | GPT0 passando, head/base atuais |
| Ready | Wagner | gates passando e autorização head/base |
| Merge | Wagner | review atual, gates passando e autorização posterior head/base |
| Builder | Wagner | escopo por GPT |

## Dependências e bloqueios

Mudança de head invalida todos os gates/autorizações. Mudança só da base invalida GPT4 e autorizações de transição. `BLOCK` e `INCONCLUSIVE` impedem Ready/merge.

## Riscos

| Risco | Mitigação |
|---|---|
| Snapshot obsoleto | resolver live |
| Merge ref validado como head | checkout explícito |
| Tabela divergente | comparação determinística |
| Estado terminal sem ação | transições terminal |
| Review material | rechecagem antes do merge |
| GitHub–Builder divergente | verificar individualmente |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

## Fora do escopo

Builder, domínios, DNS, hospedagem, deploy, produção, SEO operacional e avaliação experimental.

## Atualização

Somente por mudança durável de política, estrutura, máquina, risco, bloqueio ou escopo; não por gate, metadata, autorização ou estado terminal.
