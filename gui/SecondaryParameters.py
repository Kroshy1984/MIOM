from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from gui.BaseView import BaseView
from Pascal import Pascal

from datetime import datetime


class SecondaryParameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/SecondaryParameters.ui', self)
        print("2")
        self.setVisible(False)
        self.pushButtonCalcSecondPhase.released.connect(self.start_calc_second_phase)
        self.pushButtonSaveParameters.released.connect(self.save_parameters)

        self.radioButtonManual.setChecked(True)
        self.radioButtonManual.toggled.connect(self.calculation_option_search)
        self.radioButtonManual.toggled.emit(True)

        self.checkBoxParametersControl.stateChanged.connect(self.change_parameters_control)
        # self.set_default_parameters()

    def set_blocked(self):
        print("set_blocked")

    def _show(self, flag, params, f):
        self.setVisible(flag)
        print("Параметры переданные из первой части \n", params)
        self.EPS = params.get("EPS")
        self.WR = params.get("WR")
        self.K1 = params.get("K1")
        self.K2 = params.get("K2")
        self.K3 = params.get("K3")
        self.K4 = params.get("K4")
        self.FP = params.get("FP")
        self.KEC = params.get("KEC")
        self.PM = params.get("PM")
        self.DZT = params.get("DZT")
        self.I00 = params.get("I00")
        self.name = params.get("name")
        self.operation = params.get("operation")
        self.PLM=params.get("PLM")
        self.LBT=params.get("LBT")
        self.DOT=params.get("DOT")
        self.ST=params.get("ST")
        self.YEMC=params.get("YEMC")
        self.LCE = params.get("LCE")
        self.CCE=params.get("CCE")
        self.R0=params.get("R0")
        self.YEMP = params.get("YEMP")
        self.NCT1 = params.get("NCT1")
        self.LCA = params.get("LCA")
        self.DCA = params.get("DCA")
        self.PPM = params.get("PPM")
        self.HSC=params.get("HSC")
        self.ZB = params.get("ZB")
        self.A_tp = params.get("A_tp")
        self.B_tp = params.get("B_tp")
        self.HB_tp = params.get("HB_tp")
        self.LB_tp = params.get("LB_tp")
        self.DIB = params.get("DIB")
        self.E_z = params.get("E_z")
        self.E_up = params.get("E_up")

        self.lineEditEps.setText(str(self.EPS))
        self.lineEditDischargeEnergy.setText(str(self.WR))
        self.lineEditK1.setText(str(self.K1))
        self.lineEditK2.setText(str(self.K2))
        self.lineEditK3.setText(str(self.K3))
        self.lineEditK4.setText(str(self.K4))
        self.lineEditFrequencyAmper.setText(str(self.FP))
        self.lineEditKe.setText(str(self.KEC))
        self.lineEditPressure.setText(str(self.PM))
        self.lineEditDelta.setText(str(self.DZT))
        self.lineEditI0.setText(str(self.I00))
        self.lineEdit_2.setText("0.03")
        self.lineEdit.setText("6000.0")
        self.lineEditAttenuationCoefField.setText("0.0")
        self.lineEditFieldFactor.setText("1.0")
        self.str = f
        self.kp1=0

    @pyqtSlot()
    def change_parameters_control(self, state):
        """
        Проверка состояния чекбокса контроля параметров
        :param state:
        :return:
        """
        if state == QtCore.Checked:
            self.kp1 = 1
        else:
            self.kp1 = 0

    @pyqtSlot()
    def start_calc_second_phase(self):
        """
        Начало расчета второй фазы
        :return:
        """
        self.U0=float(self.lineEdit.text())
        self.eps=float(self.lineEdit_2.text())
        self.kappa=float(self.lineEditFieldFactor.text())
        self.kn=float(self.lineEditAttenuationCoefField.text())
        calc={"U0":self.U0,"poisk":self.Poisk,"kp1":self.kp1,"eps":self.EPS,"pm":self.PLM,
              "l0":self.LBT,"dh":self.DOT,"h0":self.ST,"pl":self.YEMC,"ek":self.eps,
              "lm":self.LCE,"c0":self.CCE, "R0":self.R0, "p3":self.YEMP,"mod_upr":self.E_z,
              "a":self.A_tp,"b":self.B_tp, "hb":self.HB_tp, "lv":self.LB_tp,"dv":self.DIB,
              "nl":self.NCT1,"l1":self.LCA,"dn":self.DCA, "sp":self.PPM, "hl":self.HSC,
              "ey":self.E_up, "H_izol":self.ZB, "kappa":self.kappa,"kn":self.kn}
        f = Pascal(calc)
        print("start_calc_second_phase")
        print(f)
        self.make_file_second_way(f)

    def make_file(self):
        self.date = datetime.now()
        f_obj = open(f"{self.date}_{self.name}_{self.operation}.txt", "w", encoding='UTF-8')
        f_obj.write(self.str + "\n")
        f_obj.close()

    def make_file_second_way(self,f):
        f_obj = open(f"{self.date}_{self.name}_{self.operation}.txt", "a", encoding='UTF-8')
        f_obj.write("ВТОРОЙ ПУТЬ\n")
        f_obj.write(str(f) + "\n")
        f_obj.close()

    @pyqtSlot()
    def save_parameters(self):
        self.make_file()
        """
        Сохранение параметров расчета первого этапа в БД
        :return:
        """
        print("save_parameters")

    @pyqtSlot(bool)
    def calculation_option_search(self, selected):
        """
        Обработка : ручной или автоматический поиск
        :return:
        """
        print("calculation_option_search")
        if selected:
            # ручной
            self.Poisk = 1
        else:
            # автоматический
            self.Poisk = 0


    def set_default_parameters(self):
        print("set_default_parameters")
        self.lineEditAttenuationCoefField.setText("Коэффициент ослабления поля")
        self.lineEditFieldFactor.setText("Фактор поля в заготовке, %")
        self.lineEditPressure.setText("Давление")
        self.lineEditFrequencyAmper.setText("Частота разрядного тока")
        self.lineEditDischargeEnergy.setText("Энергия разряда")

        self.lineEditK1.setText("K1")
        self.lineEditK2.setText("K2")
        self.lineEditK3.setText("K3")
        self.lineEditK4.setText("K4")
        self.lineEditKe.setText("Ke")

        self.lineEditI0.setText("I0")
        # self.lineEditF.setText("F")
        self.lineEditDelta.setText("Delta")
        self.lineEditEps.setText(self.EPS)
