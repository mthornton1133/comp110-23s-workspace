def free_buscuits(inp_dict: dict[str, list[int]]) -> dict[str, bool]:
    final_dict: dict[str, bool] = {}
    for games in inp_dict:
        total: int = 0
        for points in inp_dict[games]:
            total += points
        if total >= 100:
            final_dict[games] = True
        else:
            final_dict[games] = False
    return final_dict

def max_key(inp_dict: dict[str, list[int]]) -> str:
    max_str: str = ""
    max_sum: int = 0
    for keys in inp_dict:
        sum: int = 0
        for nums in inp_dict[keys]:
            sum += nums
        if sum > max_sum:
            max_sum = sum
            max_key = keys
    return max_key

def multiples(inp_list: list[int]) -> list[bool]:
    mask: list[bool] = []
    i: int = 0
    while i < len(inp_list):
        if i == 0:
            mask.append(inp_list[i] % inp_list[len(inp_list) - 1 == 0])
        else:
            mask.append(inp_list[i] % inp_list[i - 1] == 0)
        i += 1
    return mask

def merge_list(input_list_str: list[str], input_list_int: list[int]) -> dict[str, int]:
    final_dict: dict[str, int] = {}
    if len(input_list_str) != len(input_list_int):
        return final_dict
    for idx in range(0, len(input_list_str)):
        final_dict[input_list_str[idx]] = input_list_int[idx]
    return final_dict

def reverse_multiply(inp_list: list[int]) -> list[int]:
    final_list: list[int] = []
    i: int = len(inp_list) - 1
    while i >= 0:
        final_list.append(inp_list[i] * 2)
        i -= 1
    return final_list

class HotCocoa:
    has_whip: bool
    flavor: str
    marshmellow_count: int
    sweetness: int

    def __init__(self, whip: bool, new_flavor: str, count: int, sweet: int):
        self.has_whip = whip
        self.flavor = new_flavor
        self.marshmellow_count = count
        self.sweetness = sweet

    def mallow_adder(self, mallows: int) -> None:
        self.marshmellow_count += mallows
        self.sweetness += mallows * 2

    def calorie_count(self) -> float:
        total_count: float = 0.0
        if self.flavor == "vanilla" or self.flavor == "peppermint":
            total_count += 30
        else:
            total_count += 20
        if self.has_whip:
            total_count += 100
        total_count += self.marshmellow_count / 2
        return total_count
    
class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, inp_name: str, inp_purpose: str, inp_minutes: int):
        self.name = inp_name
        self.purpose = inp_purpose
        self.minutes = inp_minutes
    
    def add_time(self, time: int) -> None:
        self.minutes += time

    def reset(self) -> int:
        time: int = self.minutes
        self.minutes = 0
        return time
    
    def report(self) -> None:
        time_in_hours: self.minutes // 60
        remaining_minutes: int = self.minutes - time_in_hours * 60
        return f"{self.name} has spent {time_in_hours} hours and {remaining_minutes} on {self. purpose}."