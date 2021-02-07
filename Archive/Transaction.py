import json

from ..Utils.Log import Log
from ..CommonDefine import ParameterType
class Transaction(object):

    PARAMETER_TRANSACTION_DISPATCHER = {
        ParameterType.MODEL: self.model_parameter_handler,
        ParameterType.DATA: self.data_parameter_handler,
        ParameterType.TRANINING: self.training_parameter_handler,
        ParameterType.MISCELLANEOUS: self.miscellaneous_parameter_handler
    }

    def __init__(self):
        self.model_parameters = dict()
        self.results = dict()
        self.training_parameters = dict()
        self.miscellaneous_parameters = dict()
        self.data_parameters = dict()
        self.models = dict()
    
    def main_parameter_handler(self, pkg:dict):
        self.PARAMETER_TRANSACTION_DISPATCHER[pkg['parameter_type']](pkg)

    def model_parameter_handler(self, pkg):
        pass

    def data_parameter_handler(self, pkg):
        pass

    def training_parameter_handler(self, pkg):
        pass

    def miscellaneous_parameter_handler(self, pkg):
        pass
    

    


if __name__ == '__main__':
    pass