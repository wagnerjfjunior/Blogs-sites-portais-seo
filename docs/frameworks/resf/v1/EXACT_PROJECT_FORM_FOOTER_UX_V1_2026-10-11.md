# RESF — Requisito 04 do padrão único: UX e CSS de formulário e rodapé — V1

**Estado:** CANDIDATE/DRAFT · 11/10/2026  
**Referência visual e de experiência:** `MoreNumTegra/src-greenn/empreendimentos/aria-higienopolis/index.html`.  
**Aplicação controlada:** `MoreNumTegra` PR #388, **Draft, não publicada**.  

## 1. Não é um novo padrão independente

Este é o **requisito 04 do padrão único RESF de construção de páginas de empreendimentos**. A seção comercial de captação e o rodapé devem ter identidade coerente, experiência mobile-first, navegação por toque, foco acessível e leitura clara. O Ária Higienópolis é a **referência de UX/CSS**, não fonte de dados para outros produtos. Não copiar endereços, preços, nomes, mapas, ofertas ou informações comerciais do Ária.

## 2. Seção do formulário — referência Ária

- Bloco com fundo claro, título e orientação de atendimento hierarquizados, formulário em **cartão branco**, borda sutil, raio de canto generoso e sombra discreta.
- Labels visíveis; inputs/selects com altura de toque adequada (referência: `min-height:48px`), bordas completas, cantos arredondados; foco visível em amarelo Tegra.
- **Mobile-first**: uma coluna em telas pequenas; duas colunas somente quando couber sem perder legibilidade; campos extensos podem ocupar linha inteira. Não criar rolagem horizontal.
- Botão primário **amarelo Tegra #EBB92E**, área de toque adequada (referência: `min-height:50px`), contraste e estado de desabilitado/“Enviando…” visíveis.
- Estados de validação, falha de rede, erro e sucesso preservados; `aria-live` e mensagens acessíveis. Não ocultar erros no CSS.
- Formulário da V1 **não pode ser visualmente padronizado às custas da integração**: preservar `id="moretegra-lead-form"`, `data-moretegra-lead-form`, nomes/IDs de campos, `tenant_id=313`, `form_id=46`, título, honeypot, validação de telefone/e-mail, runtime/atribuição, submissão nativa conforme contrato vigente. Não introduzir segredos, backend ou bibliotecas pesadas.
- Preservar informação de privacidade e consentimento válidos, sem afirmar comportamento de tracking que não esteja verificado. Não copiar automaticamente todos os textos do Ária.

## 3. Rodapé — referência Ária

- Fundo escuro, tipografia de leitura confortável, espaçamentos consistentes, logo Tegra **real**, links de alto contraste e hierarquia clara entre apresentação, ressalvas comerciais, endereço e contato profissional.
- Preservar marcadores do padrão jurídico/comercial: `data-mnt-commercial-footer`, `data-mnt-footer-address` e conteúdo obrigatório do consumidor.
- O endereço exato **do respectivo empreendimento** permanece no rodapé comercial conforme regra de localização da V1; nunca importar endereço do Ária para outros empreendimentos.
- Manter CRECI, telefone, identidade/URL oficial de atendimento, links úteis e ressalvas sobre preço de referência, disponibilidade e condições, com fatos atualizados e aprovados.
- O footer não deve colidir com CTAs fixos nem ficar encoberto por barra de privacidade no mobile.

## 4. Portabilidade e CSS

- Priorizar **HTML semântico, CSS e JS vanilla**. Estilos devem ser reaproveitáveis com classes/escopo próprios, evitando seletores genéricos que afetem galerias, hero, mapas, catálogos e formulários de outras páginas.
- Não importar stylesheet global de outra página se isso provocar mudanças colaterais; se necessário, usar CSS escopado e migrar depois para componente/arquivo compartilhado com testes.
- Preservar desempenho e acessibilidade: contraste, foco, tamanho dos alvos, comportamento teclado/toque, preferência por redução de movimento; validar resoluções móveis e desktop antes do merge.
- Respeitar a política de produção Greenn/Vercel e a estabilidade do Form 46; alterações cosméticas **não autorizam** refatoração de eventos de lead, tracking, integrações ou dados.

## 5. Gates de homologação

| Gate | Aceite |
|---|---|
| Paridade UX | Aparência funcional com o Ária: formulário branco, inputs visíveis, botão amarelo arredondado, footer escuro |
| Mobile | 320/375/390px sem overflow, campos legíveis e acessíveis; desktop sem perda de hierarquia |
| Funcional | Submit, validação, mensagens, duplo clique, falha de rede e sucesso compatíveis com a implementação aprovada e ambiente seguro de teste |
| Contrato | `tenant_id`, `form_id`, `name`, `id`, `data-*`, runtime de Form 46 e captura/atribuição intactos |
| Comercial | Endereço **deste produto**, CRECI, telefone, disclaimers e identidade preservados |
| Regressão | Outras seções (hero, catálogo, imagens, FAQ, JSON-LD, SEO metadata) não alteradas inadvertidamente |
| Release | Branch, PR, CI, autorização, deployment SHA + rollback, revisão mobile real e teste humano de formulário permitido |

## 6. Evidência registrada

- Ária Higienópolis: referência de markup/formulário `.mt-section-head`, `.mt-local-form`, `.mt-field`, `.mt-form-grid`, `.mt-lead-submit` e footer `.mt-footer-standard`, `.mt-footer-contact`.
- Ampère Brooklin: **PR #388 em Draft** adapta sua seção de formulário/footer com CSS escopado, mantém dados e runtime do projeto, e inclui `scripts/validate-ampere-form-footer-aria-ux.mjs` e CI dedicados.
- A documentação **não** constitui prova de publicação ou de testes visuais manuais. O resultado só passa a `PRODUCTION_VALIDATED` após merge/deployment e aceite responsivo/comportamental com evidências.

**Relação com os demais requisitos:** 01 JSON-LD, 02 sinais de imagens para busca, 03 FAQ estratégico SEO. Formulário e footer formam **um único quarto requisito de UX/CSS**, não um padrão alternativo.
