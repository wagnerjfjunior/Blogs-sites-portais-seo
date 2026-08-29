# MoreNumTegra — Estratégia de preço de conversão — 2026-08-29

## Status

`PROVIDER_STRATEGY / PRICE_CLAIMS_REQUIRE_UNIT_LEVEL_EVIDENCE / NO_CONSUMER_MUTATION_AUTHORITY`

## 1. Objetivo

Usar preço e condição comercial como gatilho forte de clique/conversão em páginas e cards BOFU do MoreNumTegra, sem transformar uma condição específica de pagamento/unidade em preço genérico do empreendimento.

`AGGRESSIVE_MARKETING != UNSUPPORTED_PRICE_CLAIM`

## 2. Evidência interna disponível

No consumer `wagnerjfjunior/MoreNumTegra`, foi confirmada a estrutura mensal:

`Tegra/Agosto/Tabela/`

`Tegra/Agosto/Tabela_Coordenação/`

`Tegra/Agosto/Espelho/`

`Tegra/Agosto/Promocionais/`

Há, entre outros, tabela comercial de Nova Vivere, tabela/espelho de Elo Duo e peças promocionais de ELO e ODE.

Em 2026-08-29, `Tegra/Setembro/` contém apenas o placeholder `Setembro.md`; portanto Agosto é o conjunto mensal efetivamente populado observado.

Os arquivos binários devem ser a prova por unidade/condição antes de publicar um preço derivado deles.

## 3. Evidência competitiva observada

### OLX

O anúncio informado pelo Product Authority aparece na superfície de busca da OLX com:

- título: `Imóvel para venda possui 105 metros quadrados com 3 quartos em Lapa - São Paulo - SP`;
- preço observado: `R$ 1.248.000`;
- área: `105 m²`;
- 3 quartos.

URL fornecida pelo owner:

`https://sp.olx.com.br/sao-paulo-e-regiao/imoveis/imovel-para-venda-possui-105-metros-quadrados-com-3-quartos-em-lapa-sao-paulo-sp-1479645971`

### Imovelweb

Também foram observados anúncios de Nova Vivere / Lapa usando explicitamente preço condicionado a pagamento à vista, inclusive um resultado de 105 m² por `R$ 1.195.000` com a frase `Valor referente ... para pagamento à vista`.

### Interpretação

Há evidência de mercado de que corretores/portais estão usando o preço à vista como principal âncora de aquisição.

Isso não prova que o mesmo preço ou desconto seja aplicável ao MoreNumTegra. Prova que a estratégia de apresentação é competitivamente relevante.

## 4. Informação do Product Authority ainda a reconciliar

O owner informou:

- preço promocional atualmente usado: aproximadamente tabela menos 8%, conforme condição aplicável;
- condição à vista pode chegar a aproximadamente 24,6% abaixo da tabela.

Evidence class atual:

`USER_PROVIDED_EVIDENCE / REQUIRES_UNIT_AND_MONTH_RECONCILIATION`

Não aplicar `-24,6%` genericamente a todos os empreendimentos.

O percentual só pode virar claim publicável quando houver:

- empreendimento;
- unidade;
- tabela-base;
- preço/condição à vista;
- mês/validade;
- arquivo de evidência;
- disponibilidade atual.

## 5. Estratégia de exibição

Quando houver prova exata, o card deve priorizar o menor preço comercial legítimo para a condição declarada.

### Padrão recomendado

`À vista a partir de R$ X`

ou:

`Condição à vista: R$ X`

Imediatamente abaixo:

`*Valor para pagamento à vista, referente à unidade selecionada. Sujeito à disponibilidade e alteração. Consulte condições vigentes.`

O asterisco/disclaimer pode ser visualmente secundário, mas deve permanecer legível e diretamente associado ao preço.

## 6. Headline comercial

Preço pode ser usado como headline quando houver uma unidade exata e condição comprovada.

Exemplos de estrutura:

`105 m² na Lapa por R$ X à vista*`

`3 suítes no Caminhos da Lapa por R$ X à vista*`

`Uma condição que muda a conta: 105 m² por R$ X à vista*`

Não esconder `à vista` no rodapé quando o valor principal só existe nessa condição. O qualificante faz parte do próprio preço.

## 7. Percentual de desconto

Percentual é um segundo gatilho, não o primeiro.

Preferência:

`R$ X à vista*`

antes de:

`até 24,6% abaixo da tabela`

Se o percentual for usado, exigir comparação reproduzível entre preço-base e preço à vista da mesma unidade/mesmo período.

Evitar:

- percentual genérico do empreendimento;
- `até X%` sem pelo menos uma unidade vigente que prove X;
- preço de uma unidade esgotada apresentado como preço atual;
- misturar tabela de um mês com condição de outro.

## 8. Data model recomendado ao consumer

Para eliminar atualização manual ambígua, cada condição publicável deveria ser representada conceitualmente por:

```text
project
unit
area_m2
table_price
promotional_price
cash_price
payment_condition
discount_vs_table
valid_from
valid_until_or_review_date
availability
evidence_path
verified_at
```

O site não deve calcular automaticamente um desconto fixo global.

`UNIT_LEVEL_EVIDENCE -> DISPLAYABLE_PRICE`

`GLOBAL_DISCOUNT_ASSUMPTION -> FORBIDDEN`

## 9. CTA

Preço baixo deve levar ao próximo passo dentro do funil:

- `Quero esta condição`
- `Consultar condição à vista`
- `Ver unidades nesta condição`

Destino:

- WhatsApp MoreNumTegra;
- Form 46;
- experiência interna de filtro/detalhe quando existir.

Não usar preço competitivo para mandar o usuário a portal terceiro.

## 10. SEO / Search

Preço é altamente útil em BOFU, mas é volátil.

Recomendação:

- usar preço/condição no conteúdo/card;
- manter source-of-truth por mês/unidade;
- não colocar preço volátil no homepage title/meta description;
- futuras páginas individuais podem usar preço visível e structured data apenas quando a atualização estiver operacionalmente garantida;
- preservar data de atualização quando houver página de produto.

`LOW_PRICE != STABLE_METADATA`

## 11. Compliance mínimo de apresentação

Fontes oficiais brasileiras exigem informação de preço correta, clara, precisa, ostensiva e legível. Quando a diferença decorre do meio/prazo de pagamento, a condição precisa ser informada junto da oferta.

Portanto:

- copy principal pode ser agressiva;
- disclaimer pode ser discreto;
- disclaimer não deve ser ilegível, distante ou contraditório;
- `à vista` deve acompanhar o preço quando for condição essencial para obter aquele valor.

Isto é guardrail de informação, não aconselhamento jurídico.

## 12. Próximo proof obligation

Antes de implementar preço à vista no MoreNumTegra:

1. selecionar uma ou mais unidades candidatas;
2. reconciliar tabela-base + promoção + condição à vista no conjunto mensal vigente;
3. calcular o percentual real apenas dessas unidades;
4. registrar evidence path e validade;
5. então entregar ao consumer a copy final e os valores publicáveis.

Nenhuma alteração de preço no consumer foi executada pelo provider.
