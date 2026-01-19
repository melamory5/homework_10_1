import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.fixture
def card_number_example():
    return 1234567812345678


def test_mask_standard(card_number_example):
    result = get_mask_card_number(card_number_example)
    assert result == "1234 56** **** 5678"


@pytest.mark.parametrize("wrong_number", [
    123456781234567,
    12345678123456789,
    ""])
def test_mask_card_invalid_length(wrong_number):
    # Проверяем, что функция корректно реагирует на неправильную длину
    with pytest.raises(ValueError):
        get_mask_card_number(wrong_number)


@pytest.mark.parametrize("wrong_number", [
    "123456781234567 ",
    "123 567812345678",
    "123-567812345678",
    "123p567812345678"])
def test_mask_card_invalid_length(wrong_number: str | int):
    # Проверяем, что функция корректно реагирует на лишние символы
    with pytest.raises(ValueError):
        get_mask_card_number(wrong_number)


@pytest.fixture
def account_number_example():
    return "64686473678894779589"


def test_mask_account_standard(account_number_example: int | str):
    result = get_mask_account(account_number_example)
    assert result == "**9589"


@pytest.mark.parametrize("wrong_number", [
    123456781234567891234,
    12345678123456789,
    ""])
def test_mask_account_invalid_length(wrong_number):
    # Проверяем, что функция корректно реагирует на неправильную длину
    with pytest.raises(ValueError):
        get_mask_account(wrong_number)


@pytest.mark.parametrize("wrong_number", [
    "1234567812345678123 ",
    "123 5678123456781234",
    "123-5678123456781234",
    "123p5678123456781234"])
def test_mask_account_invalid_length(wrong_number: str | int):
    # Проверяем, что функция корректно реагирует на лишние символы
    with pytest.raises(ValueError):
        get_mask_account(wrong_number)
