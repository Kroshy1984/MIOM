
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QPushButton, QHBoxLayout
from PyQt5.uic import loadUi
from gui.InitialParameters import InitialParameters
from gui.SecondaryParameters import SecondaryParameters
from gui.ThirdParams import ThirdParams
from gui.CalculateButtons import CalculateButtons
from gui.OutputWindow import OutputWindow
from gui.BaseView import BaseView

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('./gui/MainWindow.ui', self)
        self.setWindowTitle('Простой расчет формовки и параметров индуктора')
        vbox = QVBoxLayout()
        hbox_params = QHBoxLayout()
        inParam = InitialParameters()
        # secondParam = SecondParams()
        # thirdParam = ThirdParams()
        # hbox.addStretch(1)
        hbox_params.addWidget(inParam)
        # hbox_params.addWidget(secondParam)
        # hbox_params.addWidget(thirdParam)

        hbox_calculate = QHBoxLayout()
        calc = CalculateButtons()
        winout = OutputWindow()
        hbox_calculate.addWidget(calc)
        hbox_calculate.addWidget(winout)



        vbox.addLayout(hbox_params)
        vbox.addLayout(hbox_calculate)
        self.centralWidget().setLayout(vbox)

        self.db_view = BaseView()