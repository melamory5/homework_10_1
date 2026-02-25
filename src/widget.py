from datetime import datetime


def mask_account_card(type_and_card_number: str) -> str:
    """Функция, принимающая тип и номер карты или счета, и выводит строку с замаскированным номером"""
    card_or_account = ""
    number_of_card_or_account = ""
    new_number_of_card_or_account = ""
    for letter in type_and_card_number:
        if not letter.isdigit():
            card_or_account = card_or_account + letter
        elif letter.isdigit():
            number_of_card_or_account = number_of_card_or_account + letter
    if len(number_of_card_or_account) == 16:
        for letter in number_of_card_or_account:
            new_number_of_card_or_account = number_of_card_or_account[: 4] + " " + number_of_card_or_account[4:6] + "**" + " " + "****" + " " + number_of_card_or_account[-4:]
    elif len(number_of_card_or_account) == 20:
        for letter in number_of_card_or_account:
            new_number_of_card_or_account = "**" + number_of_card_or_account[-4:]
    else:
        print("Неправильный номер")

    return card_or_account + new_number_of_card_or_account


def get_date(date_str: str) -> str:
    """Функция, принимающая дату в ISO формате и возвращающая ДД.ММ.ГГГГ"""
    if not isinstance(date_str, str):
        raise TypeError("На вход должна подаваться строка")
    if not date_str.strip():
        raise ValueError("Строка с датой пуста")
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except (ValueError, IndexError):
        raise ValueError("Некорректный формат даты")
