from pyATK.utils.misc import if_else


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
    """
    OPTION_REQUIRED = 0x0
    OPTION_OPTIONAL = 0x1
    OPTION_NONE = 0x2
    OFFSET = 35
    MAX_LENGTH_PER_LINE = 80

    def __init__(self, short_form, long_form=None, description=None, value_required=None):
        self.shortForm = short_form
        self.longForm = long_form
        self.description = description
        self.valueRequired = value_required
        self.value = None

    def __str__(self):
        ret_string = "-" + self.shortForm + if_else(self.longForm is not None, ", --" + self.longForm, "")
        if self.valueRequired == InputOption.OPTION_REQUIRED:
            ret_string += "=<VALUE>"
        elif self.valueRequired == InputOption.OPTION_OPTIONAL:
            ret_string += "=[VALUE]"
        else:
            pass

        ret_string = ret_string.ljust(InputOption.OFFSET)
        if self.description is not None:
            if len(self.description) > InputOption.MAX_LENGTH_PER_LINE:
                ret_string += self.description[:InputOption.MAX_LENGTH_PER_LINE] + "\n"
                ret_string += self.description[InputOption.MAX_LENGTH_PER_LINE:].rjust(InputOption.OFFSET +
                                                                                       len(self.description) -
                                                                                       InputOption.MAX_LENGTH_PER_LINE)
            else:
                ret_string += self.description

        return ret_string

    def __repr__(self):
        return self.__str__()
