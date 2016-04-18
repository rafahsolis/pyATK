#!/usr/bin/python3

                
def is_ascii(data):
    try:
        data.decode('ASCII')
    except UnicodeDecodeError:
        return False
    else:
        return True


def is_utf8(data):
    try:
        data.decode('UTF-8')
    except UnicodeDecodeError:
        return False
    else:
        return True

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)