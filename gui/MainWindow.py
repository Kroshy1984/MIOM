
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
from gui.InitialParameters import InitialParameters
from gui.SecondaryParameters import SecondaryParameters
from gui.OutputWindow import OutputWindow
from gui.BaseView import BaseView
from  gui.ResultsButtons import ResultsButtons

class MainWindow(QMainWindow):
    def __init__(self, model, controller, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('./gui/MainWindow.ui', self)
        self.mModel = model
        self.mController = controller
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

    def get_inductor_parameters(self):
        """
        Собирает параметры индуктора из полей ввода
        :return:
        """
        params = self.initial_parameters.get_inductor_parameters()

        return params

    def show_message(self, text, type=None):
        if type==None:
            type = QMessageBox.Warning
            print(QMessageBox.Warning)
            title = "Предупреждение"
        msg = QMessageBox()
        msg.setIcon(type)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()
        print("Нет выбранных строк")