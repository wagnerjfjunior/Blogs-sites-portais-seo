# Bootstrap Canônico — Ecossistema de Blogs, Sites, Portais e SEO

## Identificação

- Projeto: Ecossistema de Blogs, Sites, Portais e SEO
- ID: `blogs-sites-portais-seo`
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Branch canônica: `main`
- Revisão: resolver o SHA live antes de agir
- Baseline de adoção: `main@65dc3a7e60a3a8a1bddefc912380f5ce24c11857`
- Autoridade: Wagner

## Regra de canonicalidade

A branch `main` aprovada é a fonte de verdade. Conversas, memória, Builder, arquivos locais e resumos são derivados.

Em caso de divergência:

1. prevalece `main` na revisão live observada;
2. `docs/NEXT_SAFE_ACTION.md` identifica a próxima ação pretendida;
3. divergência material exige parada e reconciliação;
4. informação ausente não pode ser inferida.

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
5. O SFJM local trata continuidade operacional; não inclui scoring, benchmark ou adjudicação experimental.
6. O YAML não prova, isoladamente, o estado efetivo do Builder.

## Lacunas

- O estado efetivo de cada GPT no Builder exige verificação externa específica.
- Ativos, domínios, métricas, tráfego, receita e produção exigem registros canônicos antes de serem tratados como fatos.

## Autorizações

Leitura, síntese, auditoria GPT0 e validação GPT4 em modo `READ_ONLY` são permitidas dentro do escopo.

Alteração canônica, Ready, merge, Builder, deploy, publicação, domínio, DNS, hospedagem, campanha, compromisso financeiro e expansão material exigem autorização explícita.

Preparar não autoriza executar. Uma etapa concluída não autoriza a seguinte.

## Próxima ação segura

- Registro autoritativo: `docs/NEXT_SAFE_ACTION.md`
- Resumo derivado: executar o gate documental GPT0 da PR de adoção do SFJM no head exato e sem mutações.

## Ações bloqueadas

Consulte `docs/BLOCKED_ACTIONS.md`. Ausência na lista não constitui autorização.

## Retomada

Antes de agir:

1. resolva os SHAs live aplicáveis;
2. leia a ordem mínima;
3. apresente até oito fatos confirmados;
4. separe fatos, decisões, propostas, hipóteses e lacunas;
5. confirme a próxima ação segura e os bloqueios;
6. pare diante de drift, divergência, evidência insuficiente ou falta de autoridade.

## Atualização

Atualize este arquivo quando mudar a fonte, a ordem de leitura, a autorização, a próxima ação resumida ou um bloqueio material. Use o histórico Git para auditoria e mantenha este arquivo curto e atual.
