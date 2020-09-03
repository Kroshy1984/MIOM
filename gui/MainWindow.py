
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
from gui.InitialParameters import InitialParameters
from gui.PMDialog import PMDialog
from gui.SecondaryParameters import SecondaryParameters
from gui.OutputWindow import OutputWindow
from gui.BaseView import BaseView
from  gui.ResultsButtons import ResultsButtons

class MainWindow(QMainWindow):
    def __init__(self, model, model_2, controller, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('./gui/MainWindow.ui', self)
        self.mModel = model
        self.mModel_2 = model_2
        self.mController = controller
        self.setWindowTitle('Простой расчет формовки и параметров индуктора')
        vbox = QVBoxLayout()
        hbox_params = QHBoxLayout()
        self.initial_parameters = InitialParameters(parent=self)
        self.secondary_parameters = SecondaryParameters(parent=self)
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

    def get_second_phase_params(self):
        params = self.secondary_parameters.get_parameters()
        return params

    def show_message(self, text, type=None, data=None):
        msg = QMessageBox()

        if type==None:
            type = QMessageBox.Warning
            print(QMessageBox.Warning)
            title = "Предупреждение"
        elif type == 1:
            type = QMessageBox.Question
            print(QMessageBox.Question)
            title = "Продолжить работу?"
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttonY = msg.button(QMessageBox.Yes)
            buttonY.setText('Да')
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Нет')
        elif type == 2:
            # окно выбора модели процесса
            dialog = PMDialog(data=data)

            bb = dialog.buttonBox
            bb.accepted.connect(dialog.accept)
            bb.rejected.connect(dialog.reject)
            # dialog.show()
            res = dialog.exec_()
            print("res = ", res)
            check = dialog.checked
            if res==0:
                return False
            elif res ==1:
                return True, check
            else:
                return False
        elif type == 3:
            # type = QMessageBox.Warning
            print(QMessageBox.Warning)
            title = "Предупреждение"
            msg.setIcon(type)
            msg.setText(text)
            msg.setWindowTitle(title)
            msg.exec_()
            return False


        msg.setIcon(type)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()
        if type == QMessageBox.Question:
            if msg.clickedButton() == buttonY:
                print("Нажато ДА")
                return True
            # YES pressed
            elif msg.clickedButton() == buttonN:
                print("Нажато Нет")
                return False
            # NO pressed
        print("Нет выбранных строк")
        return None