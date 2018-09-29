# -*- coding: UTF-8 -*-
from lexer.head import *

class Type(Words):
    def __init__(self, s, t, w):
        Words.__init__(self, s, t)
        self.width = w


class Types(Type):
    Int = Type("int", Tag.BASIC, 4)
    Float = Type("float", Tag.BASIC, 8)
    Char = Type("char", Tag.BASIC, 1)
    Bool = Type("bool", Tag.BASIC, 1)

    @staticmethod
    def numeric(p):
        if p == Types.Float or p == Types.Int or p == Types.Char:
            return True
        else:
            return False

    @staticmethod
    def max(self, p1, p2):
        if not self.numeric(p1) or not self.numeric(p2):
            return None
        elif p1 == Types.Float or p2 == Types.Float:
            return Types.Float
        elif p1 == Types.Int or p2 == Types.Int:
            return Types.Int
        else:
            return Types.Char

