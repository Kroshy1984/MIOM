from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView
from PyQt5.uic import loadUi
from utils.tex_to_qpixmap import mathTex_to_QPixmap

class AddRecord(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/AddRecord.ui', self)
        self.label_2.setText("PPM_test")
        self.setWindowTitle("Добавление материала")
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
        # self.label_3.setPixmap(qpixmaps[0])
        self.label_2.setPixmap(qpixmaps[0])
        self.label_3.setPixmap(qpixmaps[1])
        self.label_4.setPixmap(qpixmaps[2])
        self.label.setPixmap(qpixmaps[3])
        self.label_6.setPixmap(qpixmaps[4])
        self.label_7.setPixmap(qpixmaps[5])
        self.label_8.setPixmap(qpixmaps[6])
        # mathTex_to_QPixmap(labels, fontsize)
        # self.pushButtonChoose.released.connect(self.choose_button_clicked)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        # print("base")
        # self.tableView.clicked.connect(self.selectChanged)
        # self.pushButtonAddRecord.released.connect(self.add_button_clicked)


