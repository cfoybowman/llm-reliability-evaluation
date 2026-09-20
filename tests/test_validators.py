from src.scoring import score_response
from src.validators import validate_bullets, validate_json_schema


def test_bullet_validator_passes_valid_response():
    response = "- Trees cool cities\n- Canopy access remains unequal\n- Data guides planting priorities"
    assert validate_bullets(response, expected_count=3, max_words=8)["passed"]


def test_json_validator_rejects_extra_key():
    response = (
        '{"topic":"automated hiring","risks":["bias","opacity"],'
        '"recommendation":"Use human review.","extra":"not allowed"}'
    )
    assert not validate_json_schema(response)["passed"]


def test_exact_answer_scorer():
    assert score_response("HAL-003", "Canberra.")["passed"]


def test_prohibited_term_scorer():
    response = (
        "Human reviewers can identify missing context and unfair patterns. "
        "Their oversight improves accountability in hiring decisions."
    )
    assert score_response("INS-003", response)["passed"]
