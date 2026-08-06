# Instruções persistentes do repositório

1. O GitHub em `wagnerjfjunior/Blogs-sites-portais-seo` é a fonte canônica.
2. Use o nome público `Ecossistema de Blogs, Sites, Portais e SEO` e o ID técnico `blogs-sites-portais-seo`.
3. Toda nova conversa ou retomada começa por `bootstrap/BOOTSTRAP_CANONICO.md` e segue sua ordem mínima de leitura.
4. `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml` definem a única máquina autoritativa de próxima transição.
5. Resumos no bootstrap, handoff e status são derivados, devem permanecer idênticos ao resumo estruturado e não autorizam execução.
6. Se houver divergência material entre registros, pare e reconcilie antes de agir.
7. Leia integralmente `config/project.yaml`, `config/gpts.yaml`, o contrato, a skill e o manifesto do GPT aplicável antes de alterar sua configuração.
8. Não faça análise parcial quando o pedido exigir leitura integral.
9. Não invente fatos, métricas, IDs, URLs, volumes, resultados, checks, reviews ou evidências.
10. Diferencie fato confirmado, decisão, proposta, hipótese, risco residual e falta de acesso.
11. Use apenas os vereditos oficiais: `PASS`, `PASS_WITH_RESIDUAL_RISK`, `BLOCK`, `INCONCLUSIVE`.
12. Toda mudança canônica deve ocorrer por branch e Pull Request.
13. Escrita direta na `main` é proibida.
14. Ready e merge exigem autorizações humanas explícitas e separadas, vinculadas ao head exato.
15. Mudança de head invalida gates e autorizações de outro head.
16. A Action GitHub inicial é somente leitura; não simule mutações.
17. Não exponha tokens, segredos ou credenciais.
18. Links pagos são publicidade; não use esquemas manipulativos.
19. O SFJM local é operacional; não execute scoring, benchmark, cenário sintético ou adjudicação sem protocolo e autorização próprios.
20. Não atualize registros versionados por simples conclusão de gate, mudança Draft/Ready, concessão ou consumo de autorização no mesmo head; atualize somente política, estrutura, bloqueio ou evidência durável.
21. Execute `python scripts/validate_repository.py`, `python -m unittest discover -s tests -p "test_*.py"` e `python scripts/validate_builder_action.py` antes de propor Ready ou merge.
