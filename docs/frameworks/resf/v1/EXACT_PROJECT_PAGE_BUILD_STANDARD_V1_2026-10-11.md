# RESF — Padrão Único RESF de construção de páginas de empreendimentos — V1 (candidato)

**Escopo atual:** somente os **quatro primeiros requisitos** do padrão de construção. O conteúdo editorial neste ciclo limita-se ao FAQ estratégico do requisito 03; UX/CSS limita-se à captação e rodapé do requisito 04. Não implica padronizar agora todo o SEO editorial, tracking, CRM ou desempenho geral.

**Governança:** especificação no provedor `wagnerjfjunior/Blogs-sites-portais-seo`; aplicação e homologação são decisões do consumidor. Estado `CANDIDATE / DRAFT` até revisão, gates e integração da PR do provedor. A adoção de módulos anteriormente diferidos no consumer exige decisão posterior.

| Requisito | Nome acessível | O que será padronizado | Especificação |
|---|---|---|---|
| **01** | **JSON-LD para o Google** | Informações reais do empreendimento, entidades, propriedades compatíveis, ligações entre elas, testes do Schema.org e Google | [JSON-LD](EXACT_PROJECT_JSONLD_GRAPH_PROFILE_V1_2026-10-11.md) |
| **02** | **Imagens principal e secundária para busca** | Prioridade e coerência entre hero visível, HTML, Open Graph, Twitter e JSON-LD, preservando as duas imagens distintas | [Imagens para busca](EXACT_PROJECT_SERP_IMAGE_OWNERSHIP_V1_2026-10-11.md) |
| **03** | **FAQ estratégico de SEO** | Seleção de dúvidas reais de busca e compra, respostas factuais publicadas no HTML, paridade literal de `FAQPage` e revisão de relevância/qualidade | [FAQ orientado à intenção de busca](EXACT_PROJECT_SEO_FAQ_INTENT_V1_2026-10-11.md) |
| **04** | **Formulário e rodapé — UX/CSS** | Referência Ária para apresentação responsiva do Form 46 e footer, preservando atributos, comportamento, identidade e informações do próprio empreendimento | [Formulário e rodapé](EXACT_PROJECT_FORM_FOOTER_UX_V1_2026-10-11.md) |

## Distinção obrigatória — coleta de fatos vs. FAQ de SEO

**Não confundir os dois tipos de perguntas:**

- **Coleta interna de fatos:** perguntas que a equipe faz para obter dados autorizados e montar corretamente o JSON-LD. A ferramenta é `templates/EXACT_PROJECT_JSONLD_INTAKE.template.yaml`. **Não é um FAQ público, nem é um recurso de SEO por si só.**
- **FAQ de SEO da página:** perguntas formuladas para responder necessidades e intenções reais de pesquisa sobre o empreendimento. Integram conteúdo público indexável, precisam ter respostas úteis, específicas e comprovadas, e só então podem aparecer no `FAQPage` com correspondência exata ao conteúdo visível.

**Referência observada:** Ária Higienópolis possui **12 perguntas e respostas estruturadas** no `FAQPage` (`MoreNumTegra` main em 11/10/2026), cobrindo estágio/entrega, metragens e tipologias, valor de referência, lazer, salas comerciais, localização, disponibilidade, visitas, entrada e financiamento. **Não são perguntas aleatórias para completar uma contagem.** A seleção deve considerar intenção de busca, características verificadas do produto e dúvidas reais de compra.

O **Item 03** documenta a **seleção e qualidade editorial das perguntas de SEO**. O Item 01 permanece responsável pela **paridade FAQ visível ↔ `FAQPage`**. Nenhum dos dois garante rich result de FAQ no Google.

## Método para cada nova página

1. **Levantar fatos, ativos e intenções de busca reais**. Perguntar o que falta: nome/endereço/CEP, marca/organização/agente, unidade e preço de referência *somente se existirem*, fotos oficiais, plantas e FAQ de SEO fundamentado realmente visível. Determinar explicitamente qual mídia é a principal e qual a secundária.
2. **Construir cada requisito aplicável do padrão único**. Não copiar fatos de Bem Moema ou Ampère para outros empreendimentos.
3. **Verificar no código e CI**: JSON-LD consistente; mesma imagem principal no hero, OG, Twitter e esquema; imagem secundária diferente; nenhuma regressão no restante da página.
4. **Publicar pelo processo do consumidor**: branch, testes, revisão/autorização, `main` canônica, deployment por SHA e rollback.
5. **Homologar em ferramentas reais**: revisão editorial das perguntas e respostas, paridade literal HTML/FAQPage, Schema.org Validator (meta 0 erro / 0 aviso); Google Rich Results (contagem e campos expandidos); presença de imagens nos sinais HTML/JSON-LD. Registrar captura, URL, SHA, data e ressalvas. A miniatura efetiva da SERP não é garantida por metadados.

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
- **Requisitos 01, 02, 03 e 04 compõem o mesmo padrão único**: JSON-LD organiza entidades; imagens para busca coordenam sinais em HTML/metadata e JSON-LD; FAQ SEO seleciona perguntas relevantes e respostas reais. O requisito 01 representa o FAQ visível em `FAQPage` quando aplicável. O requisito 04 cuida somente do UX/CSS do formulário e do rodapé, sem mudar captação ou dados comerciais.
- O provedor não altera a produção do consumidor. A homologação da imagem na SERP real permanece evidência separada.
- **Ampère FAQ 6 → 12** é evidência da PR #387 em Draft no consumidor; não afirmar que esteja em produção ou validado no Google antes de merge e novos testes.
- Próximos itens do padrão geral podem ser adicionados posteriormente com aprovação de escopo.
