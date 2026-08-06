# Ações Bloqueadas — Ecossistema de Blogs, Sites, Portais e SEO

- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Regra: ausência nesta lista não constitui autorização.
- Next action ID: `resolve-live-lifecycle-transition-v1`

Este registro contém bloqueios estruturais. Estado de PR, gates, checks e autorizações deve ser resolvido live.

## 1. Bloqueios ativos

| Ação bloqueada | Motivo estrutural | Condição de liberação | Autoridade | Evidência exigida |
|---|---|---|---|---|
| Marcar uma PR como Ready sem autorização válida | Ready é mutação independente | autorização explícita para o head exato | Wagner | autorização live vinculada ao head |
| Fazer merge sem autorização posterior e separada | Ready não implica merge | autorização de merge para o head exato, gates atuais e threads materiais resolvidas | Wagner | autorização live e estado GitHub |
| Corrigir arquivos sem escopo material autorizado | review não autoriza implementação | autorização corretiva delimitada | Wagner | escopo autorizado e diff |
| Configurar qualquer GPT no Builder | estado externo exige escopo próprio | autorização por GPT, fonte e evidência atual | Wagner | registro da configuração e privacidade |
| Criar Action GitHub mutável | perfil atual é READ_ONLY | PR separada e revisão específica | Wagner | schema, riscos e autorização |
| Alterar domínio, DNS ou hospedagem | ativos e ambientes não registrados | inventário, plano, rollback e autorização | Wagner | registro canônico e evidência técnica |
| Publicar, fazer deploy ou iniciar produção | arquitetura e ambiente não aprovados | gates técnicos e autorização | Wagner | checks, plano e rollback |
| Executar campanha ou contato externo | compromisso com terceiros | escopo, público, conteúdo e autorização | Wagner | aprovação registrada |
| Executar scoring ou cenário experimental SFJM | fora do bootstrap operacional | protocolo experimental separado | Wagner | escopo e controles próprios |

## 2. Ações que sempre exigem autorização explícita

- modificar ou substituir a fonte canônica;
- corrigir arquivos, marcar Ready, fazer merge, deploy, release ou publicação;
- configurar Builder ou alterar compartilhamento;
- enviar dados ou comunicação a terceiros;
- criar compromisso financeiro;
- executar ação destrutiva, irreversível ou de difícil reversão;
- acessar, transferir ou divulgar dados sensíveis;
- ampliar materialmente o escopo;
- declarar conclusão ou aprovação em nome da Product Authority.

## 3. Limites de interpretação

- Preparar não autoriza executar.
- Revisar não autoriza corrigir, aprovar ou alterar.
- Criar PR não autoriza Ready ou merge.
- Workflow verde não prova Builder, produção ou conformidade ampla.
- Uma autorização vale somente para a transição e o head declarados.
- Autorização de Ready não autoriza merge.
- Silêncio, expectativa ou sequência lógica não substituem autorização.

## 4. Bloqueios por evidência ausente

| Evidência ausente | Ação afetada | Fonte esperada | Tratamento |
|---|---|---|---|
| estado efetivo dos GPTs no Builder | qualquer update no Builder | inspeção individual do Builder | parar e verificar |
| inventário de domínios e sites | arquitetura e publicação | registro canônico futuro | não presumir |
| ambiente, DNS, hospedagem e rollback | deploy e produção | documentação técnica futura | manter bloqueado |
| métricas de tráfego, SEO e receita | decisões quantitativas | fontes datadas e identificadas | não inventar |

## 5. Exceções e autorizações live

Não há exceção estrutural ativa. Autorizações concedidas são evidência externa vinculada ao head e são consumidas pela máquina de transição sem se tornarem snapshot neste arquivo.

## 6. Procedimento para desbloqueio

1. Resolver live a condição objetiva, o head e a autorização aplicável.
2. Quando a autorização estiver ausente, solicitar somente o escopo mínimo necessário.
3. Quando a autorização válida estiver presente, executar somente a transição autorizada.
4. Não atualizar os registros versionados apenas por conclusão de gate, mudança Draft/Ready ou consumo de autorização no mesmo head.
5. Atualizar este documento somente se mudar política, bloqueio estrutural, autoridade ou evidência canônica durável.
6. Preservar evidência externa e não iniciar automaticamente a etapa seguinte.

## 7. Dúvida

Quando o enquadramento não estiver claro, tratar a ação como bloqueada, declarar a lacuna e solicitar a menor decisão necessária.
