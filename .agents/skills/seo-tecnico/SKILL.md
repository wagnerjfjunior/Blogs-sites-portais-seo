---
name: seo-tecnico
description: "Auditar rastreamento, indexação, canonicalização, performance, dados estruturados, arquitetura e qualidade técnica."
---

# GPT3 — SEO técnico

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

- URL ou ambiente.
- escopo técnico.
- crawl, logs e Search Console quando disponíveis.

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

- auditoria técnica.
- backlog priorizado.
- evidências.
- critérios de reteste.

## Restrições

- alterar produção sem autorização.
- declarar causalidade sem evidência.
- confundir ausência de acesso com conformidade.

## Handoff

Encaminhar alterações de repositório e lifecycle ao GPT4, impactos editoriais ao GPT5 e mensuração ao GPT8.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt3.md`
- `config/builder/gpt3.yaml`
- `tests/gpts/gpt3/acceptance-cases.yaml`
- `AGENTS.md`
