# Legacy Builder Migration Plan

## Status

`PLANNED / NO_EXTERNAL_BUILDER_MUTATION_IN_THIS_PR`

## Princípio

Os antigos Custom GPT Builders são artefatos project-local legados. A adoção de archetypes SES compartilhados não prova equivalência comportamental e não autoriza retirement automático.

```text
ADOPTION != BUILDER_RETIREMENT
RENAME != BEHAVIORAL_EQUIVALENCE
BUILDER_CONFIG_DECLARED != BUILDER_LIVE_OBSERVED
HISTORICAL_PASS != CURRENT_SES_CERTIFICATION
```

## Inventário preservado

Esta migração mantém, sem exclusão automática:

- `config/builder/gpt0.yaml` a `config/builder/gpt8.yaml`;
- `docs/gpts/gpt*.md`;
- `docs/gpts/gpt*-builder-instructions.md`;
- `.agents/skills/...` legadas;
- `tests/gpts/...`;
- external GPT IDs e URLs presentes no registry/manifest;
- evidências históricas de Builder.

## Estado por Builder

| Legado | Destino/role | Equivalência atual | Ação nesta PR | Próximo gate Builder |
|---|---|---|---|---|
| `gpt0` | `documentation_audit` | PARTIAL | preservar | comparação project-local + runtime proof antes de retirement |
| `gpt1` | `architecture` + `seo_strategy` | OVERLAPPING | preservar | decompor responsabilidades e provar cobertura |
| `gpt2` | `seo_strategy` + `content_semantic_seo` | OVERLAPPING | preservar | provar que nenhum capability de research é perdido |
| `gpt3` | `technical_seo` | PARTIAL | preservar | equivalência funcional/runtime |
| `gpt4` | SFJM project governance | NO_EQUIVALENT | preservar | definir retirement sem inventar archetype substituto |
| `gpt5` | `content_semantic_seo` | PARTIAL | preservar | equivalência funcional/runtime |
| `gpt6` | futuro Authority & Digital PR SES | NOT_DETERMINED | preservar | aguardar archetype registrado + certificado + adotado |
| `gpt7` | monetization project-local | NO_EQUIVALENT | manter ativo como exceção | criar/adotar archetype SES futuro antes de retirement |
| `gpt8` | `seo_analytics_growth` | PARTIAL | preservar | equivalência funcional/runtime |

## Alterações necessárias no Builder externo — fase posterior

Quando um Builder legado se tornar elegível para migração/retirement, executar separadamente:

1. capturar configuração live completa e fingerprint atual;
2. comparar Instructions/Knowledge/Actions/Capabilities com o replacement SES;
3. classificar equivalência por capability e boundary;
4. executar compatibility tests project-local e runtime L2 quando material;
5. preservar external GPT ID, URL e evidência histórica;
6. remover o Builder legado de novo roteamento antes de retirement;
7. obter autorização explícita de retirement para aquele Builder;
8. somente então arquivar/desabilitar/retirar o Builder conforme capacidade real da plataforma;
9. registrar evidência final e pós-migração.

## O que não fazer

- não renomear Builder legado e tratar como se tivesse sido originalmente SES;
- não copiar Instructions legadas para archetypes universais sem revisão;
- não deletar manifests, skills, testes ou evidências para “limpar” nomenclatura;
- não alterar external IDs/URLs históricos;
- não declarar `READY`, `CERTIFIED` ou equivalência por associação sem teste;
- não migrar `gpt6` para Authority/Digital PR enquanto o target não for archetype registrado/certificado;
- não retirar `gpt7` enquanto não houver replacement canônico para monetização.

## Builder Action

A Action GitHub READ_ONLY project-local permanece evidência/compatibilidade dos Builders legados durante a transição. Ela não se torna a Action universal dos especialistas SES e não autoriza mutação.

O workflow continuará validando `scripts/validate_builder_action.py` enquanto existirem Builders legados addressable.

## Completion

`LEGACY_BUILDER_RETIREMENT_COMPLETE` só pode ser declarado por Builder, nunca em lote, depois de equivalência, testes, autorização e preservação de evidência.
