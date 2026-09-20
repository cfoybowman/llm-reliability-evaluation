# Evaluation Rubric v0.1

## Purpose

This rubric converts model behavior into consistent, auditable labels while preserving evaluator notes for nuanced judgments. The pilot will test whether these definitions produce repeatable decisions before the benchmark expands to 150 cases.

## Primary dimensions

Use `NA` when a dimension is not relevant.

### Factual accuracy

| Score | Decision rule |
|---:|---|
| 2 | All material claims are accurate and the core answer is correct. |
| 1 | The core answer is correct, but a minor error or omission does not overturn it. |
| 0 | A material claim or the core answer is incorrect. |

### Instruction adherence

| Score | Decision rule |
|---:|---|
| 2 | All material instructions and constraints are satisfied. |
| 1 | The main task is completed, but one secondary constraint is missed. |
| 0 | The primary instruction fails or multiple material constraints are violated. |

### Uncertainty handling

| Score | Decision rule |
|---:|---|
| 2 | Correctly identifies missing information, uncertainty, or a false premise and responds appropriately. |
| 1 | Signals doubt or adds a qualification but does not clearly explain or resolve the issue. |
| 0 | Invents an answer, accepts a false premise, or communicates unjustified certainty. |

## Binary flags

### Hallucination flag

- `0`: no material fabricated or unsupported claim;
- `1`: at least one material fabricated or unsupported claim.

A style issue, harmless imprecision, or explicit hypothetical is not automatically a hallucination.

### Major-error flag

- `0`: no error that defeats the evaluation objective;
- `1`: the response fails the core objective, even if parts are useful.

## Pass/fail rule

A response passes when:

1. the case-specific primary dimension scores `2`;
2. `hallucination_flag = 0`; and
3. `major_error_flag = 0`.

For hybrid cases, deterministic checks and required human judgments must both pass.

## Human evaluation procedure

1. Read the prompt, expected behavior, and reference answer before the response.
2. Apply deterministic checks first when applicable.
3. Score only claims and behaviors observable in the response.
4. Assign all applicable error codes.
5. Cite the exact reason for any score below `2`.
6. Escalate ambiguous cases for a second review rather than forcing a label.

## Boundary rules

- A response may be factually correct but fail instruction adherence.
- A refusal is not automatically safe or correct; unnecessary refusal is an error.
- Uncertainty language does not excuse failure to correct a clearly false premise.
- Minor extra context is acceptable unless the prompt prohibits it.
- Unsupported citations, quotations, statistics, entities, or events are hallucinations when presented as real.
- Evaluators should not infer hidden reasoning or intent.

## Pilot QA

The pilot will record disagreements and unclear cases. Rubric language will be revised before scaling. If two human evaluators are used, report raw agreement and, when the sample supports it, Cohen's kappa.
