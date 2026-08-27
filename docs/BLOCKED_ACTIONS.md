# Ações Bloqueadas — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Regra: ausência nesta lista não constitui autorização.
- Next action ID: `resolve-live-lifecycle-transition-v1`

Este registro contém bloqueios estruturais. Estado de PR, gates, checks, autorizações e verificações deve ser resolvido live.

## 1. Bloqueios ativos

| Ação bloqueada | Motivo | Condição de liberação | Autoridade | Evidência |
|---|---|---|---|---|
| Ready com gate `BLOCK` ou `INCONCLUSIVE` | somente vereditos de passagem permitem avanço | documentation audit e lifecycle governance atuais com `PASS` ou `PASS_WITH_RESIDUAL_RISK` | Wagner | gates do head/base aplicáveis |
| Ready sem autorização válida | Ready é mutação independente | autorização para head e base exatos | Wagner | autorização live |
| Merge com autorização antecipada ou conjunta ao Ready | merge precisa de decisão posterior | nova autorização após Ready para head/base atuais | Wagner | ordem temporal verificável |
| Merge sem autorização posterior | Ready não implica merge | autorização pós-Ready, gates passando e review atual | Wagner | autorização e estado GitHub |
| Corrigir arquivos sem escopo | review não autoriza implementação | autorização corretiva delimitada | Wagner | escopo e diff |
| Tratar `config/gpts.yaml` como novo routing authority | registry é legado após migração | usar `config/specialists.yaml` + SES Adapter | Wagner | config/adapter vigentes |
| Fazer fuzzy mapping de label legado para archetype | SES exige resolução exata | role/archetype explícitos | SES/project governance | registry + adapter |
| Configurar ou renomear Builder legado como SES sem prova | rename não prova equivalência | fingerprint + compatibility/runtime proof + autorização | Wagner | evidência por Builder |
| Aposentar Builder legado em lote | retirement é individual | replacement elegível, equivalência, testes e autorização por Builder | Wagner | migration evidence |
| Tratar Local SEO ou Authority/Digital PR TARGET como active/certified | lifecycle SES pendente | registry/certification SES atuais + adoption explícita | SES + Wagner | ledger/adapter |
| Retirar monetização project-local sem replacement | não há archetype SES canônico atual | replacement canônico + adoption + equivalência | Wagner | SES + testes |
| Criar Action mutável | perfil project-local é READ_ONLY | PR separada e revisão específica | Wagner | schema e riscos |
| Alterar domínio, DNS ou hospedagem | ativos não registrados | inventário, rollback e autorização | Wagner | evidência técnica |
| Deploy, publicação ou produção | ambiente não aprovado | gates técnicos e autorização | Wagner | checks e rollback |
| Campanha ou contato externo | compromisso com terceiros | escopo e autorização | Wagner | aprovação |
| Scoring ou cenário experimental | fora do bootstrap | protocolo separado | Wagner | controles próprios |

## 2. Ações que sempre exigem autorização explícita

Correção, Ready, merge, Builder externo, Builder retirement, deploy, release, publicação, comunicação externa, compromisso financeiro, ação destrutiva, dados sensíveis e expansão material.

## 3. Limites

Preparar não autoriza executar. Review não autoriza corrigir. Workflow verde não prova Builder ou produção. `CERTIFIED_FOR_ANY_PROJECT` não implica adoção. `ADOPTED` não implica contexto pronto. Contexto pronto não autoriza mutação. Ready não autoriza merge.

## 4. Evidência ausente

Builder live, equivalência/retirement dos Builders legados, inventário de ativos, ambientes, rollback e métricas permanecem bloqueados até fonte datada e identificada.

## 5. Autorizações live

Autorizações são evidência externa vinculada ao head e à base. A autorização de merge precisa ser posterior ao Ready. Nenhuma autorização se torna snapshot neste arquivo.

## 6. Procedimento para desbloqueio

1. Resolver condição, head, base, gates, Ready e autorização live.
2. Resolver role/archetype via SES/Adapter quando a decisão envolver especialista.
3. Ausência de autorização: solicitar somente o escopo mínimo.
4. Autorização de merge anterior ou conjunta ao Ready: considerar inelegível e solicitar nova autorização posterior.
5. Autorização válida e gates passando: executar somente a transição autorizada.
6. `BLOCK`, `INCONCLUSIVE` ou drift: parar.
7. Não atualizar os registros versionados apenas por conclusão de gate, metadata, autorização ou estado terminal.
8. Atualizar somente política, bloqueio, autoridade, specialist adoption ou evidência durável.
9. Não iniciar automaticamente etapa posterior.

## 7. Dúvida

Tratar como bloqueado, declarar a lacuna e solicitar a menor decisão necessária.
