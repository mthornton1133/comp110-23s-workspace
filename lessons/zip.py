"""Function for zip."""

def zip(strings: list[str], numbers: list[int]) -> dict[str, int]:
    """Returns the strings as keys and numbers as values."""
    final_dict: dict[str, int] = dict()
    i: int = 0
    if len(strings) !=len(numbers) or len(strings) == 0 and len(numbers) == 0:
        return dict()
    while i < len(strings):
        final_dict[strings[i]] = numbers[i]
        i += 1
    return final_dict