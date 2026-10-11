# RESF — Fechamento canônico do padrão único de páginas imobiliárias — 11/10/2026

**Estado do documento:** FINALIZADO e versionado no provedor. **Estado do produto:** o padrão de seis requisitos foi aplicado ao piloto Ampère Brooklin em produção Git/Vercel. **Limite:** documentar um padrão no provedor não promove automaticamente todos os módulos C07/C17 nem autoriza refatoração de outras páginas.

## 1. Governança e identidade

- **Provider (norma e método):** `wagnerjfjunior/Blogs-sites-portais-seo`. A PR #23 foi mergeada na `main` em `f9b6bfb1f92f49aa9e49a47f9b1c7e3157beeccf`.
- **Consumer (produto e release):** `wagnerjfjunior/MoreNumTegra`. `main` e os baselines SFJM são a fonte operacional; Vercel é Preview e, para o site atual, deployment Git-driven publicado no domínio comercial.
- **Página piloto:** `https://www.moretegra.com.br/empreendimentos/ampere-brooklin/`.
- **Padrão único, não seis padrões alternativos:** `v1/EXACT_PROJECT_PAGE_BUILD_STANDARD_V1_2026-10-11.md` é a entrada canônica. Os seis documentos abaixo são requisitos testáveis e complementares.
- **Objetivo de negócio:** descoberta por marca/bairro/tipologia, compreensão do produto, confiança no conteúdo, visita, consulta de condições e lead via Form 46; preservar mobile, performance e SEO.
- **Não inventar:** preço, estoque, metragem, suíte/vagas, endereço, tempo de trajeto, estágio, facilidade de financiamento, fotos ou atributos do projeto.

## 2. Inventário dos seis requisitos

| ID | Requisito | Especificação | Aceite mínimo |
|---|---|---|---|
| 01 | JSON-LD factual para busca | `EXACT_PROJECT_JSONLD_GRAPH_PROFILE_V1_2026-10-11.md` | Propriedades compatíveis, entidades ligadas, preço/planos evidenciados, Schema.org/Rich Results; sem relações inventadas |
| 02 | Imagem principal e secundária para busca | `EXACT_PROJECT_SERP_IMAGE_OWNERSHIP_V1_2026-10-11.md` | Hero, OG/Twitter, ImageObject, WebPage.image e primaryImageOfPage coerentes; duas imagens distintas; nenhuma garantia de miniatura SERP |
| 03 | FAQ útil orientado à intenção de busca | `EXACT_PROJECT_SEO_FAQ_INTENT_V1_2026-10-11.md` | HTML visível + `FAQPage` com perguntas e respostas literais; factual; sem meta de 12 universal |
| 04 | Formulário e footer: UX/CSS | `EXACT_PROJECT_FORM_FOOTER_UX_V1_2026-10-11.md` | Referência visual Ária; Form 46, IDs, inputs, validação, medição, endereços, CRECI e links preservados |
| 05 | Hero e faixa `.facts`: UX/CSS | `EXACT_PROJECT_HERO_FACTS_UX_V1_2026-10-11.md` | Hero sem `hero-meta` redundante, quadros factuais legíveis 2×2 mobile / 4 desktop |
| 06 | SEO editorial, copy, localização e conversão | `EXACT_PROJECT_SEO_COMMERCIAL_COPY_V1_2026-10-11.md` | Autoridade da página, H1 único, H2 por intenção, marca/nome natural, singular/plural contextualizados, copy para comprador, localização com imagens, visita e negociação honestas |

Os seis requisitos **não autorizam** carregamento global de CSS, implementação em massa ou adoção de dados do Ampère por outros projetos.

## 3. Histórico de PRs e release conferido

| Repositório | PR | Desfecho | Evidência |
|---|---|---|---|
| MoreNumTegra | [#387](https://github.com/wagnerjfjunior/MoreNumTegra/pull/387) | CLOSED / NOT MERGED | Versão preliminar FAQ 6→12; substituída pela integração mais atual na #389 |
| MoreNumTegra | [#388](https://github.com/wagnerjfjunior/MoreNumTegra/pull/388) | MERGED | SHA `d53122638a46888a39e17ec340121ef0b8412ac8` |
| MoreNumTegra | [#389](https://github.com/wagnerjfjunior/MoreNumTegra/pull/389) | MERGED | SHA `b6497954e45d77cf37dd639dbea3c18bd29a4040` |
| RESF Provider | [#23](https://github.com/wagnerjfjunior/Blogs-sites-portais-seo/pull/23) | MERGED | SHA `f9b6bfb1f92f49aa9e49a47f9b1c7e3157beeccf` |

**Deployment consumer comprovado via Vercel:** `dpl_6QQCpeSGVrpVJsFkap9o99Zbbw3M`, status `READY`, target `production`, branch `main`, Git SHA `b6497954e45d77cf37dd639dbea3c18bd29a4040`, aliases incluindo `www.moretegra.com.br`. `READY` confirma implantação concluída, **não** valida por si só imagem carregada, fluxo real de Form 46, Core Web Vitals, indexação no Google ou comportamento mobile.

**Verificações de CI:** 9/9 na #388; 10/10 na versão final da #389 antes do merge, contemplando padrão comercial, JSON-LD, mídia, metadados de compartilhamento, favicon, `RealEstateAgent`, cobertura de dados estruturados, contrato de endereço, formulário/footer e copy/FAQ. Provedor PR #23 teve `validate-agent-framework: SUCCESS`. Distinguir essas evidências automatizadas de testes manuais e GSC.

**Validação do usuário:** Schema.org/GSC foram reportados como sem erros para versão verificada pelo usuário. Não alegar que essa checagem foi repetida no novo SHA em produção, nem que Rich Results, snippets, rank ou lead sejam garantidos.

## 4. Fatos de referência do piloto — não replicar em outras páginas

| Campo | Ampère Brooklin |
|---|---|
| Marca/apresentação | Tegra Ampère Brooklin |
| H1 | `Tegra Ampère Brooklin — apartamentos em construção` |
| H2 do hero | `Apartamentos no Brooklin de 262 m² privativos, com 4 suítes, 4 vagas e dois terraços em torre única.` |
| Metragem residencial de referência | 262 m² privativos; unidade 0121 com 262,35 m² |
| Referência de preço | R$ 4.770.000 · unidade 0121 · R$ 18.181/m²; disponibilidade e condições sujeitos à confirmação |
| Estágio | Em construção — **não pronto para morar** |
| Diferencial | Living Double View, com dois terraços por apartamento |
| Plantas apresentadas | Padrão, opção com cozinha aberta e ilha, opção com suíte master ampliada; confirmar configuração de cada unidade |
| Lazer divulgado | Piscinas, gourmet, churrasqueira, salão de festas, fitness, coworking, sauna, playground, brinquedoteca |
| Região | Brooklin, São Paulo; referência à Avenida Berrini sem inventar minutos/deslocamento |
| Link regional complementar | `/regioes/brooklin/` na seção de localização — não no menu superior |
| FAQ | 12 pares visíveis/JSON-LD idênticos, sem estoque ou condições fictícias |
| Leads | Form 46, tenant 313, campos/atributos/scripts existentes preservados |
| Rodapé | Tegra Vendas, Sabrina da Tegra, CRECI-SP 209.905-F e endereço aprovado específico do Ampère |

## 5. Localização com três mídias oficiais (requisito 06)

A seção deve equilibrar argumento comercial, imagens e mapa, com link interno ao bairro contextualizado. **Arquivos usados no consumer:** sob a origem `https://stracctegra.blob.core.windows.net/assets/EmpreendimentoVitrine/351/Imagem/`:

1. `Tegra-Incorporadora-Localizacao-Ponte-Estaiada-Apartamentos-Ampere-Brooklin-Sao-Paulo-SP-1400x1400-1722438997006.jpg`.
2. `Tegra-Incorporadora-Localizacao-Bairro-Brooklin-Apartamentos-Ampere-Brooklin-Sao-Paulo-SP-1400x1400-1722438997006.jpg`.
3. `Tegra-Incorporadora-Localizacao-Bairro-Brooklin-Marginal-Pinheiros-Apartamentos-Ampere-Brooklin-Sao-Paulo-SP-1400x1400-1722438997006.jpg`.

Critérios: `alt` distintos, `width="1400"`/`height="1400"`, `loading="lazy"`, `decoding="async"`, proporção definida, CSS de uma coluna no mobile e três no desktop. Carregar as URLs **diretas** sem depender do proxy `/_next/image` corporativo; imagens fora da dobra não devem competir com LCP. Preservar hero/OG primários e seus sinais SEO. As imagens são do bairro, **não** promessa de vista de nenhuma unidade. Disponibilidade HTTP real e desempenho móvel requerem smoke externo.

## 6. Matriz de construção reaproveitável (SOP)

1. **Governança:** resolver GitHub `main`, bootstrap, CURRENT, PROJECT_STATUS, NEXT_SAFE_ACTION, BLOCKED_ACTIONS e baselines; conferir autorização do Product Authority; registrar SHA/branch.
2. **Intake factual:** levantar ficha aprovada e fontes para nome, localização, estágio, áreas, vagas, suítes, plantas, mídia, ofertas, preço/unidade, lazer, atendimento, links e status de comercialização. Classificar incertezas e não completar por inferência.
3. **Search intent e SEO editorial:** mapear buscas da marca e [tipologia + bairro + característica + etapa de compra]; checar GSC quando disponível; manter um único H1 e H2 por assunto, incluindo marca natural e variações singulares/plurais onde couberem; não inflar contagem de palavras nem produzir keyword stuffing.
4. **Copy imobiliária:** apresentar atributo → benefício real → CTA relevante. Não justificar decisões de SEO ao visitante, escrever em terceira pessoa sobre “a página”, prometer estoque/financiamento ou usar texto jurídico no lugar da copy de vendas.
5. **Hero e facts:** hero com mídia, identidade e CTA; informações de quatro quadros quando factualmente disponíveis; sem `hero-meta` duplicado; botões acessíveis por toque e responsividade.
6. **Tipologias, lazer, plantas e galeria:** títulos específicos, imagens com origem autorizada, alternativa textual, largura/altura, carregamento abaixo da dobra; separar dados de apresentação quando útil.
7. **Localização:** argumento de bairro verificado, imagens reais sem promessa de vista, mapa conforme política de privacidade/localização, link regional dentro da seção, CTA para solicitar localização/visita.
8. **Visita e negociação:** CTA para atendimento; visita sob confirmação quando obra em andamento. Entrada, financiamento, taxas e crédito só com fatos; não copiar exemplos financeiros do Ária para Ampère.
9. **FAQ:** perguntas do comprador sobre preço, estágio, tipologias, lazer, local, visita e pagamento; respostas úteis e verificadas; paridade literal entre HTML e `FAQPage`; 12 foi número do piloto, **não quota**.
10. **JSON-LD e imagem para busca:** grafo com tipos/propriedades compatíveis, @id único, ofertas e FloorPlan evidenciados, primária/secundária coerentes com hero/OG/Twitter; não atribuir recursos do Google automaticamente.
11. **Form 46, medição e rodapé:** escopo CSS, nomes, IDs, valores, eventos/GA4/GTM, consentimento, rodapé jurídico e CRECI sem mudanças acidentais.
12. **QA/gates:** CI de HTML, schema, SEO, endereço, fatos e fluxo; teste mobile real 320/375/390px + desktop; toque, teclado, CTA, formulário, estado de erro/sucesso, imagens, CLS/LCP, links e acessibilidade; provas antes/depois.
13. **Release:** PR e revisão humana; merge somente autorizado; identificar SHA da `main`, deployment `READY`, aliases; executar smoke no domínio público, Schema.org/Google, formulário e monitoramento; registrar rollback candidato e evidências.
14. **Handoff:** atualizar documento de fechamento, pontos não testados, PRs encerradas, próximo passo seguro, e matriz de aplicação por empreendimento para evitar regressão.

## 7. Pendências residuais e status de aceite

| Área | Estado no fechamento |
|---|---|
| Código e CI consumer | Integrado; checks registrados como sucesso antes do merge |
| Release Vercel | Production READY / SHA confirmado |
| Provedor RESF | Especificações das seis partes integradas à main |
| Mobile visual real 320/375/390 | **SEM EVIDÊNCIA INDEPENDENTE NESTE FECHAMENTO** |
| Form 46 lead real / CRM | **NÃO VALIDADO NESTE FECHAMENTO** |
| Três mídias bairro — HTTP, dimensões renderizadas e transferência real | **NÃO TESTADAS EXTERNAMENTE NESTE FECHAMENTO** |
| Schema.org/Rich Results após último release | **NÃO REVALIDADOS NESTE FECHAMENTO** |
| GSC pós-recrawl, queries/posição/CTR | **AGUARDAR DADOS** |
| Ranking, LCP/INP/CLS, conversão, receita | **NENHUM GANHO COMPROVADO** |

**Próxima ação segura:** realizar smoke pós-release no domínio publicado, inclusive três imagens do bairro, navegação, formulário em ambiente permitido, 12 FAQs, paridade de JSON-LD, experiência mobile e Core Web Vitals; anexar evidência ao consumer. Não iniciar alteração em massa. Caso haja falha, abrir correção limitada à seção afetada, com rollback no SHA anterior aprovado.

## 8. Checklist rápido para a próxima página

- [ ] Estado canônico e autorização resolvidos; ficha factual verificada
- [ ] SEO title, description, H1 único, H2 temáticos e copy comercial original
- [ ] Brand e estágio corretos; bairro em contexto, singular/plural natural
- [ ] Mídia hero, OG/Twitter, secundária e galeria sem conflito
- [ ] Ficha de plantas, vagas, metragens e oferta alinhada ao JSON-LD
- [ ] Quatro `.facts` apenas se comprovados, sem `hero-meta` redundante
- [ ] FAQ público relevante e literal em `FAQPage`
- [ ] Localização com mídia e link regional contextualizado, sem tempos inventados
- [ ] Visita/negociação sem prometer condições nem estágio de produto errado
- [ ] Greenn Form 46 e métricas preservados; CTA e footer claros
- [ ] Testes automáticos, mobile real, PR, merge, Vercel READY e smoke
- [ ] Registrar fatos, limites, SHAs, aceites e pendências no handoff

## 9. Retomada em nova conversa

> Retomar o projeto MoreNumTegra pelo SFJM. Antes de editar, conferir main, BOOTSTRAP_CANONICO, CURRENT, PROJECT_STATUS, NEXT_SAFE_ACTION e BLOCKED_ACTIONS. Ler o padrão único do RESF em `docs/frameworks/resf/v1/EXACT_PROJECT_PAGE_BUILD_STANDARD_V1_2026-10-11.md` e o fechamento em `docs/frameworks/resf/v1/RESF_EXACT_PROJECT_RELEASE_CLOSURE_2026-10-11.md`. O Ampère Brooklin passou por PRs #388/#389, main `b6497954e45d77cf37dd639dbea3c18bd29a4040` e Vercel production READY `dpl_6QQCpeSGVrpVJsFkap9o99Zbbw3M`; PR #387 foi fechada sem merge porque FAQ final entrou na #389. Não inventar aceites visuais, Schema.org/GSC pós-release ou entregas de CRM. Identificar primeiro a nova página e seus dados específicos, propor slice seguro e aguardar autorização antes de alterar/publicar.

---

**Fonte de verdade:** GitHub main e evidências live por SHA. Este documento é o fechamento documental da conversa, não substitui medição no ambiente comercial.
