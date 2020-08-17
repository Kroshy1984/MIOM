import math

from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
# from Computing import *
from core.FirstPhase import Inductor, Form
# from core.FirstPhase import Form
from datetime import datetime
from utils.RegValidator import QRV


class InitialParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._parent = parent
        loadUi('./gui/InitialParameters.ui', self)

        self.pushButtonMaterialBillet.released.connect(self.open_materials_db_billet)
        self.pushButtonMaterialInductor.released.connect(self.open_materials_db_inductor)
        self.pushButtonMachine.released.connect(self.open_machines_db)

        # self.pushButtonCalcInductor.released.connect(self.calculate_inductor)
        self.pushButtonCalcInductor.released.connect(self._parent.mController.start_inductor_calculation)

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
        self.set_validators()
        # шрифт MS Shell Dlg 2
        self.db_view = BaseView(caller_view=self)

    #
    #

    @pyqtSlot('QString')
    def changed_type(self, text):
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
        self.groupBox_7.setEnabled(True)
        self.get_parameters()

        a = Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                 float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        print(a)
        g = Inductor(float(self.LBT), self.operation, float(self.DOT), float(self.ST),
                     float(self.YEMP), float(self.FCE), float(self.LCE), 1 * pow(10, -12),
                     float(self.CCE), float(self.SC), float(self.HSC), float(self.PLM), float(self.BCM),
                     float(self.KDM), float(self.MM), float(self.KPD),
                     float(self.RC), float(self.NCT1), float(self.ZS), float(self.ZB), float(self.ZA),
                     float(self.YEMC), float(self.LTC))
        print(g)

        self.lineEditNumberCoilsInductor.setText(str(round(g.NCTC)))
        self.lineEditDiameter.setText(str(round(g.DCA, 4)))
        self.lineEditInductorLength.setText(str(round(g.LCA, 4)))

    @pyqtSlot('QString')
    def changed(self, text):
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

    @pyqtSlot(bool)
    def inductor_calculations_option(self, selected):
        """
        Блокирование полей ввода при автоматическом расчете индуктора
        :return:
        """
        if selected:
            self.groupBox_7.setEnabled(False)
            self.flag = True
        else:
            self.groupBox_7.setEnabled(True)
            self.flag = False
        self.pushButtonCalcInductor.setEnabled(selected)

    @pyqtSlot()
    def open_materials_db_billet(self):
        """
        Выбор материала для заготовки
        :return:
        """
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
        db_name = "mashins.db"
        slot_name = "machines"
        sql = "select* from Machines"
        self.db_view.show_db_view(db_name, sql, slot_name)

    @pyqtSlot()
    def start_calc_first_phase(self):  # рассчитать первый этап
        self._parent.res_buttons.set_active_first_phase_button(True)
        self.get_parameters()
        a = Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                 float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        print(a)
        g = Inductor(float(self.LBT), self.operation, float(self.DOT), float(self.ST),
                     float(self.YEMP), float(self.FCE), float(self.LCE), 1 * pow(10, -12),
                     float(self.CCE), float(self.SC), float(self.HSC), float(self.PLM), float(self.BCM),
                     float(self.KDM), float(self.MM), float(self.KPD),
                     float(self.RC), float(self.NCT1), float(self.ZS), float(self.ZB), float(self.ZA),
                     float(self.YEMC), float(self.LTC))
        print(g)
        self.make_file(g, a)

        params = {"WR": round(g.WR, 4), "I00": g.I00, "FP": round(g.FP, 4), "DZT": round(g.DZT, 4),
                  "KEC": round(g.KEC, 4), "EPS": round(a.EPS, 4), "K1": round(g.K1, 4), "K2": round(g.K2, 4),
                  "K3": round(g.K3, 4), "K4": round(g.K4, 4), "PM": round(g.PM, 4), "name": self.name,
                  "operation": self.operation, "PLM": self.PLM, "LBT": self.LBT, "DOT": self.DOT,
                  "ST": self.ST, "YEMC": self.YEMC, "LCE": self.LCE, "CCE": self.CCE, "R0": self.R0,
                  "YEMP": self.YEMP, "NCT1": self.NCT1, "LCA": round(g.LCA, 4), "DCA": round(g.DCA, 4),
                  "PPM": self.PPM, "HSC": self.HSC, "ZB": self.ZB, "A_tp": self.A_tp, "B_tp": self.B_tp,
                  "HB_tp": self.HB_tp, "LB_tp": self.LB_tp, "DIB": round(a.DIB, 4),
                  "E_up": self.E_up, "E_z": self.E_z

                  }
        print(params)
        self._parent.secondary_parameters._show(True, params, self.f)

    def make_file(self, g, a):
        date = datetime.now()
        self.f = "П Р О Т О К О Л    Р А С Ч Е Т А" + "\n"
        self.f += "ИСХОДНЫЕ ДАННЫЕ" + "\n"
        self.f += f"Название заготовки - {self.name}" + "\n"
        self.f += f"Диаметр наружной трубы - {self.DOT}" + "\n"
        self.f += f"коэффициенты степенной аппроксимации кривой упрочнения материала BCM - {self.BCM}" + "\n"
        self.f += f"коэффициент динамичности материала - {self.KDM}" + "\n"
        self.f += f"коэффициенты степенной аппроксимации кривой упрочнения материала MM - {self.MM}" + "\n"
        self.f += f"длина деформированной зоны - {self.LBT}" + "\n"
        self.f += f"Операция - {self.operation}" + "\n"
        self.f += f"КПД - {self.KPD}" + "\n"
        self.f += f"геометрические параметры заготовки - {self.RC}" + "\n"
        self.f += f"Частота тока - {self.FW}" + "\n"
        self.f += f"Удельное электрическое сопротивление материала заготовки - {self.YEMP}" + "\n"
        self.f += f"Удельное электрическое сопротивление материала индуктора - {self.YEMC}" + "\n"
        self.f += f"Частота колебаний разрядного тока МИУ в режиме короткого замыкания- {self.FCE}" + "\n"
        self.f += f"Индуктивность колебаний разрядного тока МИУ в режиме короткого замыкания- {self.LCE}" + "\n"
        self.f += f"емкость батареи конденсаторов МИУ - {self.CCE}" + "\n"
        self.f += f"Длина витка индуктора - {self.SC}" + "\n"
        self.f += f"Высота витка индуктора - {self.HSC}" + "\n"
        self.f += f"Плотность материала - {self.PLM}" + "\n"
        self.f += f"коэффициент динамичности материала - {self.KDM}" + "\n"
        self.f += f"Реальное количество витков - {self.NCT1}" + "\n"
        self.f += f"Толщина изоляции витка- {self.ZS}" + "\n"
        self.f += f"Толщина основной изоляции - {self.ZB}" + "\n"
        self.f += f" Толщина воздушного зазора индуктора- {self.ZA}" + "\n"
        self.f += f" Индуктивность токоподводов индуктора- {self.LTC}" + "\n"
        self.f += f"Р Е З У Л Ь Т А Т" + "\n"
        self.f += str(a) + "\n"
        self.f += str(g) + '\n'

    @pyqtSlot()
    def load_parameters(self):
        print("load_parameters")

    def set_default_parameters(self):
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
        self.lineEditRadius.setText("73.95")
        self.lineEditGapWidth.setText("0.25")
        self.lineEditMainIsolation.setText("1")
        self.lineEditSizeIsolationInductor.setText("-")
        self.lineEditMaterialInductor.setText("Метериал индуктора")
        self.lineEditWidthCoilInductor.setText("4")
        self.lineEditHeightCoilInductor.setText("8")
        self.lineEditNumberCoilsInductor.setText("Количество витков")
        self.lineEditSizeIsolationInductor.setText("0.65")
        self.lineEditInductance.setText("0.07")
        self.lineEditA_tp.setText("1.00")
        self.lineEditB_tp.setText("1.00")
        self.lineEditHB_tp.setText("1.00")
        self.lineEditLB_tp.setText("1.00")

    def set_validators(self):
        validator = QRV()
        self.lineEditBilletName.setText("Наименование")
        self.lineEditOuterDiameter.setValidator(validator)
        self.lineEditSideThickness.setValidator(validator)
        self.lineEditLengthDeform.setValidator(validator)
        self.lineEditBilletMaterial.setText("Материал")

        self.lineEditKPD.setValidator(validator)
        self.lineEditMachineName.setText("Оборудование")
        # self.lineEditKP.setText("Кп_3%")
        # self.lineEditKappa.setText("Kappa")
        self.lineEditRadius.setValidator(validator)
        self.lineEditGapWidth.setValidator(validator)
        self.lineEditMainIsolation.setValidator(validator)
        self.lineEditSizeIsolationInductor.setValidator(validator)
        self.lineEditDiameter.setValidator(validator)
        self.lineEditInductorLength.setValidator(validator)
        self.lineEditMaterialInductor.setText("Метериал индуктора")
        self.lineEditWidthCoilInductor.setValidator(validator)
        self.lineEditHeightCoilInductor.setValidator(validator)
        self.lineEditNumberCoilsInductor.setValidator(validator)
        self.lineEditSizeIsolationInductor.setValidator(validator)
        self.lineEditInductance.setValidator(validator)
        self.lineEditA_tp.setValidator(validator)
        self.lineEditB_tp.setValidator(validator)
        self.lineEditHB_tp.setValidator(validator)
        self.lineEditLB_tp.setValidator(validator)

    def get_inductor_parameters(self):
        self.get_parameters()
        # params = dict()
        # a = Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
        #          float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        # print(a)


        # p1_form = dict()
        # p1_form["DOT"] = self.DOT
        # p1_form["ST"] = self.ST
        # p1_form["BCM"] = self.BCM
        # p1_form["KDM"] = self.KDM
        # p1_form["MM"] = self.MM
        # p1_form["LBT"] = self.LBT
        # p1_form["KPD"] = self.KPD
        # p1_form["RC"] = self.RC
        # p1_form["operation"] = self.operation
        # print(p1_form)
        p2_form = dict()
        # g = Inductor(float(self.LBT), self.operation, float(self.DOT), float(self.ST), float(self.FW),
        #              float(self.YEMP), float(self.FCE), float(self.LCE), 1 * pow(10, -12),
        #              float(self.CCE), float(self.SC), float(self.HSC), float(self.PLM), float(self.BCM),
        #              float(self.KDM), float(self.MM), float(self.KPD),
        #              float(self.RC), float(self.NCT1), float(self.ZS), float(self.ZB), float(self.ZA),
        #              float(self.YEMC), float(self.LTC))

        p2_form["LBT"] = self.LBT
        p2_form["operation"] = self.operation
        p2_form["DOT"] = self.DOT
        p2_form["ST"] = self.ST
        # p2_form["FW"] = self.FW
        p2_form["YEMP"] = self.YEMP
        p2_form["FCE"] = self.FCE
        p2_form["LCE"] = self.LCE
        # p2_form["LCB"] = pow(10, -12)
        p2_form["LCB"] = 0
        p2_form["CCE"] = self.CCE
        p2_form["SC"] = self.SC
        p2_form["HSC"] = self.HSC
        p2_form["PLM"] = self.PLM
        p2_form["PYM"] = self.PYM
        p2_form["BCM"] = self.BCM
        p2_form["KDM"] = self.KDM
        p2_form["MM"] = self.MM
        p2_form["KPD"] = self.KPD
        p2_form["RC"] = self.RC
        p2_form["NCT1"] = self.NCT1
        p2_form["ZS"] = self.ZS
        p2_form["ZB"] = self.ZB
        p2_form["ZA"] = self.ZA
        p2_form["YEMC"] = self.YEMC
        p2_form["LTC"] = self.LTC
        return p2_form


        # self.name = self.lineEditBilletName.text()
        # self.DOT = float(self.lineEditOuterDiameter.text()) * pow(10, -3)
        # self.ST = float(self.lineEditSideThickness.text()) * pow(10, -3)
        # self.LBT = float(self.lineEditSideThickness.text()) * pow(10, -3)
        # self.RC = float(self.lineEditLengthDeform.text()) * pow(10, -3)
        # self.operation1 = self.comboBoxOperationType.currentText()
        # self.operation2 = self.comboBoxOperationName.currentText()
        # self.operation = self.get_operation()
        # # if self.operation1 == "Раздача" and self.operation2 == "Формовка цилиндра":
        # #     self.operation = "a1"
        # self.KPD = self.lineEditKPD.text()
        # self.SC = float(self.lineEditSizeIsolationInductor.text()) * pow(10, -3)
        # self.HSC = float(self.lineEditHeightCoilInductor.text()) * pow(10, -3)
        # self.NCT1 = 11
        # self.ZS = float(self.lineEditSizeIsolationInductor.text()) * pow(10, -3)
        # self.ZB = float(self.lineEditMainIsolation.text()) * pow(10, -3)
        # self.ZA = float(self.lineEditGapWidth.text()) * pow(10, -3)
        # self.LTC = float(self.lineEditInductance.text()) * pow(10, -7)
        # self.A_tp = self.lineEditA_tp.text()
        # self.B_tp = self.lineEditB_tp.text()
        # self.HB_tp = self.lineEditHB_tp.text()
        # self.LB_tp = self.lineEditLB_tp.text()



    def get_parameters(self):
        """
        Считывание данных с формы
        :return:
        """
        self.name = self.lineEditBilletName.text()
        self.DOT = float(self.lineEditOuterDiameter.text()) * pow(10, -3)
        self.ST = float(self.lineEditSideThickness.text()) * pow(10, -3)
        self.LBT = float(self.lineEditLengthDeform.text()) * pow(10, -3)
        self.RC = float(self.lineEditRadius.text()) * pow(10, -3) # радиус цилиндра
        self.operation1 = self.comboBoxOperationType.currentText()
        self.operation2 = self.comboBoxOperationName.currentText()
        self.operation = self.get_operation()
        # if self.operation1 == "Раздача" and self.operation2 == "Формовка цилиндра":
        #     self.operation = "a1"
        self.KPD = float(self.lineEditKPD.text())
        self.SC = float(self.lineEditSizeIsolationInductor.text()) * pow(10, -3)
        self.HSC = float(self.lineEditHeightCoilInductor.text()) * pow(10, -3)
        self.NCT1 = 11
        self.ZS = float(self.lineEditSizeIsolationInductor.text()) * pow(10, -3)
        self.ZB = float(self.lineEditMainIsolation.text()) * pow(10, -3)
        self.ZA = float(self.lineEditGapWidth.text()) * pow(10, -3)
        self.LTC = float(self.lineEditInductance.text()) * pow(10, -6)
        self.A_tp = self.lineEditA_tp.text()
        self.B_tp = self.lineEditB_tp.text()
        self.HB_tp = self.lineEditHB_tp.text()
        self.LB_tp = self.lineEditLB_tp.text()

    def set_billet_material(self, billet):
        self.billet_material = billet
        self.name_mat = self.billet_material.get("Name")
        self.PLM = float(self.billet_material.get("PLM"))  #
        self.PYM = float(self.billet_material.get("PYD"))
        self.MM = self.billet_material.get("M_M")  #
        self.BCM1 = self.billet_material.get("B")  #
        self.BCM = float(self.BCM1) * pow(10, 7)
        self.KDM = self.billet_material.get("KDM")
        self.YEMP = float(self.billet_material.get("YEMP")) * pow(10, -8)
        self.PPM = float(self.billet_material.get("PPM")) * pow(10, 7)
        self.E_up = self.billet_material.get("E_up")
        self.E_z = self.billet_material.get("E_z")
        self.lineEditBilletMaterial.setText(self.name_mat)

    def set_inductor_material(self, inductor):
        self.inductor_material = inductor
        self.name_in = self.inductor_material.get("Name")
        self.YEMC = float(self.inductor_material.get("YEMP")) * pow(10, -8)
        self.lineEditMaterialInductor.setText(self.name_in)

    def set_machine(self, machine):
        self.machine = machine
        self.nama_mash = self.machine.get("Name")
        self.LCE = float(self.machine.get("LCE")) * pow(10, -9)
        self.CCE = float(self.machine.get("CCE")) * pow(10, -6)
        self.FCE = float(self.machine.get("FCE"))
        # self.FW = float(self.machine.get("FW"))
        self.R0 = float(self.machine.get("R0")) * math.pow(10, 6)
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
        if 1 <= name <= 4:
            operation_name += str(name)
        return operation_name
