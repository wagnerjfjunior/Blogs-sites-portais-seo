# Provider Framework Registry

This file is the durable discovery index for provider-local frameworks. Inclusion here means only that a framework artifact exists in this repository; it does not imply consumer adoption, runtime authority, lifecycle promotion, deployment or publication.

## Registered frameworks

| Framework | Version | Variant | Lifecycle | Manifest | Evidence origin |
|---|---:|---|---|---|---|
| RESF — Real Estate Search Framework | v1 | Search-to-Lead | `CANDIDATE` | `docs/frameworks/resf/v1/MANIFEST.yaml` | `wagnerjfjunior/ProjetosCyrela@193c5c3245019b99d3a3070b3e485f48796e7e37/docs/architecture/resf-v1-origin/` |

## Governance

`FRAMEWORK_REGISTRATION != CONSUMER_ADOPTION`

`FRAMEWORK_REGISTRATION != PROJECT_AUTHORITY`

`CANDIDATE != RECOMMENDED`

Consumers must explicitly select, override, defer or reject modules under their own project authority. Lifecycle transitions remain governed by the provider repository and require the applicable gates and authorizations.
