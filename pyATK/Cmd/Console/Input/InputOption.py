# -*- coding: utf-8 -*-

from datetime import datetime

from pyATK.Misc.Misc import if_else
from pyATK.Text.Regex import Regex


class InputOption:
    """
    >>> opt = InputOption('all','a',  'enable all options', InputOption.VALUE_NONE)
    >>> opt.__str__()
    '-a, --all                          enable all options'
    >>> opt.__repr__()
    '-a, --all                          enable all options'
    >>> opt = InputOption('very-long', 'v', 'this should be a very very very extra mega long description field with extra detailed information about the usage of this option', InputOption.VALUE_NONE)
    >>> opt.__str__()
    '-v, --very-long                    this should be a very very very extra mega long description field with extra det\\n                                   ailed information about the usage of this option'
    >>> opt = InputOption('input-file', 'i', 'the input file', InputOption.VALUE_REQUIRED)
    >>> opt.__str__()
    '-i, --input-file=<VALUE>           the input file'
    >>> opt = InputOption('output-file', 'o', 'the output file', InputOption.VALUE_OPTIONAL)
    >>> opt.__str__()
    '-o, --output-file=[VALUE]          the output file'
    >>> opt = InputOption("iterations", 'i', "number of iterations", InputOption.VALUE_REQUIRED)
    >>> opt.getOptionCouple()
    ['-i', '--iterations']
    >>> opt.setValue('2')
    >>> opt.asNumber()
    2
    >>> opt.setValue("2.3")
    >>> opt.asNumber()
    2.3
    >>> opt.asString()
    '2.3'
    """
    VALUE_REQUIRED = 0x0
    VALUE_OPTIONAL = 0x1
    VALUE_NONE = 0x2
    VALUE_IS_ARRAY = 0x04
    OFFSET = 35
    MAX_LENGTH_PER_LINE = 80

    def __init__(self, longForm, shortForm, description=None, mode=None, type_=str, defaultValue=None):
        self._value = None
        self._description = description

        if shortForm is not None and shortForm.startswith('-') is False:
            self._shortForm = "-" + shortForm
        else:
            self._shortForm = shortForm

        if longForm is not None and longForm.startswith('--') is False:
            self._longForm = "--" + longForm
        else:
            self._longForm = longForm

        self._name = self._longForm
        while self._name[0] == '-':
            self._name = self._name[1:]

        self._mode = mode
        self._defined = False
        self._defaultValue = defaultValue
        self._type = type_

    def setValue(self, value):
        self._value = value

    def getOptionCouple(self):
        return [self._shortForm, self._longForm]

    def __str__(self):
        retString = self._shortForm + if_else(self._longForm is not None, ", " + self._longForm, "")
        if self._mode == InputOption.VALUE_REQUIRED:
            retString += "=<VALUE>"
        elif self._mode == InputOption.VALUE_OPTIONAL:
            retString += "=[VALUE]"
        else:
            pass

        retString = retString.ljust(InputOption.OFFSET)
        if self._description is not None:
            if len(self._description) > InputOption.MAX_LENGTH_PER_LINE:
                retString += self._description[:InputOption.MAX_LENGTH_PER_LINE] + "\n"
                retString += self._description[InputOption.MAX_LENGTH_PER_LINE:].rjust(InputOption.OFFSET +
                                                                                       len(self._description) -
                                                                                       InputOption.MAX_LENGTH_PER_LINE)
            else:
                retString += self._description

        return retString

    def setDefined(self, defined):
        self._defined = defined
        return self

    def isDefined(self):
        return self._defined is True

    def getShortForm(self):
        return self._shortForm

    def getLongForm(self):
        return self._longForm

    def getName(self):
        return self._name

    def getMode(self):
        return self._mode

    def __repr__(self):
        return self.__str__()

    def asNumber(self):
        if Regex.isReal(self._value):
            return float(self._value)
        return int(self._value)

    def asDate(self, fmt="%Y-%m"):
        return datetime.strptime(self._value, "%Y-%m-%d").strftime(fmt)

    def asString(self):
        return str(self._value)

    def asBoolean(self):
        return bool(self._value)

    def getValue(self):
        if self._value is None:
            return None

        if self._type is not str:
            return self._value

        if Regex.isInteger(self._value):
            return int(self._value)
        elif Regex.isReal(self._value):
            return float(self._value)
        else:
            return self.asString()

