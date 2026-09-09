# Provider Framework Registry

This is the durable discovery index for provider-local frameworks. Registration means the framework exists; it does not imply consumer adoption, runtime authority, deployment, publication or lifecycle promotion.

## Registered frameworks

| Framework | Version | Variant | Lifecycle | Human entrypoint | AI entrypoint | Manifest |
|---|---:|---|---|---|---|---|
| RESF — Real Estate Search Framework | v1 | Search-to-Lead | `CANDIDATE` | `docs/frameworks/resf/README.md` | `docs/frameworks/resf/AI_INSTRUCTIONS.md` | `docs/frameworks/resf/v1/MANIFEST.yaml` |

## Discovery rule

When a task concerns a real-estate digital asset:

1. read `docs/frameworks/resf/README.md`;
2. resolve `docs/frameworks/resf/CURRENT.md`;
3. resolve the consumer repository and its adoption manifest;
4. execute only adopted modules;
5. preserve provider/consumer authority.

When the domain is not real estate, RESF is not automatically applicable.

## Governance

`FRAMEWORK_REGISTRATION != CONSUMER_ADOPTION`

`FRAMEWORK_REGISTRATION != PROJECT_AUTHORITY`

`CANDIDATE != RECOMMENDED`

Consumers may adopt, override, defer or reject modules under their own authority. The provider lifecycle remains governed by this repository's SFJM and requires explicit transition authority.
