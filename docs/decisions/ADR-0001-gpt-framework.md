# ADR-0001 — Framework canônico dos GPTs

- **Status:** Proposto
- **Data:** 2026-08-04

## Contexto

O projeto possui nove GPTs privados. A configuração precisa ser rastreável no GitHub e aplicável manualmente no Builder sem criar uma segunda fonte de regras.

## Decisão

Adotar:

- `config/project.yaml` para identidade e políticas;
- `config/gpts.yaml` como registro dos nove GPTs;
- um contrato e uma skill por GPT;
- uma projeção de Instructions e um manifesto de Builder por GPT;
- testes de aceitação por GPT;
- uma Action OpenAPI GitHub estritamente somente leitura;
- governança explícita de autorização, lifecycle, ferramentas e provisioning;
- validação determinística em Pull Requests.

## Consequências

- O GitHub permanece a fonte canônica.
- O Builder é uma implantação derivada e deve registrar o commit-fonte.
- Alteração de head invalida gates anteriores.
- Ready e merge são decisões separadas.
- A Action inicial não executa mutações.
