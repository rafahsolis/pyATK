# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


class String(str):
    """
    >>> s = String('Hello World')
    >>> s.rightOf(' ')
    World
    >>> s = String('Hello World')
    >>> s.rightOf('Beautiful')
    Hello World
    >>> s = String('Hello World')
    >>> s.rightOf('Hello World')
    <BLANKLINE>
    >>> s = String('Hello World')
    >>> s.leftOf(' ')
    Hello
    >>> s = String('Hello World')
    >>> s.leftOf('Beautiful')
    Hello World
    >>> s = String('Hello World')
    >>> s.leftOf('Hello World')
    <BLANKLINE>
    >>> String._upper('a')
    'A'
    >>> String._upper('A')
    'A'
    >>> String._upper('1')
    '1'
    >>> String._lower('A')
    'a'
    >>> String._lower('a')
    'a'
    >>> String._lower('1')
    '1'
    >>> s = String('hello world')
    >>> s.capitalizeWords()
    Hello World
    >>> s = String('hello there')
    >>> s.capitalize()
    Hello there
    >>> s = String("Je suis allé à l'école")
    >>> s.removeAccents()
    Je suis alle a l'ecole
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

    def __init__(self, s):
        super().__init__()
        self._s = s

    def __str__(self):
        return self._s

    def __repr__(self):
        return self.__str__()

    def toString(self):
        return str(self._s)

    def rightOf(self, separator=None):
        if separator is None:
            return self
        else:
            if separator in self._s:
                self._s = self._s.split(separator, 1)[1]
            else:
                pass
        return self

    def leftOf(self, separator=None):
        if separator is None:
            return self
        else:
            if separator in self._s:
                self._s = self._s.split(separator, 1)[0]
            else:
                pass
            return self

    @staticmethod
    def _upper(c):
        if ord(c) in range(97, 122):
            return chr(ord(c) - 32)
        return c

    def upper(self):
        """
        """
        s = self._s
        self._s = "".join([String._upper(c) for c in s])
        return self

    @staticmethod
    def _lower(c):
        if ord(c) in range(65, 90):
            return chr(ord(c) + 32)
        return c

    def lower(self):
        """
        """
        self._s = "".join([String._lower(c) for c in self._s])
        return self

    def capitalize(self):
        """
        """
        if self._s is None:
            return self
        s = self._s
        self._s = self._upper(s[0]) + s[1:].lower()
        return self

    def capitalizeWords(self):
        """
        """
        self._s = " ".join([String(word).capitalize().toString() for word in self._s.split(" ")])
        return self

    def removeAccents(self):
        """
        """
        for plain, funny_set in (('a', 'áàâãäå\u0101'), ('e', 'éèêẽë'), ('i', "íìîĩï"), ('o', 'óòôõöø'),
                                 ('u', "úùûũü"), ('A', 'ÁÀÂÃÄÅ'), ('E', 'ÉÈÊẼË'), ('I', "ÍÌÎĨÏ"),
                                 ('O', 'ÓÒÔÕÖØ'), ('U', "ÚÙÛŨÜ"), ('n', "ñ"), ('c', "ç"), ('N', "Ñ"),
                                 ('C', "Ç"), ('d', "Þ"), ('ss', "ß"), ('ae', "æ"), ('oe', 'œ')):
            for funny in funny_set:
                self._s = self._s.replace(funny, plain)
        return self

    @classmethod
    def ordinal(cls, n):
        """
        Formats an ordinal.
        Doesn't handle negative numbers.
        """
        if n < 0:
            return None
        if n % 100 in [11, 12, 13]:
            return str(n) + "th"
        return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

    @classmethod
    def levenshtein(cls, s1, s2):
        """
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
