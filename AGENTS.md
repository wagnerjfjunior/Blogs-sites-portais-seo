# Instruções persistentes do repositório

1. O GitHub em `wagnerjfjunior/Blogs-sites-portais-seo` é a fonte canônica project-local.
2. Use o nome público `Ecossistema de Blogs, Sites, Portais e SEO` e o ID técnico `blogs-sites-portais-seo`.
3. A arquitetura universal de especialistas pertence ao SES; novo roteamento usa `ROLE -> ARCHETYPE_ID` via Project Adapter e `config/specialists.yaml`.
4. Labels `GPT0`–`GPT8` são continuidade/história e não identidade canônica para novo trabalho.
5. Toda nova conversa ou retomada começa por `bootstrap/BOOTSTRAP_CANONICO.md` e segue sua ordem mínima.
6. `docs/NEXT_SAFE_ACTION.md` e `config/sfjm.yaml` definem uma única máquina autoritativa e devem corresponder exatamente.
7. Resumos no bootstrap, handoff e status são derivados e comparados deterministicamente.
8. Estados open, Draft, Ready, closed e merged são resolvidos live e sempre produzem transição calculável.
9. Se houver divergência material, `BLOCK` ou `INCONCLUSIVE`, pare antes de mutações.
10. A tentativa mais recente do workflow canônico para o head exato é a única autoridade de CI.
11. O gate `documentation_audit` é vinculado ao head; o gate de lifecycle SFJM é vinculado ao head e à base.
12. Autorizações de Ready e merge são separadas e vinculadas ao head e à base; merge só aceita autorização concedida depois de Ready.
13. Mudança de head invalida gates e autorizações; mudança somente de base invalida lifecycle governance e autorizações de transição.
14. Toda mudança canônica ocorre por branch e PR; escrita direta em `main` é proibida.
15. A Action GitHub project-local inicial é somente leitura; não simule mutações.
16. Não invente fatos, métricas, IDs, URLs, checks, reviews, evidências ou autorizações.
17. Diferencie fato, decisão, proposta, hipótese, risco residual e falta de acesso.
18. Use somente `PASS`, `PASS_WITH_RESIDUAL_RISK`, `BLOCK` e `INCONCLUSIVE`.
19. Workflow de PR valida `github.event.pull_request.head.sha`, não o merge ref.
20. O validador confere estruturalmente `if`, `uses`, `ref`, comandos e ordem dos passos do workflow.
21. Validações repetidas devem ignorar `__pycache__`, `.pyc` e `.pyo`.
22. Não exponha tokens, segredos ou credenciais.
23. Links pagos são publicidade; não use esquemas manipulativos.
24. `CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED != PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE`.
25. Builders legados não são aposentados por rename ou adoção; retirement exige equivalência, testes/runtime proof e autorização explícita por Builder.
26. Local SEO e Authority & Digital PR não podem ser tratados como archetypes ativos/adotados enquanto o SES os mantiver como TARGET/certification pending.
27. Monetização permanece exceção project-local até replacement SES canônico.
28. O SFJM local é operacional; não execute scoring, benchmark ou cenário sintético sem protocolo próprio.
29. Não atualize registros por conclusão de gate, metadata, autorização ou estado terminal já representado.
30. Execute `python scripts/validate_repository.py`, `python -m unittest discover -s tests -p "test_*.py"` e `python scripts/validate_builder_action.py` antes de Ready ou merge.
