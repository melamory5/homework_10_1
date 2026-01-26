import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "CANCELED", "amount": 200},
        {"id": 3, "state": "EXECUTED", "amount": 300},
        {"id": 4, "state": "PENDING", "amount": 400},
    ]


@pytest.mark.parametrize("state", ["EXECUTED",
                                   "CANCELED",
                                   "DELETED",
                                   ""])
def test_filter_by_state_empty_list(state: str) -> None:
    assert filter_by_state([], "EXECUTED") == []


def test_filter_by_state_no_state_key() -> None:
    no_state_list = [{"id": 1, "amount": 100}]
    assert filter_by_state(no_state_list, "EXECUTED") == []


@pytest.fixture
def example_of_dates() -> list:
    return [
        {"id": 1, "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "date": "2023-05-20T12:32:10.879000"},
        {"id": 3, "date": "2025-01-01T10:20:05.005550"},
    ]


def test_sort_by_date_descending(example_of_dates: list) -> None:
    result = sort_by_date(example_of_dates)
    assert result[0]["id"] == 3
    assert result[1]["id"] == 1
    assert result[2]["id"] == 2


def test_sort_by_date_ascending(example_of_dates: list):
    result = sort_by_date(example_of_dates, reverse=False)
    assert result[0]["id"] == 2
    assert result[2]["id"] == 3
