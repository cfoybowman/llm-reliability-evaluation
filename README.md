# LLM Reliability Evaluation Benchmark

A reproducible AI evaluation and data analysis project measuring how reliably large language models handle factual questions, misleading premises, explicit constraints, and uncertainty.

## Research question

> How reliably do large language models respond to factual, misleading, and constraint-based prompts, and what systematic failure patterns emerge across models and evaluation categories?

## Project scope

| Domain | Target cases | Primary measures |
|---|---:|---|
| Factual reliability and hallucination | 50 | Accuracy, fabrication, unsupported claims |
| Instruction following | 50 | Constraint adherence, formatting, task completion |
| Uncertainty and false-premise handling | 50 | Clarification, premise correction, calibrated uncertainty |

The planned study will evaluate three language models, producing approximately 450 scored responses.

## Evaluation approach

- Deterministic validation for machine-checkable constraints
- Human rubric scoring for factual nuance and uncertainty handling
- Optional LLM-as-judge scoring after human labels are established
- Python and pandas analysis of pass rates, error patterns, and grader agreement
- A final Tableau or Power BI dashboard

## Repository map

```text
data/benchmark/   Benchmark cases
docs/             Methodology, rubric, and taxonomy
src/              Validators and scoring utilities
tests/            Automated tests
notebooks/        Exploratory and comparative analysis
results/          Raw responses, scored responses, and metrics
dashboard/        Dashboard files
assets/           Documentation images
```

## Current status

**Day 1 — September 20, 2026**

- [x] Research question and scope
- [x] Benchmark and results schemas
- [x] Rubric v0.1 and error taxonomy v0.1
- [x] Ten-case pilot benchmark
- [x] Initial validation and scoring utilities
- [ ] Pilot model responses and rubric QA
- [ ] Full 150-case benchmark
- [ ] Model evaluation runs
- [ ] Analysis, dashboard, and final report

## Core references

- [Inspect AI](https://inspect.aisi.org.uk/)
- [Stanford HELM](https://crfm.stanford.edu/helm/)
- [TruthfulQA](https://github.com/sylinrl/TruthfulQA)
- [HaluEval](https://github.com/RUCAIBox/HaluEval)
- [OpenAI evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)

## Reproducibility note

Prompts, expected behaviors, scoring rules, model identifiers, run settings, and evaluator decisions will be documented. Author-created cases will be distinguished from adapted or externally sourced cases.
