# RESF — Requisito 06 do padrão único: SEO editorial e copy de conversão — V1

**Estado:** CANDIDATE/DRAFT, 11/10/2026. **Escopo:** construção de páginas comerciais de empreendimentos com autoridade própria, linguagem voltada ao comprador e termos de busca incorporados naturalmente. Não é um padrão concorrente: é o sexto requisito do **único padrão de construção RESF**.

## 1. Princípio de autoridade da página

A página de cada empreendimento deve responder, por conta própria, às buscas de marca, tipologia e localização que correspondam àquele produto. Não transferir prematuramente o visitante para uma página regional pelo topo/header. Um link interno de bairro pode existir **no contexto apropriado da seção de localização**, como caminho complementar, não fuga da página de vendas.

**Rejeitar metalinguagem e justificativas de bastidores:** frases como “esta página mantém o foco”, “a página regional concentra a descoberta”, “galeria ampliada com imagens oficiais”, “o material oficial destaca...” não ajudam o comprador. Escrever para quem quer morar ou negociar, não para quem audita a arquitetura SEO.

## 2. Regras editoriais verificáveis

1. **H1 único:** nome reconhecível do produto sem repetir bairro desnecessariamente, como “Ampère Brooklin” e não “Ampère Brooklin Brooklin”.
2. **H2 e abertura de intenção:** frase natural com “apartamento no Brooklin”, metragem, suítes, vagas e tipo de empreendimento **quando comprovados**. Evitar repetição mecânica de termos para ranqueamento.
3. **Voz de atendimento direto:** priorizar segunda pessoa (“você”, “conheça”, “explore”, “agende”) e frases comerciais que transmitam o benefício real da característica. Não falar sobre “o site”, “esta página”, “o material oficial” nem usar tom de relatório técnico como copy de vendas.
4. **Benefícios sustentados por atributos verdadeiros:** explicar por que uma planta, dois terraços, torre única e áreas de lazer podem interessar; não inferir vista garantida, acessos/tempo de trajeto, condomínio exclusivo, entrega, itens de infraestrutura, preço de outras unidades ou disponibilidade.
5. **Galeria e plantas:** trocar texto de interface/documentação por convites específicos aos ambientes existentes. Não usar falsa urgência ou disponibilidade garantida.
6. **Localização:** apresentar o bairro como benefício contextual real; link interno de região como leitura adicional abaixo do conteúdo de venda, sem desalojar o leitor logo no primeiro contato. Endereço exato visível conforme a política local do consumidor; usar WhatsApp para solicitação de rota quando previsto.
7. **Argumentação comercial:** dar motivos para visitar, comparar plantas e consultar condições; preservar oferta de referência vinculada à unidade, disponibilidade sujeita a confirmação e textos legais.
8. **SEO técnico:** manter title, description, canonical, H1/H2, mídia, JSON-LD, FAQ, mobile e Form46 intactos, salvo autorização específica. Contratos de fatos, brand e tracking não podem ser quebrados pela copy.
9. **Não confundir H2 com tamanho visual:** manter hierarquia semântica correta mesmo no hero. Validar legibilidade, contraste e dobras em dispositivos reais.
10. **Avaliação:** auditoria de intenção e utilidade, revisão factual/comercial e comparação before/after no HTML. Ganho orgânico/CTR/lead não pode ser afirmado sem analytics e observação da SERP.

## 3. Procedimento repetível por empreendimento

1. Ler main, status SFJM e baselines; mapear conteúdo da página e consultas/intenção plausíveis sem inventar volume de pesquisa.
2. Listar **termos-alvo factuais**, H1/H2 existentes, frases metalinguísticas, links que retiram visitantes cedo, CTAs e seções com repetição.
3. Coletar fatos do próprio empreendimento, não de outra página: nome, bairro, estágio, tipologias/metragens, suítes/vagas, plantas oficiais, diferenciais, lazer, unidade e valor de referência, localização governada.
4. Reescrever seção por seção com **benefício + evidência + próximo passo**. Uma expressão técnica de produto pode ser explicada por sua utilidade ao comprador.
5. Verificar que a página é autoridade do projeto e contém link regional somente como navegação complementar.
6. Executar testes automatizados para H1, hierarquia, links, strings ruins, mídias, dados estruturados, Form46, preço e área, e conferir visualmente mobile/desktop.
7. Branch/PR, revisão e aprovação do Product Authority; só depois merge e Vercel READY com SHA conferido; repetir Schema.org/Google e registrar evidência. Nunca supor ranking ou conversão.

## 4. Referência de caso: Ampère Brooklin

**Situação original observada:** H1 duplicando “Brooklin”, saída para `/regioes/brooklin/` no canto superior, hero descritivo em `<p>` genérico, frases explicando a “página regional” e “galeria ampliada”, justificativa “material oficial” e seção de localização sem argumento comercial.

**Evolução proposta:** consumidor `wagnerjfjunior/MoreNumTegra` **PR #389 (Draft)**, branch `feat/ampere-brooklin-seo-commercial-copy-20261011`, empilhada sobre a PR #388. Após nova revisão editorial, H1: “Tegra Ampère Brooklin — apartamentos em construção”; H2: “Apartamentos no Brooklin de 262 m² privativos, com 4 suítes, 4 vagas e dois terraços em torre única”. O estágio *em construção* é factual; não substituir por “pronto para morar” só para captar a expressão.

**Keywords:** cobrir, quando fizer sentido editorial e houver produto correspondente, singular (“apartamento no Brooklin”) e plural (“apartamentos no Brooklin”) em seções diferentes, sem repetição artificial. Inserir marca Tegra em H1, title, meta description, seções e respostas, preservando o nome próprio Ampère Brooklin.

**Meta description:** resumo objetivo, único e persuasivo que antecipe atributos verificáveis, estágio e caminho comercial; não é atributo `meta keywords` nem promessa de ranking. Manter em paridade com a descrição da entidade `WebPage` quando aplicável.

**FAQ e conversão:** incorporar na própria branch de copy **12 perguntas visíveis e 12 respostas idênticas em `FAQPage`**, integrando assuntos de preço vinculado à unidade 0121, 262 m², quatro suítes/vagas, living com dois terraços, torre única, lazer, localização, visita e possibilidade de financiamento. Isso integra semanticamente o escopo antes separado na PR #387, cuja reconciliação formal deve ser resolvida antes do merge. Nunca criar condições financeiras, percentuais, cronogramas ou estoque fictícios.

**Visita e pagamento:** novas seções específicas com CTA para Form 46. Empreendimento em construção: visita/acesso sob confirmação prévia. Financiamento pode ser estudado dependendo de unidade, tabela, estágio e banco, sem taxas nem aprovação garantidas. É incorreto copiar do Ária a entrada indicativa de 10–20% ou a condição de empreendimento entregue.

**Evidência e estado:** PR #389 permanece Draft, sem integração à main ou publicação. A versão editorial ampliada passou **10/10 checks automáticos** no SHA `b01372985058660d7aad97db3ba9ac92f21316a1`, incluindo paridade FAQ HTML/JSON-LD, inventário de 18 nós, imagens, footer, Form 46 e endereços. Revisão visual mobile/desktop, decisão sobre PR #387 e aprovação humana continuam pendentes. O responsável informou que havia validado Schema.org e GSC para o estado anterior; isso não valida automaticamente esta nova versão antes de publicação.

## 4.1. Localização com prova visual e link regional complementar

O padrão único RESF deve equilibrar **copy comercial, material visual real do bairro e CTA útil**. Se a localização ficar excessivamente textual, apresentar uma galeria factual de imagens autorizadas diretamente do acervo do empreendimento/bairro, com `alt` descritivo, legenda identificadora, largura/altura declaradas, `loading="lazy"` e CSS responsivo sem dependência de hover.

**Referência de aplicação:** Ampère Brooklin, PR #389 (Draft), introduz três imagens do próprio acervo Tegra: Ponte Estaiada, Brooklin e entorno da Marginal Pinheiros, usando a origem direta `stracctegra.blob.core.windows.net` em lugar do proxy `tegraincorporadora.com.br/_next/image`. Faixa de três colunas em desktop e uma coluna mobile; preservar mapa e CTA de localização exata.

Usar título comercial convidativo, sem afirmar tempo de trajeto não medido. A menção a **Avenida Berrini** e ambiente arborizado contextualiza o bairro, mas não deve virar promessa de distância, trajeto, condições de trânsito ou atrativo imediatamente adjacente sem evidência. Evitar inserir endereço completo fora do rodapé governado.

A página continua como autoridade do empreendimento. O link `/regioes/brooklin/` aparece **na própria seção de localização**, depois do argumento comercial e da galeria, não no cabeçalho. Isso também melhora a navegação interna sem afastar o lead na abertura.

Gates adicionais: 3 URLs e origem autorizadas; disponibilidade/HTTP de cada arquivo a verificar quando houver acesso de rede; alternativas textuais e dimensões; lazy-loading; mobile sem overflow; imagens reais que representem o bairro; preservação de `og:image`, imagem principal e secundária do projeto, Form46 e JSON-LD. **Não qualificar imagem como entregue por CDN responsiva sem derivados de largura efetivamente disponíveis e verificados.**

## 5. Gates mínimos para aprovação do requisito 06

- `SEO_EDITORIAL`: H1 único e não redundante, H2 natural e semanticamente correto, narrativa de intenção de busca.
- `PRODUCT_TRUTH`: números, atributos, condições e unidade de referência corretos, sem invenção.
- `COPY_CONVERSION`: linguagem direta, benefício concreto, CTA útil e comercialmente honesto.
- `INTERNAL_LINKS`: link regional contextualizado e não posicionado como fuga no primeiro viewport.
- `INVARIANTS`: nenhuma regressão em JSON-LD, imagens, conteúdo legal, Form46, tracking, acessibilidade.
- `MOBILE_REVIEW`: validar leitura, hierarquia, hero e form com capturas/responsividade reais.
- `SEARCH_VALIDATION`: testes Schema.org/Google pós-deploy e observação GSC futura, quando disponível.

A aplicação é **por projeto e por fatos comprovados**. Não usar a copy do Ampère literalmente em outras páginas, nem criar um novo “padrão número 6” independente.
