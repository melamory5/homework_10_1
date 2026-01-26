def filter_by_currency(transactions: list, currency: str):
    """Функция, принимает список транзакций и возвращает итератор, выдающий соответствующие заданной операции"""
    for transaction in transactions:
        if "operationAmount" not in transaction:
            continue
        operation_amount = transaction["operationAmount"]
        if "currency" not in operation_amount:
            continue
        currency_info = operation_amount["currency"]
        if (currency_info.get("name") == currency and
                currency_info.get("code") == currency):
            yield transaction


def transaction_descriptions(transactions: list):
    """Функция, принимает транзакции и возвращает описание"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop):
    """Функция, которая выдает номера банковских карт"""
    for number in range(start, stop):
        number_str = f"{number:016d}"
        formatted_number = number_str[:4] + " " + number_str[4:8] + " " + number_str[8:12] + " " + number_str[12:16]
        yield formatted_number
    if start < 1:
        raise ValueError("start должен быть ≥ 1")
    if stop > 10 ** 16:
        raise ValueError("stop ≤ 10**16")
    if start > stop:
        raise ValueError("start не может быть больше stop")
