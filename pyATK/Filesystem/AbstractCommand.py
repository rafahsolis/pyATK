# -*- coding: utf-8 -*-
import abc
from six import with_metaclass


class AbstractCommand(with_metaclass(abc.ABCMeta)):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass
