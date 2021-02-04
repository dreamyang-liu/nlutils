import time
import os
from datetime import datetime
from enum import Enum

class LogLevel(Enum):
    FATAL = 0
    ERROR = 1
    EXCEPTION = 2
    WARNING = 3
    INFO = 4
    PERFORMANCE = 5
    DEBUG = 6

def get_local_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Logger(object):

    def __init__(self, level=LogLevel.INFO, write_to_file=False, log_path='/tmp/log-{}'.format(get_local_time()), show_full_path=False):
        self.write_to_file = write_to_file
        self.show_full_path = show_full_path
        if write_to_file:
            if not log_path:
                raise ValueError("Argument [log_path] cannot be None when write_to_file is True")
            else:
                self.log_path = log_path
        self.level = level

    @staticmethod
    def instance():
        return Logger()

    def set_log_path(self, log_path):
        self.log_path = log_path

    def set_level(self, level):
        self.level = level

    def log_fatal(self, message):
        if self.level.value>= LogLevel.FATAL.value:
            log_content = "\033[1;36m{}\033[0m \033[4;32m{}\033[0m \033[1;35mFATAL LOG: {}\033[0m".format(get_local_time(), os.path.realpath(__file__) if self.show_full_path else __file__, message)
            print(log_content)
            if self.write_to_file and os.path.isfile(self.log_path):
                with open(self.log_path, 'a') as f:
                    f.writelines([log_content])
    
    def log_error(self, message):
        if self.level.value >= LogLevel.ERROR.value:
            log_content = "\033[1;36m{}\033[0m \033[4;32m{}\033[0m \033[1;31mERROR LOG: {}\033[0m".format(get_local_time(), os.path.realpath(__file__) if self.show_full_path else __file__, message)
            print(log_content)
            if self.write_to_file and os.path.isfile(self.log_path):
                with open(self.log_path, 'a') as f:
                    f.writelines([log_content])

    def log_warning(self, message):
        if self.level.value >= LogLevel.WARNING.value:
            log_content = "\033[1;36m{}\033[0m \033[4;32m{}\033[0m \033[1;33mWARNING LOG: {}\033[0m".format(get_local_time(), os.path.realpath(__file__) if self.show_full_path else __file__, message)
            print(log_content)
            if self.write_to_file and os.path.isfile(self.log_path):
                with open(self.log_path, 'a') as f:
                    f.writelines([log_content])
    
    def log_info(self, message):
        if self.level.value >= LogLevel.INFO.value:
            log_content = "\033[1;36m{}\033[0m \033[4;32m{}\033[0m \033[1;32mINFO LOG: {}\033[0m".format(get_local_time(), os.path.realpath(__file__) if self.show_full_path else __file__, message)
            print(log_content)
            if self.write_to_file and os.path.isfile(self.log_path):
                with open(self.log_path, 'a') as f:
                    f.writelines([log_content])
    
    def log_debug(self, message):
        if self.level.value >= LogLevel.DEBUG.value:
            log_content = "\033[1;36m{}\033[0m \033[4;32m{}\033[0m \033[1;37mDEBUG LOG: {}\033[0m".format(get_local_time(), os.path.realpath(__file__) if self.show_full_path else __file__, message)
            print(log_content)
            if self.write_to_file and os.path.isfile(self.log_path):
                with open(self.log_path, 'a') as f:
                    f.writelines([log_content])
    
    @staticmethod
    def log_performance(func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            print("\033[1;36m{}\033[0m \033[4;32m{}\033[0m \033[1;34mPERFORMANCE LOG: {} consumes {} seconds\033[0m".format(get_local_time(), os.path.realpath(__file__), func.__name__, end -start))
        return wrapper        




@Logger.log_performance
def calculate_time():
    for i in range(1000000):
        i

if __name__ == '__main__':
    calculate_time()
    Logger.instance().log_warning("This is a test warning.")
    Logger.instance().log_error("This is a test error.")
    Logger.instance().log_fatal("This is a test fatal.")
    Logger.instance().log_info("This is a test info.")
    Logger.instance().log_debug("This is a test debug.")