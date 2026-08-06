# Bootstrap Canônico — Ecossistema de Blogs, Sites, Portais e SEO

## Identificação

- Projeto: Ecossistema de Blogs, Sites, Portais e SEO
- ID: `blogs-sites-portais-seo`
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Revisão: resolver o SHA live antes de agir
- Autoridade: Wagner
- Next action ID: `resolve-live-lifecycle-transition-v1`

## Regra de canonicalidade

A branch `main` aprovada é a fonte de verdade. Conversas, memória, Builder, arquivos locais e resumos são derivados.

Em caso de divergência:

1. prevalece `main` na revisão live observada;
2. `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml` definem a máquina autoritativa;
3. divergência material exige parada e reconciliação;
4. informação ausente não pode ser inferida.

Estado volátil de PR, head, checks, gates, autorizações, reviews e threads deve ser resolvido live, não copiado para este documento como snapshot.

## Ordem mínima de leitura

1. `handoffs/CURRENT.md`
2. `docs/PROJECT_STATUS.md`
3. `docs/NEXT_SAFE_ACTION.md`
4. `docs/BLOCKED_ACTIONS.md`
5. `config/project.yaml`
6. `config/gpts.yaml`

Para trabalho de um GPT específico, leia também seu contrato, skill, Instructions, manifesto e testes aplicáveis.

## Estado confirmado

1. O projeto possui GPT0 a GPT8, totalizando nove GPTs privados.
2. A Action GitHub inicial é `READ_ONLY`.
3. Escrita direta em `main` é proibida pelo contrato.
4. Ready e merge exigem autorizações humanas separadas e vinculadas ao head exato.
5. O SFJM local trata continuidade operacional; não inclui scoring, benchmark ou avaliação experimental.
6. O YAML não prova, isoladamente, o estado efetivo do Builder.
7. A adoção do SFJM é rastreada pela PR #2; seu estado deve ser resolvido live.

## Lacunas

- O estado efetivo de cada GPT no Builder exige verificação externa específica.
- Ativos, domínios, métricas, tráfego, receita e produção exigem registros canônicos antes de serem tratados como fatos.
- Estado atual de lifecycle nunca deve ser inferido deste arquivo.

## Autorizações

Leitura, síntese, auditoria GPT0 e validação GPT4 em modo `READ_ONLY` são permitidas quando forem a primeira transição aplicável.

Alteração canônica, Ready, merge, Builder, deploy, publicação, domínio, DNS, hospedagem, campanha, compromisso financeiro e expansão material exigem autorização explícita.

Preparar não autoriza executar. Uma etapa concluída não autoriza a seguinte.

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: resolver o estado live e executar somente a primeira transição aplicável da máquina de lifecycle.

A progressão GPT0 → GPT4 → Ready no mesmo head não exige atualização deste arquivo.

## Ações bloqueadas

Consulte `docs/BLOCKED_ACTIONS.md`. Ausência na lista não constitui autorização.

## Retomada

Antes de agir:

1. resolva os SHAs e o estado live aplicáveis;
2. leia a ordem mínima;
3. apresente até oito fatos confirmados;
4. separe fatos, decisões, propostas, hipóteses e lacunas;
5. confirme o `Next action ID`, a primeira transição e os bloqueios;
6. pare diante de drift, finding material, evidência insuficiente ou falta de autoridade.

## Atualização

Atualize este arquivo apenas quando mudar fonte, política, ordem de leitura, `Next action ID`, autorização estrutural ou bloqueio material. Não atualizar por simples avanço de gate, autorização ou metadata da PR.
