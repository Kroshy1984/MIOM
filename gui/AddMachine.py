from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog
from PyQt5.uic import loadUi
from utils.tex_to_qpixmap import mathTex_to_QPixmap

class AddMachine(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/AddMachine.ui', self)
        self.setWindowTitle("Добавление установки")
        headerLabels = [
            '$(PPM), \\sigma_{u} \cdot 10^7, Pa$',
            '$(PYM), \\sigma_{y} \cdot 10^7, Pa$',
            '$(PLM), \\rho_{u} \cdot 10^3, kg/m^3$',
            '$(MM), m_{m}$',
            '$(BCM), B \cdot 10^7, Pa$',
            '$(YEM), \\rho_{e} \cdot 10^{-8}, \Omega_{m}$',
            '$(KDM), K_{d} $'
            # '$C_{soil}=(1 - n) C_m + \\theta_w C_w$',
            # '$k_{soil}=\\frac{\\sum f_j k_j \\theta_j}{\\sum f_j \\theta_j}$',
            # '$\\lambda_{soil}=k_{soil} / C_{soil}$'
        ]
        qpixmaps = []
        indx = 0
        fontsize = 12
        for labels in headerLabels:
            print(labels)
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))
            # self.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            indx += 1
        print(qpixmaps)

        self.pushButtonClose.released.connect(self.close_window)
        self.pushButtonAdd.released.connect(self.add_button_clicked)

    @pyqtSlot()
    def close_window(self):
        self.close()

    @pyqtSlot()
    def add_button_clicked(self):
        """
        Добавление записи в БД установок
        :return:
        """
        print("add_button_clicked")