#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


class Regex:
    @classmethod
    def is_number(cls, n):
        if cls.is_integer(n) or cls.is_real(n):
            return True
        return False

    @classmethod
    def is_real(cls, n):
        if re.match("^[-+]?[0-9]*\.[0-9]+$", n):
            return True
        return False

    @classmethod
    def is_integer(cls, n):
        """
        >>> Regex.is_integer("-9")
        True
        >>> Regex.is_integer("+982798739")
        True
        >>> Regex.is_integer("0")
        True
        >>> Regex.is_integer("1.0")
        False
        >>> Regex.is_integer("some random string")
        False
        """
        if re.match("^[-+]?[0-9]+$", n):
            return True
        return False

    @classmethod
    def is_hex(cls, s):
        """
        >>> Regex.is_hex("0x123")
        True
        >>> Regex.is_hex("0xCAFE")
        True
        >>> Regex.is_hex("AAA")
        False
        >>> Regex.is_hex("0xGGG")
        False
        """
        if re.match("^0x[a-fA-F0-9]+$", s, re.IGNORECASE):
            return True
        return False

    @classmethod
    def is_valid_ip_address(cls, s):
        if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s):
            return True
        return False

    @classmethod
    def is_blank(cls, s):
        """
        >>> Regex.is_blank("")
        True
        >>> Regex.is_blank("not so empty")
        False
        """
        if re.match("^$", s):
            return True
        return False

    @classmethod
    def is_email(cls, s):
        """
        >>> Regex.is_email("Test-123_456@gmail.com")
        True
        >>> Regex.is_email("whatever@example")
        False
        """
        if re.match("^[a-zA-Z0-9_\.-]+@[a-zA-Z\.]+[a-zA-Z]{3}", s):
            return True
        return False
