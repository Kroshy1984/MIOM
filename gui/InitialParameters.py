from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView

class InitialParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/InitialParameters.ui', self)
        print("1")

        self.pushButtonMaterialBillet.released.connect(self.open_materials_db_billet)
        self.pushButtonMaterialInductor.released.connect(self.open_materials_db_inductor)
        self.pushButtonMachine.released.connect(self.open_machines_db)

        self.radioButtonCalc.setChecked(True)
        # self.radioButtonCalc.toggled.connect(self.inductor_calculations_option())

        self.db_view = BaseView()

    def inductor_calculations_option(self):
        """
        Блокирование полей ввода при автоматическом расчете индуктора
        :return:
        """
        print("inductor_calculations_option")
        # self.lineEditWidthCoilInductor.setReadOnly(True)

    @pyqtSlot()
    def open_materials_db_billet(self):
        """
        Выбор материала для заготовки
        :return:
        """
        print("Open materials db")
        db_name = "Metalls.db"
        self.db_view.show_db_view(db_name)

    @pyqtSlot()
    def open_materials_db_inductor(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open materials ind db")
        db_name = "Metalls.db"
        self.db_view.show_db_view(db_name)

    @pyqtSlot()
    def open_machines_db(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open mashins ind db")
        db_name = "mashins.db"
        self.db_view.show_db_view(db_name)
