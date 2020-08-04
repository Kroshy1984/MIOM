import os
from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel
from PyQt5.uic import loadUi


class ResultsButtons(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._parent = parent
        loadUi('./gui/ResultsButtons.ui', self)
        # print("ResultsButtons")
        self.pushButtonAllResults.released.connect(self.all_results_button_clicked)
        self.pushButtonResultsFirstPhase.released.connect(self.first_phase_results_button_clicked)
        self.pushButtonResultsSecondPhase.released.connect(self.second_phase_results_button_clicked)
        self.set_active_all_results_button(False)
        self.set_active_first_phase_button(False)
        self.set_active_second_phase_button(True)

    @pyqtSlot()
    def all_results_button_clicked(self):
        print("all_results_button_clicked")


    @pyqtSlot()
    def first_phase_results_button_clicked(self):
        """
        Открывается текстовый файл редактором по умолчанию
        TODO: передать нужное имя файла
        :return:
        """
        print("first_phase_results_button_clicked")
        # self._parent.show_output_window(True)

        filename = "C:\Work\PyCharmProjects\MIOM\\buf.txt"
        try:
            os.startfile(filename)
        except FileNotFoundError:
            print("File not found")

    @pyqtSlot()
    def second_phase_results_button_clicked(self):
        # print("second_phase_results_button_clicked")
        self._parent.winout._show()


    def set_active_first_phase_button(self, state):
        self.pushButtonResultsFirstPhase.setEnabled(state)

    def set_active_second_phase_button(self, state):
        self.pushButtonResultsSecondPhase.setEnabled(state)

    def set_active_all_results_button(self, state):
        self.pushButtonAllResults.setEnabled(state)
