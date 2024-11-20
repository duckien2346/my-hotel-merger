import re
from typing import Callable

class Helper:
    """Helper class for common functions"""

    @staticmethod
    def is_exist(obj: dict[str,object], key: str):
        """Check if key exists in object and has a value"""
        return key in obj and obj[key]

    @staticmethod
    def compare_str(s_1: str, s_2: str):
        """Compare two strings and return the difference in length"""
        return len(s_1) - len(s_2)

    @staticmethod
    def format_list_str(lst: list[str] | None, formatters: list[Callable] | None = None) -> list[str] | None:
        """Format a list of strings using the provided formatters"""
        if lst is None:
            return None
        result = []
        for item in lst:
            item = Helper.format_str(item, formatters)
            if item:
                result.append(item)
        return result

    @staticmethod
    def format_str(string: str | None, formatters: list[Callable] | None = None) -> str | None:
        """Format a string using the provided formatters"""
        if string is None:
            return None
        # formatters = Helper.default_formatter() if formatters is None else formatters
        if formatters is None:
            formatters = Helper.default_formatter()
        for formatter in formatters:
            string = formatter(string)
        return string


    # Formatters
    @staticmethod
    def default_formatter() -> list[Callable]:
        """Default formatters for string"""
        return [Helper.__trim, Helper.__remove_multi_spaces]

    @staticmethod
    def amenities_formatter() -> list[Callable]:
        """Formatters for amenities"""
        return [
            Helper.__trim,
            Helper.__remove_multi_spaces,
            Helper.__format_cap_letters,
            Helper.__to_lower
        ]


    # Private methods
    @staticmethod
    def __format_cap_letters(string: str) -> str:
        """Format string with capital letters"""
        special_cases = ["wifi","tv","bathtub","childcare","aircon","kettle","iron","pool","bar"]
        if string.lower() in special_cases:
            return string
        return re.sub(r"(\w)([A-Z])", r"\1 \2", string)

    @staticmethod
    def __to_lower(string: str) -> str:
        return string.lower()

    @staticmethod
    def __trim(string: str) -> str:
        return string.strip()

    @staticmethod
    def __remove_multi_spaces(string: str) -> str:
        return re.sub(' +', ' ', string)
