from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel
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
        # self.set_default_parameters()
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
            # self.groupBox_7.setVisible(True)
            # self.groupBox_8.setVisible(False)
            self.groupBox_7.setEnabled(False)
            # self.groupBox_8.setEnabled(False)
        else:
            # self.groupBox_7.setVisible(False)
            # self.groupBox_8.setVisible(True)
            self.groupBox_7.setEnabled(True)
            # self.groupBox_8.setEnabled(True)
        # print("inductor_calculations_option")
        # print(selected)
        # blocked = not selected
        # self.lineEditWidthCoilInductor.setEnabled(blocked)
        # self.lineEditHeightCoilInductor.setEnabled(blocked)
        # self.lineEditNumberCoilsInductor.setEnabled(blocked)
        # self.lineEditSizeIsolationInductor.setEnabled(blocked)
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
        # self.lineEditKP.setText("Кп_3%")
        # self.lineEditKappa.setText("Kappa")

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
        self.name = self.lineEditBilletName.text()
        self.DOT = self.lineEditOuterDiameter.text()
        self.ST = self.lineEditSideThickness.text()
        self.LBT = self.lineEditSideThickness.text()
        self.RC = self.lineEditLengthDeform.text()

    def set_billet_material(self, billet):
        self.billet_material = billet
        print("self.billet_material =", self.billet_material)
        self.name = self.billet_material.get("Name")
        self.PLM = self.billet_material.get("PLM")  #
        self.M_M = self.billet_material.get("M_M")  #
        self.BCM = self.billet_material.get("B")  #
        self.KDM = self.billet_material.get("KDM")
        self.lineEditBilletMaterial.setText(self.name)

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
