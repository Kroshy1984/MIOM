from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class BaseView(QWidget):
    def __init__(self, db_name, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/BaseView.ui', self)
        self.pushButtonChoose.released.connect(self.choose_button_clicked)
        print("base")
        print(db_name)
        self.show()

    @pyqtSlot()
    def choose_button_clicked(self):
        """
        Выбран материал
        :return:
        """
        print("Choosed record")
        self.close()