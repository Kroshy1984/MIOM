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
        self.radioButtonCalc.toggled.connect(self.inductor_calculations_option)
        self.radioButtonCalc.toggled.emit(True)

        self.db_view = BaseView()

    @pyqtSlot(bool)
    def inductor_calculations_option(self, selected):
        """
        Блокирование полей ввода при автоматическом расчете индуктора
        :return:
        """
        print("inductor_calculations_option")
        print(selected)
        blocked = not selected
        self.lineEditWidthCoilInductor.setEnabled(blocked)
        self.lineEditHeightCoilInductor.setEnabled(blocked)
        self.lineEditNumberCoilsInductor.setEnabled(blocked)
        self.lineEditSizeIsolationInductor.setEnabled(blocked)
        self.lineEditInductance.setEnabled(blocked)
        self.lineEditA_tp.setEnabled(blocked)
        self.lineEditB_tp.setEnabled(blocked)
        self.lineEditHB_tp.setEnabled(blocked)
        self.lineEditLB_tp.setEnabled(blocked)
        # self.lineEditLB_tp.setText("0.1")
        self.pushButtonCalcInductor.setEnabled(selected)


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
