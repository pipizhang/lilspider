# -*- coding: utf-8 -*-
from typing import List
from ..exceptions import CheckerError

class Dictionary(object):
    name = "DictionaryChecker" # type:str
    dicts = [] # type:List

    def __init__(self, example: str) -> None:
        self.example = example

    def read_dict_file(self, dictfile: str) -> None:
        pass

    def throw(self, msg: str=None) -> None:
        if msg == None:
            msg = 'Failed to pass "{}" check'.format(self.name)
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

