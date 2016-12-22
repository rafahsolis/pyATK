# -*- coding: utf-8 -*-

import os
import sys
import argparse

from pyATK.Cmd.Console import InputArgument
from pyATK.Cmd.Console import InputOption
from pyATK.Cmd.Console import Input
from pyATK.Cmd.Console import Output


class BaseApplication:
    """
    >>> myApp = BaseApplication()
    >>> myApp.doConfigure()
    >>> myApp.addArgument("argument", "argument description")
    <pyATK.Cmd.Base.BaseApplication.BaseApplication object at 0x...>
    >>> myApp.addOption("o", "option", "option description")
    <pyATK.Cmd.Base.BaseApplication.BaseApplication object at 0x...>
    """

    STATUS_SUCCESS = 0x0
    STATUS_FAILURE = 0x1

    def __init__(self, name="", version="", description=""):
        self._name = name
        self._version = version
        self._description = description
        self._expectingOptions = False
        self._expectingArguments = False
        self._argumentParser = argparse.ArgumentParser(prog=self._name, description=self._description)
        self._argumentParser.add_argument('--version', action='version', version='%(prog)s 2.0')

        self._input = Input(self._argumentParser)
        self._output = Output()

    def addOption(self, longForm, shortForm, description=None, valueRequired=InputOption.VALUE_NONE):
        if valueRequired == InputOption.VALUE_NONE:
            _type = bool
        else:
            _type = str
        newOption = InputOption(longForm, shortForm, description, valueRequired, _type)
        self._input.addOption(newOption)
        return self

    def addArgument(self, argumentName, description, type_=str, defaultValue=None):
        newArgument = InputArgument(argumentName, description, defaultValue=defaultValue, type_=type_)
        self._input.addArgument(newArgument)
        return self

    def run(self):
        self.doConfigure()

        if len(sys.argv) > 1:
            self._input.parse(sys.argv)

        self.doRun()
        sys.exit(self.STATUS_SUCCESS)

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(self.STATUS_SUCCESS)
        except OSError:
            print("Unable to fork Process. Aborting ...")
            sys.exit(self.STATUS_FAILURE)

        os.chdir("/")
        os.setsid()
        os.umask(0)

        # Second fork
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(self.STATUS_SUCCESS)
        except OSError:
            print("Unable to fork Process. Aborting ...")
            sys.exit(self.STATUS_FAILURE)

    def doConfigure(self):
        return

    def doRun(self):
        return
