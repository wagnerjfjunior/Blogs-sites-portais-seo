# ADR-0001 — Configuração canônica dos GPTs

- **Status:** Proposto
- **Data:** 2026-08-04

## Contexto
O projeto possui nove GPTs privados e necessita de configuração, skills e contratos versionados.

## Decisão
Adotar `config/project.yaml`, `config/gpts.yaml`, uma skill em `.agents/skills/` e um contrato em `docs/gpts/` para cada GPT, além de validação automática em Pull Requests.

O SFJM não faz parte desta decisão.

## Consequências
Escopo, entradas, saídas, restrições e rastreabilidade ficam versionados. IDs e URLs externos dos GPTs permanecem nulos até serem fornecidos.
