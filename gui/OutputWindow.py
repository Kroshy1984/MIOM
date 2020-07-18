
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.uic import loadUi

class OutputWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/OutputWindow.ui', self)
        print("output")
        main_vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        main_vbox.addLayout(hbox)

        # vbox.addLayout(hbox_calculate)
        self.setLayout(main_vbox)
