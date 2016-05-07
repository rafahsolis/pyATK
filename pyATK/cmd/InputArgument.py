
class InputArgument:
    """
    >>> argument = InputArgument('arg-name', 'the description', InputArgument.ARGUMENT_REQUIRED)
    >>> argument.__str__()
    '<arg-name>'
    >>> argument.__repr__()
    '<arg-name>'
    >>> argument = InputArgument('arg-name', 'desc', InputArgument.ARGUMENT_OPTIONAL)
    >>> argument.__str__()
    '[arg-name]'
    """
    ARGUMENT_REQUIRED = 0x0
    ARGUMENT_OPTIONAL = 0x1

    def __init__(self, argument_name, description, value_required):
        self.name = argument_name
        self.description = description
        self.valueRequired = value_required
        self.value = None

    def __str__(self):
        if self.valueRequired == InputArgument.ARGUMENT_REQUIRED:
            return "<" + self.name + ">"
        elif self.valueRequired == InputArgument.ARGUMENT_OPTIONAL:
            return "[" + self.name + "]"

    def __repr__(self):
        return self.__str__()
