# RESF — Requisito 05 do padrão único: hero sem duplicação + faixa facts — V1

**Estado:** CANDIDATE/DRAFT · 11/10/2026  
**Escopo:** arquitetura visual/UX da abertura de páginas comerciais de empreendimentos; é **um requisito do padrão único RESF**, não um padrão separado.

## 1. Princípio

O `hero` deve apresentar foto principal, identificação do produto, proposta comercial em linguagem natural e CTA claro. **Não duplicar no hero uma faixa de metadados que já aparece imediatamente abaixo.** Remover `hero-meta` ou blocos equivalentes quando repetirem a faixa `.facts`.

A faixa `.facts` deve apresentar quatro quadros de leitura rápida **quando os dados estiverem comprovados e fizerem sentido no produto**, preservando o padrão mobile-first e acesso por toque.

## 2. Quatro posições de informação

| Posição | Assunto padrão | Exemplo aprovado na implementação Ampère |
|---|---|---|
| 1 | Área / metragem de referência comprovada | 262 m² · Área privativa |
| 2 | Vagas da tipologia/unidade de referência | 4 vagas |
| 3 | Bairro/região e diferencial verdadeiro e relevante | Brooklin · Living Double View |
| 4 | Estágio comercial/obra comprovado | Em construção |

Dados de outros empreendimentos **não são preenchidos com os números do Ampère**. Se não houver evidência de vagas, metragem, estágio ou diferencial, classificar o fato como ausente e ajustar o conteúdo a partir de informações reais, sem inventar campos apenas para completar quatro posições.

Outros aspectos comprovados como dormitórios/suítes continuam em conteúdo semântico indexável, ficha do produto e JSON-LD pertinente, sem forçar redundância no hero.

## 3. Critérios UX e CSS

- `hero-meta` redundante ausente da página; `hero` com título, texto descritivo e CTA preservados.
- Exatamente quatro quadros no modelo comercial completo, com hierarquia clara: legenda e dado principal; diferencial contextual subordinado ao bairro.
- Mobile: grid **2 × 2**, responsivo para 320/375/390px, `minmax(0,1fr)`, texto longo com quebra adequada, sem overflow horizontal e sem depender de hover.
- Desktop: **quatro colunas** quando largura permitir; alinhamento e divisão discretos.
- Contraste adequado ao tema do projeto; preservar identidade Tegra (amarelo `#EBB92E` em elementos de ação quando pertinente), texto legível, redução de CLS e CSS simples.
- Sem alterar foto principal/OG/Twitter, formulário Form 46, preço, catálogo, eventos, FAQ, schema ou endereço sem autorização separada.

## 4. Gates de validação

1. Código: ausência de `hero-meta` duplicado e presença de uma única faixa `.facts`.
2. Dados: valores da faixa correspondem a fatos aprovados e ao restante do conteúdo comercial.
3. Responsivo: grade 2×2 no mobile e quatro colunas desktop; validar visualmente em dispositivos reais/viewport.
4. Regressão: hero, CTA, JSON-LD, mídias, preço, Form 46 e conversão preservados.
5. Governança: branch, PR, testes, revisão, autorização de merge e deployment SHA; registrar evidência real de produção e rollback.

## 5. Referência concreta

**Ampère Brooklin**, `MoreNumTegra` PR #388 (**Draft**), branch `feat/ampere-form-footer-aria-ux-20261011`, commit testado `d139cd6e515730e7059804789f4f800bcfc976dc`: remove `hero-meta` duplicado, transforma a faixa em 262 m² / 4 vagas / Brooklin + Living Double View / Em construção. Os quatro quadros têm CSS mobile 2×2 e desktop 4 colunas; mantém 4 suítes no texto principal.

A PR #388 também contém o requisito 04 (UX de formulário/rodapé). Os controles automatizados passaram **9/9** nesse commit. Isso **não equivale** a teste visual humano ou publicação em produção. A PR #387 (FAQ SEO) é mudança independente e não integra automaticamente a branch #388.

**Limite:** este requisito não autoriza modificações retroativas em todas as páginas nem implica promessa de melhora de Core Web Vitals ou SEO sem medições.
