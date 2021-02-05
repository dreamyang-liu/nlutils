import json

from ..Utils.Log import Log

class Transaction(object):

    def __init__(self):
        self.parameters = dict()
        self.results = dict()
        self.data_parameters = dict()
        self.models = dict()

    def add_data_parameter(self, key, value):
        self.data_parameters[key] = value
    
    def remove_data_parameter(self, key):
        self.data_parameters.pop(key)

    def update_data_parameter(self, key, value):
        self.data_parameters[key] = value
    
    def get_data_parameters(self, key):
        return self.data_parameters[key]

    def add_parameter(self, key, value):
        self.parameters[key] = value
    
    def remove_parameter(self, key):
        self.parameters.pop(key)

    def update_parameter(self, key, value):
        self.parameters[key] = value
    
    def get_parameters(self, key):
        return self.parameters[key]

    def add_result(self, key, value):
        self.results[key] = value
    
    def remove_result(self, key):
        self.results.pop(key)

    def update_result(self, key, value):
        self.results[key] = value
    
    def get_result(self, key):
        return self.results[key]
    
    def register_model(self, name, model):
        self.models[name] = model
        model.transaction = self
    
    def unregister_model(self, name):
        self.models.pop(name)
        model.transaction = None
    


if __name__ == '__main__':
    pass