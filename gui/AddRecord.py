from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView
from PyQt5.uic import loadUi
from utils.tex_to_qpixmap import mathTex_to_QPixmap

class AddRecord(QWidget):
    def __init__(self, parent=None, bd_view=None, record=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/AddRecord.ui', self)
        self._bd_view = bd_view
        self.label_2.setText("PPM_test")
        self.setWindowTitle("Добавление материала")
        headerLabels = [
            '$Название$',
            '$(PPM), \\sigma_{u} \cdot 10^7, Pa$',
            '$(PYM), \\sigma_{y} \cdot 10^7, Pa$',
            '$(PLM), \\rho_{u} \cdot 10^3, kg/m^3$',
            '$(MM), m_{m}$',
            '$(BCM), B \cdot 10^7, Pa$',
            '$(YEM), \\rho_{e} \cdot 10^{-8}, \Omega_{m}$',
            '$(KDM), K_{d} $',
            '$E_z, 10^7, Pa$',
            '$E_up, 10^7, Pa$'
            # '$C_{soil}=(1 - n) C_m + \\theta_w C_w$',
            # '$k_{soil}=\\frac{\\sum f_j k_j \\theta_j}{\\sum f_j \\theta_j}$',
            # '$\\lambda_{soil}=k_{soil} / C_{soil}$'
        ]
        # labels =
        qpixmaps = []
        indx = 0
        fontsize = 8
        for labels in headerLabels:
            print(labels)
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))
            # self.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            indx += 1
        print(qpixmaps)
        # self.label_3.setPixmap(qpixmaps[0])
        self.label_5.setPixmap(qpixmaps[0])
        self.label_2.setPixmap(qpixmaps[1])
        self.label_3.setPixmap(qpixmaps[2])
        self.label_4.setPixmap(qpixmaps[3])
        self.label.setPixmap(qpixmaps[4])
        self.label_6.setPixmap(qpixmaps[5])
        self.label_7.setPixmap(qpixmaps[6])
        self.label_8.setPixmap(qpixmaps[7])
        self.label_9.setPixmap(qpixmaps[8])
        self.label_10.setPixmap(qpixmaps[9])
        # mathTex_to_QPixmap(labels, fontsize)
        self.pushButtonClose.released.connect(self.close_window)
        self.pushButtonAdd.released.connect(self.add_button_clicked)
        if record is not None:
            self.setWindowTitle("Редактирование материала")
            self.pushButtonAdd.setText("Сохранить")
            print("Передана запись")
            print(record)
            self.set_record(record)
        # self.pushButtonChoose.released.connect(self.choose_button_clicked)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        # print("base")
        # self.tableView.clicked.connect(self.selectChanged)
        # self.pushButtonAddRecord.released.connect(self.add_button_clicked)

    @pyqtSlot()
    def close_window(self):
        self.close()

    @pyqtSlot()
    def add_button_clicked(self):
        """
        Добавление записи в БД материалов
        :return:
        """
        print("add_button_clicked")

    def set_record(self, record):
        self.lineEditName.setText(record['Name'])
        self.lineEditPPM.setText(str(record['PPM']))
        self.lineEditPYM.setText(str(record['PYD']))
        self.lineEditPLM.setText(str(record['PLM']))
        self.lineEditMM.setText(str(record['M_M']))
        self.lineEditBCM.setText(str(record['B']))
        self.lineEditYEM.setText(str(record['YEMP']))
        self.lineEditKDM.setText(str(record['KDM']))
        self.lineEditEz.setText(str(record['E_z']))
        self.lineEditEup.setText(str(record['E_up']))