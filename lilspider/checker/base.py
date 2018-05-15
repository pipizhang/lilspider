# -*- coding: utf-8 -*-
import re

class CheckerError(Exception):
    pass

class Base:
    def __init__(self, rule: str, example: str) -> None:
        self.example = example
        self.rule = rule

    def throw(self, msg: str=None) -> None:
        if msg == None:
            msg = self.rule
        raise CheckerError(msg)

    def run(self) -> None:
        raise NotImplementedError

class Include(Base):
    def run(self) -> None:
        if self.rule not in self.example:
            self.throw('Include invalid "{}"'.format(self.rule))

class UnInclude(Base):
    def run(self) -> None:
        if self.rule in self.example:
            self.throw('UnInclude invalid "{}"'.format(self.rule))

class Regex(Base):
    def run(self) -> None:
        if not re.match(self.rule, self.example):
            self.throw('Regex invalid "{}"'.format(self.rule))


