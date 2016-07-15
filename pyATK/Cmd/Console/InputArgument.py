

class InputArgument:
    """
    """

    def __init__(self, argumentName, description, defaultValue=None, type_=str):
        self.name = argumentName
        self.value = defaultValue
        self.description = description
        self.type = type_

    def setValue(self, value):
        self.value = value

    def __str__(self):
            return "<" + self.name + ">"

    def __repr__(self):
        return self.__str__()
