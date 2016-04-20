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


def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)


def mkdir(folder_name):
    pass


def touch(file_name):
    pass


def rm(file_path):
    abs_path = get_absolute_path(file_path)
    if os.path.isfile(abs_path):
        if os.access(abs_path, os.W_OK):
            os.remove(abs_path)
        else:
            raise PermissionError("Permission denied")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
