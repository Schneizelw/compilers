# -*- coding: UTF-8 -*-
from symbols.head import *
from lexer.head import *

class Array(Types):

    def __init__(self, sz, p):
        Types.__init__(self, "[]", Tag.INDEX, sz*p.width)
        self.size = sz #数组长度
        self.of = p    #元素类型 p为Type类型

    def to_string(self):
        return "["+str(self.size) + "]" + self.of.to_string()

if __name__ == "__main__":
    b = Type("int", Tag.BASIC, 4)
    c = Array(10, b)
    res = c.to_string()
    print(res)
