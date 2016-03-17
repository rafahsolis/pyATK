# -*- coding: utf-8 -*-

import os
import fnmatch


###
# List files within folder tree (generator)
#
def walkThroughFiles(topdir, folder_filter="", file_filter=""):
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


def walkThrough(topdir):
    for dirpath, subdirs, files in os.walk(topdir):
        pass

###
# List child folders of top directory (generator)
#
def walkThroughFolders(topdir):
    for dirpath, _, _ in os.walk(topdir):
        yield dirpath


###
# Returns the size of a folder's content. Returns 0 if the argument is not a folder
#
def folderSize(topdir):
    if os.path.isdir(topdir) is False:
        return 0
    else:
        total_size = 0
        for filename in walkThroughFiles(topdir):
            total_size += os.path.getsize(filename)
        return total_size


###
#
#
def compareFiles(left, right):
    if not os.path.isfile(left):
        raise Exception(str(left) + " is not a file!")
    if not os.path.isfile(right):
        raise Exception(str(right) + " is not a file!")

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


def getAbsolutePath(relativePath):
    return os.path.abspath(relativePath)


def rm(filePath):
    absPath = getAbsolutePath(filePath)
    if os.path.isfile(absPath):
        if os.access(absPath, os.W_OK):
            os.remove(absPath)
        else:
            print("Permission denied: " + absPath + " is not writable.")


def replaceInFile(filePath, pattern, replaceByStr, caseSensitive=True):
    import re
    from misc import if_else
    output = ""
    absPath = getAbsolutePath(filePath)
    if os.path.isfile(absPath):
        file = open(absPath, 'r')
    else:
        raise IOError(absPath + " is not a valid file")

    for line in file:
        print("reading line " + line)
        output = output + re.sub(pattern, replaceByStr, line, if_else(caseSensitive, None, re.IGNORECASE)) + os.linesep

    file.close()
    rm(absPath)
    file = open(absPath, 'w')
    if file:
        file.write(output)
    file.close()



def readFileContent(path, removeEmptyLines=False, _encoding="utf-8"):
    absPath = getAbsolutePath(path)
    file = open(absPath, mode="r", encoding=_encoding)
    if file:
        content = ""
        for line in file:
            if removeEmptyLines is True:
                if line:
                    content = content + line
            else:
                content = content + line
    else:
        raise Exception("File not found")
    return content


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
