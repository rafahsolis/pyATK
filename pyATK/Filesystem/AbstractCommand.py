# -*- coding: utf-8 -*-
from abc import ABCMeta
from six import with_metaclass

class AbstractCommand(with_metaclass(ABCMeta)):
    def __init__(self):
        pass

    def execute(self):
        pass

    def undo(self):
        pass
