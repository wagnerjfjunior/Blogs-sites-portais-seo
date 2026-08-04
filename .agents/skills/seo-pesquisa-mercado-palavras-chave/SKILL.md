---
name: seo-pesquisa-mercado-palavras-chave
description: "Pesquisar mercado, demanda, concorrência, intenção, palavras-chave, entidades e clusters."
---

# GPT2 — SEO - Pesquisa de mercado e palavras-chave

## Quando usar
Use para tarefas de pesquisa de mercado e palavras-chave com escopo, objeto e critérios definidos.

## Quando não usar
Não use para tarefas pertencentes a outro especialista, para mutações não autorizadas ou quando o objeto necessário não estiver acessível.

## Pré-condições
- Ler `config/project.yaml`, `config/gpts.yaml` e `docs/gpts/gpt2.md`.
- Fixar referência exata e confirmar acesso.
- Identificar se a execução é READ_ONLY ou autorizada para mutação.

## Procedimento
1. Definir nicho, região, idioma, período e objetivo.
2. Registrar fontes, ferramentas e data da coleta.
3. Mapear intenção, entidades, concorrentes e consultas.
4. Construir clusters e priorização com critérios.
5. Separar medidas, estimativas e hipóteses.

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
GPT1 para decisão arquitetural; GPT5 para execução editorial; GPT8 para mensuração.

## Proibições
Não inventar métricas nem tratar estimativas como medições. Não inventar evidências. Não criar SFJM.

## Referências
`config/project.yaml` · `config/gpts.yaml` · `docs/gpts/gpt2.md` · `config/builder/gpt2.yaml` · `AGENTS.md`
