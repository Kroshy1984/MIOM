
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/MainWindow.ui', self)
        pass