from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView

class InitialParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._parent = parent
        loadUi('./gui/InitialParameters.ui', self)
        print("1")

        self.pushButtonMaterialBillet.released.connect(self.open_materials_db_billet)
        self.pushButtonMaterialInductor.released.connect(self.open_materials_db_inductor)
        self.pushButtonMachine.released.connect(self.open_machines_db)

        self.comboBoxOperationType.addItems(["Не выбрано", "Обжим", "Раздача"])
        self.comboBoxOperationName.addItems(["Не выбрано",
                                             "Формовка цилиндра",
                                             "Формовка конуса",
                                             "Формовка сферы",
                                             "Формовка рифтов"])

        self.radioButtonCalc.setChecked(True)
        self.radioButtonCalc.toggled.connect(self.inductor_calculations_option)
        self.radioButtonCalc.toggled.emit(True)

        self.pushButtonLoadParameters.released.connect(self.load_parameters)
        self.pushButtonCalcFirsPhase.released.connect(self.start_calc_first_phase)

        # self.set_default_parameters()
        self.db_view = BaseView()

    @pyqtSlot(bool)
    def inductor_calculations_option(self, selected):
        """
        Блокирование полей ввода при автоматическом расчете индуктора
        :return:
        """
        # print("inductor_calculations_option")
        # print(selected)
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
        sql="select* from material"
        self.db_view.show_db_view(db_name, sql)

    @pyqtSlot()
    def open_materials_db_inductor(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open materials ind db")
        db_name = "Metalls.db"
        sql="select* from material"
        self.db_view.show_db_view(db_name,sql)

    @pyqtSlot()
    def open_machines_db(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open mashins ind db")
        db_name = "mashins.db"
        self.db_view.show_db_view(db_name)

    @pyqtSlot()
    def start_calc_first_phase(self):
        print("start_calc_first_phase")
        self._parent.secondary_parameters._show(True)
        self.get_parameters()



    @pyqtSlot()
    def load_parameters(self):
        print("load_parameters")

    def set_default_parameters(self):
        print("set_default_parameters")
        self.lineEditBilletName.setText("Наименование")
        self.lineEditOuterDiameter.setText("Наружный диаметр")
        self.lineEditSideThickness.setText("Толщина стенки")
        self.lineEditLengthDeform.setText("Длина деформируемой зоны")
        self.lineEditBilletMaterial.setText("Материал")

        self.lineEditKPD.setText("КПД")
        self.lineEditMachineName.setText("Оборудование")
        self.lineEditKP.setText("Кп_3%")
        self.lineEditKappa.setText("Kappa")

        self.lineEditMaterialInductor.setText("Метериал индуктора")
        self.lineEditWidthCoilInductor.setText("Ширина витка по оси детали")
        self.lineEditHeightCoilInductor.setText("Высота витка")
        self.lineEditNumberCoilsInductor.setText("Количество витков")
        self.lineEditSizeIsolationInductor.setText("Размер межвитковой изоляции")
        self.lineEditInductance.setText("Индуктивность токоподводов индуктора")
        self.lineEditA_tp.setText("A_ТП")
        self.lineEditB_tp.setText("B_ТП")
        self.lineEditHB_tp.setText("HB_ТП")
        self.lineEditLB_tp.setText("LB_ТП")

    def get_parameters(self):
        self.name=self.lineEditBilletName.text()
        self.DOT=self.lineEditOuterDiameter.text()
        self.ST=self.lineEditSideThickness.text()
        self.LBT=self.lineEditSideThickness.text()
        self.RC=self.lineEditLengthDeform.text()




