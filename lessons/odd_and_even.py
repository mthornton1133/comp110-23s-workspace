def odd_and_even(nums: list[int]) -> list[int]:
    """Fn returns values that are odd with even indexes in new list."""
    new_list: list[int] = []
    i: int = 0
    while i < len(nums):
        if i % 2 == 0 and nums[i] % 2 == 1:
            new_list.append(nums[i])
            i += 1
        else:
            i += 1
    return new_list