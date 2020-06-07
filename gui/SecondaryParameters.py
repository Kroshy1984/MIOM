from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView

class SecondaryParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/SecondaryParameters.ui', self)
        print("2")
        self.setVisible(False)
        self.pushButtonCalcSecondPhase.released.connect(self.start_calc_second_phase)

    def set_blocked(self):
        print("set_blocked")

    def _show(self, flag):
        self.setVisible(flag)

    @pyqtSlot()
    def start_calc_second_phase(self):
        """
        Начало расчета второй фазы
        :return:
        """
        print("start_calc_second_phase")