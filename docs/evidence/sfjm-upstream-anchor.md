# Evidência da âncora upstream do SFJM

- Coletada em: 2026-08-06
- Método: leitura autenticada e não destrutiva pelo conector GitHub
- Repositório upstream: `wagnerjfjunior/StopJuniorMode`
- Revisão congelada: `d03d477c3b329aa973a38ec4e949c249fa017929`
- Caminho upstream: `docs/CANONICAL_BOOTSTRAP_PROTOCOL.md`
- Git blob SHA observado: `7befd02533aad6c2df5544c7307e4a66dce28844`
- Tamanho do conteúdo decodificado: `7960` bytes UTF-8
- Cópia local imutável: `docs/references/sfjm/CANONICAL_BOOTSTRAP_PROTOCOL.md.gz.b64`
- Codificação da cópia: conteúdo original UTF-8 comprimido com gzip determinístico (`mtime=0`) e codificado em Base64

## Critério de verificação

O validador deve:

1. ler a cópia local;
2. remover espaços em branco da representação Base64;
3. decodificar Base64;
4. descomprimir gzip;
5. calcular o Git blob SHA com `sha1(b"blob " + tamanho + b"\0" + conteúdo)`;
6. exigir correspondência exata com `7befd02533aad6c2df5544c7307e4a66dce28844`;
7. exigir correspondência entre o conteúdo verificado e a âncora declarada em `config/sfjm.yaml`.

A cópia local é evidência versionada para auditoria. A fonte normativa upstream continua sendo o repositório, revisão e caminho declarados acima.
