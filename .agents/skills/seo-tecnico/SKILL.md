---
name: seo-tecnico
description: "Auditar rastreamento, indexação, canonicalização, performance, dados estruturados e arquitetura técnica."
---

# GPT3 — SEO técnico

## Quando usar
Use para tarefas de SEO técnico com escopo, objeto e critérios definidos.

## Quando não usar
Não use para tarefas pertencentes a outro especialista, para mutações não autorizadas ou quando o objeto necessário não estiver acessível.

## Pré-condições
- Ler `config/project.yaml`, `config/gpts.yaml` e `docs/gpts/gpt3.md`.
- Fixar referência exata e confirmar acesso.
- Identificar se a execução é READ_ONLY ou autorizada para mutação.

## Procedimento
1. Fixar URLs, ambiente, período e escopo.
2. Avaliar crawling, indexação, canonicals, HTTP e arquitetura.
3. Avaliar performance, mobile, dados estruturados e links internos.
4. Registrar evidências e impacto.
5. Priorizar correções e critérios de reteste.

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
GPT1 para mudança arquitetural; GPT4 para lifecycle; GPT8 para monitoramento.

## Proibições
Não alterar produção sem autorização explícita. Não inventar evidências. Não criar SFJM.

## Referências
`config/project.yaml` · `config/gpts.yaml` · `docs/gpts/gpt3.md` · `config/builder/gpt3.yaml` · `AGENTS.md`
