def short_words(words: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    short_list: list[str] = []
    for x in words:
        if len(x) < 5:
            short_list.append(x)
        else:
            print(f"{x} is too long!")
    return short_list