## Objetivo

## Escopo

## Base, branch e head esperado

## Arquivos e GPTs afetados

## Leitura integral

- [ ] Arquivos relevantes lidos integralmente
- [ ] Referências cruzadas conferidas
- [ ] Evidências associadas às revisões exatas

## Continuidade SFJM

- [ ] Estado volátil foi resolvido live
- [ ] `Next action ID`, resumo, tabela e manifesto estão sincronizados
- [ ] Workflow de PR faz checkout do head exato
- [ ] GPT0 está vinculado ao head; GPT4 ao head e à base
- [ ] `BLOCK` e `INCONCLUSIVE` impedem Ready e merge
- [ ] Estados closed e merged têm transições explícitas
- [ ] Registros não foram reescritos por mero avanço de lifecycle
- [ ] Divergências materiais foram reconciliadas antes do congelamento

## Validação

```text
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_builder_action.py
```

## Riscos e rollback

## Autorizações

- [ ] Ready, quando aplicável, identifica head e base exatos
- [ ] Merge é posterior, separado e identifica head e base exatos
- [ ] Nenhuma credencial foi versionada
- [ ] A Action READ_ONLY não contém mutações
