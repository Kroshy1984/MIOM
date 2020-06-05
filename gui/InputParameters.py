
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class InputParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/InputParameters.ui', self)
        print("1")
