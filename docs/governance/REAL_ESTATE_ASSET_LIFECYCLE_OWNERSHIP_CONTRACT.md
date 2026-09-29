# Real Estate Asset Lifecycle Ownership Contract

- Project: Ecossistema de Blogs, Sites, Portais e SEO
- Scope: real-estate sibling assets with durable entity surfaces and current commercial surfaces
- Status: CANDIDATE
- Authority: Product Authority for business-state predicates; consumer repositories for implementation/runtime
- Mutation authority: NONE

## 1. Purpose

Define stable ownership semantics for real-estate entities whose current developer-commercial role changes over time while the underlying project/place entity remains useful and searchable.

This contract prevents normal lifecycle changes from forcing recurring architecture redesign.

## 2. Core concepts

### Durable entity property

The portfolio surface responsible for long-term entity/context value such as identity, history, master-development membership, relationship among phases and stable place information.

### Active commercial owner

The governed surface responsible for current developer-commercial intent such as availability, current price, conditions, active units, sales CTA and conversion.

### External official source

A first-party or institutional source outside this portfolio that can provide evidence for official facts. It is evidence, not a portfolio asset and not an internal ownership node.

## 3. Invariants

```text
DURABLE_ENTITY_PROPERTY != ACTIVE_COMMERCIAL_OWNER

ENTITY_MEMBERSHIP = STABLE_UNLESS_GOVERNED_FACT_CHANGES
COMMERCIAL_OWNERSHIP = LIFECYCLE_DEPENDENT
URL_DISPOSITION = SEPARATE_DECISION

COMMERCIAL_STATE != PHYSICAL_ENTITY_STATE
SOLD_OUT != AUTOMATIC_PAGE_RETIREMENT
DELIVERED != ACTIVE_INVENTORY
SECONDARY_MARKET_DEMAND != DEVELOPER_INVENTORY
COMMERCIAL_EXCEPTION != GENERAL_STOCK_REOPENING

LIFECYCLE_TRANSITION != AUTOMATIC_RUNTIME_OR_SEARCH_MUTATION
```

## 4. Commercial state

Canonical concepts that must be representable:

- `PRE_COMMERCIAL`
- `ACTIVE_COMMERCIAL`
- `COMMERCIAL_EXCEPTION`
- `COMMERCIAL_CLOSED`

The exact Product Authority predicate for entering or leaving these states is consumer/project specific and must not be inferred from page wording alone.

## 5. Physical/entity state

Separately represent:

- `FUTURE`
- `LAUNCHED`
- `UNDER_DEVELOPMENT`
- `DELIVERED`
- `ESTABLISHED`

A project can be `DELIVERED` and `ACTIVE_COMMERCIAL` simultaneously. A project can be `UNDER_DEVELOPMENT` and already `COMMERCIAL_CLOSED`.

## 6. Activation and closure guards

### Commercial activation guard

A commercial surface may become active only when governed evidence establishes sufficient present-tense developer commercialization.

At minimum, do not infer activation merely from:

- a planned future phase;
- historical launch copy;
- a third-party listing;
- prior availability.

### Commercial closure guard

Ownership review should be triggered by a governed commercial condition, preferably the end of developer-commercial responsibility rather than a visual `sold out` label alone.

Product Authority must define the exact predicate, including treatment of:

- zero developer inventory;
- official commercial closure;
- cancelled/returned units;
- narrow exception inventory.

## 7. Responsibility matrix

| Commercial / entity condition | Durable entity property | Active commercial owner | Allowed durable content | Allowed commercial content |
|---|---|---|---|---|
| Future / pre-commercial | may establish verified constituent relationship | none by default | verified name/context/relationship | none without activation guard |
| Launch / active sales | keeps stable entity/master context | governed commercial surface | durable facts, history, relationship, concise summary | current price/availability/plants/CTA if governed |
| Commercial exception | keeps entity role | exact owner only for the narrow validated exception | stable entity/history | exception-specific facts only |
| Commercial closed, not delivered | becomes primary long-term context | none by default | sold/closed truth, history, specs/context | no general active-inventory claims |
| Delivered with active inventory | keeps delivered/entity role | governed commercial surface | delivery/entity context | current remaining inventory only if verified |
| Established | primary durable representation | none for developer inventory by default | identity/history/place/relationships | no developer-sales claims without new authority |

## 8. Search and URL disposition

A state change does not by itself decide whether a URL:

- remains live;
- changes content role;
- becomes noindex;
- redirects;
- changes canonical target;
- leaves a sitemap;
- is deleted.

Technical disposition requires URL-level evidence, replacement equivalence, Search demand/backlinks and explicit authorization.

Preferred order:

```text
BUSINESS STATE VERIFIED
-> RESPONSIBILITY SET UPDATED
-> SEMANTIC ROLE ADJUSTED
-> SEARCH PERFORMANCE OBSERVED
-> TECHNICAL CONSOLIDATION ONLY IF JUSTIFIED
```

## 9. Sold and delivered pages

A sold/delivered project can remain useful for:

- project/entity identity;
- specifications;
- floor plans;
- address/history;
- delivery/status research;
- resident/research context;
- legitimate historical Search demand.

The page must not imply normal developer inventory when none exists.

## 10. Secondary market

Secondary-market demand does not reactivate developer-commercial ownership.

Unless a consumer explicitly adopts an authorized resale business model, do not convert resale demand into developer inventory claims or active developer-sales CTAs.

## 11. Cross-asset links

Cross-asset links are allowed when they express a real entity/user relationship.

Examples:

- master/context property -> active exact commercial project;
- exact commercial project -> master-development context.

Do not create exact-match reciprocal networks, sitewide link quotas or duplicate surfaces for PageRank transfer.

## 12. Required state fields

The ecosystem model must be able to record, directly or equivalently:

- `durable_entity_property`
- `commercial_owner`
- `commercial_state`
- `physical_entity_state`
- `commercial_activation_guard`
- `commercial_closure_guard`
- `exception_inventory_guard`
- `master_development_membership`
- `verified_at` / evidence freshness
- `transition_authority`

## 13. Actions that never happen automatically

A lifecycle state transition must not itself cause:

- redirect;
- page deletion;
- canonical-target change;
- sitemap removal;
- URL reuse;
- content wipe;
- domain migration;
- deindexing;
- form removal/addition;
- conversion CTA activation;
- availability reactivation;
- cross-domain runtime ownership transfer.

Each action requires its own evidence, lifecycle gate, authorization and rollback semantics where applicable.

## 14. Caminhos da Lapa application

For the current sibling-asset model:

- `caminhosdalapategra.com.br` is the portfolio durable specialist property for Caminhos da Lapa context and constituent continuity;
- `moretegra.com.br` remains the current Tegra commercial conversion hub for governed active project inventory;
- `caminhosdalapaoficial.com.br` is an external official/institutional reference, not a portfolio asset.

This application does not authorize implementation.

## 15. Product Authority decisions still required

Before automating routine transitions, Product Authority must define:

1. exact commercial closure predicate;
2. returned/cancelled/exception-unit semantics;
3. minimum commercial activation evidence;
4. whether `SOLD_OUT` and `COMMERCIAL_CLOSED` are distinct in each consumer;
5. historical-page retention policy;
6. whether any resale business model exists.

Until then, uncertain states fail closed.
