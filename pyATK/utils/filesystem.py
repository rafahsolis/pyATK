# -*- coding: utf-8 -*-

import os
import fnmatch


###
# List files within folder tree (generator)
#
def walk_through_files(top_dir, folder_filter="", file_filter=""):
    for dir_path, _, file_names in os.walk(top_dir):
        if folder_filter in dir_path:
            pass
        else:
            continue
        for fname in file_names:
            if file_filter == "":
                yield os.path.join(dir_path, fname)
            else:
                if fnmatch.fnmatch(fname, file_filter) is True:
                    yield os.path.join(dir_path, fname)


###
# List child folders of top directory (generator)
#
def walk_through_folders(top_dir):
    for dir_path, _, _ in os.walk(top_dir):
        yield dir_path


###
# Returns the size of a folder's content. Returns 0 if the argument is not a folder
#
def folder_size(top_dir):
    if os.path.isdir(top_dir) is False:
        return 0
    else:
        total_size = 0
        for filename in walk_through_files(top_dir):
            total_size += os.path.getsize(filename)
        return total_size


def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)


def mkdir(folder_name):
    pass


def touch(file_name):
    f = open(file_name, 'w')
    f.close()


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
