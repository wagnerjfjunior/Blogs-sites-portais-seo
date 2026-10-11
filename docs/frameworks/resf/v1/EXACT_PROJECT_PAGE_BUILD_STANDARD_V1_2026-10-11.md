# RESF — Padrão de construção de páginas de empreendimentos — V1 (candidato)

**Escopo atual:** somente os **dois primeiros itens** do padrão de construção. Não implica padronizar agora UX, conteúdo editorial, tracking, CRM ou desempenho geral.

**Governança:** especificação no provedor `wagnerjfjunior/Blogs-sites-portais-seo`; aplicação e homologação são decisões do consumidor. Estado `CANDIDATE / DRAFT` até revisão, gates e integração da PR do provedor. A adoção de módulos anteriormente diferidos no consumer exige decisão posterior.

| Item | Nome acessível | O que será padronizado | Especificação |
|---|---|---|---|
| **01** | **JSON-LD para o Google** | Informações reais do empreendimento, entidades, propriedades compatíveis, ligações entre elas, testes do Schema.org e Google | [JSON-LD](EXACT_PROJECT_JSONLD_GRAPH_PROFILE_V1_2026-10-11.md) |
| **02** | **Imagens principal e secundária para busca** | Prioridade e coerência entre hero visível, HTML, Open Graph, Twitter e JSON-LD, preservando as duas imagens distintas | [Imagens para busca](EXACT_PROJECT_SERP_IMAGE_OWNERSHIP_V1_2026-10-11.md) |

## Método para cada nova página

1. **Levantar fatos e ativos reais**. Perguntar o que falta: nome/endereço/CEP, marca/organização/agente, unidade e preço de referência *somente se existirem*, fotos oficiais, plantas e FAQ realmente visível. Determinar explicitamente qual mídia é a principal e qual a secundária.
2. **Construir cada item aplicável**. Não copiar fatos de Bem Moema ou Ampère para outros empreendimentos.
3. **Verificar no código e CI**: JSON-LD consistente; mesma imagem principal no hero, OG, Twitter e esquema; imagem secundária diferente; nenhuma regressão no restante da página.
4. **Publicar pelo processo do consumidor**: branch, testes, revisão/autorização, `main` canônica, deployment por SHA e rollback.
5. **Homologar em ferramentas reais**: Schema.org Validator (meta 0 erro / 0 aviso); Google Rich Results (contagem e campos expandidos); presença de imagens nos sinais HTML/JSON-LD. Registrar captura, URL, SHA, data e ressalvas. A miniatura efetiva da SERP não é garantida por metadados.

## Evidência de referência — 11/10/2026

| Página | Antes no Google | Depois no Google | Schema.org após | JSON-LD após |
|---|---|---|---|---|
| Bem Moema | inicialmente 0, depois 3 | **6 itens válidos** | **0 erros / 0 avisos / 5 itens** | **18 nós** |
| Ampère Brooklin | **1 item válido** (breadcrumb) | **6 itens válidos** | **0 erros / 0 avisos / 5 itens** | **18 nós** |

Fonte da medição: **capturas fornecidas pela Product Authority** após publicação em produção. Ampère: consumer PR #386, `wagnerjfjunior/MoreNumTegra@09efee712a625075ff1b2e1d1dc9fa84ece90e24`, deployment Vercel `dpl_2XNToN3fPizGANgu9Qa2Tf2thBU4` READY; resultado confirmado em comentário de PR #386. Bem Moema: PRs #379, #381, #382, #384, #385, `MoreNumTegra@7e5e2297c21eb6a01cad52c829a0533f5c1b7214`.

**Interpretação:** Google mostra seis *itens elegíveis*, não seis tipos Schema.org; a interface Schema.org mostra cinco *itens de topo*, e o grafo tem dezoito *nós*. Repetir seis não é meta absoluta quando faltarem entidades comprovadas. O ganho de detecção não comprova ganho de posição, CTR ou controle de miniatura na SERP.

## Limites deste primeiro ciclo

- Não criar preço, disponibilidade, reviews, rating, plantas, endereço, agentes ou imagens para completar contagens.
- Não aplicar automaticamente aos demais empreendimentos: fazer intake, diagnosticar e criar PR por escopo autorizado.
- **Item 01 e Item 02 são distintos**: JSON-LD organiza entidades; imagens para busca coordenam sinais em HTML/metadata e JSON-LD. Ambos devem concordar na imagem principal.
- O provedor não altera a produção do consumidor. A homologação da imagem na SERP real permanece evidência separada.
- Próximos itens do padrão geral podem ser adicionados posteriormente com aprovação de escopo.
