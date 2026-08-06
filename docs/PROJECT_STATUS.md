# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Política de estado: resolver lifecycle live; não manter snapshot volátil neste arquivo
- Adoção SFJM: rastreada pela PR #2
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Resultado pretendido

Operar um ecossistema de ativos digitais com nove GPTs especializados, governança versionada e continuidade entre conversas baseada em estado verificável, bloqueios explícitos e uma máquina segura de transição.

## Estado por frente

| Frente | Estado durável | Evidência | Próximo marco calculado live | Bloqueio estrutural |
|---|---|---|---|---|
| Framework GPT0–GPT8 | concluído | PR #1 e `main` | manter sincronismo | Builder não revalidado |
| Action GitHub READ_ONLY | concluída | `config/actions/github-read-only.openapi.yaml` | preservar perfil | mutações desabilitadas |
| Governança de lifecycle | definida | `docs/governance/` | aplicar máquina live | autorizações não se propagam |
| Adoção SFJM | em lifecycle pela PR #2 | PR e branch | resolver primeira transição | merge ainda exige autorização própria |
| Inventário de ativos | não iniciado | registro ausente | definir modelo e responsáveis | dados ausentes |
| Produção e monetização | bloqueada | restrições vigentes | planejamento e autorizações | ambientes não aprovados |

## Marcos

| Marco | Situação durável | Evidência |
|---|---|---|
| Framework GPT | atingido | PR #1 |
| Kit SFJM inicial | preparado | PR #2 |
| Âncora upstream | versionada | evidência e cópia local |
| Máquina de lifecycle | definida | manifesto e próxima ação |
| Validação adversarial | exigida pela CI | workflow canônico |
| Merge SFJM | estado live | requer gates, reviews e autorização exata |

## Decisões necessárias

| Decisão | Autoridade | Condição live |
|---|---|---|
| Veredito documental | GPT0 | workflow verde e head congelado |
| Elegibilidade de lifecycle | GPT4 | GPT0 elegível no mesmo head |
| Ready | Wagner | gates atuais e autorização vinculada ao head |
| Merge | Wagner | Ready, reviews reconciliadas e autorização posterior |
| Builder | Wagner | escopo e evidência por GPT |

## Dependências e bloqueios

- O SFJM só se torna canônico após merge aprovado.
- Mudança de head invalida workflow decisório e gates anteriores.
- Mudança apenas de metadata da PR não invalida gates do mesmo head.
- Builder, produção e ativos externos permanecem fora desta etapa.
- Domínios, ambientes e métricas não podem ser presumidos.

## Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Snapshot documental obsoleto | média | alto | resolver estado live |
| Reutilizar gate de outro head | média | alto | exigir evidência head-bound |
| Ordem ou ação divergente | baixa | alto | validação determinística |
| Review material após Ready | média | alto | rechecagem antes de merge |
| Divergência GitHub–Builder | média | alto | verificar individualmente |
| Avançar sem autorização | média | alto | primeira transição e autorização específica |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina.

A passagem GPT0 → GPT4 → Ready no mesmo head não altera este status versionado.

## Fora do escopo atual

- Builder e publicação dos GPTs.
- Domínios, DNS, hospedagem, deploy e produção.
- Pesquisa, conteúdo, link building, monetização e analytics.
- Scoring, benchmark, cenários e avaliação experimental do SFJM.

## Critério de atualização

Atualizar quando mudar política, estrutura, decisão durável, risco estrutural, bloqueio material, `Next action ID` ou escopo. Não atualizar por simples conclusão de gate, check ou mudança Draft/Ready no mesmo head.
