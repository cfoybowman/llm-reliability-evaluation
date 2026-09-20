"""Objective scoring helpers for the pilot benchmark."""

from __future__ import annotations

from typing import Any, Callable

from src.validators import (
    exact_match,
    sentence_count,
    validate_bullets,
    validate_json_schema,
    validate_plain_sorted_lines,
    validate_prohibited_terms,
)


def score_hal_003(response: str) -> dict[str, Any]:
    passed = exact_match(response, "Canberra")
    return {"prompt_id": "HAL-003", "passed": passed, "checks": {"exact_match": passed}}


def score_ins_001(response: str) -> dict[str, Any]:
    result = validate_bullets(response, expected_count=3, max_words=8)
    return {"prompt_id": "INS-001", "passed": result["passed"], "checks": result}


def score_ins_002(response: str) -> dict[str, Any]:
    result = validate_json_schema(response)
    return {"prompt_id": "INS-002", "passed": result["passed"], "checks": result}


def score_ins_003(response: str) -> dict[str, Any]:
    prohibited = validate_prohibited_terms(response, ["artificial intelligence", "AI"])
    sentences = sentence_count(response)
    passed = prohibited["passed"] and sentences == 2
    return {
        "prompt_id": "INS-003",
        "passed": passed,
        "checks": {"prohibited_terms": prohibited, "sentence_count": sentences},
    }


def score_ins_004(response: str) -> dict[str, Any]:
    result = validate_plain_sorted_lines(response, expected_count=5)
    return {"prompt_id": "INS-004", "passed": result["passed"], "checks": result}


SCORERS: dict[str, Callable[[str], dict[str, Any]]] = {
    "HAL-003": score_hal_003,
    "INS-001": score_ins_001,
    "INS-002": score_ins_002,
    "INS-003": score_ins_003,
    "INS-004": score_ins_004,
}


def score_response(prompt_id: str, response: str) -> dict[str, Any]:
    if prompt_id not in SCORERS:
        raise KeyError(f"No deterministic scorer registered for {prompt_id}.")
    return SCORERS[prompt_id](response)
