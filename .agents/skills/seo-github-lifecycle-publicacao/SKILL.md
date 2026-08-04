---
name: seo-github-lifecycle-publicacao
description: "Governar branches, commits, Pull Requests, checks, reviews, releases e elegibilidade de publicação."
---

# GPT4 — SEO - GitHub, lifecycle e publicação

## Quando usar
Use para tarefas de GitHub e lifecycle com escopo, objeto e critérios definidos.

## Quando não usar
Não use para tarefas pertencentes a outro especialista, para mutações não autorizadas ou quando o objeto necessário não estiver acessível.

## Pré-condições
- Ler `config/project.yaml`, `config/gpts.yaml` e `docs/gpts/gpt4.md`.
- Fixar referência exata e confirmar acesso.
- Identificar se a execução é READ_ONLY ou autorizada para mutação.

## Procedimento
1. Confirmar autorização e estado live do repositório.
2. Fixar base, head, commits, arquivos e drift.
3. Validar checks, workflow, reviews, threads e proteção.
4. Determinar elegibilidade sem executar mutação não autorizada.
5. Registrar estado e próxima ação.

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
GPT0 para auditoria documental; responsável humano para Ready e merge.

## Proibições
Não marcar ready, fazer merge ou publicar sem autorização específica. Não inventar evidências. Não criar SFJM.

## Referências
`config/project.yaml` · `config/gpts.yaml` · `docs/gpts/gpt4.md` · `config/builder/gpt4.yaml` · `AGENTS.md`
