# -*- coding: UTF-8 -*-
from lexer.head import *

class Word(Token):
    def __init__(self, s, t):
        Token.__init__(self, t)
        self.lexeme = s

    def to_string(self):
        return self.lexeme

class Words(Word):
    word_and = Word("&&", Tag.AND)
    word_or = Word("||", Tag.OR)
    word_eq = Word("==", Tag.EQ)
    word_ne = Word("!=", Tag.NE)
    word_le = Word("<=", Tag.LE)
    word_ge = Word(">=", Tag.GE)
    word_minus = Word("minus", Tag.OR)
    word_True = Word("true", Tag.TRUE)
    word_False = Word("false", Tag.FALSE)
    word_temp = Word("t", Tag.TEMP)