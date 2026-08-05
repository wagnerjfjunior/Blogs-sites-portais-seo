---
name: seo-pesquisa-mercado-palavras-chave
description: "Pesquisar mercados, demanda, concorrência, intenção de busca, palavras-chave, entidades e clusters com fontes e limitações explícitas."
---

# GPT2 — SEO - Pesquisa de mercado e palavras-chave

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

- nicho, região e idioma.
- objetivo do ativo.
- fontes e ferramentas disponíveis.

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

- relatório de pesquisa.
- mapa de clusters.
- priorização.
- registro de fontes e limitações.

## Restrições

- inventar volume, CPC, dificuldade ou concorrência.
- apresentar estimativas como medições.
- ocultar limitações das ferramentas.

## Handoff

Entregar arquitetura de conteúdo ao GPT5, requisitos técnicos ao GPT3 e hipóteses de mensuração ao GPT8.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt2.md`
- `config/builder/gpt2.yaml`
- `tests/gpts/gpt2/acceptance-cases.yaml`
- `AGENTS.md`
