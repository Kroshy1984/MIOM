from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog
from PyQt5.uic import loadUi
from utils.tex_to_qpixmap import mathTex_to_QPixmap

class AddMachine(QDialog):
    def __init__(self, parent=None, record=None):
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
        if record is not None:
            self.setWindowTitle("Редактирование установки")
            self.pushButtonAdd.setText("Сохранить")
            print("Передана запись")
            print(record)
            self.set_record(record)

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

    def set_record(self, record):
        self.lineEditName.setText(record['Name'])
        self.lineEditWME.setText(str(record['W_mash']))
        self.lineEditCCE.setText(str(record['CCE']))
        self.lineEditLCE.setText(str(record['LCE']))
        self.lineEditFCE.setText(str(record['FCE']))
        self.lineEditFW8.setText(str(record['Ro']))
        self.lineEditFW9.setText(str(record['FW']))
        # self.lineEditKDM.setText(str(record['KDM']))
        # self.lineEditEz.setText(str(record['E_z']))
        # self.lineEditEup.setText(str(record['E_up']))