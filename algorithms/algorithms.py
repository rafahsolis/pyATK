#!/usr/bin/python3
# -*- coding: utf-8 -*-


import re


class String:
    @classmethod
    def natural_sort(lst):
        """
        >>> natural_sort(["elem1", "elem10", "elem2", "elem20"])
        ['elem1', 'elem2', 'elem10', 'elem20']
        """
        return sorted(lst, key=lambda key: [(lambda c: int(c) if c.isdigit() else c.lower())(c)
                                        for c in re.split('([0-9]+)', key)])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
