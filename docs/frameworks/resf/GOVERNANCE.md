# RESF Governance

## Ownership

Provider: `wagnerjfjunior/Blogs-sites-portais-seo`.

Consumers retain authority over product facts, commercial claims, brand, code, CMS, domain, DNS, deployment, analytics, CRM, campaigns, consent, risk and release.

## Lifecycle

Allowed states: `EXPERIMENTAL`, `CANDIDATE`, `RECOMMENDED`, `STABLE`, `DEPRECATED`, `SUPERSEDED`, `ARCHIVED`.

Documentation completeness does not promote maturity. Any lifecycle change requires a dedicated provider branch/PR, evidence, current SFJM gates and a formal Product Authority decision.

## Adoption

Adoption is explicit, version-bound and module-selective. The consumer manifest must pin an immutable provider SHA. An override changes the consumer implementation only; it does not modify the provider framework.

## Learning loop

`CONSUMER EVIDENCE -> EVIDENCE INTAKE -> CLASSIFICATION -> PATTERN CANDIDATE -> CONTROLLED REVALIDATION -> PROVIDER REVIEW -> LIFECYCLE DECISION -> VERSIONED UPDATE`

Every intake preserves consumer, repository SHA, date, evidence, limitation, conflicts, applicability and human decision.

## Anti-loop

Do not rewrite durable framework files merely because a PR becomes Ready, merges, a check changes state or an authorization is granted. Those are live lifecycle states.
