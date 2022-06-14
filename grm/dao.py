"""
    GRM package
    DAO abstract class
"""


import json
import operator
import types

from .try_os import try_os_io


class DAO:
    """ DAO class with static functions to work with JSON data on a file """

    @staticmethod
    @try_os_io
    def load(filename: str, depth: int = 0) -> list[dict[any]]:
        """ Load data from JSON file

        Can raise InternalServerError

        :param filename: JSON filename
        :param depth: Number of records to return. If depth<=0 returns all records. (default=0)
        :return: List with raw python data
        """

        with open(filename, "rt", encoding="utf-8") as fin:
            data = json.load(fin)

        if depth <= 0:
            return data

        return data[:min(len(data), depth)]

    @staticmethod
    @try_os_io
    def save(filename: str, data: list[any]) -> None:
        """ Save data to JSON file

        Can raise InternalServerError

        :param filename: JSON filename
        :param data: Raw python data to JSON serialize
        """
        with open(filename, "wt", encoding="utf-8") as fou:
            json.dump(data, fou, ensure_ascii=False)

    @staticmethod
    def select_all_by_field(data: list[any],
                            field: str, value: any,
                            compare: types.FunctionType = operator.eq, depth=0) -> list[dict[any]]:
        """ Select all records from raw data

        Can raise ValueError, KeyError

        :param data: Raw data
        :param field: Name of field
        :param value: Value of named field in record
        :param compare: Compare function
        :param depth: How many records do you want to load
        :return: List with raw python data
        """
        if depth <= 0:
            return [item for item in data if compare(item[field], value)]

        result = []
        for item in data:
            if compare(item[field], value):
                result.append(item)
                depth -= 1
                if depth <= 0:
                    break
        return result

    @staticmethod
    def select_one_by_field(data: list[any],
                            field: str, value: any,
                            compare: types.FunctionType = operator.eq) -> dict[any] or None:
        """ Select one record from raw JSON data

        Can raise ValueError, KeyError

        :param data: Raw data
        :param field: Name of field
        :param value: Value of named field in record
        :param compare: Compare function
        :return: Rec
        """
        for item in data:
            if compare(item[field], value):
                return item
        return None

    @staticmethod
    def update_field_by_field(data,
                              source_field, source_value,
                              dest_field, dest_value,
                              compare=operator.eq) -> None:
        """ Update the field if the comparison of another field was successful

        Can raise ValueError, KeyError

        :param data: Raw data
        :param source_field: Source field (to search)
        :param source_value: Source value (to search)
        :param dest_field:  Dest field (to change)
        :param dest_value: Dest value or object with __call__ method (to change)
        :param compare: Compare function
        :return: None
        """
        for item in data:
            if compare(item[source_field], source_value):
                if hasattr(dest_value, '__call__'):
                    item[dest_field] = dest_value(item[dest_field])
                else:
                    item[dest_field] = dest_value
                break
