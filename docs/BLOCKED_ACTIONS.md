# Ações Bloqueadas — Ecossistema de Blogs, Sites, Portais e SEO

- Atualizado em: 2026-08-05
- Fonte canônica: `wagnerjfjunior/Blogs-sites-portais-seo`
- Baseline: `main@65dc3a7e60a3a8a1bddefc912380f5ce24c11857`
- Regra: ausência nesta lista não constitui autorização.

## 1. Bloqueios ativos

| Ação bloqueada | Motivo | Condição de liberação | Autoridade | Evidência exigida |
|---|---|---|---|---|
| Marcar a PR SFJM como Ready | gates ainda não concluídos | GPT0 e GPT4 elegíveis no head exato | Wagner | autorização explícita vinculada ao head |
| Fazer merge da PR SFJM | Ready não implica merge | PR elegível e autorização separada | Wagner | autorização de merge vinculada ao head |
| Configurar qualquer GPT no Builder | estado externo não revalidado | escopo por GPT, fonte e evidência do estado atual | Wagner | registro da configuração e privacidade |
| Criar Action GitHub mutável | perfil atual é READ_ONLY | PR separada e revisão específica | Wagner | schema, riscos e autorização |
| Alterar domínio, DNS ou hospedagem | ativos e ambientes não registrados | inventário, plano, rollback e autorização | Wagner | registro canônico e evidência técnica |
| Publicar, fazer deploy ou iniciar produção | arquitetura e ambiente não aprovados | gates técnicos e autorização | Wagner | checks, plano e rollback |
| Executar campanha ou contato externo | compromisso com terceiros | escopo, público, conteúdo e autorização | Wagner | aprovação registrada |
| Executar scoring ou cenário experimental SFJM | fora do bootstrap operacional | protocolo experimental separado | Wagner | escopo e controles próprios |

## 2. Ações que sempre exigem autorização explícita

- modificar ou substituir a fonte canônica;
- marcar Ready, fazer merge, deploy, release ou publicação;
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
- Uma etapa concluída não autoriza a etapa seguinte.
- Silêncio, expectativa ou sequência lógica não substituem autorização.

## 4. Bloqueios por evidência ausente

| Evidência ausente | Ação afetada | Fonte esperada | Tratamento |
|---|---|---|---|
| estado efetivo dos GPTs no Builder | qualquer update no Builder | inspeção individual do Builder | parar e verificar |
| inventário de domínios e sites | arquitetura e publicação | registro canônico futuro | não presumir |
| ambiente, DNS, hospedagem e rollback | deploy e produção | documentação técnica futura | manter bloqueado |
| métricas de tráfego, SEO e receita | decisões quantitativas | fontes datadas e identificadas | não inventar |

## 5. Exceções autorizadas

Nenhuma exceção ativa.

## 6. Procedimento para desbloqueio

1. Confirmar a condição objetiva.
2. Obter e registrar a autorização quando exigida.
3. Atualizar este documento e `docs/NEXT_SAFE_ACTION.md`.
4. Executar somente o escopo liberado.
5. Preservar evidência e não iniciar automaticamente a etapa seguinte.

## 7. Dúvida

Quando o enquadramento não estiver claro, tratar a ação como bloqueada, declarar a lacuna e solicitar a menor decisão necessária.
