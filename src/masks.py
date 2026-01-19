def get_mask_card_number(card_number: int) -> str:
    """Функция, которая принимает номер карты и выводит его маску"""
    card_number_only_digits = "".join(i for i in str(card_number) if i.isdigit())
    card_number_str = str(card_number_only_digits)

    if len(card_number_only_digits) != 16:
            raise ValueError('Неверный номер карты')

    return card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[-4:]


def get_mask_account(account_number: int) -> str:
    """Функция, которая принимает номер счёта и выводит его маску"""
    account_number_only_digits = "".join(i for i in str(account_number) if i.isdigit())
    account_number_str = str(account_number)

    if len(account_number_only_digits) != 20:
            raise ValueError('Неверный номер карты')

    return "**" + account_number_str[-4:]
