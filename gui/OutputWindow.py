from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt5.uic import loadUi

from utils.PlotCanvas import PlotCanvas
from utils.WidgetPlot import WidgetPlot
import random
import numpy as np


class OutputWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/OutputWindow.ui', self)
        # print("output")
        # main_vbox = QVBoxLayout()
        main_vbox = self.layout()
        hbox = QHBoxLayout()

        textEdit = QTextEdit()
        # plotCanv = PlotCanvas(self ,width=8, height=4)
        self.widget_plot = WidgetPlot(self)
        # plotCanv.move(0, 0)
        hbox.addWidget(textEdit)
        hbox.addWidget(self.widget_plot)
        # (self.widget, width=self.widget.width(), height = self.widget.height() - 50)
        # vbox.addLayout(hbox_calculate)
        main_vbox.addLayout(hbox)
        self.setLayout(main_vbox)

    def _show(self):
        self.show()
        x = [i for i in range(1, 25)]
        y = np.sin(x)
        self.plot(x, y, 1, 'Line', 'x', 'y')

    def plot(self, x, y, flag, label, xlabel, ylabel):
        # print("plot")
        self.widget_plot.plot(x, y, flag, label, xlabel, ylabel)
