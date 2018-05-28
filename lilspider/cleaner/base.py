# -*- coding: utf-8 -*-
import re
from typing import Any

class Base(object):
    def __init__(self, example: str, pattern: Any, replacement: str="") -> None:
        self.example = example
        self.pattern = pattern
        self.replacement = replacement

    def run(self) -> str:
        raise NotImplementedError

class Replace(Base):
    def run(self) -> str:
        if isinstance(self.pattern, list):
            for v in self.pattern:
                self.example = self.example.replace(v, self.replacement)
        elif isinstance(self.pattern, dict):
            for k,v in self.pattern.items():
                self.example = self.example.replace(k, v)
        else:
            self.example = self.example.replace(self.pattern, self.replacement)
        return self.example

class ReplaceOnce(Base):
    def run(self) -> str:
        if isinstance(self.pattern, list):
            for v in self.pattern:
                self.example = self.example.replace(v, self.replacement, 1)
        elif isinstance(self.pattern, dict):
            for k,v in self.pattern.items():
                self.example = self.example.replace(k, v, 1)
        else:
            self.example = self.example.replace(self.pattern, self.replacement, 1)
        return self.example


