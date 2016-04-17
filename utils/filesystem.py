# -*- coding: utf-8 -*-

import os
import fnmatch


###
# List files within folder tree (generator)
#
def walk_through_files(topdir, folder_filter="", file_filter=""):
    for dirpath, _, filenames in os.walk(topdir):
        if folder_filter in dirpath:
            pass
        else:
            continue
        for fname in filenames:
            if file_filter == "":
                yield os.path.join(dirpath, fname)
            else:
                if fnmatch.fnmatch(fname, file_filter) is True:
                    yield os.path.join(dirpath, fname)


def walk_through(topdir):
    for dirpath, subdirs, files in os.walk(topdir):
        pass

###
# List child folders of top directory (generator)
#
def walk_through_folders(topdir):
    for dirpath, _, _ in os.walk(topdir):
        yield dirpath


###
# Returns the size of a folder's content. Returns 0 if the argument is not a folder
#
def folder_size(topdir):
    if os.path.isdir(topdir) is False:
        return 0
    else:
        total_size = 0
        for filename in walk_through_files(topdir):
            total_size += os.path.getsize(filename)
        return total_size


###
#
#
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


def get_absolute_path(relativePath):
    return os.path.abspath(relativePath)


def rm(filePath):
    absPath = get_absolute_path(filePath)
    if os.path.isfile(absPath):
        if os.access(absPath, os.W_OK):
            os.remove(absPath)
        else:
            raise PermissionError("Permission denied")


def replace_in_file(file_path, pattern, replace_by_string, case_sensitive=True):
    import re
    from pyATK.utils.misc import if_else
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
