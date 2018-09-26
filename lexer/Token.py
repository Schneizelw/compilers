# -*- coding: UTF-8 -*-

class Token(object):
    def __init__(self, t):
        self.tag = t

    def to_string(self):
        return str(self.tag)