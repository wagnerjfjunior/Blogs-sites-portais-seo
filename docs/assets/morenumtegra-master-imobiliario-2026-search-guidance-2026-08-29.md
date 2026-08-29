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
- base: `4202356b6199fef720919eb639168aa4158ae3d8`
- head observado: `38a8c20de236c9fda75b0b57236df94592803c1a`
- superfícies: `src-greenn/blocks/01-html-inicial.html`, `src-greenn/moretegra.css`, `src-greenn/moretegra.js`

Estado de lifecycle é volátil e deve ser resolvido live. Este documento não autoriza mutação no consumer, Ready, merge, Vercel Production ou Green.

## 2. Evidência factual

Fonte externa primária:

SECOVI-SP — Conheça os vencedores do Prêmio Master Imobiliário 2026  
https://secovi.com.br/conheca-os-vencedores-do-premio-master-imobiliario-2026/

Observado em 2026-08-29:

1. `Profissional – Soluções Arquitetônicas`
   - Empresa: Tegra
   - Case: `RIIO BY PIERO LISONI - O Rio com alma italiana`
   - Localização: Rio de Janeiro/RJ

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

- `RIIO BY PIERO LISONI — Soluções Arquitetônicas`
- `Caminhos da Lapa — Qualificação Urbana`

Pode haver uma linha de impacto acima, como `Reconhecido pelo setor`, mas não substituir a categoria oficial por uma abstração que reduza Search/AEO/GEO citability.

## 7. Badge nos cards de Caminhos da Lapa

Evitar o badge isolado:

`PROJETO PREMIADO`

porque pode ser entendido como prêmio individual do empreendimento exibido.

### Copy curta recomendada

`CAMINHOS DA LAPA · PREMIADO 2026`

ou, se o espaço for muito restrito:

`MASTER 2026 · CAMINHOS DA LAPA`

### Copy expandida / accessible label

`Empreendimento integrante do Caminhos da Lapa, vencedor do Prêmio Master Imobiliário 2026 na categoria Qualificação Urbana.`

A palavra `masterplan` pode existir no tooltip, aria-label ou corpo, mas não precisa ser a única mensagem comercial.

## 8. Search / AEO / GEO

Relações factuais a preservar:

`Tegra -> Prêmio Master Imobiliário 2026 -> RIIO by Piero Lissoni -> Soluções Arquitetônicas`

`Caminhos da Lapa -> Prêmio Master Imobiliário 2026 -> Qualificação Urbana -> Helbor + Toledo Ferrari + Tegra`

Para futuras páginas estáveis de empreendimento/Caminhos da Lapa, essa evidência poderá sustentar:

- seção factual curta sobre o prêmio;
- relação entre masterplan e empreendimentos;
- internal linking;
- conteúdo de resposta quando útil;
- structured data apenas quando houver tipo adequado e conteúdo visível correspondente.

Não criar schema artificial de prêmio, review ou rating.

## 9. Finding de reconciliação da PR #32

No head observado:

- o corpo da PR #32 declara badge em Nova Vivere, Caminhos da Lapa Elo Duo e Reserva;
- o JavaScript também aplica badge em Garden Design.

Garden Design tem vínculo factual com o complexo. Portanto, o problema não é elegibilidade factual; é a divergência documental:

`PR_DESCRIPTION != IMPLEMENTATION_DIFF`

A PR do consumer deve reconciliar a descrição com os quatro cards antes do fechamento de lifecycle.

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

`BLOCK`

Escopo do BLOCK:

`SEARCH_APPROVAL_FOR_GREEN_PUBLICATION_OF_MORENUMTEGRA_PR32_AT_OBSERVED_HEAD`

Motivos:

1. o badge curto `PROJETO PREMIADO` pode superestimar o prêmio do masterplan como prêmio individual;
2. a copy deve ser ajustada para conversão sem depender de `masterplan` como mensagem principal;
3. a descrição da PR deve refletir os quatro cards efetivamente marcados.

Não é necessário adicionar link outbound para SECOVI-SP. A provenance permanece internamente versionada.

Nenhuma mutação no consumer foi executada pelo provider.
