## Objetivo

## Escopo

## Base, branch e head esperado

## Arquivos e GPTs afetados

## Leitura integral realizada

- [ ] Arquivos relevantes lidos integralmente
- [ ] Referências cruzadas conferidas
- [ ] Evidências associadas ao head exato

## Continuidade SFJM

- [ ] Estado volátil foi resolvido live e não copiado como snapshot documental
- [ ] `Next action ID` e resumo derivado permanecem sincronizados
- [ ] Existe exatamente uma máquina autoritativa em `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml`
- [ ] `docs/BLOCKED_ACTIONS.md` contém apenas bloqueios estruturais afetados
- [ ] Conclusão de gate ou mudança Draft/Ready não gerou reescrita documental intermediária
- [ ] Divergências materiais foram reconciliadas antes do congelamento do head

## Validação

```text
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_builder_action.py
```

## Riscos e rollback

## Autorizações

- [ ] Autorização de Ready, quando aplicável, identifica o head exato
- [ ] Autorização de merge é posterior, separada e identifica o head exato
- [ ] Nenhuma credencial foi versionada
- [ ] A Action READ_ONLY não contém métodos de mutação
