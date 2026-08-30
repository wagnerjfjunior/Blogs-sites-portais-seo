# MoreNumTegra — Search Guidance — Prêmio Master Imobiliário 2026

## Status

`PROVIDER_SEARCH_GUIDANCE / CROSS_PROJECT / NO_CONSUMER_MUTATION_AUTHORITY`

## 1. Escopo

Orientação Search/SEO para transformar os reconhecimentos do Prêmio Master Imobiliário 2026 em argumento de autoridade e conversão no MoreNumTegra, preservando precisão factual e sem retirar o usuário da página comercial.

Consumer / Product Authority:

`wagnerjfjunior/MoreNumTegra`

Search provider:

`wagnerjfjunior/Blogs-sites-portais-seo`

Consumer implementation observado:

- PR #32 — `feat: destacar Prêmio Master Imobiliário 2026`
- base: `76f6d5c543173382803c42bba04d2e63554b2f14`
- head observado: `287793959a1da8667f042b8177d4476ad43e6821`
- superfícies: `src-greenn/blocks/01-html-inicial.html`, `src-greenn/moretegra.css`, `src-greenn/moretegra.js`

Estado de lifecycle é volátil e deve ser resolvido live. Este documento não autoriza mutação no consumer, Ready, merge, Vercel Production ou Green.

## 2. Evidência factual

Fonte externa primária:

SECOVI-SP — Conheça os vencedores do Prêmio Master Imobiliário 2026  
https://secovi.com.br/conheca-os-vencedores-do-premio-master-imobiliario-2026/

Observado em 2026-08-29:

1. `Profissional – Soluções Arquitetônicas`
   - Empresa: Tegra
   - Case no heading da fonte SECOVI-SP: `RIIO BY PIERO LISONI - O Rio com alma italiana`
   - Localização: Rio de Janeiro/RJ
   - Normalização de marca/copy: usar `RIIO by Piero Lissoni`; `LISONI` é preservado somente como transcrição do heading da fonte, não como grafia canônica da marca.

2. `Empreendimento – Qualificação Urbana`
   - Empresas: `Helbor | Toledo Ferrari | Tegra`
   - Case: `Caminhos da Lapa: redesenhando um bairro`
   - Localização: São Paulo/SP

O segundo reconhecimento é do case/masterplan Caminhos da Lapa. Não prova que cada condomínio/fase recebeu individualmente um prêmio autônomo.

## 3. Relação entre masterplan e produtos do catálogo

Fontes oficiais Tegra sustentam o vínculo de:

- Nova Vivere;
- Garden Design;
- Caminhos da Lapa Elo Duo;
- Reserva Caminhos da Lapa;

com o complexo/masterplan Caminhos da Lapa.

Portanto, é factual comunicar que esses empreendimentos fazem parte do Caminhos da Lapa premiado, desde que a copy não transforme o prêmio do masterplan em prêmio individual de cada torre.

## 4. Regra de conversão

MoreNumTegra é uma página de conversão. O reconhecimento deve aumentar confiança e clique, não desviar tráfego.

### Decisão

- NÃO colocar link outbound visível para SECOVI-SP no bloco comercial;
- manter a URL/fonte no repositório e na evidência interna para auditabilidade;
- usar o nome oficial do prêmio e das categorias na própria página;
- CTA do bloco deve permanecer dentro do funil MoreNumTegra: filtros, cards, WhatsApp ou formulário.

`PROVENANCE_INTERNAL != OUTBOUND_CTA_REQUIRED`

## 5. Copy recomendada

O termo `masterplan` sozinho tem baixa clareza para público geral. Ele pode aparecer como precisão técnica em texto de apoio, mas não deve ser o principal gatilho.

### Eyebrow

`PRÊMIO MASTER IMOBILIÁRIO 2026`

### Headline preferida

`Dois prêmios em 2026. Um deles está no seu próximo endereço.`

### Supporting copy

`A Tegra foi reconhecida em duas categorias do Prêmio Master Imobiliário 2026. Em São Paulo, o Caminhos da Lapa venceu em Qualificação Urbana — e você pode escolher entre empreendimentos que fazem parte desse complexo premiado.`

### Alternativa mais direta

`Caminhos da Lapa foi premiado. E você pode morar dentro desse projeto.`

Supporting:

`O complexo desenvolvido por Helbor, Toledo Ferrari e Tegra venceu o Prêmio Master Imobiliário 2026 em Qualificação Urbana. Conheça os empreendimentos disponíveis no MoreNumTegra.`

### Regra

Headline pode ser comercialmente forte. A precisão factual deve estar imediatamente no supporting copy.

## 6. Cards institucionais

Preferir:

- `RIIO BY PIERO LISSONI — Soluções Arquitetônicas`
- `Caminhos da Lapa — Qualificação Urbana`

Pode haver uma linha de impacto acima, como `Reconhecido pelo setor`, mas não substituir a categoria oficial por uma abstração que reduza Search/AEO/GEO citability.

## 7. Badge nos cards de Caminhos da Lapa

Evitar o badge isolado:

`PROJETO PREMIADO`

porque pode ser entendido como prêmio individual do empreendimento exibido.

### Copy curta recomendada

`PRÊMIO MASTER IMOBILIÁRIO 2026`

com segunda camada visível:

`Caminhos da Lapa · um bairro inteiro de opções`

### Copy expandida / accessible label

`Empreendimento integrante do Caminhos da Lapa, vencedor do Prêmio Master Imobiliário 2026 na categoria Qualificação Urbana.`

A palavra `masterplan` pode existir no tooltip, aria-label ou corpo, mas não precisa ser a única mensagem comercial.

## 8. Search / AEO / GEO

Relações factuais a preservar:

`Tegra -> Prêmio Master Imobiliário 2026 -> RIIO by Piero Lissoni -> Soluções Arquitetônicas`

`SOURCE_HEADING_TYPO_LISONI != CANONICAL_BRAND_SPELLING_LISSONI`

`Caminhos da Lapa -> Prêmio Master Imobiliário 2026 -> Qualificação Urbana -> Helbor + Toledo Ferrari + Tegra`

Para futuras páginas estáveis de empreendimento/Caminhos da Lapa, essa evidência poderá sustentar:

- seção factual curta sobre o prêmio;
- relação entre masterplan e empreendimentos;
- internal linking;
- conteúdo de resposta quando útil;
- structured data apenas quando houver tipo adequado e conteúdo visível correspondente.

Não criar schema artificial de prêmio, review ou rating.

## 9. Estado reconciliado da PR #32

No head observado `287793959a1da8667f042b8177d4476ad43e6821`:

- o bloco institucional usa o nome oficial `Prêmio Master Imobiliário 2026`;
- o badge curto genérico `PROJETO PREMIADO` foi substituído pelo nome oficial completo do prêmio;
- a segunda camada comunica `Caminhos da Lapa · um bairro inteiro de opções`;
- Nova Vivere aparece em dois cards de conversão na mesma home: 72 m² no início e 105 m² no meio;
- o card 105 m² usa `R$ 1.129.900 à vista*` com disclaimer próximo e CTA interno;
- não há outbound link para SECOVI-SP no bloco comercial;
- a descrição da PR foi reconciliada com o diff observado.

## 10. Fronteira de autoridade

### MoreNumTegra / Product Authority

Responsável por:

- design visual;
- geometria/cor/posição do badge;
- CTA;
- HTML/CSS/JS;
- Vercel;
- Green;
- risco comercial e publicação.

### Search provider

Responsável por:

- precisão factual;
- copy Search/AEO/GEO;
- uso de entidades/categorias;
- guardrail de claim;
- estratégia de conversão Search;
- evidência/provenance interna.

`SEARCH_GUIDANCE != CONSUMER_IMPLEMENTATION_AUTHORITY`

## 11. Verdict Search sobre a implementação observada

`PASS_WITH_RESIDUAL_RISK`

Escopo:

`SEARCH_APPROVAL_FOR_PREVIEW_AND_LIFECYCLE_PROGRESS_OF_MORENUMTEGRA_PR32_AT_OBSERVED_HEAD`

Passa porque:

1. o nome oficial do prêmio está visível;
2. a relação Caminhos da Lapa / Qualificação Urbana permanece factual;
3. a headline é comercial, mas o supporting copy preserva precisão;
4. o usuário não é enviado para fora do funil;
5. a condição à vista está associada à unidade e ao disclaimer;
6. a provenance está versionada no consumer.

Risco residual:

- disponibilidade e condição comercial da unidade 708 são voláteis e precisam ser reconfirmadas antes da publicação Green;
- Search approval não substitui Product Authority, lifecycle, merge ou publicação.

Nenhuma autorização de merge ou Green é criada por este verdict.
