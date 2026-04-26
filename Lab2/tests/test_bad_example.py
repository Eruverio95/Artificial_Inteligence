import pytest
from Lab2.bad_example import average_age


def test_average_age_basic_case():
    records = [
        {'name': 'Anna', 'age': 20},
        {'name': 'Jan', 'age': 30},
    ]
    assert average_age(records) == 25


def test_average_age_empty_list():
    with pytest.raises(Exception):
        average_age([])


def test_average_age_corrected():
    sample2 = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Piotr', 'age': 23},
        {'name': 'Maria', 'age': 25},
        {'name': 'Maria', 'age': 27},
        {'name': 'Maria', 'age': 29},
    ]
    assert average_age(sample2) == 25.0


# EDGE CASES
def test_average_age_empty_list():
    with pytest.raises(ZeroDivisionError):
        average_age([])


def test_average_age_single_person():
    records = [{'name': 'Solo', 'age': 45}]
    assert average_age(records) == 45


def test_average_age_float_ages():
    records = [{'name': 'Anna', 'age': 20.5}, {'name': 'Jan', 'age': 29.5}]
    assert average_age(records) == 25.0


def test_average_age_zero_age():
    records = [{'name': 'Baby', 'age': 0}, {'name': 'Mom', 'age': 30}]
    assert average_age(records) == 15


def test_average_age_negative_age():
    records = [{'name': 'Backwards', 'age': -10}, {'name': 'Forward', 'age': 30}]
    assert average_age(records) == 10
