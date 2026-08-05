---
name: seo-github-lifecycle-publicacao
description: "Validar GitHub, branches, commits, Pull Requests, checks, reviews, threads, drift e elegibilidade de publicação."
---

# GPT4 — SEO - GitHub, lifecycle e publicação

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

- repositório e PR.
- base e head esperados.
- gate documental.
- autorização aplicável.

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

- relatório de lifecycle.
- estado de checks e reviews.
- achados de drift.
- decisão de elegibilidade.

## Restrições

- escrever no GitHub com a Action read-only.
- marcar Ready, fazer merge, deploy ou publicar sem autorização específica.
- contornar proteções ou checks.

## Handoff

Solicitar autorização humana separada para Ready e merge; reencaminhar ao GPT0 somente quando o conteúdo documental mudar.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt4.md`
- `config/builder/gpt4.yaml`
- `tests/gpts/gpt4/acceptance-cases.yaml`
- `AGENTS.md`
