#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


class RegexHelper:
    @classmethod
    def is_number(cls, n):
        """
        >>> RegexHelper.is_number('1876123')
        True
        >>> RegexHelper.is_number('a number')
        False
        """
        if cls.is_integer(n) or cls.is_real(n):
            return True
        return False

    @classmethod
    def is_real(cls, n):
        """
        >>> RegexHelper.is_real('.9')
        True
        >>> RegexHelper.is_real('0')
        False
        >>> RegexHelper.is_real('0.0')
        True
        """
        if re.match("^[-+]?[0-9]*\.[0-9]+$", n):
            return True
        return False

    @classmethod
    def is_integer(cls, n):
        """
        >>> RegexHelper.is_integer("-9")
        True
        >>> RegexHelper.is_integer("+982798739")
        True
        >>> RegexHelper.is_integer("0")
        True
        >>> RegexHelper.is_integer("1.0")
        False
        >>> RegexHelper.is_integer("some random string")
        False
        """
        if re.match("^[-+]?[0-9]+$", n):
            return True
        return False

    @classmethod
    def is_hex(cls, s):
        """
        >>> RegexHelper.is_hex("0x123")
        True
        >>> RegexHelper.is_hex("0xCAFE")
        True
        >>> RegexHelper.is_hex("AAA")
        False
        >>> RegexHelper.is_hex("0xGGG")
        False
        """
        if re.match("^0x[a-fA-F0-9]+$", s, re.IGNORECASE):
            return True
        return False

    @classmethod
    def is_valid_ip_address(cls, s):
        """
        >>> RegexHelper.is_valid_ip_address('127.0.0.1')
        True
        >>> RegexHelper.is_valid_ip_address('127 apples')
        False
        """
        if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s):
            return True
        return False

    @classmethod
    def is_blank(cls, s):
        """
        >>> RegexHelper.is_blank("")
        True
        >>> RegexHelper.is_blank("not so empty")
        False
        """
        if re.match("^$", s):
            return True
        return False

    @classmethod
    def is_email(cls, s):
        """
        >>> RegexHelper.is_email("Test-123_456@gmail.com")
        True
        >>> RegexHelper.is_email("not really an email address")
        False
        """
        if re.match("^[a-zA-Z0-9_\.-]+@[a-zA-Z\.]+[a-zA-Z]{3}", s):
            return True
        return False
