#!/usr/bin/python3
# -*- coding: utf-8 -*-


import re


class String:
    @classmethod
    def natural_sort(cls, lst):
        """
        >>> String.natural_sort(["elem1", "elem10", "elem2", "elem20"])
        ['elem1', 'elem2', 'elem10', 'elem20']
        """
        return sorted(lst, key=lambda key: [(lambda c: int(c) if c.isdigit() else c.lower())(c)
                                            for c in re.split('([0-9]+)', key)])

    @classmethod
    def longest_common_substring(cls, s1, s2):
        """
        >>> String.longest_common_substring("Hello World 123", "Hello World")
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
    def levenshtein(cls, s1, s2):
        """
        >>> String.levenshtein("Hello", "Hell")
        1
        >>> String.levenshtein("Cat", "cat")
        1
        >>> String.levenshtein("Cat", "Dog")
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

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
