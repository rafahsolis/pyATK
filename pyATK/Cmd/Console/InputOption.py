# -*- coding: utf-8 -*-

from datetime import datetime
from pyATK.Misc.Misc import if_else
from pyATK.Text.RegexHelper import RegexHelper


class InputOption:
    """
    >>> opt = InputOption('a', 'all', 'enable all options', InputOption.OPTION_NONE)
    >>> opt.__str__()
    '-a, --all                          enable all options'
    >>> opt.__repr__()
    '-a, --all                          enable all options'
    >>> opt = InputOption('v', 'very-long', 'this should be a very very very extra mega long description field with extra detailed information about the usage of this option', InputOption.OPTION_NONE)
    >>> opt.__str__()
    '-v, --very-long                    this should be a very very very extra mega long description field with extra det\\n                                   ailed information about the usage of this option'
    >>> opt = InputOption('i', 'input-file', 'the input file', InputOption.OPTION_REQUIRED)
    >>> opt.__str__()
    '-i, --input-file=<VALUE>           the input file'
    >>> opt = InputOption('o', 'output-file', 'the output file', InputOption.OPTION_OPTIONAL)
    >>> opt.__str__()
    '-o, --output-file=[VALUE]          the output file'
    >>> opt = InputOption('i', "iterations", "number of iterations", InputOption.OPTION_REQUIRED)
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
    OPTION_REQUIRED = 0x0
    OPTION_OPTIONAL = 0x1
    OPTION_NONE = 0x2
    OFFSET = 35
    MAX_LENGTH_PER_LINE = 80

    def __init__(self, shortForm, longForm=None, description=None, optionRequired=None, type_=str, defaultValue=None):
        self.name = longForm
        self.value = None
        self.description = description
        self.shortForm = "-" + shortForm
        self.longForm = "--" + longForm
        self.optionRequired = optionRequired
        self.isDefined = False
        self.defaultValue = defaultValue
        self.type = type_

    def setValue(self, value):
        self.value = value

    def getOptionCouple(self):
        return [self.shortForm, self.longForm]

    def __str__(self):
        retString = self.shortForm + if_else(self.longForm is not None, ", " + self.longForm, "")
        if self.optionRequired == InputOption.OPTION_REQUIRED:
            retString += "=<VALUE>"
        elif self.optionRequired == InputOption.OPTION_OPTIONAL:
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

    def __repr__(self):
        return self.__str__()

    def asNumber(self):
        if RegexHelper.isInteger(self.value):
            return int(self.value)
        return float(self.value)

    def asDate(self, fmt="%Y-%m"):
        return datetime.strptime(self.value, "%Y-%m-%d").strftime(fmt)

    def asString(self):
        return str(self.value)
