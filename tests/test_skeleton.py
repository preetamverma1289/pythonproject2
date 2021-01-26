# -*- coding: utf-8 -*-

import pytest

from pythonproject2.skeleton import fib

__author__ = "Preetam Verma"
__copyright__ = "Preetam Verma"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
