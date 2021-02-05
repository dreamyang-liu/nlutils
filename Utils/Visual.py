import os
import matplotlib.pyplot as plt
import numpy as np
# from functools import singledispatch
from Figure import Figure
from CommonDefine import FigureType

def bar_plot(figure):
    if figure.figure_size is not None:
        plt.figure(figsize=figure.figure_size)
    else:
        plt.figure()
    for idx, (x, y, style) in enumerate(zip(figure.Xs, figure.Ys, figure.styles)):
        plt.bar(list(map(lambda s: s+idx*0.3, x)), y, 0.3, **style)
        for x_real_number, y_real_number in zip(x, y):
            plt.text(x_real_number+idx*0.3, y_real_number+0.1, '%.0f' % y_real_number, ha='center', va='bottom', fontsize=10)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)
    plt.show()

def polyline_plot(figure):
    if figure.figure_size is not None:
        plt.figure(figsize=figure.figure_size)
    else:
        plt.figure()
    for x, y, style in zip(figure.Xs, figure.Ys, figure.styles):
        plt.plot(x, y, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)
    plt.show()

def histogram_plot(figure):
    pass

def scatter_plot(figure):
    pass

def heatmap_plot(figure):
    pass

VISUAL_DISPATCHER = {
    FigureType.POLYLINE_PLOT:polyline_plot,
    FigureType.BAR_PLOT:bar_plot,
    FigureType.HISTOGRAM_PLOT:histogram_plot,
    FigureType.SCATTER_PLOT:scatter_plot,
    FigureType.HEATMAP_PLOT:heatmap_plot
}



def draw_single_figure(figure):
    VISUAL_DISPATCHER[figure.figure_type](figure)

def draw_multi_figures(figure_dict):
    pass


if __name__ == '__main__':
    # Unit test for compare_visualization_polyline
    Xs = [[1, 2, 3, 4, 5, 6], [1, 2, 6, 8, 9, 11]]
    Ys = [[1, 2, 6, 7, 8, 9], [2, 5, 7, 8, 9, 11]]
    legends = ['x1', 'x2']
    styles = [{'color':'yellow', 'alpha':0.5, 'edgecolor':'green'}, {'color':'blue', 'alpha':0.3,'edgecolor':'red'}]
    fig = Figure(FigureType.BAR_PLOT, legends, Xs, Ys, styles, title="Test Case")
    draw_single_figure(fig)