from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
from Computing import *
# from core.FirstPhase import Form


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

        self.comboBoxOperationType.currentTextChanged.connect(self.changed_type)
        # self.comboBoxOperationType.currentTextChanged.emit(True, "Не выбрано")
        self.comboBoxOperationName.currentTextChanged.connect(self.changed)
        # self.comboBoxOperationName.currentTextChanged.emit(True, "Не выбрано")
        self.radioButtonCalc.setChecked(True)
        self.radioButtonCalc.toggled.connect(self.inductor_calculations_option)
        self.radioButtonCalc.toggled.emit(True)

        # self.pushButtonLoadParameters.released.connect(self.load_parameters)
        self.pushButtonCalcFirsPhase.released.connect(self.start_calc_first_phase)
        # self.lineEditRadius = QLineEdit()
        # self.labelRadius = QLabel()
        self.labelRadius.setVisible(False)
        self.lineEditRadius.setVisible(False)
        self.set_default_parameters()
        # шрифт MS Shell Dlg 2
        self.db_view = BaseView(caller_view=self)

    #
    #

    @pyqtSlot('QString')
    def changed_type(self, text):
        print("changed_type")
        print(text)
        if text == "Не выбрано":
            self.widget_2.setVisible(False)
        else:
            self.widget_2.setVisible(True)
            if text == "Обжим":
                self.labelDiameter.setText("Внутренний диаметр индуктора")
            else:
                self.labelDiameter.setText("Внешний диаметр индуктора")

    @pyqtSlot()
    def calculate_inductor(self):
        """
        Расчет индуктора
        :return:
        """
        print("calculate_inductor")
        self.get_parameters()
        print(self.operation)
        # try:
        #     float(self.DOT)
        # except:
        #     print("1")
        # try:
        #     float(self.ST)
        # except:
        #     print("2")
        a = Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                 float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        print(a)
        g = Inductor(float(self.LBT), self.operation, float(self.DOT), float(self.ST), float(self.FW),
                               float(self.YEMP), float(self.FCE), float(self.LCE), 1 * pow(10, -12),
                               float(self.CCE), float(self.SC), float(self.HSC), float(self.PLM), float(self.BCM),
                               float(self.KDM), float(self.MM), float(self.KPD),
                               float(self.RC), float(self.NCT1), float(self.ZS), float(self.ZB), float(self.ZA),
                               float(self.YEMC), float(self.LTC))
        print(g)

    @pyqtSlot('QString')
    def changed(self, text):
        print("changed")
        print(text)
        if text == "Не выбрано":
            self.labelRadius.setVisible(False)
            self.lineEditRadius.setVisible(False)
            return
        elif text in ["Формовка цилиндра", "Формовка конуса", "Формовка сферы", "Формовка рифтов"]:
            self.labelRadius.setVisible(True)
            self.lineEditRadius.setVisible(True)
            t = text.split()[1]
            if t == "конуса":
                label = "Максимальный радиус " + text.split()[1]
            else:
                label = "Радиус " + text.split()[1]
            self.labelRadius.setText(label)
            print(label)
            # self.

        # if
        # if self.comboBoxOperationName.

    @pyqtSlot(bool)
    def inductor_calculations_option(self, selected):
        """
        Блокирование полей ввода при автоматическом расчете индуктора
        :return:
        """
        if selected:
            print("выбран расчет")
            self.groupBox_7.setEnabled(False)
            self.flag=True
        else:
            self.groupBox_7.setEnabled(True)
            self.flag=False
        self.pushButtonCalcInductor.setEnabled(selected)
        print(self.flag)

    @pyqtSlot()
    def open_materials_db_billet(self):
        """
        Выбор материала для заготовки
        :return:
        """
        print("Open materials db")
        db_name = "Metalls.db"
        slot_name = "billet"
        sql = "select* from material"
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
        sql = "select* from material"
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
        sql = "select* from Mashines"
        self.db_view.show_db_view(db_name, sql, slot_name)

    @pyqtSlot()
    def start_calc_first_phase(self):  # рассчитать первый этап
        print("start_calc_first_phase")
        self._parent.secondary_parameters._show(True)
        self.get_parameters()
        print(self.operation)

        a = Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                 float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        print(a)

    @pyqtSlot()
    def load_parameters(self):
        print("load_parameters")

    def set_default_parameters(self):
        print("set_default_parameters")
        # self.lineEditBilletName.setText("Наименование")
        # self.lineEditOuterDiameter.setText("Наружный диаметр")
        # self.lineEditSideThickness.setText("Толщина стенки")
        # self.lineEditLengthDeform.setText("Длина деформируемой зоны")
        # self.lineEditBilletMaterial.setText("Материал")
        #
        # self.lineEditKPD.setText("КПД")
        # self.lineEditMachineName.setText("Оборудование")
        # self.lineEditMaterialInductor.setText("Метериал индуктора")
        # self.lineEditWidthCoilInductor.setText("Ширина витка по оси детали")
        # self.lineEditHeightCoilInductor.setText("Высота витка")
        # self.lineEditNumberCoilsInductor.setText("Количество витков")
        # self.lineEditSizeIsolationInductor.setText("Размер межвитковой изоляции")
        # self.lineEditInductance.setText("Индуктивность токоподводов индуктора")
        # self.lineEditA_tp.setText("A_ТП")
        # self.lineEditB_tp.setText("B_ТП")
        # self.lineEditHB_tp.setText("HB_ТП")
        # self.lineEditLB_tp.setText("LB_ТП")
        self.comboBoxOperationType.setCurrentIndex(1)
        self.comboBoxOperationName.setCurrentIndex(1)

        self.lineEditBilletName.setText("Наименование")
        self.lineEditOuterDiameter.setText("151.4")
        self.lineEditSideThickness.setText("1.2")
        self.lineEditLengthDeform.setText("30")
        self.lineEditBilletMaterial.setText("Материал")

        self.lineEditKPD.setText("0.03")
        self.lineEditMachineName.setText("Оборудование")
        # self.lineEditKP.setText("Кп_3%")
        # self.lineEditKappa.setText("Kappa")
        self.lineEditRadius.setText("75.2")
        self.lineEditGapWidth.setText("0.25")
        self.lineEditMainIsolation.setText("1")
        self.lineEditSizeIsolationInductor.setText("-")
        self.lineEditMaterialInductor.setText("Метериал индуктора")
        self.lineEditWidthCoilInductor.setText("4")
        self.lineEditHeightCoilInductor.setText("8")
        self.lineEditNumberCoilsInductor.setText("Количество витков")
        self.lineEditSizeIsolationInductor.setText("0.65")
        self.lineEditInductance.setText("0.07")
        self.lineEditA_tp.setText("A_ТП")
        self.lineEditB_tp.setText("B_ТП")
        self.lineEditHB_tp.setText("HB_ТП")
        self.lineEditLB_tp.setText("LB_ТП")

    def get_parameters(self):
        self.name = self.lineEditBilletName.text()
        self.DOT = self.lineEditOuterDiameter.text()
        self.ST = self.lineEditSideThickness.text()
        self.LBT = self.lineEditSideThickness.text()
        self.RC = self.lineEditLengthDeform.text()
        self.operation1 = self.comboBoxOperationType.currentText()
        self.operation2 = self.comboBoxOperationName.currentText()
        print(self.operation2)
        self.operation = self.get_operation()
        # if self.operation1 == "Раздача" and self.operation2 == "Формовка цилиндра":
        #     self.operation = "a1"
        print(self.operation)
        self.KPD = self.lineEditKPD.text()
        self.SC = self.lineEditSizeIsolationInductor.text()
        self.HSC =self.lineEditHeightCoilInductor.text()
        self.NCT1=11
        self.ZS =self.lineEditSizeIsolationInductor.text()
        self.ZB =self.lineEditMainIsolation.text()
        self.ZA =self.lineEditGapWidth.text()
        self.LTC=self.lineEditInductance.text()

    def set_billet_material(self, billet):
        self.billet_material = billet
        print("self.billet_material =", self.billet_material)
        self.name_mat = self.billet_material.get("Name")
        self.PLM = self.billet_material.get("PLM")  #
        self.MM = self.billet_material.get("M_M")  #
        self.BCM1 = self.billet_material.get("B")  #
        self.BCM = float(self.BCM1) * pow(10, 7)
        self.KDM = self.billet_material.get("KDM")
        self.YEMP = self.billet_material.get("YEMP")
        self.lineEditBilletMaterial.setText(self.name_mat)

    def set_inductor_material(self, inductor):
        self.inductor_material = inductor
        print("self.inductor_material =", self.inductor_material)
        self.name_in = self.inductor_material.get("Name")
        self.YEMC = self.inductor_material.get("YEMP")
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

    def get_operation(self):
        operation_name = ""
        type = self.comboBoxOperationType.currentText()
        print(type)
        if type == "Обжим":
            operation_name = "b"
        elif type == "Раздача":
            operation_name = "a"
        else:
            print("Not found operation type, choose from ComboBox!")
        # self.comboBoxOperationType.setCurrentIndex(1)
        name = self.comboBoxOperationName.currentIndex()
        print("name =", name)
        if 1 <= name <= 4:
            operation_name += str(name)
        return operation_name
