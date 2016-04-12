from pyATK.utils.misc import if_else


class InputOption:
    OPTION_REQUIRED = 0x0
    OPTION_OPTIONAL = 0x1
    OPTION_NONE = 0x2

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

        ret_string += if_else(self.description is not None, "\t\t" + self.description, "")
        return ret_string

    def __repr__(self):
        return self.__str__()