"""EX07 - Dictionary Utils - making fns to tests the utils of dicts."""

__author__ = "730546472"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """This fn inverts the keys to values and value to keys."""
    new_dict: dict[str, str] = dict()
    for elem in inp_dict:
        new_dict[inp_dict[elem]] = elem
    return new_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Returns the color that appears most often in the dictionary."""
    new_dict: dict[str, int] = {}
    for name in inp_dict:
        if inp_dict[name] in new_dict:
            new_dict[inp_dict[name]] += 1
        else:
            new_dict[inp_dict[name]] = 1
    highest_key: str = ""
    current_max: int = 0
    for elem in new_dict:
        if new_dict[elem] > current_max:
            current_max = new_dict[elem]
            highest_key = elem
    return highest_key


def count(values: list[str]) -> dict[str, int]:
    """This fn makes the values of the list the keys of dict and the values of the dict are the frequency of their occurrences."""
    final_dict: dict[str, int] = dict()
    for elem in values:
        if elem in final_dict:
            final_dict[elem] += 1
        else:
            final_dict[elem] = 1
    return final_dict