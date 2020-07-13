from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
from Pascal import Pascal

from datetime import datetime


class SecondaryParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/SecondaryParameters.ui', self)
        print("2")
        self.setVisible(False)
        self.pushButtonCalcSecondPhase.released.connect(self.start_calc_second_phase)
        self.pushButtonSaveParameters.released.connect(self.save_parameters)

        self.radioButtonManual.setChecked(True)
        self.radioButtonManual.toggled.connect(self.calculation_option_search)
        self.radioButtonManual.toggled.emit(True)

        self.checkBoxParametersControl.stateChanged.connect(self.change_parameters_control)
        # self.set_default_parameters()

    def set_blocked(self):
        print("set_blocked")

    def _show(self, flag, params, f):
        self.setVisible(flag)
        print("Параметры переданные из первой части \n", params)
        self.EPS = params.get("EPS")
        self.WR = params.get("WR")
        self.K1 = params.get("K1")
        self.K2 = params.get("K2")
        self.K3 = params.get("K3")
        self.K4 = params.get("K4")
        self.FP = params.get("FP")
        self.KEC = params.get("KEC")
        self.PM = params.get("PM")
        self.DZT = params.get("DZT")
        self.I00 = params.get("I00")
        self.name = params.get("name")
        self.operation = params.get("operation")
        self.lineEditEps.setText(str(self.EPS))
        self.lineEditDischargeEnergy.setText(str(self.WR))
        self.lineEditK1.setText(str(self.K1))
        self.lineEditK2.setText(str(self.K2))
        self.lineEditK3.setText(str(self.K3))
        self.lineEditK4.setText(str(self.K4))
        self.lineEditFrequencyAmper.setText(str(self.FP))
        self.lineEditKe.setText(str(self.KEC))
        self.lineEditPressure.setText(str(self.PM))
        self.lineEditDelta.setText(str(self.DZT))
        self.lineEditI0.setText(str(self.I00))
        self.lineEdit_2.setText("0.03")
        self.str = f

    @pyqtSlot()
    def change_parameters_control(self, state):
        """
        Проверка состояния чекбокса контроля параметров
        :param state:
        :return:
        """
        if state == QtCore.Checked:
            self.kp1 = 1
        else:
            self.kp1 = 0

    @pyqtSlot()
    def start_calc_second_phase(self):
        """
        Начало расчета второй фазы
        :return:
        """
        f = Pascal()
        print("start_calc_second_phase")

    def make_file(self):
        date = datetime.now()
        f_obj = open(f"{date}_{self.name}_{self.operation}.txt", "w", encoding='UTF-8')
        f_obj.write(self.str + "\n")
        f_obj.close()

    @pyqtSlot()
    def save_parameters(self):
        self.make_file()
        """
        Сохранение параметров расчета первого этапа в БД
        :return:
        """
        print("save_parameters")

    @pyqtSlot(bool)
    def calculation_option_search(self, selected):
        """
        Обработка : ручной или автоматический поиск
        :return:
        """
        print("calculation_option_search")
        if selected:
            # ручной
            self.Poisk = 1
        else:
            # автоматический
            self.Poisk = 0


    def set_default_parameters(self):
        print("set_default_parameters")
        self.lineEditAttenuationCoefField.setText("Коэффициент ослабления поля")
        self.lineEditFieldFactor.setText("Фактор поля в заготовке, %")
        self.lineEditPressure.setText("Давление")
        self.lineEditFrequencyAmper.setText("Частота разрядного тока")
        self.lineEditDischargeEnergy.setText("Энергия разряда")

        self.lineEditK1.setText("K1")
        self.lineEditK2.setText("K2")
        self.lineEditK3.setText("K3")
        self.lineEditK4.setText("K4")
        self.lineEditKe.setText("Ke")

        self.lineEditI0.setText("I0")
        # self.lineEditF.setText("F")
        self.lineEditDelta.setText("Delta")
        self.lineEditEps.setText(self.EPS)
