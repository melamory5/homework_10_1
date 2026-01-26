import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_string, expected_output", [
    ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
    ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
    ("MasterCard 0000000000000000", "MasterCard 0000 00** **** 0000"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 12345678901234567890", "Счет **7890")
])
def test_mask_account_card(input_string: str, expected_output: str) -> None:
    assert mask_account_card(input_string) == expected_output


@pytest.mark.parametrize("wrong_account_card", [
    "VisaClassic 12345678345678",
    "estro 11122 2233334444",
    "Masteard 000000000",
    "Счт 7430135874305",
    "чет 123478901234567890"])
def wrong_account_card(wrong_account_card: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(wrong_account_card)


@pytest.fixture
def sample_iso_date() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date_standard(sample_iso_date: str) -> None:
    assert get_date(sample_iso_date) == "11.03.2024"


@pytest.mark.parametrize("input_date, expected", [
    ("2026-01-01T00:00:00.000000", "01.01.2026"),
    ("2024-02-29T12:00:00.000000", "29.02.2024"),
    ("2025-12-31T23:59:59.999999", "31.12.2025"),
])
def test_get_date_parametrized(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected


@pytest.mark.parametrize("invalid_input", [
    "",
    "   ",
    "not-a-date",
    "2024/03/11",
    "31.12.2024",
    "2024-13-01T00:00"
])
def test_get_date_errors(invalid_input: str) -> None:
    with pytest.raises(ValueError):
        get_date(invalid_input)


