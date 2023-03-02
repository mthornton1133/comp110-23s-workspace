"""EX05 - 'List' Utility Functions - More List Utils."""

__author__ = "730546472"

def only_evens(numbers: list[int]) -> list[int]:
    """Fn that only returns even numbers."""
    i: int = 0
    even_nums: list[int] = []
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            even_nums.append(numbers[i])
            i += 1
        else:
            i += 1
    return even_nums


def concat(nums1: list[int], nums2: list[int]) -> list[int]:
    """Fn that concatenates the items of the second list after the items of the first."""
    i: int = 0
    alt_i: int = 0
    full_list: list[int] = []
    while i < len(nums1):
        full_list.append(nums1[i])
        i += 1
    while alt_i < len(nums2):
        full_list.append(nums2[alt_i])
        alt_i += 1
    return full_list


def sub(multi_ints: list[int], idx1: int, idx2: int) -> list[int]:
    """Fn that takes the first idx of a list then the second idx -1 and makes them into a new list."""
    final_list: list[int] = []
    if len(multi_ints) == 0 or idx1 >= len(multi_ints) or idx2 <= 0:
        final_list = []
        return final_list
    elif idx1 < 0:
        idx1 = 0
        final_list.append(multi_ints[idx1])
        final_list.append(multi_ints[idx2 - 1])
        return final_list
    elif idx2 > len(multi_ints):
        idx2 = len(multi_ints)
        final_list.append(multi_ints[idx1])
        final_list.append(multi_ints[idx2 - 1])
        return final_list
    else:
        final_list.append(multi_ints[idx1])
        final_list.append(multi_ints[idx2 - 1])
        return final_list