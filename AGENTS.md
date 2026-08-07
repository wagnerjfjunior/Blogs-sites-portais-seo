# Instruções persistentes do repositório

1. O GitHub em `wagnerjfjunior/Blogs-sites-portais-seo` é a fonte canônica.
2. Use o nome público `Ecossistema de Blogs, Sites, Portais e SEO` e o ID técnico `blogs-sites-portais-seo`.
3. Toda nova conversa ou retomada começa por `bootstrap/BOOTSTRAP_CANONICO.md` e segue sua ordem mínima.
4. `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml` definem uma única máquina autoritativa e devem corresponder exatamente.
5. Resumos no bootstrap, handoff e status são derivados e comparados deterministicamente.
6. Estados open, Draft, Ready, closed e merged são resolvidos live e sempre produzem transição calculável.
7. Se houver divergência material, `BLOCK` ou `INCONCLUSIVE`, pare antes de mutações.
8. A tentativa mais recente do workflow canônico para o head exato é a única autoridade de CI.
9. GPT0 é vinculado ao head; GPT4 é vinculado ao head e à base.
10. Autorizações de Ready e merge são separadas e vinculadas ao head e à base; merge só aceita autorização concedida depois de Ready.
11. Mudança de head invalida gates e autorizações; mudança somente de base invalida GPT4 e autorizações de transição.
12. Toda mudança canônica ocorre por branch e PR; escrita direta em `main` é proibida.
13. A Action GitHub inicial é somente leitura; não simule mutações.
14. Não invente fatos, métricas, IDs, URLs, checks, reviews, evidências ou autorizações.
15. Diferencie fato, decisão, proposta, hipótese, risco residual e falta de acesso.
16. Use somente `PASS`, `PASS_WITH_RESIDUAL_RISK`, `BLOCK` e `INCONCLUSIVE`.
17. Workflow de PR valida `github.event.pull_request.head.sha`, não o merge ref.
18. O validador confere estruturalmente `if`, `uses`, `ref`, comandos e ordem dos passos do workflow.
19. Validações repetidas devem ignorar `__pycache__`, `.pyc` e `.pyo`.
20. Não exponha tokens, segredos ou credenciais.
21. Links pagos são publicidade; não use esquemas manipulativos.
22. O SFJM local é operacional; não execute scoring, benchmark ou cenário sintético sem protocolo próprio.
23. Não atualize registros por conclusão de gate, metadata, autorização ou estado terminal já representado.
24. Execute `python scripts/validate_repository.py`, `python -m unittest discover -s tests -p "test_*.py"` e `python scripts/validate_builder_action.py` antes de Ready ou merge.
