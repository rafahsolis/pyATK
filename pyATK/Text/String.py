# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


class String:
    @classmethod
    def rightOf(cls, string, separator=None):
        """
        >>> String.rightOf('Hello World', ' ')
        'World'
        >>> String.rightOf('Hello World', 'Beautiful')
        'Hello World'
        >>> String.rightOf('Hello World')
        'Hello World'
        """
        if separator is None:
            return string
        else:
            if separator in string:
                return string.split(separator, 1)[1]
            else:
                return string

    @classmethod
    def leftOf(cls, string, separator=None):
        """
        >>> String.leftOf('Hello World', ' ')
        'Hello'
        >>> String.leftOf('Hello World', 'Beautiful')
        'Hello World'
        >>> String.leftOf('Hello World')
        'Hello World'
        """
        if separator is None:
            return string
        else:
            if separator in string:
                return string.split(separator, 1)[0]
            else:
                return string

    @classmethod
    def ordinal(cls, n):
        """
        Formats an ordinal.
        Doesn't handle negative numbers.
        >>> String.ordinal(-1)

        >>> String.ordinal(1)
        '1st'
        >>> String.ordinal(0)
        '0th'
        >>> String.ordinal(13)
        '13th'
        >>> String.ordinal(101)
        '101st'
        >>> [String.ordinal(x) for x in [111, 112, 113, 114, 115]]
        ['111th', '112th', '113th', '114th', '115th']
        """
        if n < 0:
            return None
        if n % 100 in [11, 12, 13]:
            return str(n) + "th"
        return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

    @classmethod
    def upper(cls, c):
        """
        >>> String.upper('a')
        'A'
        >>> String.upper('A')
        'A'
        >>> String.upper('1')
        '1'
        """
        if ord(c) in range(97, 122):
            return chr(ord(c) - 32)
        return c

    @classmethod
    def lower(cls, c):
        """
        >>> String.lower('A')
        'a'
        >>> String.lower('a')
        'a'
        >>> String.lower('1')
        '1'
        """
        if ord(c) in range(65, 90):
            return chr(ord(c) + 32)
        return c

    @classmethod
    def capitalize(cls, s):
        """
        >>> String.capitalize('hello there')
        'Hello there'
        >>> String.capitalize('Hello there')
        'Hello there'
        """
        return cls.upper(s[0]) + s[1:]

    @classmethod
    def capitalizeWords(cls, s):
        """
        >>> String.capitalizeWords("hello world")
        'Hello World'
        """
        return " ".join([cls.capitalize(s) for s in s.split(" ")])

    @classmethod
    def removeAccents(cls, text):
        """
        >>> String.removeAccents("Je suis allé à l'école")
        "Je suis alle a l'ecole"
        """
        for plain, funny_set in (('a', 'áàâãäå\u0101'), ('e', 'éèêẽë'), ('i', "íìîĩï"), ('o', 'óòôõöø'),
                                 ('u', "úùûũü"), ('A', 'ÁÀÂÃÄÅ'), ('E', 'ÉÈÊẼË'), ('I', "ÍÌÎĨÏ"),
                                 ('O', 'ÓÒÔÕÖØ'), ('U', "ÚÙÛŨÜ"), ('n', "ñ"), ('c', "ç"), ('N', "Ñ"),
                                 ('C', "Ç"), ('d', "Þ"), ('ss', "ß"), ('ae', "æ"), ('oe', 'œ')):
            for funny in funny_set:
                text = text.replace(funny, plain)
        return text

    @classmethod
    def levenshtein(cls, s1, s2):
        """
        >>> String.levenshtein("Hello", "Hell")
        1
        >>> String.levenshtein("Cat", "cat")
        1
        >>> String.levenshtein("Cat", "Dog")
        3
        >>> String.levenshtein("Cat", "Dodge")
        5
        >>> String.levenshtein("Cat", "")
        3
        """
        if len(s1) < len(s2):
            return cls.levenshtein(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    @classmethod
    def longestCommonSubstring(cls, s1, s2):
        """
        >>> String.longestCommonSubstring("Hello World 123", "Hello World")
        'Hello World'
        """
        m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
        longest, x_longest = 0, 0
        for x in range(1, 1 + len(s1)):
            for y in range(1, 1 + len(s2)):
                if s1[x - 1] == s2[y - 1]:
                    m[x][y] = m[x - 1][y - 1] + 1
                    if m[x][y] > longest:
                        longest = m[x][y]
                        x_longest = x
                else:
                    m[x][y] = 0
        return s1[x_longest - longest: x_longest]

    @classmethod
    def naturalSort(cls, lst):
        """
        >>> String.naturalSort(["elem1", "elem10", "elem2", "elem20"])
        ['elem1', 'elem2', 'elem10', 'elem20']
        """
        return sorted(lst, key=lambda key: [(lambda c: int(c) if c.isdigit() else c.lower())(c)
                                            for c in re.split('([0-9]+)', key)])