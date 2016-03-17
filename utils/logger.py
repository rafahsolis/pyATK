import logging
import os

class Logger:
    CRITICAL = logging.CRITICAL
    ERROR	 = logging.ERROR
    WARNING  = logging.WARNING
    INFO     = logging.INFO
    DEBUG    = logging.DEBUG
    NOTSET   = logging.NOTSET

    def __init__(self, fileName, overwrite=False):
        FORMAT = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
        DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
        FILE_MODE = "a"
        if overwrite is True:
            FILE_MODE = "w"

        logging.basicConfig(filename=fileName,level=logging.NOTSET,format= FORMAT,datefmt=DATE_FORMAT,
                            filemode=FILE_MODE)
        self.internalLogger = logging.getLogger(fileName.split(os.pathsep)[-1])
        print("GetLogger with " + fileName.split(os.pathsep)[-1])

    def setFormat(self, newFormat):
        logging.basicConfig(format=newFormat)

    def setDateFormat(self, newDateFormat):
        logging.basicConfig(datefmt=newDateFormat)

    def log(self, msg, level=NOTSET):
        if level == Logger.CRITICAL:
            self.internalLogger.critical(msg)
        elif level == Logger.ERROR:
            self.internalLogger.error(msg)
        elif level == Logger.WARNING:
            self.internalLogger.warning(msg)
        elif level == Logger.INFO:
            self.internalLogger.info(msg)
        else:
            self.internalLogger.debug(msg)

    def critical(self, msg):
        self.log(msg, Logger.CRITICAL)

    def error(self, msg):
        self.log(msg, Logger.ERROR)

    def warn(self, msg):
        self.log(msg, Logger.WARNING)

    def info(self, msg):
        self.log(msg, Logger.INFO)

    def debug(self, msg):
        self.log(Logger.DEBUG)



