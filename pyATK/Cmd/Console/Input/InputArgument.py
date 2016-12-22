# -*- coding: utf-8 -*-
import datetime

from pyATK.Text import Regex


class InputArgument:
    """
    """

    def __init__(self, argumentName, description, defaultValue=None, type_=str):
        self._name = argumentName
        self._defaultValue = defaultValue
        self._value = None
        self._description = description
        self._type = type_

    def getName(self):
        return self._name

    def getDefaultValue(self):
        return self._defaultValue

    def getDescription(self):
        return self._description

    def getType(self):
        return self._type
    
    def setValue(self, value):
        self._value = value

    def __str__(self):
            return "<" + self._name + ">"

    def __repr__(self):
        return self.__str__()

    def asNumber(self):
        if Regex.isInteger(self._value):
            return int(self._value)
        return float(self._value)

    def asDate(self, fmt="%Y-%m"):
        return datetime.strptime(self._value, "%Y-%m-%d").strftime(fmt)

    def asString(self):
        return str(self._value)

    def getValue(self):
        if self._value is None:
            return self._defaultValue

        if self._type is not str:
            return self._value

        # Try type guessing
        if Regex.isInteger(self._value):
            return int(self._value)
        elif Regex.isReal(self._value):
            return float(self._value)
        else:
            return self.asString()
