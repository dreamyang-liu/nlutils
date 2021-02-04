from CommonDefine import FigureType

class Figure(object):
    optional_args = ['figure_size', 'save_path', 'title']

    def __init__(self, figure_type, legends, Xs, Ys, styles=None, **kwargs):
        if styles is None:
            assert Xs.__len__() == Ys.__len__() == legends.__len__() 
        else:
            assert Xs.__len__() == Ys.__len__() == legends.__len__() == styles.__len__()
        self.figure_type = figure_type
        self.legends = legends
        self.Xs = Xs
        self.Ys = Ys
        self.styles = styles if styles is not None else [{} for _ in range(len(Xs))]

        for optional_arg in self.optional_args:
            setattr(self, optional_arg, None)
            if optional_arg in kwargs.keys():
                setattr(self, optional_arg, kwargs[optional_arg])

    
