from multiprocessing import Pool, Queue, Process
from .Log import Logger
from functools import wraps
import time
import os


def gpu_wrapper():
    def decorate(func, gpu_id):
        os.system("export CUDA_VISIBLE_DEVICES={}".format(gpu_id))

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorate


class TrainingManager(object):
    def __init__(self):
        self.training_pool = None

    @staticmethod
    def shell_training(cmd_str):
        Logger.get_logger().info(f"Process {os.getpid()} is running")
        os.system(cmd_str)

    def start_shell_training(self, cmd_strs):
        self.training_pool = Pool(len(cmd_strs))
        self.training_pool.map(TrainingManager.shell_training, cmd_strs)
        self.training_pool.close()
        self.training_pool.join()
