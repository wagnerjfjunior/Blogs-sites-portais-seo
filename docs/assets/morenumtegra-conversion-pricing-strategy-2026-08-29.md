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

## 3. Evidência comercial rastreável

O consumer passou a versionar a condição no próprio repositório:

- `Tegra/Agosto/Anuncios/Anúncios.md`;
- `Tegra/Agosto/Anuncios/Anuncio NovaVivere Olx valor a vista-29-08-26.png`.

Registro reconciliado para os valores absolutos:

- Nova Vivere;
- unidade 708;
- 105 m²;
- valor à vista: `R$ 1.129.900,00`;
- confirmação: 29/08/2026;
- valor de tabela versionado em `Tegra/Agosto/Valores_a_vista.md`: `R$ 1.468.100`;
- anúncio OLX preservado como evidência de mercado.

Há divergência material entre percentuais versionados no consumer: `Tegra/Agosto/Anuncios/Anúncios.md` registra `24,6%`, enquanto `Tegra/Agosto/Valores_a_vista.md` registra `23,1%` para os valores absolutos acima. Portanto, nenhum percentual é considerado reconciliado ou publicável por este provider result.

A leitura anterior de `R$ 1.248.000` para esse anúncio estava incorreta e foi removida desta evidência.

`ABSOLUTE_PRICE_SUPPORTED != DISCOUNT_PERCENTAGE_RECONCILED`

### Interpretação

Há agora provenance interna suficiente para usar `R$ 1.129.900 à vista*` como claim de conversão da unidade 708 no Preview, desde que o disclaimer permaneça próximo e a condição seja reconfirmada antes da Green.

`VERSIONED_EVIDENCE != PERMANENT_AVAILABILITY`

## 4. Regra para percentual de desconto

O percentual da unidade 708 está **bloqueado para uso factual/comercial** enquanto as fontes canônicas do consumer permanecerem divergentes.

Não usar `24,6%`, `23,1%` ou qualquer outro percentual derivado como claim até reconciliação explícita da tabela-base, condição e cálculo no consumer.

Qualquer percentual futuro exige:

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

Percentual só pode ser uma segunda camada depois de reconciliação reproduzível entre preço-base e preço à vista da mesma unidade e do mesmo período. Enquanto a divergência atual permanecer, omitir percentual.

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

Para a unidade 708, o proof obligation de provenance está atendido apenas para os **valores absolutos** observados. O percentual de desconto permanece `UNRESOLVED_CONFLICT`.

Antes de qualquer nova publicação/atualização comercial:

1. reconfirmar disponibilidade da unidade 708;
2. reconfirmar que `R$ 1.129.900` continua sendo condição à vista vigente;
3. preservar o disclaimer junto ao preço;
4. não publicar percentual até reconciliar as fontes conflitantes no consumer;
5. se preço/condição mudar, atualizar a fonte canônica antes da publicação.

Para novas unidades, repetir o mesmo modelo de evidência.

O provider não adquire autoridade de publicação por esta recomendação.
