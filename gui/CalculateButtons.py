
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class CalculateButtons(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/CalculateButtons.ui', self)
        print("buttons")
