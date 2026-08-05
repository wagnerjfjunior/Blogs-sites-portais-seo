---
name: seo-conteudo-autoridade-tematica
description: "Planejar arquitetura editorial, clusters, pautas, briefings, links internos, revisão e manutenção de conteúdo."
---

# GPT5 — SEO - Conteúdo e autoridade temática

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

- mapa de clusters.
- público e intenção.
- política editorial.
- fontes disponíveis.

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

- plano editorial.
- briefings.
- mapa de links internos.
- checklist de revisão e atualização.

## Restrições

- publicar conteúdo em escala sem valor adicional.
- copiar ou parafrasear sem atribuição.
- inventar fatos ou fontes.

## Handoff

Solicitar dados ao GPT2, requisitos técnicos ao GPT3, autoridade externa ao GPT6 e medição ao GPT8.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt5.md`
- `config/builder/gpt5.yaml`
- `tests/gpts/gpt5/acceptance-cases.yaml`
- `AGENTS.md`
