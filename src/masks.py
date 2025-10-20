def get_mask_card_number(card_number: int) -> str:
    """Функция, кооторая принимает номер карты и выводит его маску"""
    card_number_str = str(card_number)

    return card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[-4:]


def get_mask_account(account_number: int) -> str:
    """Функция, которая принимает номер счёта и выводит его маску"""
    account_number_str = str(account_number)

    return "**" + account_number_str[-4:]
