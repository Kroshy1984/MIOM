from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
from Computing import Form

class InitialParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._parent = parent
        loadUi('./gui/InitialParameters.ui', self)
        print("1")

        self.pushButtonMaterialBillet.released.connect(self.open_materials_db_billet)
        self.pushButtonMaterialInductor.released.connect(self.open_materials_db_inductor)
        self.pushButtonMachine.released.connect(self.open_machines_db)
        self.pushButtonCalcInductor.released.connect(self.calculate_inductor)

        self.comboBoxOperationType.addItems(["Не выбрано", "Обжим", "Раздача"])
        self.comboBoxOperationName.addItems(["Не выбрано",
                                             "Формовка цилиндра",
                                             "Формовка конуса",
                                             "Формовка сферы",
                                             "Формовка рифтов"])

        self.radioButtonCalc.setChecked(True)
        self.radioButtonCalc.toggled.connect(self.inductor_calculations_option)
        self.radioButtonCalc.toggled.emit(True)

        # self.pushButtonLoadParameters.released.connect(self.load_parameters)
        self.pushButtonCalcFirsPhase.released.connect(self.start_calc_first_phase)

        # self.set_default_parameters()
        self.db_view = BaseView(caller_view=self)

    @pyqtSlot()
    def calculate_inductor(self):#расчет индуктора
        self.get_parameters()
        print(self.operation)
        а = Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                 float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        """
        Расчет индуктора
        :return:
        """
        print("calculate_inductor")



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
        # self.lineEditInductance.setEnabled(blocked)
        # self.lineEditA_tp.setEnabled(blocked)
        # self.lineEditB_tp.setEnabled(blocked)
        # self.lineEditHB_tp.setEnabled(blocked)
        # self.lineEditLB_tp.setEnabled(blocked)
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
        slot_name = "billet"
        sql="select* from material"
        self.db_view.show_db_view(db_name, sql, slot_name)

    @pyqtSlot()
    def open_materials_db_inductor(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open materials ind db")
        db_name = "Metalls.db"
        slot_name = "inductor"
        sql="select* from material"
        self.db_view.show_db_view(db_name, sql, slot_name)

    @pyqtSlot()
    def open_machines_db(self):
        """
        Выбор материала для индуктора
        :return:
        """
        print("Open mashins ind db")
        db_name = "mashins.db"
        slot_name = "machines"
        sql="select* from Mashines"
        self.db_view.show_db_view(db_name, sql, slot_name)


    @pyqtSlot()
    def start_calc_first_phase(self): # рассчитать первый этап
        print("start_calc_first_phase")
        self._parent.secondary_parameters._show(True)
        self.get_parameters()
        print(self.operation)
        а=Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                           float(self.LBT), float(self.KPD), float(self.RC), self.operation)

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
        self.operation1=self.comboBoxOperationType.currentText()
        self.operation2=self.comboBoxOperationName.currentText()
        print(self.operation2)
        if self.operation1 == "Раздача" and self.operation2 == "Формовка цилиндра":
            self.operation="a1"
        self.KPD=self.lineEditKPD.text()

    def set_billet_material(self, billet):
        self.billet_material = billet
        print("self.billet_material =", self.billet_material)
        self.name_mat = self.billet_material.get("Name")
        self.PLM = self.billet_material.get("PLM")  #
        self.MM = self.billet_material.get("M_M")  #
        self.BCM1 = self.billet_material.get("B")  #
        self.BCM=float(self.BCM1) * pow(10, 7)
        self.KDM = self.billet_material.get("KDM")

        self.lineEditBilletMaterial.setText(self.name_mat)

    def set_inductor_material(self, inductor):
        self.inductor_material = inductor
        print("self.inductor_material =", self.inductor_material)
        self.name_in = self.inductor_material.get("Name")
        self.YEMP = self.inductor_material.get("YEMP")
        self.lineEditMaterialInductor.setText(self.name_in)


    def set_machine(self, machine):
        self.machine = machine
        print("self.machine =", self.machine)
        self.nama_mash = self.machine.get("Name")
        self.LCE = self.machine.get("LCE")
        self.CCE = self.machine.get("CCE")
        self.FCE = self.machine.get("FCE")
        self.FW = self.machine.get("FW")
        self.lineEditMachineName.setText(self.nama_mash)


