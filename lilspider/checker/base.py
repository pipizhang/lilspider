# -*- coding: utf-8 -*-
import re
import logging
from typing import List
from ..exceptions import CheckerError

logger = logging.getLogger(__name__)

class Base(object):
    def __init__(self, rule: str, example: str) -> None:
        self.example = example
        self.rule = rule

    def throw(self, msg: str=None) -> None:
        if msg == None:
            msg = self.rule
        if isinstance(msg, str):
            logger.debug(msg)
        raise CheckerError(msg)

    def run(self) -> None:
        raise NotImplementedError

    def yes(self) -> bool:
        try:
            self.run()
            return True
        except CheckerError:
            pass
        return False

    def no(self) -> bool:
        return not self.yes()

class Included(Base):
    def run(self) -> None:
        if self.rule not in self.example:
            self.throw('Included invalid "{}"'.format(self.rule))


class Excluded(Base):
    def run(self) -> None:
        if self.rule in self.example:
            self.throw('Excluded invalid "{}"'.format(self.rule))


class Regex(Base):
    def run(self) -> None:
        if not re.match(self.rule, self.example):
            self.throw('Regex invalid "{}"'.format(self.rule))

class MIncluded(Base):
    def __init__(self, rules: List, example: str) -> None:
        self.example = example
        self.rules = rules

    def run(self) -> None:
        for rule in self.rules:
            Included(rule, self.example).run()

class MExcluded(Base):
    def __init__(self, rules: List, example: str) -> None:
        self.example = example
        self.rules = rules

    def run(self) -> None:
        for rule in self.rules:
            Excluded(rule, self.example).run()

