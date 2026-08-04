---
name: seo-monetizacao
description: "Estruturar publicidade, publieditoriais, patrocínios, afiliados, leads, diretórios premium, newsletters e precificação."
---

# GPT7 — SEO - Monetização

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

- audiência e inventário.
- métricas disponíveis.
- custos e objetivos.
- restrições jurídicas e editoriais.

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

- modelo de monetização.
- catálogo comercial.
- precificação.
- critérios de aprovação e mensuração.

## Restrições

- prometer métricas sem evidência.
- ocultar natureza patrocinada.
- misturar decisão editorial com pagamento sem transparência.

## Handoff

Encaminhar conteúdo patrocinado ao GPT5, links e PR ao GPT6, dados ao GPT8 e lifecycle ao GPT4.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt7.md`
- `config/builder/gpt7.yaml`
- `tests/gpts/gpt7/acceptance-cases.yaml`
- `AGENTS.md`
