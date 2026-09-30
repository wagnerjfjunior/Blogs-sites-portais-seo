# CI Cost and Regression Policy

## Purpose

Preserve the regression-detection value of the canonical GitHub Actions gate while reducing redundant runner consumption in the private repository.

## Canonical behavior

The workflow `.github/workflows/validate-agent-framework.yml`:

- runs the full validation on every pull request;
- checks out the exact pull-request head;
- runs the canonical repository validator;
- runs the SFJM adversarial tests;
- revalidates after tests;
- validates legacy Builder compatibility;
- can be started manually with `workflow_dispatch`;
- cancels an older in-progress PR validation when a newer head supersedes it.

The workflow does **not** run the full validation again on every push to `main`. That execution was redundant with the PR gate and consumed additional Actions quota.

A narrow `push/main` trigger remains only when the workflow file itself changes, so a workflow-policy modification is still exercised after merge.

## Regression safety

Removing the duplicate post-merge run does not remove the PR regression gate.

The authoritative sequence remains:

```text
PR head
  ↓
full CI validation
  ↓
documentation gate
  ↓
lifecycle gate
  ↓
Ready / merge
  ↓
SFJM post-merge verification
```

The SFJM lifecycle continues to require the latest canonical workflow attempt for the exact head to be successful before Ready or merge.

## Failure semantics

If GitHub Actions is unavailable, quota-exhausted, billing-blocked, runner-blocked or otherwise cannot produce a completed successful attempt:

- the result is not treated as PASS;
- it remains INCONCLUSIVE/BLOCKED according to the applicable SFJM transition;
- no Ready or merge follows from an unavailable check.

## Scope

This policy applies to the canonical ecosystem repository. Consumer repositories may have their own CI strategy and must not inherit this workflow automatically.
