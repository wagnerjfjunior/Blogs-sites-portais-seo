# Ações Bloqueadas — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Regra: ausência nesta lista não constitui autorização.
- Next action ID: `resolve-live-lifecycle-transition-v1`

Este registro contém bloqueios estruturais. Estado de PR, gates, checks, autorizações e verificações deve ser resolvido live.

## 1. Bloqueios ativos

| Ação bloqueada | Motivo | Condição de liberação | Autoridade | Evidência |
|---|---|---|---|---|
| Ready com gate `BLOCK` ou `INCONCLUSIVE` | somente vereditos de passagem permitem avanço | GPT0 e GPT4 atuais com `PASS` ou `PASS_WITH_RESIDUAL_RISK` | Wagner | gates do head/base aplicáveis |
| Ready sem autorização válida | Ready é mutação independente | autorização para head e base exatos | Wagner | autorização live |
| Merge com autorização antecipada ou conjunta ao Ready | merge precisa de decisão posterior | nova autorização após Ready para head/base atuais | Wagner | ordem temporal verificável |
| Merge sem autorização posterior | Ready não implica merge | autorização pós-Ready, gates passando e review atual | Wagner | autorização e estado GitHub |
| Corrigir arquivos sem escopo | review não autoriza implementação | autorização corretiva delimitada | Wagner | escopo e diff |
| Configurar Builder | estado externo exige escopo próprio | autorização por GPT | Wagner | configuração e privacidade |
| Criar Action mutável | perfil é READ_ONLY | PR separada e revisão específica | Wagner | schema e riscos |
| Alterar domínio, DNS ou hospedagem | ativos não registrados | inventário, rollback e autorização | Wagner | evidência técnica |
| Deploy, publicação ou produção | ambiente não aprovado | gates técnicos e autorização | Wagner | checks e rollback |
| Campanha ou contato externo | compromisso com terceiros | escopo e autorização | Wagner | aprovação |
| Scoring ou cenário experimental | fora do bootstrap | protocolo separado | Wagner | controles próprios |

## 2. Ações que sempre exigem autorização explícita

Correção, Ready, merge, Builder, deploy, release, publicação, comunicação externa, compromisso financeiro, ação destrutiva, dados sensíveis e expansão material.

## 3. Limites

Preparar não autoriza executar. Review não autoriza corrigir. Workflow verde não prova Builder ou produção. Autorização vale apenas para transição, head, base e ordem temporal declarados. Ready não autoriza merge.

## 4. Evidência ausente

Builder, inventário de ativos, ambientes, rollback e métricas permanecem bloqueados até fonte datada e identificada.

## 5. Autorizações live

Autorizações são evidência externa vinculada ao head e à base. A autorização de merge precisa ser posterior ao Ready. Nenhuma autorização se torna snapshot neste arquivo.

## 6. Procedimento para desbloqueio

1. Resolver condição, head, base, gates, Ready e autorização live.
2. Ausência de autorização: solicitar somente o escopo mínimo.
3. Autorização de merge anterior ou conjunta ao Ready: considerar inelegível e solicitar nova autorização posterior.
4. Autorização válida e gates passando: executar somente a transição autorizada.
5. `BLOCK`, `INCONCLUSIVE` ou drift: parar.
6. Não atualizar os registros versionados apenas por conclusão de gate, metadata, autorização ou estado terminal.
7. Atualizar somente política, bloqueio, autoridade ou evidência durável.
8. Não iniciar automaticamente etapa posterior.

## 7. Dúvida

Tratar como bloqueado, declarar a lacuna e solicitar a menor decisão necessária.
