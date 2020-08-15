# Длина деформируемой зоны LBT
# Название операции operation
# Диаметр наружной трубы DOT
# Толщина стенки трубы ST
# астота разрядного тока FW
# Глубина проникновения ИМП в материал заготовки BP
# обозначение удельного электрического сопротивления заготовки YEMP
# обозначение удельного электрического сопротивления материала индуктора YEMC
# собственное значение индукционного тока FWE
# from math import sqrt, pow
import math


class Inductor():
    def __init__(self, LBT=0, operation="", DOT=0, ST=0, YEMP=0, FCE=0, LCE=0, LCB=0, CCE=0, SC=0, HSC=0, PLM=0,
                 BCM=0, KDM=0, MM=0, KPD=0,
                 geometry=0, NCT1=0, ZS=0, ZB=0, ZA=0, YEMC=0, LTC=0):
        # self.pi = math.pi
        self.pi = 3.1413926
        # self.mu = 4 * self.pi * math.pow(10, -7)  # магнитная проницаемость в вакууме
        self.mu = 0.000001256
        self.LBT = LBT
        self.operation = operation
        self.DOT = DOT
        self.ST = ST
        self.BCM = BCM
        self.KDM = KDM
        self.MM = MM
        self.KPD = KPD
        self.ZS = ZS  # Толщина изоляции витка индуктора
        self.ZB = ZB  # Толщина основной изоляции индуктора
        self.ZA = ZA  # Толщина воздушного зазора
        self.LTC = LTC  # Индуктивность токоподводов индуктора
        self.YEMP = YEMP  # обозначение удельного электрического сопротивления заготовки
        self.YEMC = YEMC  # удельное сопротивление шины(медь)
        self.FCE = FCE
        self.CCE = CCE  # емкость батареи конденсаторов МИУ
        self.LCE = LCE  # индуктивность собственная
        self.LCB = LCB  # индуктивность кабеля
        self.SC = SC  # шина изоляции (Ширина шины изоляции) Индуктора. Ширина витка по оси детали
        self.HSC = HSC  # высота шины
        self.PLM = PLM  # плотность
        self.geometry = geometry
        # self.FW = FW  # Частота разрядного тока
        self.NCT1 = NCT1
        self._mObservers = []  # список наблюдателей

    def set_data_from_dict(self, params):
        print("set_data_from_dict")
        print(params)
        self.LBT = params["LBT"]
        self.operation = params["operation"]
        self.DOT = params["DOT"]
        self.ST = params["ST"]
        # self.FW = params["FW"]
        self.YEMP = params["YEMP"]
        self.FCE = params["FCE"]
        self.LCE = params["LCE"]
        self.LCB = params["LCB"]
        self.CCE = params["CCE"]
        self.SC = params["SC"]
        self.HSC = params["HSC"]
        self.PLM = params["PLM"]
        self.BCM = params["BCM"]
        self.KDM = params["KDM"]
        self.MM = params["MM"]
        self.KPD = params["KPD"]
        self.geometry = params["RC"]
        self.NCT1 = params["NCT1"]
        self.ZS = params["ZS"]
        self.ZB = params["ZB"]
        self.ZA = params["ZA"]
        self.YEMC = params["YEMC"]
        self.LTC = params["LTC"]

    def set_data(self, LBT, operation, DOT, ST, YEMP, FCE, LCE, LCB, CCE, SC, HSC, PLM, BCM, KDM, MM, KPD,
                 geometry, NCT1, ZS, ZB, ZA, YEMC, LTC):
        self.LBT = LBT
        self.operation = operation
        self.DOT = DOT
        self.ST = ST
        self.BCM = BCM
        self.KDM = KDM
        self.MM = MM
        self.KPD = KPD
        self.ZS = ZS  # Толщина изоляции витка индуктора
        self.ZB = ZB  # Толщина основной изоляции индуктора
        self.ZA = ZA  # Толщина воздушного зазора
        self.LTC = LTC  # Индуктивность токоподводов индуктора
        self.YEMP = YEMP  # обозначение удельного электрического сопротивления заготовки
        self.YEMC = YEMC  # удельное сопротивление шины(медь)
        self.FCE = FCE
        self.CCE = CCE  # емкость батареи конденсаторов МИУ
        self.LCE = LCE  # индуктивность собственная
        self.LCB = LCB  # индуктивность кабеля
        self.SC = SC  # шина изоляции (Ширина шины изоляции) Индуктора. Ширина витка по оси детали
        self.HSC = HSC  # высота шины
        self.PLM = PLM  # плотность
        # self.ZCP = self.ZS + self.ZB + self.ZA
        # self.DCA = self.DOT + 2 * self.ST + 2 * self.ZCP
        # self.FW = FW  # Частота разрядного тока
        self.geometry = geometry
        self.NCT1 = NCT1

    def addObserver(self, inObserver):
        self._mObservers.append(inObserver)

    def removeObserver(self, inObserver):
        self._mObservers.remove(inObserver)

    def notifyObservers(self, message="", type=None):
        results = []
        for x in self._mObservers:
            users_result = x.modelIsChanged(message, type)
            results.append(users_result)
        return users_result

    def calculate_inductor_parameters(self):
        print("calculate_inductor_parameters")
        pi = self.pi
        mu = self.mu
        # ----- начало расчета -----
        self.LDC = self.LCE + self.LCB + self.LTC  # Паразитная индуктивность разрядного контура
        self.LDC = self.LCE + 7 * 10 ** (-8)
        self.FDC = math.sqrt(1 / (self.LDC * self.CCE)) / (
                    2 * pi)  # Частота разряда при наличии только паразитных индуктивностей
        FW8 = self.FDC * math.sqrt(0.2)

        self.FW = FW8

        self.ZCP = self.ZS + self.ZB + self.ZA
        # self.DCA = self.DOT + 2 * self.ST + 2 * self.ZCP
        if self.operation[0] == "a":  # раздача
            self.DCA = self.DOT - 2 * self.ST - 2 * self.ZCP
        elif self.operation[0] == "b":  # обжим
            self.DCA = self.DOT + 2 * self.ZCP
        # self.FW = FW  # Частота разрядного тока
        self.BC = math.sqrt(self.YEMC / (pi * mu * self.FW))  # Глубина проникновения ИМП в материал индуктор
        self.BP = math.sqrt(self.YEMP / (pi * mu * self.FW))  # Глубина проникновения ИМП в материал заготовки
        # self.NCT1 = NCT1
        if self.BP >= self.ST:
            self.FW = self.YEMP / (pi * mu * math.pow(self.ST, 2))
            print("FW=", self.FW)
        else:
            self.FW = FW8

        if self.FW > self.FCE:
            message = "Значение частоты разрядного тока превышает собственное значение индукционного тока. Продолжить расчет?"
            result = self.notifyObservers(message, type=1)
            print("Значение Частоты разрядного тока превышает собственное значение индукционного тока")
            # Если отказ, то прекращение расчетов
            if not result:
                return
        self.BC = math.sqrt(self.YEMC / (pi * mu * self.FW))  # Глубина проникновения ИМП в материал индуктор
        self.BP = math.sqrt(self.YEMP / (pi * mu * self.FW))  # Глубина проникновения ИМП в материал заготовки

        # self.FDC = math.sqrt(1 / (self.LDC * self.CCE)) / 2 * math.pi  # Частота разряда при наличии только паразитных индуктивностей
        self.K1 = (math.pow(self.FDC, 2) - math.pow(self.FW, 2)) / math.pow(self.FDC,
                                                                            2)  # Величина коэффициента согласования
        self.ZEK = self.ZCP + 0.5 * (self.BC + self.BP)  # Значение эквивалентного зазора между индуктором и заготовкой
        self.get_LCA()  # TODO
        # self.NCTC = math.sqrt(abs(self.K1 * self.LDC * self.LCA / (math.pi * mu * self.DCA * self.ZEK * (1 - self.K1))))  # Количество витков индуктора
        self.NCTC = math.sqrt(self.K1 * self.LDC * self.LCA / (
                pi * mu * self.DCA * self.ZEK * (1 - self.K1)))  # Количество витков индуктора
        self.NCT = round(self.NCTC)  # Целое количество рабочих витков
        self.LU = self.SC * self.NCT  # Длина индуктора
        self.SCIC = self.LCA / self.NCT  # Расчетный шаг витков индуктора
        # self.SSC = self.SCIC - self.ZS  # Ширина медной шины по оси индуктора
        self.SSC = self.SCIC - 2 * self.ZS  # Ширина медной шины по оси индуктора
        if self.operation[0] == "a":
            self.ROC = self.DCA / 2  # наружный радиус индуктора
            self.RIC = self.ROC - self.HSC  # Внутренний радиус индуктора
            self.KEC = math.pow(((2 * self.ROC / self.RIC) * (self.ZEK / self.RIC) - 1), 2)
        else:
            self.KEC = 1
        self.NCWC = self.LBT / self.SCIC  # Расчетное количество рабочих витков
        self.NCW = round(self.NCWC)
        self.NCF = self.NCT - self.NCW  # Количество свободных витков
        # TODO: неизвестный кусок
        # if self.NCF == 0:
        #     self.NCT = self.NCT1
        #     self.LU = self.SC * self.NCT  # Длина индуктора
        #     self.SCIC = (self.LCA / self.NCT)  # Расчетный шаг витков индуктора
        #     self.SSC = self.SCIC - self.ZS  # Ширина медной шины по оси индуктора
        #     if self.operation[0] == "a":
        #         self.ROC = self.DCA / 2  # наружный радиус индуктора
        #         self.RIC = self.ROC - self.HSC  # Внутренний радиус индуктора
        #         self.KEC = math.pow(((2 * self.ROC / self.RIC) * (self.ZEK / self.RIC) - 1), 2)
        #     else:
        #         self.KEC = 1
        #     self.NCWC = self.LBT / self.SCIC  # Расчетное количество рабочих витков
        #     self.NCW = round(self.NCWC)
        #     self.NCF = round(self.NCT - self.NCW)  # Количество свободных витков
        # TODO: неизвестный кусок
        # выбирать шину 4х8 4 - ширина 8 высота.
        self.LCC = (pi * mu * (self.DCA + self.ZCP) * self.NCT * self.ZCP * self.NCT) / (self.KEC * self.LU)
        if self.operation[0] == "b":  # если обжим
            self.LCC = (pi * mu * (self.DCA - self.ZCP) * self.NCT * self.ZCP * self.NCT) / (self.KEC * self.LU)
        self.LUC2 = self.LCC
        self.get_LUC()

        f = Form(self.DOT, self.ST, self.BCM, self.KDM, self.MM, self.LBT, self.KPD, self.geometry, self.operation)

        self.VCR = math.sqrt(
            2 * f.WYD / self.PLM)  # Расчет режима обработки. Средняя скорость по деформируемому участку заготовки.
        # self.LUC()
        self.PM = 4.4 * self.VCR * self.FR * self.PLM * self.ST  # Амплитудное значение давления ИМП
        self.SPYR = 0.141 * self.VCR / self.FR  # Величина перемещений заготовки на участке разгона
        if self.SPYR > (f.RIB - self.geometry):
            self.SPYR = f.RIB - self.geometry
        # ================Расчет коэффициентов===================================================
        BRC = self.BC
        BRP = self.BP
        BLC = self.BC / 2
        BLP = self.BP / 2
        # ===============Диаметры===============================================
        # DRC = self.DCA - BRC
        # DRP = f.DIB + BRP
        # DLP = f.DIB + BLP

        DRC = self.DCA - 2 * BRC
        DRP = f.DIB + 2 * BRP
        DLC = self.DCA - BLC
        DLP = f.DIB + BLP

        # ==================Коэффициенты==========================================
        ALFA = self.LU / f.DIB
        F = 22.7 / (1 + 2.35 * ALFA)
        # ===================Индуктивность и сопротивление заготовки================
        LP = F * DLP * math.pow(10, -7)
        RP = pi * DRP * self.YEMP / (BRP * self.LBT)
        # =========================================================================
        self.QP = 2 * pi * self.FR * LP / RP  # Добротность заготовки
        self.KZ = self.SSC * self.NCT / self.LU  # Коэффициент заполнения индуктора
        self.RC_ind = pi * DRC * self.YEMC / (BRC * self.LU * self.KZ)  # Сопротивление индуктора
        # =индуктивность однородная
        LOC = pi * mu * self.DCA * self.LCA / (4 * self.LU)
        L1S = F * (self.DCA + self.ZCP) * math.pow(10, -7)
        LOCS = LOC / (math.pow(self.NCT, 2))
        LZSD = L1S / (1 + (L1S / LOCS) - (L1S / LOC))
        # =====Взаимная индуктивность индуктора и заготовки================================================
        self.M = math.sqrt(LP * math.fabs(L1S - LZSD))  # !!!!!!!!! поставил модуль
        QQ = math.pow(self.QP, 2)
        print("QQ = ", QQ)
        LSDQ = (LZSD * QQ + L1S) / (QQ + 1)
        MDL = math.pow((self.M / LP), 2)
        RSDQ = self.RC_ind + MDL * QQ * RP / (QQ + 1)
        # ==========Суммарная добротность контура========================================================================
        QS = 2 * pi * self.FR * LSDQ / RSDQ
        LOZ = pi * mu * self.DCA / self.LU
        DL05 = L1S / LOZ
        DEZ = self.ZCP / DL05
        # =====K1=====
        self.K1 = 1 - pow(self.FR / self.FDC, 2)
        print(self.K1)
        # ====K2======
        self.K2 = math.exp(-math.atan(2 * QS) / QS)
        # ===Коэффициент К3
        self.K3 = 1 / (1 + DEZ)
        self.LK = L1S / LZSD
        self.K4 = QQ / (QQ + self.LK)
        # Площадь создаваемого давления ИМП
        if self.operation[0] == "a":
            self.SUMP = pi * (self.DCA + self.ZCP) * self.LU
        else:
            self.SUMP = pi * (self.DOT + self.ZCP) * self.LU
        # Необходимая энергия разряда МИУ
        self.WR = self.PM * self.SUMP * (self.ZPR + 0.5 * self.SPYR) * self.KEC * self.KEC / (
                self.K1 * self.K2 * self.K3 * self.K4)
        # Параметры разрядного тока.Значение тока I0 = IOO
        self.I00 = math.sqrt(2 * self.WR / math.fabs(self.LCC + self.LDC))
        # Частота разрядного  тока
        self.FP = F
        # Декремент затухания
        self.DZT = RSDQ / (2 * LSDQ)

    def KEC(self):
        return self.KEC

    def DZT(self):
        return self.DZT

    def FP(self):
        return self.FP

    def I00(self):
        return round(self.I00, 4)

    def VCR(self):
        return self.VCR

    def PM(self):  # Давление
        return self.PM

    def NCF(self):
        return self.NCF

    def NCWC(self):
        return self.NCWC

    def WR(self):
        return self.WR

    def M(self):
        return self.M

    def get_LCA(self):  # Длина индуктора
        if self.operation == "a1":
            self.LCA = 1.1 * self.LBT  # формовка цилиндра
        elif self.operation == "a2":
            self.LCA = 1.3 * self.LBT  # формовка конуса
        elif self.operation == "a3":
            self.LCA = self.LBT  # формовка сферы
        elif self.operation == "a4":
            self.LCA = 0.75 * self.LBT  # формовка рифта
        elif self.operation == "b1":
            self.LCA = 1.1 * self.LBT
        return self.LCA

    def ZCP(self):  # Величина зазора между индуктором и заготовкой
        return self.ZCP

    def DCA(self):  # диаметр индуктора
        return self.DCA

    def BP(self):  # Глубина проникновения ИМП в материал заготовки
        return self.BP

    def BC(self):  # Глубина проникновения ИМП в материал индуктор
        return self.BC

    def LDC(self):  # Паразитная индуктивность разрядного контура
        return self.LDC

    def FDC(self):  # Частота разряда при наличии только паразитных индуктивностей
        return self.FDC

    def K1(self):  # Коэффициент К1
        return self.K1

    def K2(self):  # Коэффициент К2
        return self.K2

    def K3(self):  # Коэффициент К3
        return self.K3

    def K4(self):  # Коэффициент К4
        return self.K4

    def ZEK(self):  # Значение эквивалентного зазора между индуктором и заготовкой
        return self.ZEK

    def NCTC(self):  # Количество витков индуктора
        return self.NCTC

    def NCW(self):
        return self.NCW  # Целое количество рабочих витков

    def NCF(self):
        return self.NCF  # Количество свободных витков

    def SCIC(self):  # Расчетный шаг витков индуктора
        return self.SCIC

    def SSC(self):  # Ширина медной шины по оси индуктора
        return self.SSC

    def ROC(self):  # наружный радиус индуктора
        return self.ROC

    def get_LUC(self):  # суммарная индуктивность
        pi = self.pi
        mu = self.mu
        # mu = 4 * pi * math.pow(10, -7)  # магнитная проницаемость в вакууме
        self.REZ = 1
        self.I = 0
        while abs(self.REZ) >= 0.01:
            LCP = self.LUC2 + self.LDC
            LUC1 = self.LUC2
            FP = (1 / (2 * pi)) * math.sqrt((1 / (LCP * self.CCE)))
            self.FR = FP
            self.BC = math.sqrt(self.YEMC / (pi * mu * FP))  # Глубина проникновения ИМП в материал индуктор
            self.BP = math.sqrt(self.YEMP / (pi * mu * FP))  # Глубина проникновения ИМП в материал заготовки
            # self.FR = (1 / (2 * 3.14)) * math.sqrt((1 / (LCP * self.CCE)))
            self.ZEK = self.ZCP + 0.5 * (self.BC + self.BP)
            self.I = 0
            for i in range(self.NCF):
                self.I = self.I + math.sqrt(math.pow(self.SC * (self.NCF - 1) + self.ZS, 2) + math.pow(self.ZEK, 2))
            self.ZPR = (self.ZEK * self.NCW + self.I) / self.NCT
            LCC = pi * mu * self.NCT * (self.DCA + self.ZCP) * self.NCT * self.ZPR / (self.LU * self.KEC)
            self.LUC2 = LCC
            self.REZ = (self.LUC2 - LUC1) / LUC1
            # print(self.REZ)
        return self.LUC2

    # TODO: процедура нигде не вызывается
    def PWS(self):  # Проверка
        self.PWS = self.WR / (self.SSC * self.HSC)
        if self.PWS > pow(10, 9):
            print("возможно вам нужно провести расчет с большим диаметром шины")
            message = "Возможно вам нужно провести расчет с большим сечением витка (Измените размеры витка индуктора). Продолжить расчет?"
            # TODO: изменить на кнопки Изменить или Отмена. Продолжать расчет нельзя
            result = self.notifyObservers(message, type=1)
            # Если отказ, то прекращение расчетов
            if not result:
                return

    # TODO: процедура нигде не вызывается
    def DDP(self, geometry):
        f = Form(self.DOT, self.ST, self.BCM, self.KDM, self.MM, self.LBT, self.KPD, geometry, self.operation)
        if self.operation == "a1":
            self.DDP = math.fabs(self.RC - f.RIB - self.SPYR)
        elif self.operation == "a2":
            self.DDP = math.fabs(geometry - f.RIB - self.SPYR)
        elif self.operation == "a3":
            self.DDP = math.fabs(geometry - f.RIB - self.SPYR)
        elif self.operation == "a4":
            self.DDP = math.fabs(geometry - self.SPYR)
        elif self.operation == "b1":
            self.DDP = math.fabs(self.RC - f.RIB - self.SPYR)
        return self.DDP

    def __str__(self):
        s = "\n" + "Длина индуктора (LCA):" + str(round(self.LCA, 4)) + ",м"
        s += "\n" + "Величина зазора между индуктором и заготовкой: (ZCP)" + str(round(self.ZCP, 4)) + ",м"
        s += "\n" + "Диаметр индуктора (DCA):" + str(round(self.DCA, 4)) + ",м"
        s += "\n" + "Глубина проникновения ИМП в материал заготовки (BP): " + str(round(self.BP, 4)) + " ,м"
        s += "\n" + "Глубина проникновения ИМП в материал индуктор (BC): " + str(round(self.BC, 4)) + " ,м"
        s += "\n" + "Паразитная индуктивность разрядного контура (LDC): " + str(round(self.LDC, 4)) + " ,Гн"
        s += "\n" + "Частота разряда при наличии только паразитных индуктивностей (FDC): " + str(
            round(self.FDC, 4)) + " ,Гц"
        s += "\n" + "Коэффициент К1: " + str(round(self.K1, 4))
        s += "\n" + "Коэффициент К2: " + str(round(self.K2, 4))
        s += "\n" + "Коэффициент К3: " + str(round(self.K3, 4))
        s += "\n" + "Коэффициент К4: " + str(round(self.K4, 4))
        s += "\n" + "Значение эквивалентного зазора между индуктором и заготовкой (ZEK): " + str(round(self.ZEK, 4))
        s += "\n" + "Количество витков индуктора (NCTC): " + str(round(self.NCTC, 4))
        s += "\n" + "Целое количество витков индуктора (NCW): " + str(round(self.NCW, 4))
        s += "\n" + "Расчетное количество рабочих витков (NCWC):" + str(round(self.NCWC, 4))
        s += "\n" + "Количество свободных витков (NCF)" + str(round(self.NCF, 4))
        s += "\n" + "Расчетный шаг витков индуктора (SCIC): " + str(round(self.SCIC, 4))
        s += "\n" + "Необходимая энергия разряда МИУ (WR): " + str(round(self.WR, 4)) + ",Дж"
        s += "\n" + "Суммарная индуктивность (LUC2): " + str(round(self.LUC2, 4)) + " ,Гн"
        s += "\n" + "Давление (PM): " + str(round(self.PM, 4)) + "Па"
        s += "\n" + "Скорость (VCR): " + str(round(self.VCR, 4)) + "м\с"
        return s


# Диаметр наружной трубы DOT
# Толщина стенки трубы ST
# Коэффициент динамичности материала KDM
# коэффициенты степенной аппроксимации кривой упрочнения материала MM
# длина деформированной зоны LBT
# коэффициент полезного действия  KPD
class Form():
    def __init__(self, DOT, ST, BCM, KDM, MM, LBT, KPD, geometry, operation):
        self.operation = operation
        self.DOT = DOT
        self.ST = ST
        self.BCM = BCM  # коэффициенты степенной аппроксимации кривой упрочнения материала
        self.KDM = KDM
        self.MM = MM
        self.LBT = LBT
        self.KPD = KPD
        self.DIB = self.DOT - 2 * self.ST  # Внутренний диаметр трубчатой заготовки
        self.RIB = self.DIB / 2  # Внутренний радиус трубчатой заготовки
        self.BCMD = self.BCM * self.KDM  # Динамическое значение коэффициента аппроксимации кривой упрочнения
        EPS = self.EPS(geometry)
        print(EPS)
        print(1 + EPS)
        self.WYD = (self.BCMD / (1 + self.MM)) * math.pow(self.EPS, (1 + self.MM))  # Удельная работа деформации WYD
        self.DVB = math.pi * (self.DOT - self.ST) * self.ST * self.LBT  # Деформируемый объем заготовки DVB
        self.WDB = self.WYD * self.DVB  # Работа деформации заготовки WDB
        self.WMIR = self.WDB / self.KPD  # Необходимая энергия для выполнения операции WMIR
        self.WMUR = self.WMIR * 1.2  # Энергоемкость установки WMUR

    def DIB(self):  # Внутренний диаметр трубчатой заготовки
        return self.DIB

    def RIB(self):  # Внутренний радиус трубчатой заготовки
        return self.RIB

    def EPS(self, geometry):  # cредняя величина деформации ESR заготовки
        if self.operation == "a1":
            self.EPS = (geometry / self.RIB) - 1
        elif self.operation == "a2":
            self.EPS = (geometry / (self.RIB - 1)) / 2
        elif self.operation == "a3":
            self.EPS = (geometry / (self.RIB - 1)) / pow(2, 0.5)
        elif self.operation == "a4":
            self.EPS = (3.14 * geometry) / (self.RIB * 4)
        elif self.operation == "b1":
            self.EPS = ((self.RIB / geometry) - 1)
            # self.EPS=0.02
        elif self.operation == "b2":
            self.EPS = (((geometry / self.RIB - 1) / 2) - 1) / 2
        elif self.operation == "b3":
            self.EPS = ((self.RIB / geometry) - 1) / math.sqrt(2)
        elif self.operation == "b4":
            self.EPS = (3.14 * geometry) / (self.RIB * 4)
        return self.EPS

    def BCMD(self):  # Динамическое значение коэффициента аппроксимации кривой упрочнения
        return self.BCMD

    def WYD(self):  # Удельная работа деформации WYD
        return self.WYD

    def DVB(self):  # Деформируемый объем заготовки DVB
        return self.DVB

    def WDB(self):  # Работа деформации заготовки WDB
        return self.WDB

    def WMIR(self):  # Необходимая энергия для выполнения операции WMIR
        return self.WMIR

    def WMUR(self):  # Энергоемкость установки
        return self.WMUR

    def __str__(self):
        F = f"Внутренний диаметр трубчатой заготовки (DIB):{round(self.DIB, 4)},м"
        F += f"\nВнутренний радиус трубчатой заготовки (RIB):{round(self.RIB, 4)} ,м"
        F += f"\nCредняя величина деформации заготовки (EPS):{round(self.EPS, 4)} ,м"
        F += f"\nДинамическое значение коэффициента аппроксимации кривой упрочнения (BCMD):{round(self.BCMD, 4)}"
        F += f"\nУдельная работа деформации (WYD):{round(self.WYD, 4)},Дж"
        F += f"\nДеформируемый объем заготовки (DVB):{round(self.DVB, 4)},mm3"
        F += f"\nРабота деформации заготовки (WDB):{round(self.WDB, 4)} ,Дж"
        F += f"\nНеобходимая энергия для выполнения операции (WMIR):{round(self.WMIR, 4)},Дж"
        F += f"\nЭнергоемкость установки (WMUR):{round(self.WMUR, 4)},Дж"
        return F
