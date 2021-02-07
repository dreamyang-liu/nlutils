import os
import matplotlib.pyplot as plt
import numpy as np
from Figure import Figure
from ..CommonDefine import FigureType
# DIS
# from .Figure import Figure
# from .CommonDefine import FigureType

def bar_plot(figure, plot):
    bar_width = figure.bar_width if figure.bar_width is not None else 0.5
    for idx, (x, y, style) in enumerate(zip(figure.Xs, figure.Ys, figure.styles)):
        plt.bar(list(map(lambda s: s+idx*bar_width, x)), y, bar_width, **style)
        for x_real_number, y_real_number in zip(x, y):
            plt.text(x_real_number+idx*bar_width, y_real_number+0.1, '%.0f' % y_real_number, ha='center', va='bottom', fontsize=10)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def polyline_plot(figure, plot):
    for x, y, style in zip(figure.Xs, figure.Ys, figure.styles):
        plt.plot(x, y, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def histogram_plot(figure, plot):
    for x, style in zip(figure.Xs, figure.styles):
        plt.hist(x, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def histogram_2d_plot(figure, plot):
    x = figure.Xs
    y = figure.Ys
    style = figure.styles
    plt.hist2d(x, y, **style)
    if figure.title is not None:
        plt.title(figure.title)

def scatter_plot(figure, plot):
    for x, y, style in zip(figure.Xs, figure.Ys, figure.styles):
        plt.scatter(x, y, **style)
    plt.legend(figure.legends)
    if figure.title is not None:
        plt.title(figure.title)

def heatmap_plot(figure, plot):
    plt.imshow(figure.Xs)
    plot.set_xticklabels(['x{}'.format(i) for i in range(7)])
    plot.set_yticklabels(['y{}'.format(i) for i in range(2)])
    if figure.title is not None:
        plt.title(figure.title)

VISUAL_DISPATCHER = {
    FigureType.POLYLINE_PLOT:polyline_plot,
    FigureType.BAR_PLOT:bar_plot,
    FigureType.HISTOGRAM_PLOT:histogram_plot,
    FigureType.SCATTER_PLOT:scatter_plot,
    FigureType.HEATMAP_PLOT:heatmap_plot,
    FigureType.HISTOGRAM_2D_PLOT: histogram_2d_plot
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
    for i in range(1, int(figure_number ** 0.5) + 1):
        col = i
        row = i
        if figure_number % i == 0:
            col = i
            row = int(figure_number / i)
        add_col = False
        while i == int(figure_number ** 0.5) and col * row < figure_number:
            col = col + 1 if add_col else col
            row = row + 1 if not add_col else row
            add_col = not add_col
    
    for plot_index in range(0, figure_number):
        # if figure_list[plot_index].figure_size is not None:
        #     plt.subplot(row, col, plot_index + 1)
        # else:
        plot = plt.subplot(col, row, plot_index + 1)
        VISUAL_DISPATCHER[figure_list[plot_index].figure_type](figure_list[plot_index], plot)
    plt.show()
    


if __name__ == '__main__':
    pass