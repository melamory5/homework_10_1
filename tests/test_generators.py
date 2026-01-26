import pytest
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 939713210,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "95824.07",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142645268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "39114.93",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


@pytest.mark.parametrize("currency", ["USD", "EUR"])
def test_filter_by_currency_exact_match(transactions, currency):
    result = list(filter_by_currency(transactions, currency))
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["name"] == currency
        assert transaction["operationAmount"]["currency"]["code"] == currency


def test_filter_by_currency_no_matches(transactions):
    result = list(filter_by_currency(transactions, "RUB"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод с карты на карту",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод со счета на счет"
    ]


def test_transaction_descriptions_empty_list():
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize("start, stop, expected", [
    (1, 2, ["0000 0000 0000 0001"]),
    (100000, 100002, [
        "0000 0000 0010 0000",
        "0000 0000 0010 0001"]),
    (9999999999999998, 9999999999999999, [
        "9999 9999 9999 9998"])])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError):
        list(card_number_generator(5, 1))
