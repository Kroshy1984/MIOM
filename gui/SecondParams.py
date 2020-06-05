from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
class SecondParams(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/SecondParams.ui', self)
        print("2")
        self.pushButtonMatZag.released.connect(self.open_materials_db_zag)
        self.pushButtonMatInd.released.connect(self.open_materials_db_ind)
        self.pushButtonUst.released.connect(self.open_mashins_db)

    @pyqtSlot()
    def open_materials_db_zag(self):
        """
        Выбор материала для заготовки
        :return:
        """
        print("Open materials db")
        db_name = "Metalls.db"
        self.db_view = BaseView(db_name)

    @pyqtSlot()
    def open_materials_db_ind(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open materials ind db")
        db_name = "Metalls.db"
        self.db_view = BaseView(db_name)

    @pyqtSlot()
    def open_mashins_db(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open mashins ind db")
        db_name = "mashins.db"
        self.db_view = BaseView(db_name)