from typing import Iterator, List, Iterable, Set, Union


def filter_(iterable: Iterator, search_the_string: str) -> Iterable:
    """Get data which contains requested text"""
    if not isinstance(search_the_string, str):
        raise TypeError("Wrong data passed, only strings needed")
    return filter(lambda line: search_the_string in line, iterable)


def sort_(iterable: Iterator, order: str = 'asc') -> List:
    """Sort data ascending or descending"""
    if order not in ('asc', 'desc'):
        raise ValueError('Wrong argument passed, only "asc" or "desc" are allowed')
    if order == 'desc':
        return sorted(iterable, reverse=True)
    return sorted(iterable, reverse=False)


def map_(iterable: Iterator, column: Union[str, int]) -> Iterable:
    """Get only column number"""
    if not str(column).isdigit():
        raise TypeError('Column number is not a digit, please repeat')
    return map(lambda line: line.split(' ')[int(column)] + '\n', iterable)


def limit_(iterable: Iterator, number: Union[str, int]) -> List:
    """Lines limitation by digit value"""
    if not str(number).isdigit():
        raise TypeError('Not digit is passed as a limit value, only digits allowed')
    return list(iterable)[:int(number)]


def unique_(iterable: Iterator, *args) -> Set:
    """Return only unique lines"""
    return set(iterable)