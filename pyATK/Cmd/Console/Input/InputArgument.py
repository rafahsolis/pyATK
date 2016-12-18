# -*- coding: utf-8 -*-
import datetime

from pyATK.Text import Regex


class InputArgument:
    """
    """

    def __init__(self, argumentName, description, defaultValue=None, type_=str):
        self.name = argumentName
        self.defaultValue = defaultValue
        self.value = None
        self.description = description
        self.type = type_

    def setValue(self, value):
        self.value = value

    def __str__(self):
            return "<" + self.name + ">"

    def __repr__(self):
        return self.__str__()

    def asNumber(self):
        if Regex.isInteger(self.value):
            return int(self.value)
        return float(self.value)

    def asDate(self, fmt="%Y-%m"):
        return datetime.strptime(self.value, "%Y-%m-%d").strftime(fmt)

    def asString(self):
        return str(self.value)

    def getValue(self):
        if self.value is None:
            return self.defaultValue

        if self.type is not str:
            return self.value

        # Try type guessing
        if Regex.isInteger(self.value):
            return int(self.value)
        elif Regex.isReal(self.value):
            return float(self.value)
        else:
            return self.asString()
