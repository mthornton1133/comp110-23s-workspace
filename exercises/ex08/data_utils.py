"""EX08 - Data Wrangling Utils - Utils for data wrangling exefcises."""

__author__ = "730546472"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], num_of_rows: int) -> dict[str, list[str]]:
    """This fn gives you how ever many rows at the start of the input dict you want."""
    if len(table) < num_of_rows:
        num_of_rows = len(table)
    final_dict: dict[str, list[str]] = dict()
    for column in table:
        table_vals: list[str] = []
        for idx in range(0, num_of_rows):
            table_vals.append(table[column][idx])
        final_dict[column] = table_vals
    return final_dict


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """This fn produces a new table with only subsets of the original one."""
    final_dict: dict[str, list[str]] = dict()
    for elem in columns:
        final_dict[elem] = table[elem]
    return final_dict


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This fn combines two column based tables together."""
    final_dict: dict[str, list[str]] = {}
    for elems in table1:
        final_dict[elems] = table1[elems]
    for items in table2:
        if items in final_dict:
            final_dict[items] += table2[items]
        else:
            final_dict[items] = table2[items]
    return final_dict


def count(keys: list[str]) -> dict[str, int]:
    """This fn produces a dict where the keys are each value of the input list and the value of the dict is the frequency of occurence."""
    final_dict: dict[str, int] = {}
    for items in keys:
        if items in final_dict:
            final_dict[items] += 1
        else:
            final_dict[items] = 1
    return final_dict