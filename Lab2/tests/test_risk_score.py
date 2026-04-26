import pytest
from Lab2.risk_score import calculate_risk_score


def test_calculate_risk_score_returns_float():
    result = calculate_risk_score(50, 200, 150)
    assert isinstance(result, float)


def test_calculate_risk_score_expected_value():
    assert calculate_risk_score(52, 240, 150) == 18.9
    # test failed


def test_calculate_risk_score_invalid_age():
    with pytest.raises(ValueError):
        calculate_risk_score(-1, 240, 150)


# AI EXAMPLES
def test_risk_score_basic():
    assert calculate_risk_score(40, 200, 150) == 13.5


def test_risk_score_zero_age_and_cholesterol():
    # Should be -3.0 (since (0*0.2)+(0*0.05)-(100*0.03)=-3)
    assert calculate_risk_score(0, 0, 100) == -3.0


def test_risk_score_min_heart_rate():
    # Max heart rate = 1 (boundary case)
    assert calculate_risk_score(20, 150, 1) == 27.97


def test_risk_score_all_zeroes_invalid():
    with pytest.raises(ValueError):
        calculate_risk_score(0, 0, 0)


def test_risk_score_negative_age():
    with pytest.raises(ValueError):
        calculate_risk_score(-1, 100, 100)


def test_risk_score_negative_cholesterol():
    with pytest.raises(ValueError):
        calculate_risk_score(30, -10, 100)


def test_risk_score_negative_max_heart_rate():
    with pytest.raises(ValueError):
        calculate_risk_score(30, 100, -10)


def test_risk_score_max_heart_rate_zero():
    with pytest.raises(ValueError):
        calculate_risk_score(30, 100, 0)


# my edge case example
def test_risk_score_my_min_values():
    assert calculate_risk_score(0, 0, 1) == -0.03
