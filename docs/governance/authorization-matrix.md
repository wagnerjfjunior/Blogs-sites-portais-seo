# Matriz de autorização

| Ação | Validador | Autorizador | Executor |
|---|---|---|---|
| Alterar documentação em branch | responsável técnico | Wagner define o escopo | executor autorizado |
| Auditar documentação | GPT0 | não aplicável | GPT0 READ_ONLY |
| Validar lifecycle | GPT4 | não aplicável | GPT4 READ_ONLY |
| Marcar Ready | GPT4 valida | Wagner autoriza explicitamente | GPT4 ou Wagner |
| Fazer merge | GPT4 valida head final | Wagner autoriza separadamente | GPT4 ou Wagner |
| Configurar Builder | contrato e checklist | Wagner | Wagner ou executor autorizado |
| Alterar compartilhamento | verificação humana | Wagner | Wagner |
| Criar SFJM | proibido neste bootstrap | exige autorização futura específica | não aplicável |

Autorização deve identificar repositório, PR, head e ação. Uma autorização não implica outra.
