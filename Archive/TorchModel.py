
import asyncio

from ..Utils.Log import Logger

class TorchModel(object):

    def __init__(self, model):
        self.model = model
        Logger.instance().log_info("Initialized torch Model.")
        self.watcher = None

    def get_model_parameters(self):
        return self.model.__str__()

    @staticmethod
    def parse_model_params_helper(lines):
        pass

    def parse_model_parameters(self):
        model_structure = [(line.__len__() - line.lstrip(' ').__len__(), line.lstrip(' ').rstrip(' '))for line in self.model.__str__().split('\n')]
        return model_structure

    def update_parameter(self):
        if self.watcher is None:
            # TODO: Add warning
            return False
        else:
            self.watcher.update_model(self)

if __name__ == '__main__':
    m = TorchModel(ResNet50())
    fetch_all_parameters(ResNet50())