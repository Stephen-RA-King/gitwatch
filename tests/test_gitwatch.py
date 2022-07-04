#!/usr/bin/env python3
"""Tests for package cookietest.py
To use tests either:
    1 - Use pip to install package as "editable"
            pip install -e .
    2 - Import pathmagic.py to enable tests to find the package
"""
# Third party modules

# First party modules
from gitwatch import gitwatch


def test_get_config() -> None:
    num, result = gitwatch.get_config()
    exp_result = [True for i in range(num)]
    assert result == exp_result


def test_fizzbuzz() -> None:
    result = gitwatch.fizzbuzz(16)
    assert result == [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
    ]


def test_fibonacci() -> None:
    result = gitwatch.fibonacci(10)
    assert result == [1, 1, 2, 3, 5, 8]
