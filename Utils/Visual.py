import os
import matplotlib.pyplot as plt


def compare_visualization_polyline(datas, legends, **kwargs):
    if 'fig_size' in kwargs.keys():
        plt.figure(figsize=kwargs['fig_size'])
    else:
        plt.figure()
    
    for data in datas:
        plt.plot(data)
    plt.legend(legends)
    plt.show()
    if 'save_path' in kwargs.keys() and kwargs['save_path']:
        plt.imsave(kwargs['save_path'])

if __name__ == '__main__':
    # Unit test for compare_visualization_polyline
    datas = [[1, 2, 6, 7, 8, 9], [2, 5, 7, 8, 9, 11]]
    legends = ['x1', 'x2']
    compare_visualization_polyline(datas, legends, fig_size=(20, 10))