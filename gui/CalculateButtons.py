from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class CalculateButtons(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/CalculateButtons.ui', self)
        self.pushButtonInductor.released.connect(self.calculate_inductor)
        self.pushButtonForm.released.connect(self.calculate_form)
        self.pushButtonEps.released.connect(self.calculate_eps)
        self.pushButtonK1.released.connect(self.calculate_k1)
        print("buttons")


    @pyqtSlot()
    def calculate_inductor(self):
        print("calculate_inductor")

    @pyqtSlot()
    def calculate_eps(self):
        print("calculate_eps")

    @pyqtSlot()
    def calculate_k1(self):
        print("calculate_k1")

    @pyqtSlot()
    def calculate_form(self):
        print("calculate_form")