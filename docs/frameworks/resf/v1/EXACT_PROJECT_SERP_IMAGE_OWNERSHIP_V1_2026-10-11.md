# RESF — Item 02: imagem principal e secundária para busca (SERP) — V1

> **Atualização de fechamento (11/10/2026):** este requisito integra o **padrão único RESF publicado no provedor** (PR #23, merge `f9b6bfb1f92f49aa9e49a47f9b1c7e3157beeccf`). Ampère Brooklin foi publicado no consumer por PRs #388/#389, Vercel `READY` no SHA `b6497954e45d77cf37dd639dbea3c18bd29a4040`. Eventuais referências abaixo a PRs Draft ou “não publicado” são **evidência histórica do período de implementação**, não o estado corrente. Veja o [fechamento com matriz, evidências e pendências](RESF_EXACT_PROJECT_RELEASE_CLOSURE_2026-10-11.md). A especificação como requisito documentado não promove automaticamente módulos gerais do framework nem dispensa testes pós-release. A PR #387 foi fechada sem merge; o FAQ final de 12 perguntas foi integrado pela PR #389.

**Status:** `CANDIDATE / USER_VALIDATED_TECHNICAL_CONFIGURATION` · **11/10/2026**  
**Objeto:** padronização de **sinais de identificação de imagem** para páginas canônicas de empreendimentos. Não é promessa de que o Google mostrará determinada foto nos resultados orgânicos.

## 1. Seleção de imagem — perguntas obrigatórias

Antes de gerar o bloco de HTML e JSON-LD, confirmar:

- Qual é a **imagem principal autorizada** do empreendimento? URL original, conteúdo e fonte; deve representar o projeto, não o profissional de vendas.
- Qual é a **imagem secundária autorizada**, visualmente distinta da primeira? URL original, conteúdo e fonte.
- Ambas as imagens representam este empreendimento e têm autorização de uso? A URL da mídia está íntegra e acessível?
- Em qual elemento aparece a imagem principal na página? Qual conteúdo textual deve compor o `alt` e a legenda?
- Há imagem da corretora? Ela pode integrar `Person`/`RealEstateAgent`, mas não assumir o papel de imagem principal do `WebPage` por engano.
- Há restrições de disponibilidade, versão, CDN ou licença da mídia que impeçam a publicação?

Se faltarem dados ou mídia aprovada, retornar `BLOCKED_BY_MISSING_FACT`, sem inventar ou reempregar foto de outro empreendimento.

## 2. Regras de implementação e aceite

| Sinal | Padrão quando aplicável | Verificação |
|---|---|---|
| Hero visível | `<img>` inicial com a URL da imagem principal em `src` ou `srcset` responsivo coerente | Conteúdo real, `alt`, dimensão declarada quando conhecida; renderizável sem JS não essencial |
| Prioridade do hero | `fetchpriority="high"` para a imagem LCP quando apropriado | Imagem realmente crítica, não lazy; evitar prioridade concorrente e avaliar impacto de desempenho |
| `og:image` | Mesma identidade de imagem principal aprovada | URL absoluta correta para a canonical |
| `twitter:image` | Mesma identidade de imagem principal aprovada | URL absoluta correta |
| `WebPage.primaryImageOfPage` | Aponta por `@id` ao `ImageObject` principal | `@id` resolve no grafo |
| `WebPage.image` | Referencia imagem principal primeiro e secundária depois | Duas identidades distintas; `@id` resolvidos |
| `ImageObject` principal | `contentUrl` da imagem de fachada/hero e legenda correspondente, conforme evidência | Paridade com HTML, OG e Twitter |
| `ImageObject` secundário | `contentUrl` de mídia secundária real, distinta, e legenda adequada | Paridade com mídia visível, não duplicar a principal |
| `ApartmentComplex.image` | Imagens reais do empreendimento, sem URLs duplicadas | Não substituí-las por fotografia da corretora; primeira imagem coerente com a prioridade do projeto |
| Outras imagens | Podem usar carregamento lazy abaixo da dobra | Não atrasar o LCP nem bloquear conteúdo crítico |

**Importante:** os metadados Open Graph/Twitter são sinais úteis para compartilhamento e consistência; não são instruções vinculantes ao Google sobre sua miniatura na SERP. O Google pode optar por outra imagem. Não tratar nenhum resultado do teste JSON-LD como prova de thumbnail orgânica escolhida.

**Separação com Item 01:** a construção de `WebPage.image` e `ImageObject` pertence ao padrão JSON-LD. A coerência com hero, Open Graph, Twitter e prioridade de carregamento pertence a este Item 02.

## 3. Referência concreta — Ampère Brooklin (aprovado tecnicamente)

Página: `https://www.moretegra.com.br/empreendimentos/ampere-brooklin/`. Consumer GitHub `main@09efee712a625075ff1b2e1d1dc9fa84ece90e24`, produção Vercel `dpl_2XNToN3fPizGANgu9Qa2Tf2thBU4` READY, verificado no mesmo commit após PR #386.

**Imagem principal: fachada**  
`https://stracctegra.blob.core.windows.net/assets/EmpreendimentoVitrine/351/ImagemPrincipal/Tegra-Incorporadora-Detalhe-da-Fachada-Empreendimento-Ampere-Brooklin-Apartamentos-Brooklin-Sao-Paulo-SP-714x640-1718890023834.jpg`

No código: hero `<img class="hero-poster">` com `fetchpriority="high"`, `og:image`, `twitter:image` e `ImageObject#primary-image` usam o mesmo arquivo; `WebPage.primaryImageOfPage` aponta para o `@id` da imagem principal.

**Imagem secundária: piscina**  
`https://stracctegra.blob.core.windows.net/assets/EmpreendimentoVitrine/351/Imagem/Tegra-Incorporadora-Area-de-Lazer-Piscina-Empreendimento-Ampere-Brooklin-Apartamentos-Brooklin-Sao-Paulo-SP-1600x900-1722456566878.jpg`

No código: segunda imagem visível com `loading="lazy"`, `ImageObject#secondary-image`, segunda referência em `WebPage.image`. URLs distintas da principal. O grafo de `ApartmentComplex.image` pode incluir outras fotos oficiais sem repetir entradas.

**Resultado de aceite observado do Item 01 na mesma página:** Schema.org Validator 0 erros / 0 avisos / 5 itens; Google Rich Results 6 itens válidos após teste da Product Authority em 11/10/2026. **Não constitui evidência de miniatura efetiva na SERP**, que ainda depende de observação separada.

## 4. Gate de QA reaproveitável

- `PASS`: principal/secundária oficiais comprovadas, URLs diferentes, imagem prioritária coerente em hero+OG+Twitter+JSON-LD, tags e nós corretos, mídia visível e não dependente de JS crítico, ausência de competição estrutural de retrato da corretora como imagem principal.
- `BLOCKED_BY_MISSING_FACT`: mídia não aprovada, URL desconhecida, indefinição de prioridade ou ausência de imagem secundária exigida no perfil.
- `FAIL`: URLs duplicadas, retrato de corretor como imagem principal indevidamente, `ImageObject` não resolvido, divergência entre hero/OG/Twitter/JSON-LD ou ausência de evidência de mídia usada.
- **Validação externa separada**: observar indexação e a miniatura exibida na SERP, se disponível; não afirmar `SERP_THUMBNAIL_CONFIRMED` com base apenas em tags, JSON-LD ou Rich Results.

O padrão é **candidato** do provedor. Adoção e execução no consumidor requerem autorização e validação específica por empreendimento; não aciona alterações retroativas nas outras URLs.
