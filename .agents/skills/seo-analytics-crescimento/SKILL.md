---
name: seo-analytics-crescimento
description: "Definir mensuração, KPIs, dashboards, experimentos e otimização de crescimento."
---

# GPT8 — SEO - Analytics e crescimento

## Quando usar
Use para tarefas de analytics e crescimento com escopo, objeto e critérios definidos.

## Quando não usar
Não use para tarefas pertencentes a outro especialista, para mutações não autorizadas ou quando o objeto necessário não estiver acessível.

## Pré-condições
- Ler `config/project.yaml`, `config/gpts.yaml` e `docs/gpts/gpt8.md`.
- Fixar referência exata e confirmar acesso.
- Identificar se a execução é READ_ONLY ou autorizada para mutação.

## Procedimento
1. Fixar objetivos, baseline, período e fontes.
2. Definir KPIs, dimensões, eventos e qualidade.
3. Normalizar dados e identificar lacunas.
4. Analisar desempenho e hipóteses.
5. Definir experimento, sucesso e decisão.

## Validações
- Conferir referências cruzadas e cobertura.
- Separar fatos, inferências, estimativas e limitações.
- Não declarar leitura integral diante de truncamento.
- Aplicar os vereditos oficiais quando houver gate.

## Condições de parada
- Head ou objeto divergente.
- Acesso insuficiente a evidência obrigatória.
- Pedido fora do escopo ou mutação sem autorização.

## Saída
Escopo, evidências, análise, achados, limitações, veredito/recomendação e próxima ação segura.

## Handoff
especialista de origem para interpretação e ação corretiva.

## Proibições
Não declarar causalidade sem desenho analítico adequado. Não inventar evidências. Não criar SFJM.

## Referências
`config/project.yaml` · `config/gpts.yaml` · `docs/gpts/gpt8.md` · `config/builder/gpt8.yaml` · `AGENTS.md`
