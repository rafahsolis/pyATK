# -*- coding: utf-8 -*-

from datetime import datetime

from pyATK.Misc.Misc import if_else
from pyATK.Text.Regex import Regex


class InputOption:
    """
    >>> opt = InputOption('a', 'all', 'enable all options', InputOption.VALUE_NONE)
    >>> opt.__str__()
    '-a, --all                          enable all options'
    >>> opt.__repr__()
    '-a, --all                          enable all options'
    >>> opt = InputOption('v', 'very-long', 'this should be a very very very extra mega long description field with extra detailed information about the usage of this option', InputOption.VALUE_NONE)
    >>> opt.__str__()
    '-v, --very-long                    this should be a very very very extra mega long description field with extra det\\n                                   ailed information about the usage of this option'
    >>> opt = InputOption('i', 'input-file', 'the input file', InputOption.VALUE_REQUIRED)
    >>> opt.__str__()
    '-i, --input-file=<VALUE>           the input file'
    >>> opt = InputOption('o', 'output-file', 'the output file', InputOption.VALUE_OPTIONAL)
    >>> opt.__str__()
    '-o, --output-file=[VALUE]          the output file'
    >>> opt = InputOption('i', "iterations", "number of iterations", InputOption.VALUE_REQUIRED)
    >>> opt.getOptionCouple()
    ['-i', '--iterations']
    >>> opt.setValue('2')
    >>> opt.asNumber()
    2
    >>> opt.value = "2.3"
    >>> opt.asNumber()
    2.3
    >>> opt.asString()
    '2.3'
    >>> opt.value = "2016-05-03"
    >>> opt.asDate()
    '2016-05'
    """
    VALUE_REQUIRED = 0x0
    VALUE_OPTIONAL = 0x1
    VALUE_NONE = 0x2
    VALUE_IS_ARRAY = 0x04
    OFFSET = 35
    MAX_LENGTH_PER_LINE = 80

    def __init__(self, shortForm, longForm, description=None, mode=None, type_=str, defaultValue=None):
        self.value = None
        self.description = description

        if shortForm is not None and shortForm.startswith('-') is False:
            self.shortForm = "-" + shortForm
        else:
            self.shortForm = shortForm

        if longForm is not None and longForm.startswith('--') is False:
            self.longForm = "--" + longForm
        else:
            self.longForm = longForm

        self.name = self.longForm
        while self.name[0] == '-':
            self.name = self.name[1:]

        self.mode = mode
        self.defined = False
        self.defaultValue = defaultValue
        self.type = type_

    def setValue(self, value):
        self.value = value

    def getOptionCouple(self):
        return [self.shortForm, self.longForm]

    def __str__(self):
        retString = self.shortForm + if_else(self.longForm is not None, ", " + self.longForm, "")
        if self.mode == InputOption.VALUE_REQUIRED:
            retString += "=<VALUE>"
        elif self.mode == InputOption.VALUE_OPTIONAL:
            retString += "=[VALUE]"
        else:
            pass

        retString = retString.ljust(InputOption.OFFSET)
        if self.description is not None:
            if len(self.description) > InputOption.MAX_LENGTH_PER_LINE:
                retString += self.description[:InputOption.MAX_LENGTH_PER_LINE] + "\n"
                retString += self.description[InputOption.MAX_LENGTH_PER_LINE:].rjust(InputOption.OFFSET +
                                                                                       len(self.description) -
                                                                                       InputOption.MAX_LENGTH_PER_LINE)
            else:
                retString += self.description

        return retString

    def setDefined(self, defined):
        self.defined = defined
        return self

    def isDefined(self):
        return self.defined is True

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

    def asBoolean(self):
        return bool(self.value)

    def getValue(self):
        if self.value is None:
            return None

        if self.type is not str:
            return self.value

        if Regex.isInteger(self.value):
            return int(self.value)
        elif Regex.isReal(self.value):
            return float(self.value)
        else:
            return self.asString()

