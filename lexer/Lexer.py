# -*- coding: UTF-8 -*-
from symbols.Type import *
from lexer.head import *

class Lexer(object):
    line = 1
    words = dict()
    cur = 0

    def reserve(self, w):
        self.words[w.lexeme] = w


    def __init__(self, filename):
        fd = open(filename, "r")
        self.src = fd.read()
        self.reserve(Word("if", Tag.IF))
        self.reserve(Word("else", Tag.ELSE))
        self.reserve(Word("while", Tag.WHILE))
        self.reserve(Word("do", Tag.DO))
        self.reserve(Word("break", Tag.BREAK))
        self.reserve(Words.word_True)
        self.reserve(Words.word_False)
        self.reserve(Types.Int)
        self.reserve(Types.Float)
        self.reserve(Types.Char)
        self.reserve(Types.Bool)

    def readch(self, index):
        while index < len(self.src):
            ch = self.src[index]
            return ch
        return None

    def nextch(self, c):
        peek = self.readch(self.cur + 1)
        if peek != c:
            return False
        return True

    def scan(self):
        ch = self.readch(self.cur)
        if ch is None:
            return None
        while ch:
            if ch == ' ' or ch == '\t':
                self.cur += 1
            elif ch == '\n':
                self.line += 1
                self.cur += 1
            else:
                break
            ch = self.readch(self.cur)
        if ch == '&':
            if self.nextch('&'):
                self.cur += 2
                return Words.word_and
            else:
                self.cur += 1
                return Token('&')
        elif ch == '|':
            if self.nextch('|'):
                self.cur += 2
                return Words.word_or
            else:
                self.cur += 1
                return Token('|')
        elif ch == '=':
            if self.nextch('='):
                self.cur += 2
                return Words.word_eq
            else:
                self.cur += 1
                return Token('=')
        elif ch == '!':
            if self.nextch('='):
                self.cur += 2
                return Words.word_ne
            else:
                self.cur += 1
                return Token('!')
        elif ch == '<':
            if self.nextch('='):
                self.cur += 2
                return Words.word_le
            else:
                self.cur += 1
                return Token('<')
        elif ch == '>':
            if self.nextch('='):
                self.cur += 2
                return Words.word_ge
            else:
                self.cur += 1
                return Token('>')
        else:
            pass
        if ch is None:
            return None
        if ch.isdigit():
            v = 0
            while ch.isdigit():
                v = 10*v + int(ch)
                self.cur += 1
                ch = self.readch(self.cur)
            if ch != '.':
                return Num(v)
            x = float(v)
            d = 10
            while 1:
                self.cur += 1
                ch = self.readch(self.cur)
                if not ch.isdigit():
                    break
                x = x + float(ch)/d
                d *= 10
            return Real(x)
        if ch is None:
            return None
        if ch.isalpha():
            s = ""
            while ch.isalnum():
                s += ch
                self.cur += 1
                ch = self.readch(self.cur)
            w = self.words.get(s, None)
            if w is not None:
                # Word type
                return w
            w = Word(s, Tag.ID)
            self.words[s] = w
            return w
        tok = Token(ch)
        self.cur += 1
        return tok

if __name__ == "__main__":
    l = Lexer("test.txt")
    while 1:
        tok = l.scan()
        if tok is None:
            break
        if type(tok) == Token:
            print("(%s)" % tok.tag)
        elif type(tok) == Word:
            print("(%s,%d)" % (tok.lexeme, tok.tag))
        elif type(tok) == Type:
            print("(%s,%d,%d)" % (tok.lexeme, tok.tag, tok.width))
        elif type(tok) == Num:
            print("(%s,%d)" % (tok.value, tok.tag))




