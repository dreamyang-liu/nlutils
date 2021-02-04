import os
import matplotlib.pyplot as plt
import numpy as np
from functools import singledispatch
from Figure import Figure
from CommonDefine import FigureType

def bar_plot(figure:Figure):
    pass

def polyline_plot(figure:Figure):
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

def histogram_plot(figure:Figure):
    pass

def scatter_plot(figure:Figure):
    pass

def heatmap_plot(figure:Figure):
    pass

VISUAL_DISPATCHER = {
    FigureType.POLYLINE_PLOT:polyline_plot,
    FigureType.BAR_PLOT:bar_plot,
    FigureType.HISTOGRAM_PLOT:histogram_plot,
    FigureType.SCATTER_PLOT:scatter_plot,
    FigureType.HEATMAP_PLOT:heatmap_plot
}



def draw_single_figure(figure:Figure):
    VISUAL_DISPATCHER[figure.figure_type](figure)

def draw_multi_figures(figure_dict):
    pass


if __name__ == '__main__':
    # Unit test for compare_visualization_polyline
    Xs = [[1, 2, 3, 4, 5, 6], [1, 2, 6, 8, 9, 11]]
    Ys = [[1, 2, 6, 7, 8, 9], [2, 5, 7, 8, 9, 11]]
    legends = ['x1', 'x2']
    styles = [{'linestyle': '-'}, {'linestyle': '--'}]
    fig = Figure(FigureType.POLYLINE_PLOT, legends, Xs, Ys, styles, title="xxx")
    draw_single_figure(fig)