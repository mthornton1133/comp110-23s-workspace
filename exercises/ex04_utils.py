"""EX04 - 'list' Utilitiy Functions - List Utilities Exercise."""

__author__ = "730546472"


def all(multi_numbers: list[int], single_number: int) -> bool:
    """fn stating whether or not the list is comprised of all the same numbers."""
    i: int = 0
    alt_i: int = 0
    while i < len(multi_numbers):
        if len(multi_numbers) == 0:
            return False
        elif single_number != multi_numbers[0]:
            return False
        else:
            while alt_i < len(multi_numbers):
                if single_number == multi_numbers[alt_i]:
                    alt_i += 1
                else:
                    return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """fn that gives the maximum value out of a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    high_num: int = input[0]
    while i < len(input):
        current_num: int = input[i]
        if high_num < current_num:
            high_num = current_num
        i += 1
    return high_num


def is_equal(numbers1: list[int], numbers2: list[int]) -> bool:
    """fn that states whether or not the lists are identical."""
    i: int = 0
    if len(numbers1) != len(numbers2):
        return False
    while i < len(numbers1) and len(numbers2):
        if numbers1[i] == numbers2[i]:
            i += 1
        else:
            return False
    return True