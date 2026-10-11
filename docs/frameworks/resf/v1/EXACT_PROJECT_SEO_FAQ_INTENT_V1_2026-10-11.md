# RESF — Item 03: FAQ estratégico de SEO para páginas de empreendimentos — V1

> **Atualização de fechamento (11/10/2026):** este requisito integra o **padrão único RESF publicado no provedor** (PR #23, merge `f9b6bfb1f92f49aa9e49a47f9b1c7e3157beeccf`). Ampère Brooklin foi publicado no consumer por PRs #388/#389, Vercel `READY` no SHA `b6497954e45d77cf37dd639dbea3c18bd29a4040`. Eventuais referências abaixo a PRs Draft ou “não publicado” são **evidência histórica do período de implementação**, não o estado corrente. Veja o [fechamento com matriz, evidências e pendências](RESF_EXACT_PROJECT_RELEASE_CLOSURE_2026-10-11.md). A especificação como requisito documentado não promove automaticamente módulos gerais do framework nem dispensa testes pós-release. A PR #387 foi fechada sem merge; o FAQ final de 12 perguntas foi integrado pela PR #389.

**Estado:** CANDIDATE / DRAFT — requer revisão, gates e integração formal no repositório provedor. **Categoria:** conteúdo de busca e resposta orientado à intenção, com paridade de marcação estruturada quando aplicável.

## 1. Objetivo e distinção essencial

O FAQ não é uma coleção de perguntas aleatórias nem o questionário interno para capturar fatos. Ele é conteúdo público, indexável e útil ao comprador, elaborado a partir de **intenções reais de pesquisa e dúvidas de decisão imobiliária**. Deve contribuir para relevância semântica, compreensão do produto e encaminhamento comercial com transparência.

O **questionário interno de intake** (`templates/EXACT_PROJECT_JSONLD_INTAKE.template.yaml`) serve exclusivamente para descobrir e validar fatos antes da implementação. **Nunca** utilizá-lo automaticamente como FAQ de SEO.

`FAQPage` é uma representação de perguntas e respostas já publicadas visivelmente no HTML — **não** a origem de respostas, nem promessa de rich result. O Google pode restringir a exibição de resultados avançados de FAQ conforme suas políticas vigentes.

## 2. Critério de escolha das perguntas (SEO first, sem keyword stuffing)

1. Mapear a **intenção de busca**: informacional (características e localização), investigação comercial (tipologias, preços de referência e comparação), transacional (disponibilidade, agendamento, entrada e formas de pagamento).
2. Identificar **atributos específicos e comprovados** do empreendimento. Perguntas sobre características não divulgadas, comércio ou financiamento não devem receber respostas especulativas.
3. Priorizar dúvidas com potencial de responder ao usuário: **estágio/entrega, metragens/tipologias, dormitórios/suítes/vagas, valor vinculado à unidade de referência, diferenciais reais, lazer, plantas, localização, confirmação de disponibilidade e próximos passos comerciais**.
4. Quando aplicável e comprovado: salas comerciais, torre única, opções oficiais de planta e diferenciais próprios (por exemplo `Living Double View`).
5. Escolher perguntas naturais, distintas e não redundantes. **12 é referência editorial observada em Ária; não é mínimo universal, tampouco meta para preenchimento artificial.** Menos perguntas boas são preferíveis a perguntas inventadas ou repetidas.
6. Responder com **linguagem comercial útil, factual e qualificações necessárias**: preço de referência sujeito a confirmação; não garantir estoque, taxas bancárias, crédito, entrega ou negociação não verificada. Incluir CTA natural para contato sem transformar cada resposta em anúncio repetitivo.
7. Evitar informações irrelevantes sobre ausência de estoque que prejudiquem o contexto comercial; nunca afirmar disponibilidade inexistente ou esconder uma restrição material.
8. Revisar consistência com hero, ficha do imóvel, catálogo, plantas oficiais, estágio, endereço e política editorial do consumidor.

## 3. Regras técnicas de aceitação

| Gate | Exigência | Falha |
|---|---|---|
| Intenção | Toda pergunta representa necessidade de pesquisa/compra e é pertinente ao projeto | Pergunta genérica, redundante ou sem demanda identificável |
| Fatos | Toda resposta é suportada pelo conteúdo e fontes aprovadas | Metragem/preço/entrega/financiamento inventados |
| Visibilidade | Pares Q/A estão no HTML público e acessível, sem exigir login ou script crítico | FAQ só existe em JSON-LD |
| Paridade | `FAQPage.mainEntity` corresponde **literalmente** aos pares do HTML, preferencialmente na mesma ordem | Pergunta, resposta ou condição divergente |
| Qualidade | Perguntas distintas, respostas claras e suficientemente informativas; usar número adequado ao projeto | Repetição artificial ou meta fixa de 10/12 |
| Preservação | Alteração do FAQ não deve modificar `Product`, `Offer`, imagens, hero, endereço, formulário ou metadados sem aprovação | Regressão em itens já homologados |
| Validação | Teste automatizado de contagem e paridade; revisão humana editorial; Schema.org Validator e Google Rich Results **quando testáveis** | Alegar 0 erros ou 6 itens sem medição |
| Resultado | Medir SEO orgânico via GSC com janela e contexto adequados; não inferir ranking pelo código | Declarar ganho orgânico sem evidência |

**Atenção:** a contagem de nós JSON-LD **não necessariamente cresce** com o número de perguntas. É possível passar de 6 para 12 pares no mesmo nó `FAQPage`.

## 4. Referências reais — MoreNumTegra, 11/10/2026

### Ária Higienópolis — referência editorial existente

Rota: `https://www.moretegra.com.br/empreendimentos/aria-higienopolis/`.

No GitHub `main` do consumidor em 11/10/2026, `FAQPage` contém **12 perguntas e respostas** sobre entrega, tipologias, preço do studio 1510, lazer, salas comerciais, bairro, localização, disponibilidade, visitas, entrada/financiamento e dormitórios. **Este inventário atesta a presença em JSON-LD; não substitui validação posterior de paridade com o HTML visível.** O objetivo é compreender **cobertura de intenções**, não copiar perguntas literalmente para outros produtos.

### Ampère Brooklin — implementação proposta com paridade automatizada

Rota: `https://www.moretegra.com.br/empreendimentos/ampere-brooklin/`.

- Estado anterior **em produção**: 6 perguntas visíveis e 6 entradas no `FAQPage`. Publicação JSON-LD com 18 nós, testes da Product Authority de Schema.org **0 erros/0 avisos/5 itens** e Google Rich Results **6 itens** após PR #386.
- **PR de consumidor #387, Draft, não publicada nesta evidência**, branch `feat/ampere-brooklin-seo-faq-intent-20261011`: 6 → **12** perguntas no HTML e JSON-LD, com seis novas intenções: valor da unidade 0121, suítes e vagas, diferencial Living Double View, plantas padrão/opção 1/opção 2 de 262 m², torre única e agendamento.
- Novo guard `scripts/validate-ampere-brooklin-jsonld-parity.mjs` compara **12 pares literais e ordem** entre HTML e `FAQPage`, unicidade, respostas novas não vazias e materialidade. Testes de regressão vigiam escopo permitido; aguardar resultado/merge do consumer antes de registrar aceitação de produção.
- **Não afirmar** que os 6 itens Google continuam detectáveis após #387 ou que as novas perguntas produziram resultados orgânicos: requer nova homologação pós-deploy.

## 5. Perguntas de qualificação para criar um FAQ

- Qual é a página/produto exato e qual estágio comercial comprovado?
- Quais tipologias, metragens, unidades, diferenciais, plantas e modalidades estão documentados?
- Qual valor é real e vinculado a qual unidade? É referência sujeita a confirmação?
- Quais dúvidas de pesquisa aparecem nos dados disponíveis (GSC, atendimento comercial, pesquisa de consultas), sem inventar volume?
- A pergunta tem resposta verificável, útil ao comprador e coerente com a página?
- Já existe pergunta semelhante que seria redundante?
- A resposta é publicada em HTML? O `FAQPage` refletirá literalmente o texto e a ordem?
- O consumidor autorizou alterações de conteúdo? Há evidência de testes e deployment?

## 6. Fronteira e governança

Este é o **Item 03** do índice proposto de construção de páginas do RESF, **separado dos Itens 01 (JSON-LD) e 02 (imagens para busca)**. O Item 01 continua responsável pelo formato e validade do nó `FAQPage`; este Item 03 define **quais perguntas e respostas merecem existir na página por valor SEO**.

Não criar novo requisito de 12 perguntas para todas as páginas, nem promover automaticamente `RESF-SEO`/`RESF-SCHEMA`/`RESF-QA` no manifesto do consumidor. Aplicação continua sujeita a aprovação por página, CI, processo de release e confirmação real.
