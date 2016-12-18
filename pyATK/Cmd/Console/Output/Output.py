# -*- coding: utf-8 -*-
import sys

from pyATK.Cmd.Helpers.ColorHelper import ColorHelper
from pyATK.Cmd.Helpers.ProgressHelper import ProgressBarHelper
from pyATK.Cmd.Helpers.TableHelper import TableHelper


class Output:
    """
    >>> output = Output()
    >>> output.write("Hello World")
    Hello World

    >>> import pyATK
    >>> output.write("Hello World", pyATK.Cmd.Helpers.ColorEnum.FG_RED)
    \x1b[31mHello World\x1b[39m
    """
    IO_HELPER = 0x01
    PROGRESS_HELPER = 0x02
    TABLE_HELPER = 0x04
    helpers = []

    VERBOSITY_QUIET = 0x01
    VERBOSITY_NORMAL = 0x02
    VERBOSITY_VERBOSE = 0x04
    VERBOSITY_VERY_VERBOSE = 0x08
    VERBOSITY_DEBUG = 0x10

    def __init__(self):
        pass

    def write(self, msg, color=None):
        if color is None:
            print(msg)
        else:
            ColorHelper.colored(msg, color)
        sys.stdout.flush()



