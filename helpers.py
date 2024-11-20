import re
from typing import Callable

class Helper:

    @staticmethod
    def is_exist(obj: dict[str,object], key: str):
        return key in obj and obj[key]

    @staticmethod
    def compare_str(s1: str, s2: str):
        return len(s1) - len(s2)

    @staticmethod
    def format_list_str(lst: list[str] | None, formatters: list[Callable] | None = None) -> list[str] | None:
        if lst is None:
            return None
        result = []
        for item in lst:
            item = Helper.format_str(item, formatters)
            if item:
                result.append(item)
        return result

    @staticmethod
    def format_str(s: str | None, formatters: list[Callable] | None = None) -> str | None:
        if s is None:
            return None
        formatters = Helper.default_formatter() if formatters is None else formatters
        for formatter in formatters:
            s = formatter(s)
        return s


    # Formatters
    @staticmethod
    def default_formatter() -> list[Callable]:
        return [Helper.__trim, Helper.__remove_multi_spaces]

    @staticmethod
    def amenities_formatter() -> list[Callable] | None:
        extend = [Helper.__add_space_before_capital_letter, Helper.__to_lower]
        return Helper.default_formatter().extend(extend)


    # Private methods
    @staticmethod
    def __add_space_before_capital_letter(s: str) -> str:
        special_cases = ["wifi","tv","bathtub","childcare","aircon","kettle","iron"]
        if s.lower() in special_cases:
            return s
        return re.sub(r"(\w)([A-Z])", r"\1 \2", s)

    @staticmethod
    def __to_lower(s: str) -> str:
        return s.lower()

    @staticmethod
    def __trim(s: str) -> str:
        return s.strip()

    @staticmethod
    def __remove_multi_spaces(s: str) -> str:
        return re.sub(' +', ' ', s)

