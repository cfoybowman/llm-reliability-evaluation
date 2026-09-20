"""Deterministic validators for benchmark responses."""

from __future__ import annotations

import json
import re
from typing import Any

BULLET_PATTERN = re.compile(r"^\s*(?:[-*•])\s+(.+?)\s*$")
NUMBERED_PATTERN = re.compile(r"^\s*(?:\d+[.)]|[-*•])\s+")


def nonempty_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def normalize_exact(text: str) -> str:
    return text.strip().rstrip(".").casefold()


def exact_match(text: str, expected: str) -> bool:
    return normalize_exact(text) == normalize_exact(expected)


def validate_bullets(text: str, expected_count: int, max_words: int) -> dict[str, Any]:
    lines = nonempty_lines(text)
    matches = [BULLET_PATTERN.match(line) for line in lines]
    all_bullets = bool(lines) and all(match is not None for match in matches)
    contents = [match.group(1) for match in matches if match]
    word_counts = [len(re.findall(r"\b[\w'-]+\b", item)) for item in contents]
    return {
        "passed": all_bullets and len(contents) == expected_count
        and all(count <= max_words for count in word_counts),
        "bullet_count": len(contents),
        "word_counts": word_counts,
        "all_lines_are_bullets": all_bullets,
    }


def validate_json_schema(text: str) -> dict[str, Any]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        return {"passed": False, "error": str(exc)}
    exact_keys = isinstance(payload, dict) and set(payload) == {
        "topic", "risks", "recommendation"
    }
    valid_types = (
        exact_keys
        and isinstance(payload["topic"], str)
        and isinstance(payload["risks"], list)
        and len(payload["risks"]) == 2
        and all(isinstance(item, str) for item in payload["risks"])
        and isinstance(payload["recommendation"], str)
    )
    return {"passed": bool(valid_types), "payload": payload}


def validate_prohibited_terms(text: str, prohibited_terms: list[str]) -> dict[str, Any]:
    found = [
        term for term in prohibited_terms
        if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", text, flags=re.IGNORECASE)
    ]
    return {"passed": not found, "found": found}


def sentence_count(text: str) -> int:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return len([part for part in parts if part])


def validate_plain_sorted_lines(text: str, expected_count: int) -> dict[str, Any]:
    lines = nonempty_lines(text)
    unmarked = all(not NUMBERED_PATTERN.match(line) for line in lines)
    alphabetized = lines == sorted(lines, key=str.casefold)
    return {
        "passed": len(lines) == expected_count and unmarked and alphabetized,
        "line_count": len(lines),
        "unmarked": unmarked,
        "alphabetized": alphabetized,
    }
