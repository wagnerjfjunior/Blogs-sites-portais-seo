# RESF — Canonical Consumption Procedure

RESF v1 is a selective real-estate Search-to-Lead framework. The consumer owns implementation and runtime.

## 0–25 canonical process

| Step | Objective | Minimum output/evidence | Blocker | Default owner | Completion | Authorization |
|---:|---|---|---|---|---|---|
| 0 | Project and portfolio fit | applicability decision | non-real-estate or redundant asset | architecture / seo_strategy | fit classified | consumer decision |
| 1 | Facts / claim registry | governed claims with sources/effective dates | material facts unresolved | product authority | claims classified | consumer |
| 2 | Market and search research | demand/intent evidence | no evidence for material search thesis | seo_strategy | evidence recorded | read-only unless external spend/action |
| 3 | Search contract | canonical intent owner/query families | intent collision unresolved | seo_strategy | C03 satisfied | consumer |
| 4 | Information architecture | page hierarchy/roles | unresolved cannibalization | architecture | C04 satisfied | consumer |
| 5 | Page contract | page type/entity/H1/actions | page owner unclear | architecture | C05 satisfied | consumer |
| 6 | Entity + schema contract | factual graph ownership | facts/schema source unresolved | technical_seo | C07 satisfied | consumer |
| 7 | Content architecture | decision-useful factual content plan | facts/intent incomplete | content_semantic_seo | C06 satisfied | consumer |
| 8 | Internal linking contract | semantic link plan | circular/manipulative linking | content_semantic_seo | C08 satisfied | consumer |
| 9 | UX + mobile + performance | interaction/performance plan | critical mobile/accessibility issue | ux_ui / technical_seo | C09/C10 satisfied | consumer |
| 10 | Conversion architecture | primary/secondary action semantics | action destination unknown | ux_ui / product authority | conversion defined | consumer |
| 11 | Tracking contract | event/destination/dedup semantics | lead validity/event identity unknown | seo_analytics_growth | C11 satisfied | consumer |
| 12 | Form + CRM contract | capture/handoff semantics | CRM destination or success condition unknown | consumer + analytics | C12 satisfied | consumer |
| 13 | Consent/privacy review | destination gating/PII policy | material privacy/security gap | application_security | C14 satisfied | consumer/risk authority |
| 14 | Paid media contract when applicable | conversion owner/query/attribution map | conversion not validated or spend not authorized | paid_search_sem | C13 satisfied | separate spend/publication authority |
| 15 | Build | consumer implementation | design contracts incomplete | consumer engineering/CMS | implementation artifact | mutation authority |
| 16 | Preview | bounded review surface | unsafe/global side effects | consumer | preview evidence | deploy/preview authority |
| 17 | Technical/content QA | canonical/content/schema checks | P0/P1 defect | technical/content owners | evidence recorded | read-only QA |
| 18 | Mobile QA | independent target-device validation | P0/P1 mobile defect | ux_ui | mobile evidence | read-only QA |
| 19 | Tracking/lead QA | valid event + lead delivery evidence | semantic/delivery failure | analytics/consumer | end-to-end evidence | runtime test authority |
| 20 | Regression | known-good baseline retained | regression P0/P1 | QA | regression evidence | read-only QA |
| 21 | Release decision | P0/P1 adjudication | material unresolved blocker | product authority | decision recorded | explicit release decision |
| 22 | Publish | authorized consumer release | no publish authority | consumer | deployment receipt | explicit publish/deploy authority |
| 23 | Post-release measurement | timestamped observations | missing runtime access/evidence | seo_analytics_growth | C16 evidence | read-only unless platform mutation |
| 24 | Result registration | outcome separated from causal claim | provenance missing | analytics/documentation | result record | provider intake is separate |
| 25 | Framework learning loop | evidence intake/pattern review | insufficient portability/revalidation | provider governance | candidate decision | separate provider PR |

## Release severity

- `P0`: critical blocker.
- `P1`: material blocker.
- `P2`: relevant non-blocking improvement.
- `P3`: future evolution.

For an implementation to become a validated reference, recommended provider gate is `P0=0` and `P1=0`. A consumer may adopt a different release gate only by explicit documented deviation; that does not change provider reference criteria.
