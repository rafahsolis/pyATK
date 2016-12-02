# -*- coding: utf-8 -*-

import re


class RegexHelper:
    @classmethod
    def isNumber(cls, n):
        """
        >>> RegexHelper.isNumber('1876123')
        True
        >>> RegexHelper.isNumber('a number')
        False
        """
        if cls.isInteger(n) or cls.isReal(n):
            return True
        return False

    @classmethod
    def isReal(cls, n):
        """
        >>> RegexHelper.isReal('.9')
        True
        >>> RegexHelper.isReal('0')
        False
        >>> RegexHelper.isReal('0.0')
        True
        >>> RegexHelper.isReal('0.')
        True
        >>> RegexHelper.isReal('.0')
        True
        >>> RegexHelper.isReal('0..0')
        False
        >>> RegexHelper.isReal('01')
        True
        >>> RegexHelper.isReal('0.0.')
        False
        """
        if re.match("^[-+]?[0-9]*\.[0-9]+$", n):
            return True
        return False

    @classmethod
    def isInteger(cls, n):
        """
        >>> RegexHelper.isInteger("-9")
        True
        >>> RegexHelper.isInteger("+982798739")
        True
        >>> RegexHelper.isInteger("0")
        True
        >>> RegexHelper.isInteger("1.0")
        False
        >>> RegexHelper.isInteger("some random string")
        False
        >>> RegexHelper.isInteger("-+1")
        False
        >>> RegexHelper.isInteger("-")
        False
        >>> RegexHelper.isInteger("+")
        False
        """
        if re.match("^[-+]?[0-9]+$", n):
            return True
        return False

    @classmethod
    def isHex(cls, s):
        """
        >>> RegexHelper.isHex("0x123")
        True
        >>> RegexHelper.isHex("0xCAFE")
        True
        >>> RegexHelper.isHex("AAA")
        False
        >>> RegexHelper.isHex("0xGGG")
        False
        >>> RegexHelper.isHex("0xdEaDbEef")
        True
        """
        if re.match("^0x[a-fA-F0-9]+$", s, re.IGNORECASE):
            return True
        return False

    @classmethod
    def isValidIpAddress(cls, s):
        """
        >>> RegexHelper.isValidIpAddress('127.0.0.1')
        True
        >>> RegexHelper.isValidIpAddress('127 apples')
        False
        >>> RegexHelper.isValidIpAddress('0.0.0.0')
        True
        >>> RegexHelper.isValidIpAddress('255.255.255.255')
        True
        >>> RegexHelper.isValidIpAddress('256.256.256.256')
        False
        >>> RegexHelper.isValidIpAddress('0377.0377.0xff.')
        False
        """
        if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s):
            return True
        return False

    @classmethod
    def isBlank(cls, s):
        """
        >>> RegexHelper.isBlank("")
        True
        >>> RegexHelper.isBlank("not so empty")
        False
        >>> RegexHelper.isBlank("\n")
        False
        """
        if re.match("^$", s):
            return True
        return False

    @classmethod
    def isEmail(cls, s):
        """
        >>> RegexHelper.isEmail("Test-123_456@gmail.com")
        True
        >>> RegexHelper.isEmail("not really an email address")
        False
        >>> RegexHelper.isEmail("fa1l@...com")
        False
        """
        if re.match("^[a-zA-Z0-9_\.-]+@[a-zA-Z\.]+[a-zA-Z]{3}", s):
            return True
        return False
