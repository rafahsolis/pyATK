# -*- coding: utf-8 -*-

import re


class Regex:
    @classmethod
    def isNumber(cls, n):
        """
        >>> Regex.isNumber('1876123')
        True
        >>> Regex.isNumber('a number')
        False
        """
        if cls.isInteger(n) or cls.isReal(n):
            return True
        return False

    @classmethod
    def isReal(cls, n):
        """
        >>> Regex.isReal('.9')
        True
        >>> Regex.isReal('0')
        True
        >>> Regex.isReal('0.0')
        True
        >>> Regex.isReal('0.')
        True
        >>> Regex.isReal('.0')
        True
        >>> Regex.isReal('0..0')
        False
        >>> Regex.isReal('01')
        True
        >>> Regex.isReal('0.0.')
        False
        """
        if re.match("^[-+]?\d*((\.(?=\d)\d+)?|\.)$", n):
            return True
        return False

    @classmethod
    def isInteger(cls, n):
        """
        >>> Regex.isInteger("-9")
        True
        >>> Regex.isInteger("+982798739")
        True
        >>> Regex.isInteger("0")
        True
        >>> Regex.isInteger("1.0")
        False
        >>> Regex.isInteger("some random string")
        False
        >>> Regex.isInteger("-+1")
        False
        >>> Regex.isInteger("-")
        False
        >>> Regex.isInteger("+")
        False
        """
        if re.match("^[-+]?[0-9]+$", n):
            return True
        return False

    @classmethod
    def isHex(cls, s):
        """
        >>> Regex.isHex("0x123")
        True
        >>> Regex.isHex("0xCAFE")
        True
        >>> Regex.isHex("AAA")
        False
        >>> Regex.isHex("0xGGG")
        False
        >>> Regex.isHex("0xdEaDbEef")
        True
        """
        if re.match("^0x[a-fA-F0-9]+$", s, re.IGNORECASE):
            return True
        return False

    @classmethod
    def isValidIpAddress(cls, s):
        """
        >>> Regex.isValidIpAddress('127.0.0.1')
        True
        >>> Regex.isValidIpAddress('127 apples')
        False
        >>> Regex.isValidIpAddress('0.0.0.0')
        True
        >>> Regex.isValidIpAddress('255.255.255.255')
        True
        >>> Regex.isValidIpAddress('256.256.256.256')
        False
        >>> Regex.isValidIpAddress('0377.0377.0xff.')
        False
        """
        if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s):
            return True
        return False

    @classmethod
    def isBlank(cls, s):
        """
        >>> Regex.isBlank("")
        True
        >>> Regex.isBlank("not so empty")
        False
        >>> Regex.isBlank("\\n")
        True
        """
        if re.match("^$", s):
            return True
        return False

    @classmethod
    def isEmail(cls, s):
        """
        >>> Regex.isEmail("Test-123_456@gmail.com")
        True
        >>> Regex.isEmail("not really an email address")
        False
        >>> Regex.isEmail("fa1l@...com")
        False
        """
        if re.match("^^[a-zA-Z0-9_\.-]+@([a-zA-Z-_]+\.?)+$", s):
            return True
        return False

    @classmethod
    def isTime(cls, s):
        if re.match("([0-9]{1,2}:?(?:[0-9]{2})?)-([0-9]{1,2}:?(?:[0-9]{2})?)\s(AM|PM)", s):
            return True
        return False

    @classmethod
    def isDate(cls, s):
        if re.match("\d{4}-\d{2}-\d{2}"):
            return True
        return False
