# -*- coding: utf-8 -*-
import pytest
from typing import Any
from lilspider.checker.base import Included, Excluded
from lilspider.checker.zh import CityIncludedChecker, CityExcludedChecker

def test_included(capsys: Any) -> None:
    assert Included('llo', 'hello world').yes() is True
    assert Included('www', 'foobar').yes() is False
    assert Included('www', 'foobar').no() is True

def test_excluded(capsys: Any) -> None:
    assert Excluded('llo', 'hello world').yes() is False
    assert Excluded('www', 'foobar').yes() is True
    assert Excluded('www', 'foobar').no() is False

def test_city_included_checker(capsys: Any) -> None:
    c = CityIncludedChecker("上海人民广场")
    assert c.yes() is True
    c = CityIncludedChecker("Shanghai People's Square")
    assert c.yes() is False

def test_city_excluded_checker(capsys: Any) -> None:
    c = CityExcludedChecker("上海人民广场")
    assert c.yes() is False
    c = CityExcludedChecker("Shanghai People's Square")
    assert c.yes() is True

