# -*- coding: utf-8 -*-

import re


def is_number(n):
    if is_integer(n) or is_real(n):
        return True
    return False


def is_real(n):
    if re.match("^[-+]?[0-9]*\.[0-9]+$", n):
        return True
    return False


def is_integer(n):
    """
    >>> is_integer("-9")
    True
    >>> is_integer("+982798739")
    True
    >>> is_integer("0")
    True
    >>> is_integer("1.0")
    False
    >>> is_integer("some random string")
    False
    """
    if re.match("^[-+]?[0-9]+$", n):
        return True
    return False


def is_hex(s):
    """
    >>> is_hex("0x123")
    True
    >>> is_hex("0xCAFE")
    True
    >>> is_hex("AAA")
    False
    >>> is_hex("0xGGG")
    False
    """
    if re.match("^0x[a-fA-F0-9]+$", s, re.IGNORECASE):
        return True
    return False


def is_valid_ip_address(s):
    if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s):
        return True
    return False


def is_blank(s):
    """
    >>> is_blank("")
    True
    >>> is_blank("not so empty")
    False
    """
    if re.match("^$", s):
        return True
    return False


def is_email(s):
    """
    >>> is_email("Test-123_456@gmail.com")
    True
    >>> is_email("salut le monde")
    False
    """
    if re.match("^[a-zA-Z0-9_\.-]+@[a-zA-Z\.]+[a-zA-Z]{3}", s):
        return True
    return False


def upper(c):
    if ord(c) in range(97, 122):
        return chr(ord(c) - 32)


def lower(c):
    if ord(c) in range(65, 90):
        return chr(ord(c) + 32)


def capitalize(s):
    return upper(s[0]) + s[1:]


def remove_accents(text):
    text = unicode(text).encode('utf-8')
    for plain, funny_set in (('a','áàâãäå\u0101'), ('e','éèêẽë'), ('i',"íìîĩï"), ('o','óòôõöø'),
                             ('u',"úùûũü"), ('A','ÁÀÂÃÄÅ'), ('E','ÉÈÊẼË'), ('I',"ÍÌÎĨÏ"),
                             ('O','ÓÒÔÕÖØ'), ('U',"ÚÙÛŨÜ"), ('n',"ñ"), ('c',"ç"), ('N',"Ñ"),
                             ('C',"Ç"), ('d',"Þ"), ('ss',"ß"), ('ae',"æ"), ('oe','œ')):
        for funny in funny_set:
            text = text.replace(funny, plain)
    return text


def deregexify(s):
    pass
 

def regexify(s):
    return re.escape(s)


def ordinal(n):
    """
    Formats an ordinal.
    Doesn't handle negative numbers.
    >>> ordinal(1)
    '1st'
    >>> ordinal(0)
    '0th'
    >>> [ordinal(x) for x in [2, 3, 4, 5, 10, 11, 12, 13, 14]]
    ['2nd', '3rd', '4th', '5th', '10th', '11th', '12th', '13th', '14th']
    >>> [ordinal(x) for x in [91, 92, 93, 94, 99, 100, 101, 102]]
    ['91st', '92nd', '93rd', '94th', '99th', '100th', '101st', '102nd']
    >>> [ordinal(x) for x in [111, 112, 113, 114, 115]]
    ['111th', '112th', '113th', '114th', '115th']
    """
    if n < 0:
        return None
    if n % 100 in [11, 12, 13]:
        return str(n) + "th"
    return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def right_of(string, separator=None):
    if separator is None:
        return None
    else:
        if separator in string:
            return string.split(separator, 1)[1]
        else:
            return None


def left_of(string, separator=None):
    if separator is None:
        return None
    else:
        if separator in string:
            return string.split(separator, 1)[0]
        else:
            return None


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
