def value_exists(words: dict[str, int], val: int) -> bool:
    """Fn will test if val is in the dict."""
    for elems in words:
        if words[elems] == val:
            return True
    return False