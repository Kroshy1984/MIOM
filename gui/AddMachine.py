from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog
from PyQt5.uic import loadUi
from utils.tex_to_qpixmap import mathTex_to_QPixmap
from utils.RegValidator import QRV

class AddMachine(QDialog):
    def __init__(self, parent=None, bd_view=None, record=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/AddMachine.ui', self)
        self._bd_view = bd_view
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

        self.edit = False
        if record is not None:
            self.setWindowTitle("Редактирование установки")
            self.pushButtonAdd.setText("Сохранить")
            print("Передана запись")
            print(record)
            self.set_record(record)
            self.edit = True


        # validator = QDoubleValidator()
        validator = QRV(r'^(0|[1-9]\d*)([.,]\d+)?')
        # self.lineEditName.setText(record['Name'])
        self.lineEditWME.setValidator(validator)
        self.lineEditCCE.setValidator(validator)
        self.lineEditLCE.setValidator(validator)
        self.lineEditFCE.setValidator(validator)
        self.lineEditFW8.setValidator(validator)
        self.lineEditFW9.setValidator(validator)

        self.lineEditWME.textChanged.connect(self.check_state)
        self.lineEditCCE.textChanged.connect(self.check_state)
        self.lineEditLCE.textChanged.connect(self.check_state)
        self.lineEditFCE.textChanged.connect(self.check_state)
        self.lineEditFW8.textChanged.connect(self.check_state)
        self.lineEditFW9.textChanged.connect(self.check_state)


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
        current_record = self.get_data()
        print(current_record)
        self._bd_view.add_record(current_record, update=self.edit)
        self.close()



    def get_data(self):
        """
                Считывание данных формы в словарь
                :return:
                """
        current_record = dict()

        current_record['Name'] = self.lineEditName.text()
        current_record['W_mash'] = self.lineEditWME.text()
        current_record['CCE'] = self.lineEditCCE.text()
        current_record['LCE'] = self.lineEditLCE.text()
        current_record['FCE'] = self.lineEditFCE.text()
        current_record['Ro'] = self.lineEditFW8.text()
        current_record['FW'] = self.lineEditFW9.text()
        return current_record

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

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)