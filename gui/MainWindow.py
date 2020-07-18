
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QPushButton, QHBoxLayout
from PyQt5.uic import loadUi
from gui.InitialParameters import InitialParameters
from gui.SecondaryParameters import SecondaryParameters
from gui.OutputWindow import OutputWindow
from gui.BaseView import BaseView
from  gui.ResultsButtons import ResultsButtons

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('./gui/MainWindow.ui', self)
        self.setWindowTitle('Простой расчет формовки и параметров индуктора')
        vbox = QVBoxLayout()
        hbox_params = QHBoxLayout()
        self.initial_parameters = InitialParameters(parent=self)
        self.secondary_parameters = SecondaryParameters()
        # thirdParam = ThirdParams()
        # hbox.addStretch(1)
        hbox_params.addWidget(self.initial_parameters)
        hbox_params.addWidget(self.secondary_parameters)
        # hbox_params.addWidget(thirdParam)

        hbox_results = QHBoxLayout()
        self.res_buttons = ResultsButtons(parent=self)
        hbox_results.addWidget(self.res_buttons)

        self.winout = OutputWindow()
        # hbox_calculate.addWidget(calc)
        # hbox_calculate.addWidget(winout)



        vbox.addLayout(hbox_params)
        vbox.addLayout(hbox_results)
        self.centralWidget().setLayout(vbox)

        self.db_view = BaseView()

    def show_output_window(self, flag):
        self.winout.setVisible(flag)