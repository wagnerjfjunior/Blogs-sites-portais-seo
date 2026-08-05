## Objetivo

## Escopo

## Base, branch e head esperado

## Arquivos e GPTs afetados

## Leitura integral realizada

- [ ] Arquivos relevantes lidos integralmente
- [ ] Referências cruzadas conferidas
- [ ] Evidências associadas ao head exato

## Continuidade SFJM

- [ ] `handoffs/CURRENT.md` permanece atual
- [ ] `docs/PROJECT_STATUS.md` reflete o estado verificável
- [ ] Existe exatamente uma próxima ação autoritativa em `docs/NEXT_SAFE_ACTION.md`
- [ ] Resumos derivados estão sincronizados com a próxima ação
- [ ] `docs/BLOCKED_ACTIONS.md` cobre bloqueios e autorizações afetados
- [ ] Divergências materiais foram reconciliadas

## Validação

```text
python scripts/validate_repository.py
python scripts/validate_builder_action.py
```

## Riscos e rollback

## Autorizações

- [ ] Ready possui autorização humana específica
- [ ] Merge possui autorização humana separada
- [ ] Nenhuma credencial foi versionada
- [ ] A Action READ_ONLY não contém métodos de mutação
