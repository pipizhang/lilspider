# -*- coding: utf-8 -*-
from typing import List
import os
from ..exceptions import CheckerError

class DictionaryChecker(object):
    name = "DictionaryChecker" # type:str
    dicts = [] # type:List

    def __init__(self, example: str) -> None:
        self.example = example

    def read_dict_file(self, dictfile: str) -> None:
        try:
            dict_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'dictionary'))
            dict_file = os.path.join(dict_path, dictfile)
            with open(dict_file, 'r') as myfile:
                data = myfile.read()
            tmp = data.split("\n")
            tmp = list(filter(None, tmp))
            tmp = list(filter(lambda x: not x.startswith('//'), tmp))
            if isinstance(tmp, list):
                self.dicts = tmp
        except Exception as e:
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

