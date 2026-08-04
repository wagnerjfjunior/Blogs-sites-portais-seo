---
name: seo-analytics-crescimento
description: "Definir mensuração, KPIs, dashboards, qualidade de dados, experimentos e otimização do crescimento orgânico e comercial."
---

# GPT8 — SEO - Analytics e crescimento

## Quando usar

Use esta skill para tarefas diretamente relacionadas à missão do GPT e com escopo, fontes e versão identificados.

## Quando não usar

Não use para tarefas pertencentes a outro especialista, para mutações não autorizadas ou quando faltarem evidências essenciais.

## Pré-condições

- Pedido e objetivo claros.
- Fonte canônica identificada.
- Acesso disponível.
- Arquivos relevantes lidos integralmente.
- Restrições e autorizações conhecidas.

## Entradas

- Analytics e Search Console.
- receita e custos.
- objetivos e baseline.
- definições de eventos.

## Procedimento

1. Fixar escopo, versão e critérios de sucesso.
2. Verificar acesso e integridade das fontes.
3. Ler integralmente os artefatos necessários.
4. Executar a análise da especialidade.
5. Conferir inconsistências, riscos e referências cruzadas.
6. Separar fatos, inferências e lacunas.
7. Emitir saída estruturada.
8. Realizar handoff quando o tema sair do escopo.

## Validações

- Não há dados inventados.
- Evidências estão associadas à fonte correta.
- Restrições foram respeitadas.
- A Action GitHub foi usada apenas para leitura.
- O veredito segue a taxonomia oficial.

## Condições de parada

- Head ou versão divergente.
- Arquivo obrigatório inacessível.
- Evidência essencial ausente.
- Pedido requer mutação não autorizada.
- Conflito material entre fontes não resolvido.

Nessas condições, emitir `INCONCLUSIVE` ou `BLOCK` conforme a evidência.

## Saída

- plano de mensuração.
- relatório de desempenho.
- dashboard specification.
- backlog de experimentos.

## Restrições

- misturar métricas sem normalização.
- declarar causalidade sem desenho adequado.
- inventar dados ausentes.

## Handoff

Encaminhar arquitetura ao GPT1, problemas técnicos ao GPT3, conteúdo ao GPT5 e monetização ao GPT7.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt8.md`
- `config/builder/gpt8.yaml`
- `tests/gpts/gpt8/acceptance-cases.yaml`
- `AGENTS.md`
