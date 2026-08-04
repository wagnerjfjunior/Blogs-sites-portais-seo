# Matriz de autorizações

| Ação | Responsável por validar | Autoridade para autorizar | Regra |
|---|---|---|---|
| Alterar documentação em branch | Especialista aplicável | Wagner | Escopo explícito |
| Auditoria documental | GPT0 | Não se aplica | READ_ONLY |
| Validação de lifecycle | GPT4 | Não se aplica | READ_ONLY |
| Marcar Ready | GPT4 pode executar | Wagner | Autorização vinculada ao head |
| Merge | GPT4 pode executar | Wagner | Autorização separada vinculada ao head |
| Configurar Builder | Executor designado | Wagner | Um GPT por vez, evidência registrada |
| Alterar compartilhamento | Executor designado | Wagner | Manter `Apenas para mim` |
| Criar Action mutável | GPT4 propõe | Wagner | PR separada e revisão específica |

## Forma mínima da autorização

```text
AÇÃO: AUTHORIZE_READY | AUTHORIZE_MERGE | AUTHORIZE_BUILDER_UPDATE
REPOSITÓRIO: wagnerjfjunior/Blogs-sites-portais-seo
OBJETO: PR ou GPT
HEAD/FONTE: SHA exato
ESCOPO: ação autorizada
EXCLUSÕES: ações não autorizadas
```

Ready nunca implica merge. Configuração do Builder nunca implica publicação pública.
