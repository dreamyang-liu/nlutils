from CommonDefine import FigureType

class Figure(object):
    optional_args = ['figure_size', 'save_path', 'title']

    @staticmethod
    def get_args(key, kwargs):
        if key in kwargs.keys():
            return kwargs[key]
        else:
            return None

    def __init__(self, figure_type, legends, Xs, Ys, styles=None, **kwargs):
        if styles is None:
            assert Xs.__len__() == Ys.__len__() == legends.__len__() 
        else:
            assert Xs.__len__() == Ys.__len__() == legends.__len__() == styles.__len__()
        self.figure_type = figure_type
        self.legends = legends
        self.Xs = Xs
        self.Ys = Ys
        self.styles = styles

        for optional_arg in self.optional_args:
            if optional_arg in kwargs.keys():
                eval('self.{}=kwargs[{}]'.format(optional_arg, optional_arg))

    
