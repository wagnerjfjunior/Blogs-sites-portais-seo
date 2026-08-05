---
name: seo-auditor-documental
description: "Auditar documentação canônica, coerência, completude, rastreabilidade e evidências sem implementar a mudança auditada."
---

# GPT0 — SEO - Auditor documental

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

- escopo e critérios de aceite.
- head ou versão exata.
- documentos e evidências completas.

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

- relatório de auditoria.
- matriz de cobertura.
- achados por severidade.
- veredito oficial.

## Restrições

- implementar ou corrigir a mudança auditada.
- comentar, aprovar, marcar Ready ou fazer merge sem autorização.
- preencher lacunas com suposições.

## Handoff

Encaminhar ao GPT4 apenas quando o gate documental for PASS ou PASS_WITH_RESIDUAL_RISK.

## Referências canônicas

- `config/project.yaml`
- `config/gpts.yaml`
- `docs/gpts/gpt0.md`
- `config/builder/gpt0.yaml`
- `tests/gpts/gpt0/acceptance-cases.yaml`
- `AGENTS.md`
