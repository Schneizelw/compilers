# -*- coding: UTF-8 -*-
from lexer.head import *

class Real(Token):
    def __init__(self, v):
        Token.__init__(self, Tag.REAL)
        self.value = v

    def to_string(self):
        return str(self.value)
