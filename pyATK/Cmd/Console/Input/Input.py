# -*- coding: utf-8 -*-

from pyATK.Cmd.Console import InputArgument
from pyATK.Cmd.Console import InputOption


class Input:
    """
    >>> import argparse
    >>> parser = argparse.ArgumentParser()
    >>> input = Input(parser)
    >>> arg = InputArgument("first-argument", "")
    >>> input.addArgument(arg)
    """

    HELP_REQUIRED = 0x01

    def __init__(self, parser):
        self._arguments = {}
        self._options = {}
        self._parser = parser
        self._isInteractive = False

    def getArgument(self, argName):
        for argumentName, argument in self._arguments.items():
            if argName in argument.getName():
                return argument
        raise Exception("Argument " + argName + " was not found")

    def addArgument(self, argument):
        self._arguments[argument.getName()] = argument
        self._parser.add_argument(argument.getName(),
                                  action='store',
                                  type=argument.getType(),
                                  default=argument.getDefaultValue(),
                                  help=argument.getDescription())

    def getOption(self, optName):
        while optName[0] == '-':
            optName = optName[1:]

        return self._options[optName]

    def addOption(self, option):
        self._options[option.getName()] = option
        if option.getMode() == InputOption.VALUE_NONE:
            self._parser.add_argument(option.getShortForm(),
                                      option.getLongForm(),
                                      action="store_true")
        else:
            self._parser.add_argument(option.getShortForm(),
                                      option.getLongForm(),
                                      action="store")
        #
        # TODO: Support ARRAY_VALUE for options
        #

    def setInteractive(self, interactive):
        self._isInteractive = interactive

    def isInteractive(self):
        return self._isInteractive is True

    def parse(self, cli_args):
        parsed = self._parser.parse_args(cli_args[1:])
        for optionName, option in self._options.items():
            if hasattr(parsed, optionName):
                option.setValue(getattr(parsed, optionName))
                option.setDefined(True)

        for argument in self._arguments:
            if hasattr(parsed, argument.getName()) and getattr(parsed, argument.getName) is not None:
                argument.setValue(getattr(parsed, argument.getName()))

    def validate(self):
        for option in self._options:
            if option.isDefined() is False:
                continue
            if option.getValue() is None and option.getMode() != InputOption.VALUE_NONE:
                raise Exception("Missing option value")
        return True

