# Methodology

## Study objective

This project evaluates large language model reliability across factual reliability and hallucination, instruction following, and uncertainty or false-premise handling. It is designed as both an AI evaluation benchmark and a data analytics study.

## Benchmark design

The final target is 150 prompts: 50 in each evaluation domain. The ten-case pilot validates the schema, rubric, scoring utilities, and workload before expansion.

## Unit of analysis

The primary unit is one model response to one benchmark prompt. Each response links to an immutable `prompt_id`, model identifier, run timestamp, and evaluation settings.

## Benchmark fields

```text
prompt_id
category
subcategory
prompt
expected_behavior
reference_answer
scoring_method
difficulty
source_type
source
notes
```

## Response-level fields

```text
prompt_id
model
model_version
run_timestamp
model_response
factual_accuracy
instruction_adherence
uncertainty_handling
hallucination_flag
major_error_flag
error_type
response_behavior
human_score
automated_score
overall_score
pass_fail
evaluator_notes
```

## Scoring architecture

1. **Deterministic scoring** validates exact answers, JSON schema, counts, prohibited terms, ordering, and other objective constraints.
2. **Human scoring** evaluates factual nuance, fabrication, premise correction, and calibrated uncertainty.
3. **Optional LLM-as-judge scoring** is added only after human labels exist, enabling agreement analysis without treating the model judge as ground truth.

## Planned metrics

- overall pass rate;
- pass rate by model, category, subcategory, and difficulty;
- hallucination rate among eligible cases;
- false-premise correction and instruction-compliance rates;
- mean applicable rubric score;
- error-code frequency and unnecessary-refusal rate;
- human and automated grader agreement.

Metric denominators will be explicit. Missing or non-applicable scores will not be treated as zero.

## Model comparison controls

Each model receives identical prompt text and equivalent settings where providers expose them. Record provider and model identifier, access date and timestamp, sampling settings, system prompt, interface or API, retries or truncation, and tool or browsing access.

## Quality assurance

The pilot precedes full data collection. Ambiguous decisions and validator failures will be logged and used to revise the rubric. A sample of human labels should receive second review if another evaluator is available.

## Source and contamination policy

Each case is labeled author-created, adapted, or directly sourced. Adapted and sourced cases include attribution and license notes. Results distinguish design inspiration from copied benchmark items.

## Limitations to report

The final report will discuss sample size, prompt selection, temporal model changes, provider settings, evaluator subjectivity, benchmark contamination, and limits on generalizing from selected models or task types.
