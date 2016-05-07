import os
import shutil
import sys
import inspect
from pyATK.patterns.Command import AbstractCommand
from pyATK.filesystem.Utils import get_absolute_path
from pyATK.utils.decorators import not_implemented


#
# File commands
#
class CopyFileCommand(AbstractCommand):
    """
    >>> import os
    >>> file = open('src.txt', 'w')
    >>> chars = file.write("Hello World from source file")
    >>> file.close()
    >>> command = CopyFileCommand('src.txt', 'dst.txt')
    >>> command.execute()
    >>> file = open('dst.txt', 'r')
    >>> file.read()
    'Hello World from source file'
    >>> file.close()
    >>> command.undo()
    >>> command.undo()
    Traceback (most recent call last):
    ...
    OSError: File not found
    >>> os.remove('src.txt')
    """
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.executed_successfully = False

    def execute(self):
        shutil.copy(self.src, self.dst)
        self.executed_successfully = True

    def undo(self):
        if self.executed_successfully is True:
            remove_command = RemoveFileCommand(self.dst)
            remove_command.execute()
            self.executed_successfully = False
        else:
            raise OSError("File not found")


class RemoveFileCommand(AbstractCommand):
    """
    >>> import os
    >>> file = open('tst.txt', 'w')
    >>> chars = file.write("Hi There")
    >>> file.close()
    >>> command = RemoveFileCommand('tst.txt')
    >>> command.execute()
    >>> command.execute()
    Traceback (most recent call last):
    ...
    OSError: File not found
    >>> command.undo()
    >>> open('tst.txt', 'r').read()
    'Hi There'
    >>> command.execute()
    """
    def __init__(self, src):
        self.src = src
        self.file_content = None

    def execute(self):
        abs_path = get_absolute_path(self.src)
        if os.path.isfile(abs_path):
            file = open(self.src, 'r')
            self.file_content = file.read()
            file.close()
            if os.access(abs_path, os.W_OK):
                os.remove(abs_path)
            else:
                raise PermissionError("Permission denied")

        else:
            raise OSError("File not found")

    def undo(self):
        file = open(self.src, 'w')
        file.write(self.file_content)
        file.close()


class TouchFileCommand(AbstractCommand):
    """
    >>> import os
    >>> command = TouchFileCommand('tst.txt')
    >>> command.execute()
    >>> command.undo()
    >>> command.undo()
    Traceback (most recent call last):
    ...
    OSError: File not found
    """
    def __init__(self, path=None):
        self.path = path

    def execute(self):
        try:
            f = open(self.path, 'w')
        except IOError:
            pass
        else:
            f.close()

    def undo(self):
        rm_command = RemoveFileCommand(self.path)
        rm_command.execute()


#
# Folder commands
#
class CopyTreeCommand(AbstractCommand):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self):
        shutil.copytree(self.src, self.dst)

    def undo(self):
        remove_command = RemoveTreeCommand(self.dst)
        remove_command.execute()


class RemoveTreeCommand(AbstractCommand):
    def __init__(self, src):
        self.src = src

    def execute(self):
        shutil.rmtree(self.src)

    def undo(self):
        pass


#
# Helper Command factory class
#
class CommandFactory:
    def __init__(self):
        self.registered_commands = []
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and obj != CommandFactory:
                self.registered_commands.append(name)

    def make_command(self, command):
        if command in self.registered_commands:
            return getattr(sys.modules[__name__], command)

