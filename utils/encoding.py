#!/usr/bin/python3

ENCODINGS = {
    "EFBBBF" : "UTF-8",
}


class Encoding:
    def __init__(self):
        pass
    
    @classmethod
    def isASCIIEncoded(filePath=None):
        if filePath is not None:
            with open(filePath, "rb") as file:
                byte = file.read(1)
                while byte != "":
                    # Do stuff with byte.
                    byte = file.read(1)
                

def isUTF8(file):
    """
    >>> 
    """
    if file:
        if file.read(3) == "EFBBBF":
            return True
        return False
    return False

def getFileEncoding(filename):
    """
    >>> getFileEncoding(eencoding.py    UTF-8
    """
    file = open(filename, "rb")
    if file:
        if isUTF8(file):
            return "UTF-8"
    file.close()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)