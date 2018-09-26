# -*- coding: UTF-8 -*-
from lexer.Token import Token
from lexer.Tag import Tag

class Num(Token):
    def __init__(self, v):
        Token.__init__(self, Tag.NUM)
        self.value = v

    def to_string(self):
        return str(self.value)