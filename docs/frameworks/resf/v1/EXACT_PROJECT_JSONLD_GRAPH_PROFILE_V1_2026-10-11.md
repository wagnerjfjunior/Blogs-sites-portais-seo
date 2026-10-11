# RESF — Exact-project JSON-LD Graph & Google Validation Profile v1

> **Atualização de fechamento (11/10/2026):** este requisito integra o **padrão único RESF publicado no provedor** (PR #23, merge `f9b6bfb1f92f49aa9e49a47f9b1c7e3157beeccf`). Ampère Brooklin foi publicado no consumer por PRs #388/#389, Vercel `READY` no SHA `b6497954e45d77cf37dd639dbea3c18bd29a4040`. Eventuais referências abaixo a PRs Draft ou “não publicado” são **evidência histórica do período de implementação**, não o estado corrente. Veja o [fechamento com matriz, evidências e pendências](RESF_EXACT_PROJECT_RELEASE_CLOSURE_2026-10-11.md). A especificação como requisito documentado não promove automaticamente módulos gerais do framework nem dispensa testes pós-release. A PR #387 foi fechada sem merge; o FAQ final de 12 perguntas foi integrado pela PR #389.

**Status:** `PROVIDER_CANDIDATE / EVIDENCE_INTAKE / NOT_ADOPTED_AUTOMATICALLY`  
**Scope:** **somente JSON-LD** de páginas canônicas de empreendimentos imobiliários; exclui criação de HTML, layout, SEO editorial, UX, performance, GTM, formulário, CRM e publicação.  
**Consumer piloto:** `wagnerjfjunior/MoreNumTegra` — Bem Moema e Universo Tatuapé Órbita.  
**Versão de evidência:** 2026-10-11.  
**Contratos RESF relacionados:** C01 (fatos), C07 (grafo), C17 (prontidão).  
**Autoridade de produto/implantação:** pertence ao consumidor; provedor descreve candidato reutilizável e não modifica seu runtime.

## 1. Resultado aceito no piloto — QUANTITATIVO e QUALITATIVO

Observação direta do usuário no **Bem Moema** (capturas de 11/10/2026, ~10h31–10h32 BRT), após a publicação da PR #385:

| Ferramenta/categoria | Resultado observado |
|---|---:|
| Schema.org Validator | **0 erros, 0 avisos, 5 itens de nível superior** |
| Google Rich Results — Snippets do produto | **1 item válido** |
| Google Rich Results — Listagens do comerciante | **1 item válido** |
| Google Rich Results — Indicadores de localização atual / Breadcrumb | **1 item válido** |
| Google Rich Results — Empresas locais | **1 item válido** |
| Google Rich Results — Organização | **2 itens válidos** |
| **Total Google Rich Results** | **6 itens válidos** |

**A distinção numérica é essencial:** Schema.org apresenta *5 itens de topo*; Google apresenta *6 instâncias elegíveis*, distribuídas em *5 categorias*; o grafo JSON-LD da página possui **18 nós**. Os números **não são a mesma métrica**. O Google assinalava avisos *não críticos* de campos opcionais em Product/Offer nas capturas anteriores: não converter aviso opcional em obrigação de inventar dados.

A evolução específica de Bem Moema foi `0 itens Google → 3 → 6`. A qualidade foi refinada com `Product.isRelatedTo → ApartmentComplex` e a limpeza da imagem repetida; a remoção de `ApartmentComplex.brand` inválido produziu evidência do Schema.org Validator com **0 erros / 0 avisos** e preservou os **6 itens** Google. O intervalo temporal não prova que cada alteração isolada *causou* a contagem; cada estágio deve permanecer documentado com SHA, captura e momento.

Referências reproduzíveis, sem tomar screenshots por evidência indexada no provider:
- Consumer `MoreNumTegra` PRs **#379** (3 rich items), **#381** (Product/Offer), **#382** (paridade Órbita e FloorPlans), **#384** (Product → projeto e dedupe), **#385** (`ApartmentComplex.brand` removido).
- Consumer `main` integrada observada: `7e5e2297c21eb6a01cad52c829a0533f5c1b7214`; Bem Moema `src-greenn/empreendimentos/bem-moema/index.html`; Órbita `src-greenn/empreendimentos/universo-tatuape-orbita/index.html`.
- Último release confirmado: Vercel Production `dpl_AsXLYpgLcU3oWCpjpfEPce5szoGm` READY / `www.moretegra.com.br` / SHA acima.
- URL testada: `https://www.moretegra.com.br/empreendimentos/bem-moema/`.
- Capturas da Product Authority na conversa 2026-10-11: Schema.org Validator 0/0/5, Google Rich Results 6 válidos. **Não integradas como arquivos ao provedor**.

## 2. Modelo de grafo — relacionamento e propriedade por tipo

Use um único emissor canônico `application/ld+json` e `@graph` com `@id` estável; cada nó deve representar **o empreendimento em questão**, não copiar informações de outro.

| Nó | Requisito orientado por fatos | Relações importantes |
|---|---|---|
| `WebSite` | Domínio canônico real | `WebPage.isPartOf` |
| `WebPage` | Canonical e entidade principal | `mainEntity → ApartmentComplex`, `breadcrumb → BreadcrumbList`, `image` primária/secundária |
| `BreadcrumbList` | Hierarquia real visível/navegável | URLs canônicas, posições coerentes |
| `Brand` | Marca efetiva e verificada | Referência em `Product.brand`, `Organization.brand` |
| `Organization` | Empresa identificável e real | `brand`, `contactPoint`, `url` |
| `ContactPoint` | Telefone/canal/componente de atendimento comprovado | Identidade real da organização |
| `Person` | Profissional identificado e credenciado quando aplicável | `worksFor`, `workLocation` comprovada, registro profissional |
| `RealEstateAgent` | Serviço/agente local verdadeiro | `address` **do projeto quando o atendimento é in loco**; canal/organização/foto real |
| `Service` | Atendimento comercial realmente prestado | `provider` e `broker` reais |
| `ApartmentComplex` | Empreendimento concreto | Endereço, imagens, `accommodationFloorPlan` com fatos |
| `ImageObject` | Hero/segunda imagem reais, distintas | `WebPage.image` e `primaryImageOfPage` |
| `FloorPlan` | Apenas plantas oficiais com correspondência comprovada | Nome/tipologia/área/URL de imagem existentes |
| `Product` | **Unidade específica** identificada na página, se houver oferta verificada | `brand`, `image`, `offers → Offer`, e relacionamento factual de produto com projeto quando validado |
| `Offer` | Valor de referência, moeda e unidade conhecidos, se publicados | Mesmo produto e mesma URL, preço coerente e qualificado |
| `FAQPage` | Somente perguntas/respostas presentes na página | Paridade exata conteúdo visível ↔ JSON-LD |

**Modelo de referência do Bem Moema:** 18 nós, pois possui **três** FloorPlans oficiais (80, 123, 148 m²). Órbita possui 19, incluindo um quarto FloorPlan de unidade específica, **não copiável**. Não impor cardinalidade fixa 18/19 a outros produtos.

**Preservação da marca:** Schema.org Validator detectou a propriedade `brand` inválida em `ApartmentComplex` (tipo Place). A correção foi **retirar somente `ApartmentComplex.brand`**, preservando o nó `Brand`, `Organization.brand`, `Product.brand`. Antes da publicação, verificar compatibilidade `domainIncludes/rangeIncludes` e validar resultados efetivos; não transferir indiscriminadamente `brand` a todos os tipos.

**Conexão do produto:** o exemplar comprovado Bem Moema usa `Product.isRelatedTo → ApartmentComplex#project`, expandido qualitativamente no Google segundo o consumidor e sem avisos no validador final. O contrato exige vínculos de significado validado; não impõe esse predicado específico cegamente a páginas sem Product ou sem projeto correspondente. Aderência a Schema.org e novas versões dos validadores deve ser revalidada com URL real.

## 3. Intake obrigatório de fatos antes de emitir JSON-LD

Perguntar **somente informações ausentes** e permitir `NOT_APPLICABLE` ou `BLOCKED_BY_MISSING_FACT`. Nenhuma invenção:

1. **Identidade e destino:** nome oficial, slug, URL canônica, tipo do projeto, tipo de página, bairro/região e estágio.
2. **Localização:** endereço completo do **empreendimento** (logradouro, número, município, UF, CEP), fonte e data; coordenadas somente se comprovadas. Para atendimento in loco, `RealEstateAgent.address == ApartmentComplex.address`; se não in loco, não atribuir endereço do projeto como fato do agente.
3. **Empresa/marca/agente:** marca, incorporadora, organização de vendas, URL e telefones autorizados, nome do profissional, registro e foto comercial aprovada; atendimento e vínculo empregatício reais.
4. **Mídia:** hero real, imagem secundária **distinta**, demais imagens oficiais autorizadas, alt/caption existentes; imagens não devem ter URL duplicada no conjunto do projeto.
5. **Plantas:** cada imagem oficial, tipologia, área, unidade de área e fonte; não preencher `FloorPlan` por aproximação.
6. **Oferta opcional:** existe unidade individual comprovada? Identificador, metragem, valor exibido na página, moeda, data/fonte da tabela, ressalva de condições, URL exata; se não existir, **não emitir** `Product/Offer` artificiais.
7. **Disponibilidade/avaliações:** `availability`, `review`, `aggregateRating` e status de estoque somente com fonte verificável; não adicionar frete e política de devolução fictícios para imóveis.
8. **FAQ de SEO:** perguntas orientadas à intenção de busca e às dúvidas reais do comprador, com respostas específicas, úteis e fundamentadas em fatos do empreendimento, *publicadas visivelmente* na página. No `FAQPage`, reproduzir exatamente essas perguntas e respostas; se ausentes, não emitir `FAQPage`. **Ária Higienópolis é referência de 12 perguntas publicadas no JSON-LD**, abrangendo estágio, tipologias, preço, lazer, localização, disponibilidade, visita e financiamento. Não impor 12 perguntas universalmente, não duplicar perguntas sem relevância e não inventar respostas para atingir contagem. O template de intake é uma ferramenta interna distinta, nunca o FAQ público.
9. **Proveniência:** caminho do HTML no commit validado, hash e janela de vigência dos dados temporais; conflitos são sinalizados e bloqueados, jamais reconciliados silenciosamente.

Use o template `docs/frameworks/resf/templates/EXACT_PROJECT_JSONLD_INTAKE.template.yaml` (proposta nesta PR) e reserve campo `missing_facts` para devolução de questionamentos ao consumidor.

## 4. Gates de aceite, em ordem

1. **Fact gate** — fonte, data e autorização de cada dado; bloquear dados materiais não comprovados.
2. **Structure gate** — JSON parse, apenas um emissor canônico, IDs estáveis e resolvidos, referências ao mesmo projeto, tipos e propriedades compatíveis, nenhum duplicado, FAQs alinhadas, projetos/endereços não misturados.
3. **Qualitative gate** — `Product` expande a entidade correta com local, imagens, plantas quando emitidos; `Offer` descreve a unidade e o preço corretos; `RealEstateAgent` reflete atendimento verdadeiro, não endereço global inventado; mini-galeria sem URLs idênticas; validar nós que se relacionam entre si.
4. **Schema.org gate** — URL real em `validator.schema.org`, objetivo **0 erros e 0 avisos** para grafos compatíveis; todo aviso deve ser classificado (incompatibilidade estrutural / repetição aninhada / externo). Não eliminar informações factuais válidas apenas para manipular contagem.
5. **Google gate** — no `search.google.com/test/rich-results`, registrar **cada categoria**, quantidade, entidades e avisos. **Perfil de referência de página comercial completa:** até 6 detecções observadas (1 Product Snippet, 1 Merchant Listing, 1 Breadcrumb, 1 Local Business, 2 Organization), **somente quando as entidades são reais e elegíveis**. Ausência de unidade/oferta ou de agentes não autoriza fabricar itens para alcançar seis. Não existe garantia universal de 6 resultados por URL ou de exibição na SERP.
6. **Regression gate** — preservar tudo fora do JSON-LD se a mudança for schema-only; comparação byte a byte de HTML excluindo o bloco alterado; validar mídia, canonical e demais contratos como proteção de fronteira, sem alterar essas áreas.
7. **Release gate** — branch/PR, HEAD exato, CI, autorização consumidor, SHA merge, deployment READY em domínio, rollback e capturas **pós-publicação**; não confundir teste local/Preview com produção.
8. **Promotion gate (provedor)** — intake de evidência, teste em mais empreendimentos com fatos diferentes, revisão humana, decisão e versionamento. O piloto não promove automaticamente RESF-SCHEMA, C07 nem C17.

## 5. Anti-padrões observados

- Declarar `Nenhum item foi detectado` como ausência/falha de sintaxe do JSON-LD sem verificar se eram apenas tipos não elegíveis.
- Acrescentar entidades apenas para inflar a quantidade de resultados.
- Copiar endereço de um empreendimento para outro ou usar sede única para atender todas as unidades.
- Duplicar o hero ou substituir imagem do empreendimento por foto do corretor na hierarquia principal.
- Copiar um `FloorPlan` que pertence exclusivamente a outro produto.
- Emitir `ApartmentComplex.brand` só porque o Google Rich Results não avisa; Schema.org Validator identifica a incompatibilidade.
- Tratar `Brand` como intrinsecamente inválido e apagá-lo de `Product`/`Organization`.
- Produzir preço, `InStock`, rating, review, frete, prazo ou política de devolução para remover avisos opcionais.
- Dar por concluída a qualidade após `6 itens válidos` sem expandir e auditar conteúdo de cada item.

## 6. Fronteira de adoção e escopo

- Este arquivo é **aprendizado candidato do RESF**; não constitui adoção automática por MoreNumTegra.
- `RESF-SCHEMA`, `RESF-SEO`, `RESF-QA` permanecem `DEFERRED` no manifesto seletivo do consumidor até decisão separada.
- Não alterar outros empreendimentos, HTML visual, formulários, GTM, CRM, SEO editorial, mídia, UX ou preços por esta documentação.
- Para uma nova página, conduzir entrevista de fatos e escolher nós aplicáveis; distinguir `MISSING` de `NOT_APPLICABLE`.
- Estado e resultado do consumidor são válidos na data observada; podem variar se Google, preço, conteúdo ou indexação mudar.
