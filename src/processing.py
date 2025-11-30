def filter_by_state(list_of_dicts: list, state: str="EXECUTED") -> list:
    """Функция, принимающая список словарей, возвращаеет новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_list_of_dicts = []
    for i in list_of_dicts:
        if i.get("state") == state:
            new_list_of_dicts.append(i)

    return new_list_of_dicts


def sort_by_date(list_of_dicts: list, reverse: bool=True) -> list:
    """Функция, принимающая список словарей, возвращает новый список словарей, отсортированный по дате"""
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x.get('date', ''), reverse=reverse)

    return sorted_list_of_dicts
