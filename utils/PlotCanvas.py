from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=None, height=None, dpi=100):
        # fig = Figure(figsize=(width, 2))
        # fig = Figure()
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        # FigureCanvas.updateGeometry(self)

        # self.plot()

        # FigureCanvas.setSizePolicy(self,
        #                             QSizePolicy.Expanding,
        #                             QSizePolicy.Expanding)
        # FigureCanvas.updateGeometry(self)
        # self.plot()

    def plot(self, x, y, flag, label, xlabel, ylabel):
        ax = self.figure.add_subplot(111)
        if flag == 1:
            ax.clear()
        ax.plot(x, y, label=label)
        if flag == -1:
            self.figure.legend()
        # ax.set_title('АЧХ фильтра')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        # self.figure.tight_layout()
        self.draw()

    # def plot(self):
    #     x = np.array([50, 30, 40])
    #     labels = ["Apples", "Bananas", "Melons"]
    #     ax = self.figure.add_subplot(111)
    #     ax.pie(x, labels=labels)
