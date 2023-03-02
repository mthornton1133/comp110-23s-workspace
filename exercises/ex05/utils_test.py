"""EX05 - 'List' Utility Functions - Unit tests for the utilities."""

__author__ = "730546472"

from exercises.ex05.utils import only_evens, concat, sub


def test_one_num() -> None:
    """Tests for even numbers when just one odd in list."""
    test_nums: list[int] = [1]
    assert only_evens(test_nums) == []


def test_one_num2() -> None:
    """Tests for even numbers when just one even in list."""
    test_nums: list[int] = [2]
    assert only_evens(test_nums) == [2]


def test_many_num() -> None:
    """Tests for even numbers in a longer list with even at the end of list."""
    test_nums: list[int] = [1, 3, 5, 7, 10, 12]
    assert only_evens(test_nums) == [10, 12]


def test_even_and_odds_num() -> None:
    """Tests for even numbers with a mix of evens and odds."""
    test_nums: list[int] = [2, 4, 6, 7, 8, 9, 11]
    assert only_evens(test_nums) == [2, 4, 6, 8]


def test_combine_one_num_in_each() -> None:
    """Tests to see of combining one just one item in each list works."""
    first_test_nums: list[int] = [1]
    second_test_nums: list[int] = [7]
    assert concat(first_test_nums, second_test_nums) == [1, 7]


def test_different_amount_of_nums() -> None:
    """Tests to see of combining terms of different lengths works."""
    first_test_nums: list[int] = [2, 5, 7, 8]
    second_test_nums: list[int] = [1, 89]
    assert concat(first_test_nums, second_test_nums) == [2, 5, 7, 8, 1, 89]


def test_many_in_both() -> None:
    """Tests to see if concatenating many terms in boths lists works."""
    first_test_nums: list[int] = [1, 3, 5, 7, 9]
    second_test_nums: list[int] = [2, 4, 6, 8, 10]
    assert concat(first_test_nums, second_test_nums) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def test_none_in_both() -> None:
    """Tests to see of combining two empty lists returns an empty list."""
    first_test_nums: list[int] = []
    second_test_nums: list[int] = []
    assert concat(first_test_nums, second_test_nums) == []


def test_none_in_one() -> None:
    """Tests to see if combining a list with one item and and empty list just returns said item in a list."""
    first_test_nums: list[int] = [63]
    second_test_nums: list[int] = []
    assert concat(first_test_nums, second_test_nums) == [63]


def test_if_list_is_empty() -> None:
    """Tests to see if the list is empty the fn returns an empty list."""
    list_of_ints: list[int] = []
    first_idx: int = 1
    second_idx: int = 4
    assert sub(list_of_ints, first_idx, second_idx) == []


def test_if_list_has_many_values() -> None:
    """Tests to see if the list has many values it returns the ones corresponding to the idxs."""
    list_of_ints: list[int] = [10, 15, 20, 25, 30]
    first_idx: int = 1
    second_idx: int = 4
    assert sub(list_of_ints, first_idx, second_idx) == [15, 25]


def test_if_list_has_values_but_first_idx_is_negative() -> None:
    """Tests to see if the list has many values but the first index is negative"""
    list_of_ints: list[int] = [1, 42, 67, 99]
    first_idx: int = -10
    second_idx: int = 3
    assert sub(list_of_ints, first_idx, second_idx) == [1, 67]


def test_if_list_is_long_and_has_normal_idx() -> None:
    """Tests to see of the fn works with a long lists and indecies greater than zero but smaller than the length of list."""
    list_of_ints: list[int] = [10, 34, 67, 87, 88, 91, 100]
    first_idx: int = 1
    second_idx: int = 4
    assert sub(list_of_ints, first_idx, second_idx) == [34, 87]