# -*- coding: utf-8 -*-
import pytest
from typing import Any
from lilspider.checker import *

def test_included(capsys: Any) -> None:
    assert Included('llo', 'hello world').yes() is True
    assert Included('www', 'foobar').yes() is False
    assert Included('www', 'foobar').no() is True

def test_excluded(capsys: Any) -> None:
    assert Excluded('llo', 'hello world').yes() is False
    assert Excluded('www', 'foobar').yes() is True
    assert Excluded('www', 'foobar').no() is False
