
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

    return card_or_account + " " + new_number_of_card_or_account


print(mask_account_card("Maestro 1596837868705199"))

print(mask_account_card("Счет 64686473678894779589"))


def get_date(date: str) -> str:
    """Функция, принимающая дату и выводящая дату в новом формате"""
    new_date = ""
    day = ""
    month = ""
    year = ""
    split_date = date.split("T")
    new_date = split_date[0]
    day = new_date[-2:]
    month = new_date[-5:-3]
    year = new_date[0:4]

    return day + "." + month + "." + year


print(get_date("2024-03-11T02:26:18.671407"))