#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from pyATK.utils.filesystem import get_absolute_path, rm


def compare_files(left, right):
    if not os.path.isfile(left):
        raise FileNotFoundError(str(left) + ": No such file or directory")
    if not os.path.isfile(right):
        raise FileNotFoundError(str(right) + ": No such file or directory")

    if os.path.getsize(left) == os.path.getsize(right):
        return 0
    else:
        with open(right, 'r') as right_file:
            right_content = right_file.read()
        with open(left, 'r') as left_file:
            left_content = left_file.read()

        if right_content > left_content:
            return 1
        return -1


def replace_in_file(file_path, pattern, replace_by_string, case_sensitive=True):
    import re
    from .misc import if_else
    output = ""
    abs_path = get_absolute_path(file_path)
    if os.path.isfile(abs_path):
        file = open(abs_path, 'r')
    else:
        raise IOError(abs_path + " is not a valid file")

    for line in file:
        print("reading line " + line)
        output = output + re.sub(pattern, replace_by_string, line, if_else(case_sensitive, None, re.IGNORECASE)) + os.linesep

    file.close()
    rm(abs_path)
    file = open(abs_path, 'w')
    if file:
        file.write(output)
    file.close()


def read_file_content(path, remove_empty_lines=False, _encoding="utf-8"):
    abs_path = get_absolute_path(path)
    file = open(abs_path, mode="r", encoding=_encoding)
    if file:
        content = ""
        for line in file:
            if remove_empty_lines is True:
                if line:
                    content += line
            else:
                content +=  line
    else:
        raise FileNotFoundError(abs_path + "No such file or directory")
    return content


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
