import os
import matplotlib.pyplot as plt
import numpy as np
from Figure import Figure
from CommonDefine import FigureType
# DIS
# from .Figure import Figure
# from .CommonDefine import FigureType

def bar_plot(figure):
    bar_width = figure.bar_width if figure.bar_width is not None else 0.5
    for idx, (x, y, style) in enumerate(zip(figure.Xs, figure.Ys, figure.styles)):
        plt.bar(list(map(lambda s: s+idx*bar_width, x)), y, bar_width, **style)
        for x_real_number, y_real_number in zip(x, y):
            plt.text(x_real_number+idx*bar_width, y_real_number+0.1, '%.0f' % y_real_number, ha='center', va='bottom', fontsize=10)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def polyline_plot(figure):
    for x, y, style in zip(figure.Xs, figure.Ys, figure.styles):
        plt.plot(x, y, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def histogram_plot(figure):
    for x, style in zip(figure.Xs, figure.styles):
        plt.hist(x, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def scatter_plot(figure):
    for x, y, style in zip(figure.Xs, figure.Ys, figure.styles):
        plt.scatter(x, y, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

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
    if figure.figure_size is not None:
        plt.figure(figsize=figure.figure_size)
    else:
        plt.figure()
    VISUAL_DISPATCHER[figure.figure_type](figure)
    plt.show()

def draw_multi_figures(figure_list):
    figure_number = figure_list.__len__()
    row = 0
    col = 0
    for i in range(1, 1000):
        if i * i >= figure_number:
            row = i
            col = i
            break
        if i * i < figure_number and i * i + i > figure_number:
            col = i + 1
            row = i
            break
    for plot_index in range(0, figure_number):
        if figure_list[plot_index].figure_size is not None:
            plt.subplot(row, col, plot_index + 1,)
        else:
            plt.subplot(row, col, plot_index + 1)
        VISUAL_DISPATCHER[figure_list[plot_index].figure_type](figure_list[plot_index])
    plt.show()
    


if __name__ == '__main__':
    pass