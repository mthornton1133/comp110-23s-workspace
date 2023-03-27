"""EX07 - Dictionary Utils - Unit tests for the dict utils."""

__author__ = "730546472"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_when_dict_is_single_chars() -> None:
    """This tests to see if it works when dict is only single chars."""
    test_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(test_dict) == {"z": "a", "y": "b", "x": "c"}


def test_with_two_words() -> None:
    """This test when just two words are given."""
    test_dict: dict[str, str] = {"apple": "cat"}
    assert invert(test_dict) == {"cat": "apple"}


def test_with_many_words() -> None:
    """This tests when many words are given."""
    test_dict: dict[str, str] = {"dog": "cat", "horse": "pig", "cow": "sheep", "chicken": "frog"}
    assert invert(test_dict) == {"cat": "dog", "pig": "horse", "sheep": "cow", "frog": "chicken"}


def test_with_one_pair() -> None:
    """This tests with only one pair."""
    test_dict: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(test_dict) == "yellow"


def test_with_many_key_pairs() -> None:
    """This tests with many key value pairs."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_with_same_val() -> None:
    """This tests with 2 different colors and that both appear twice."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "John": "yellow"}
    assert favorite_color(test_dict) == "yellow"


def test_for_one_item() -> None:
    """This test to see that with just one input it returns one."""
    test_list: list[str] = ["Matt"]
    assert count(test_list) == {"Matt": 1}


def test_for_two_different_items() -> None:
    """Thsi tests to see that two different items returns one of each."""
    test_list: list[str] = ["Matt", "John"]
    assert count(test_list) == {"Matt": 1, "John": 1}


def test_for_many_items() -> None:
    """This test to see if many items counts correctly."""
    test_list: list[str] = ["Matt", "John", "Lucas", "Ayden", "Darren", "Darren", "Ayden", "Timmy"]
    assert count(test_list) == {"Matt": 1, "John": 1, "Lucas": 1, "Ayden": 2, "Darren": 2, "Timmy": 1}