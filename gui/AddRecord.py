from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView
from PyQt5.uic import loadUi
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
# from PySide import QtGui, QtCore
from PyQt5 import QtGui, QtCore

class AddRecord(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/AddRecord.ui', self)
        self.label_2.setText("PPM_test")
        headerLabels = [
            '$C_{soil}=(1 - n) C_m + \\theta_w C_w$',
            '$k_{soil}=\\frac{\\sum f_j k_j \\theta_j}{\\sum f_j \\theta_j}$',
            '$\\lambda_{soil}=k_{soil} / C_{soil}$']
        # labels =
        qpixmaps = []
        indx = 0
        fontsize = 12
        for labels in headerLabels:
            print(labels)
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))
            # self.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            indx += 1
        print(qpixmaps)
        self.label_3.setPixmap(qpixmaps[0])
        # mathTex_to_QPixmap(labels, fontsize)
        # self.pushButtonChoose.released.connect(self.choose_button_clicked)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        # print("base")
        # self.tableView.clicked.connect(self.selectChanged)
        # self.pushButtonAddRecord.released.connect(self.add_button_clicked)


def mathTex_to_QPixmap(mathTex, fs):

    #---- set up a mpl figure instance ----

    # fig = mpl.Figure()
    # fig = mpl.figure.Figure()
    fig = plt.figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    #---- plot the mathTex expression ----

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs)

    #---- fit figure size to text artist ----

    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)

    text_bbox = t.get_window_extent(renderer)

    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height

    fig.set_size_inches(tight_fwidth, tight_fheight)

    #---- convert mpl figure to QPixmap ----

    buf, size = fig.canvas.print_to_buffer()
    qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                  QtGui.QImage.Format_ARGB32))
    qpixmap = QtGui.QPixmap(qimage)

    return qpixmap