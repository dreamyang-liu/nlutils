
class DeviceNotAvailableException(Exception):

    def __init__(self, *args):
        self.args = args

class CUDANotFoundException(Exception):
    
    def __init__(self, *args):
        self.args = args

        