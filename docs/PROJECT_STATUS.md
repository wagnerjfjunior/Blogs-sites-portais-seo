# Status do Projeto — Ecossistema de Blogs, Sites, Portais e SEO

- Data de referência: 2026-08-05
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Baseline: `main@65dc3a7e60a3a8a1bddefc912380f5ce24c11857`
- Fase atual: SFJM operacional em PR #2 Draft
- Saúde geral: amarelo — framework aprovado, SFJM ainda não canônico e produção não iniciada

## Resultado pretendido

Operar um ecossistema de ativos digitais com nove GPTs especializados, governança versionada e continuidade entre conversas baseada em estado verificável, bloqueios explícitos e uma única próxima ação segura.

## Estado por frente

| Frente | Estado | Evidência | Próximo marco | Bloqueio |
|---|---|---|---|---|
| Framework GPT0–GPT8 | concluída | PR #1; `main@65dc3a7e...` | manter sincronismo | Builder não revalidado |
| Action GitHub READ_ONLY | concluída | `config/actions/github-read-only.openapi.yaml` | preservar perfil | mutações desabilitadas |
| Governança de lifecycle | concluída | `docs/governance/` | aplicar à PR #2 | transições não automáticas |
| Continuidade SFJM | PR Draft | PR #2 | gates GPT0 e GPT4 | Ready e merge sem autorização |
| Inventário de ativos | não iniciada | registro ausente | definir modelo e responsáveis | dados ausentes |
| Estratégia SEO | não iniciada | artefato ausente | arquitetura inicial GPT1 | depende do inventário |
| Produção e monetização | bloqueada | restrições vigentes | planejamento e autorizações | ambientes não aprovados |

## Marcos

| Marco | Situação | Evidência |
|---|---|---|
| Framework GPT | atingido | PR #1 mergeada em 2026-08-05 |
| Validação pós-merge | atingido | run #28, `success` |
| Kit SFJM | em PR Draft | PR #2 |
| Gate GPT0 | pendente | exige head final congelado |
| Gate GPT4 | pendente | exige gate GPT0 elegível |
| Merge SFJM | bloqueado | exige autorização separada |

## Decisões necessárias

| Decisão | Autoridade | Condição |
|---|---|---|
| Veredito documental | GPT0 | head exato e arquivos completos |
| Elegibilidade de lifecycle | GPT4 | gate GPT0 elegível e dados live |
| Ready | Wagner | autorização vinculada ao head |
| Merge | Wagner | autorização posterior e separada |
| Builder | Wagner | escopo e evidência por GPT |

## Dependências e bloqueios

- O SFJM só se torna canônico após merge aprovado.
- Mudança de head invalida checks e gates anteriores para decisão final.
- Builder, produção e ativos externos estão fora desta etapa.
- Domínios, ambientes e métricas não podem ser presumidos.

## Riscos

| Risco | Probabilidade | Impacto | Mitigação autorizada |
|---|---|---|---|
| Estado documental obsoleto | média | alto | atualizar registros no mesmo fluxo |
| Divergência GitHub–Builder | média | alto | verificar individualmente |
| Confundir SFJM operacional com experimental | média | médio | manter exclusões no manifesto |
| Avançar sem autorização | média | alto | gates e bloqueios separados |
| Usar check de head anterior | média | alto | validar o run mais recente |

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: executar o gate GPT0 da PR #2 no head exato.

## Fora do escopo atual

- Builder e publicação dos GPTs.
- Domínios, DNS, hospedagem, deploy e produção.
- Pesquisa, conteúdo, link building, monetização e analytics.
- Scoring, benchmark, cenários e adjudicação experimental do SFJM.

## Critério de atualização

Atualizar quando mudar revisão, PR, fase, gate, decisão, bloqueio, risco ou próxima ação. Não registrar intenção como progresso.
