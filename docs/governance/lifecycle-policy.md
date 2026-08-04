# Política de lifecycle

1. A PR permanece Draft durante implementação e auditoria documental.
2. Após a última alteração, registre e congele o head.
3. Mudança no head invalida gates anteriores; mudança apenas na base exige revalidação de impacto pelo GPT4.
4. GPT0 emite `PASS`, `PASS_WITH_RESIDUAL_RISK`, `BLOCK` ou `INCONCLUSIVE`.
5. GPT4 valida base, head, commits, arquivos, checks, reviews, threads e mergeabilidade.
6. Ready exige autorização humana específica.
7. Sem mudança de head, a conferência pós-Ready limita-se a checks, reviews, threads e mergeabilidade.
8. Merge exige nova autorização humana com head esperado e método.
9. Após merge, confirme SHA da main e presença dos artefatos.
