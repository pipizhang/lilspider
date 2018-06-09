# -*- coding: utf-8 -*-
from typing import List
import jieba.analyse

def extract_tags(content: str, topK: int=5) -> List[str]:
    allow = ('n','vn','ns','t')
    words = jieba.analyse.extract_tags(content, topK=topK, allowPOS=allow)
    return words


