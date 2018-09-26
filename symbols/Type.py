# -*- coding: UTF-8 -*-
from lexer.Word import Word
from lexer.Tag import Tag

class Type(Word):
    def __init__(self, s, t, w):
        Word.__init__(self, s, t)
        self.width = w

class Types(Type):
    Int = Type("int", Tag.BASIC, 4)
    Float = Type("float", Tag.BASIC, 8)
    Char = Type("char", Tag.BASIC, 1)
    Bool = Type("bool", Tag.BASIC, 1)
