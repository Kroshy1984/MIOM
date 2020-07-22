from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog
from PyQt5.uic import loadUi
from utils.tex_to_qpixmap import mathTex_to_QPixmap
from utils.RegValidator import QRV

class AddRecord(QDialog):
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
        self.edit = False
        if record is not None:
            self.setWindowTitle("Редактирование материала")
            self.pushButtonAdd.setText("Сохранить")
            print("Передана запись")
            print(record)
            self.set_record(record)
            self.edit = True

        # lineedit = QtGui.QLineEdit(self)
        # validator = QDoubleValidator()
        # validator = QRV(r'^(?:\d{1,2})[.,]\d{2}$')
        # validator = QRV(r'^[-+]?[0-9]*[.,]?[0-9]+(?:[eE][-+]?[0-9]+)?$')
        validator = QRV(r'^(0|[1-9]\d*)([.,]\d+)?')
        self.lineEditPPM.setValidator(validator)
        self.lineEditPYM.setValidator(validator)
        self.lineEditPLM.setValidator(validator)
        self.lineEditMM.setValidator(validator)
        self.lineEditBCM.setValidator(validator)
        self.lineEditYEM.setValidator(validator)
        self.lineEditKDM.setValidator(validator)
        self.lineEditEz.setValidator(validator)
        self.lineEditEup.setValidator(validator)

        self.lineEditPPM.textChanged.connect(self.check_state)
        self.lineEditPYM.textChanged.connect(self.check_state)
        self.lineEditPLM.textChanged.connect(self.check_state)
        self.lineEditMM.textChanged.connect(self.check_state)
        self.lineEditBCM.textChanged.connect(self.check_state)
        self.lineEditYEM.textChanged.connect(self.check_state)
        self.lineEditKDM.textChanged.connect(self.check_state)
        self.lineEditEz.textChanged.connect(self.check_state)
        self.lineEditEup.textChanged.connect(self.check_state)
        # self.lineEditName.setText(record['Name'])
        # self.lineEditPPM.setText(str(record['PPM']))

        # self.pushButtonChoose.released.connect(self.choose_button_clicked)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        # print("base")
        # self.tableView.clicked.connect(self.selectChanged)
        # self.pushButtonAddRecord.released.connect(self.add_button_clicked)

    def __del__(self):
        print("del")

    @pyqtSlot()
    def close_window(self):
        self.close()

    def get_data(self):
        """
        Считывание данных формы в словарь
        :return:
        """
        current_record = dict()
        current_record['Name'] = self.lineEditName.text()
        current_record['PPM'] = self.lineEditPPM.text()
        current_record['PYD'] = self.lineEditPYM.text()
        current_record['PLM'] = self.lineEditPLM.text()
        current_record['M_M'] = self.lineEditMM.text()
        current_record['B'] = self.lineEditBCM.text()
        current_record['YEMP'] = self.lineEditYEM.text()
        current_record['KDM'] = self.lineEditKDM.text()
        if self.lineEditEz.text() == '':
            current_record['E_z'] = ''
        else:
            current_record['E_z'] = self.lineEditEz.text()
        if self.lineEditEup.text() == '':
            current_record['E_up'] = ''
        else:
            current_record['E_up'] = self.lineEditEup.text()

        # current_record['PPM'] = float(self.lineEditPPM.text())
        # current_record['PYD'] = float(self.lineEditPYM.text())
        # current_record['PLM'] = float(self.lineEditPLM.text())
        # current_record['M_M'] = float(self.lineEditMM.text())
        # current_record['B'] = float(self.lineEditBCM.text())
        # current_record['YEMP'] = float(self.lineEditYEM.text())
        # current_record['KDM'] = float(self.lineEditKDM.text())
        # if self.lineEditEz.text() == '':
        #     current_record['E_z'] = ''
        # else:
        #     current_record['E_z'] = float(self.lineEditEz.text())
        # if self.lineEditEup.text() == '':
        #     current_record['E_up'] = ''
        # else:
        #     current_record['E_up'] = float(self.lineEditEup.text())

        return current_record


    @pyqtSlot()
    def add_button_clicked(self):
        """
        Добавление записи в БД материалов
        :return:
        """
        print("add_button_clicked")
        current_record = self.get_data()
        print(current_record)
        self._bd_view.add_record(current_record, update=self.edit)
        self.close()


    def set_record(self, record):
        self.lineEditName.setText(str(record['Name']))
        self.lineEditPPM.setText(str(record['PPM']))
        self.lineEditPYM.setText(str(record['PYD']))
        self.lineEditPLM.setText(str(record['PLM']))
        self.lineEditMM.setText(str(record['M_M']))
        self.lineEditBCM.setText(str(record['B']))
        self.lineEditYEM.setText(str(record['YEMP']))
        self.lineEditKDM.setText(str(record['KDM']))
        self.lineEditEz.setText(str(record['E_z']))
        self.lineEditEup.setText(str(record['E_up']))

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