from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
from Pascal import Pascal

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
        #self.set_default_parameters()

    def set_blocked(self):
        print("set_blocked")

    def _show(self, flag, params):
        self.setVisible(flag)
        print("Параметры переданные из первой части \n", params)
        self.EPS=params.get("EPS")
        self.WR=params.get("WR")
        self.K1=params.get("K1")
        self.K2=params.get("K2")
        self.K3=params.get("K3")
        self.K4=params.get("K4")
        self.lineEditEps.setText(str(self.EPS))
        self.lineEditDischargeEnergy.setText(str(self.WR))
        self.lineEditK1.setText(str(self.K1))
        self.lineEditK2.setText(str(self.K2))
        self.lineEditK3.setText(str(self.K3))
        self.lineEditK4.setText(str(self.K4))


    @pyqtSlot()
    def start_calc_second_phase(self):
        """
        Начало расчета второй фазы
        :return:
        """
        f = Pascal()
        print("start_calc_second_phase")


    @pyqtSlot()
    def save_parameters(self):
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
        #self.lineEditF.setText("F")
        self.lineEditDelta.setText("Delta")
        self.lineEditEps.setText(self.EPS)