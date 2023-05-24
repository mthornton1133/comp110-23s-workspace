"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730546472"


class Simpy:
    """This is the Simpy class that is being defined."""

    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, numbers: list[float]):
        """Construct the objects for class Simpy."""
        self.values = numbers

    def __str__(self) -> str:
        """Give ability to print the objects of class Simpy."""
        elems: list[float] = []
        for x in self.values:
            elems.append(x)
        return f"Simpy({elems})"
    
    def fill(self, fill_value: float, exp_len_of_list: int) -> None:
        """Fill the object with the desired floats."""
        i: int = 0
        while i < exp_len_of_list:
            if i < len(self.values):
                i += 1
            else:
                self.values.append(fill_value)
                i += 1
        for x in range(0, len(self.values)):
            if self.values[x] != fill_value:
                self.values[x] = fill_value
        idx_for_remove: int = len(self.values)
        if idx_for_remove > exp_len_of_list:
            while idx_for_remove > exp_len_of_list:
                self.values.pop(int(self.values[idx_for_remove - 1]))
                idx_for_remove -= 1
        elif idx_for_remove < exp_len_of_list:
            while idx_for_remove < exp_len_of_list:
                self.values.append(fill_value)
                idx_for_remove += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill the objects with floats that range from the start and stop values."""
        assert step != 0.0
        while start < stop or start > stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Add all of the values in the object of class Simpy."""
        total_sum: float = 0.0
        for val in self.values:
            total_sum += val
        return total_sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operation Overload for add."""
        new_simp: Simpy = Simpy([])
        list_for_new_simp: list[float] = []
        if type(rhs) == float:
            for x in self.values:
                list_for_new_simp.append(x + rhs)
            new_simp = Simpy(list_for_new_simp)
            return new_simp
        else:
            for idx in range(0, len(self.values)):
                list_for_new_simp.append(self.values[idx] + rhs.values[idx])
            new_simp = Simpy(list_for_new_simp)
            return new_simp
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operation Overload for exponentaition."""
        new_simp: Simpy = Simpy([])
        list_for_new_simp: list[float] = []
        if type(rhs) == float:
            for x in self.values:
                list_for_new_simp.append(x ** rhs)
            new_simp = Simpy(list_for_new_simp)
            return new_simp
        else:
            for idx in range(0, len(self.values)):
                list_for_new_simp.append(self.values[idx] ** rhs.values[idx])
            new_simp = Simpy(list_for_new_simp)
            return new_simp
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload for the == operator."""
        bool_list: list[bool] = []
        if type(rhs) == float:
            for x in self.values:
                if x == rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
        else:
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload for the greater than operator."""
        bool_list: list[bool] = []
        if type(rhs) == float:
            for x in self.values:
                if x > rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
        else:
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload operation to use subscription on Simpy."""
        final_simpy: Simpy = Simpy([])
        list_for_simpy: list[float] = []
        if type(rhs) == int:
            for idx in range(0, len(self.values)):
                if self.values[idx] == self.values[rhs]:
                    return self.values[idx]
        else:
            for idx in range(0, len(self.values)):
                if rhs[idx]:
                    list_for_simpy.append(self.values[idx])
            final_simpy = Simpy(list_for_simpy)
            return final_simpy