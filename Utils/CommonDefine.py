from enum import Enum

class FigureType(Enum):
    HEATMAP_PLOT = 0
    POLYLINE_PLOT = 1
    BAR_PLOT = 2
    SCATTER_PLOT = 3
    HISTOGRAM_PLOT = 4
    HISTOGRAM_2D_PLOT = 5

class DataType(Enum):
    NUMPY_ARRAY = 0
    LIST = 1

class LogLevel(Enum):
    FATAL = 0
    ERROR = 1
    EXCEPTION = 2
    WARNING = 3
    INFO = 4
    PERFORMANCE = 5
    DEBUG = 6
