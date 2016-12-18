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
    >>> opt = InputOption("help", "null description", InputOption.VALUE_REQUIRED)
    >>> input.addOption(opt)
    """

    HELP_REQUIRED = 0x01

    def __init__(self, parser):
        self.arguments = []
        self.options = {}
        self.parser = parser
        self.isInteractive = False

    def getArgument(self, argName):
        for argument in self.arguments:
            if argName in argument.name:
                return argument
        raise Exception("Argument " + argName + " was not found")

    def addArgument(self, argument):
        self.arguments.append(argument)
        self.parser.add_argument(argument.name,
                                 action='store',
                                 type=argument.type,
                                 default=argument.defaultValue,
                                 help=argument.description)

    def getOption(self, optName):
        while optName[0] == '-':
            optName = optName[1:]

        return self.options[optName]

    def addOption(self, option):
        self.options[option.name] = option
        if option.mode == InputOption.VALUE_NONE:
            self.parser.add_argument(option.shortForm,
                                     option.longForm,
                                     action="store_true")
        else:
            self.parser.add_argument(option.shortForm,
                                     option.longForm,
                                     action="store")
        #
        # TODO: Support ARRAY_VALUE for options
        #

    def setInteractive(self, interactive):
        self.isInteractive = interactive

    def getInteractive(self):
        return self.isInteractive

    def isInteractive(self):
        return self.isInteractive is True

    def parse(self, cli_args):
        parsed = self.parser.parse_args(cli_args[1:])
        for option in self.options:
            if hasattr(parsed, option.name):
                option.setValue(getattr(parsed, option.name))
                option.setDefined(True)

        for argument in self.arguments:
            if hasattr(parsed, argument.name) and getattr(parsed, argument.name) is not None:
                argument.setValue(getattr(parsed, argument.name))

    def validate(self):
        for option in self.options:
            if option.isDefined() is False:
                continue
            if option.getValue() is None and option.mode != InputOption.VALUE_NONE:
                raise Exception("Missing option value")
        return True

