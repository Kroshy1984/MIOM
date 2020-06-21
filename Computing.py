# Длина деформируемой зоны LBT
# Название операции operation
# Диаметр наружной трубы DOT
# Толщина стенки трубы ST
# астота разрядного тока FW
# Глубина проникновения ИМП в материал заготовки BP
# обозначение удельного электрического сопротивления заготовки YEMP
# обозначение удельного электрического сопротивления материала индуктора YEMC
# собственное значение индукционного тока FWE
import math


class Inductor():
    def __init__(self, LBT, operation, DOT, ST, FW, YEMP, FCE, LCE, LCB, CCE, SC, HSC, PLM, BCM, KDM, MM, KPD,
                 geometry,NCT1,ZS,ZB,ZA,YEMC,LTC):
        mu = 4 * 3.14 * pow(10, -7)  # магнитная проницаемость в вакууме
        self.LBT = LBT
        self.operation = operation
        self.DOT = DOT
        self.ST = ST
        self.BCM = BCM
        self.KDM = KDM
        self.MM = MM
        # self.LBT=MM
        self.KPD = KPD
        self.ZS = ZS  # Толщина изоляции витка
        self.ZB = ZB  # Толщина основной изоляции индуктора
        self.ZA = ZA  # Толщина воздушного зазора
        self.LTC = LTC  # Индуктивность токоподводов индуктора
        self.YEMP = YEMP  # обозначение удельного электрического сопротивления заготовки
        self.YEMC = YEMC# удельное сопротивление шины(медь)
        self.FCE = FCE
        self.CCE = CCE  # емкость батареи конденсаторов МИУ
        self.LCE = LCE  # индуктивность собственная
        self.LCB = LCB  # индуктивность кабеля
        self.SC = SC  # шина изоляции
        self.HSC = HSC  # высота шины
        self.PLM = PLM  # плотность
        self.ZCP = self.ZS + self.ZB + self.ZA
        self.DCA = self.DOT + 2 * self.ST + 2 * self.ZCP
        self.FW = FW  # Частота разрядного тока
        self.BC = pow(self.YEMC / (3.14 * mu * self.FW), 0.5)  # Глубина проникновения ИМП в материал индуктор
        self.BP = pow(self.YEMP / (3.14 * mu * self.FW), 0.5)  # Глубина проникновения ИМП в материал заготовки
        self.NCT1=NCT1
        if self.BP > self.ST:
            self.FW = self.YEMP / (3.14 * mu * pow(self.ST, 2))
            print('FW=' + str(self.FW))
        if self.FW > self.FCE: print(
            "Значение Частоты разрядного тока превышает собственное значение индукционного тока")

        self.LDC = self.LCE + self.LCB + self.LTC  # Паразитная индуктивность разрядного контура
        self.FDC = math.sqrt(1 / (self.LDC * self.CCE)) / (
                    2 * 3.14)  # Частота разряда при наличии только паразитных индуктивностей
        self.K1 = (pow(self.FDC, 2) - pow(self.FW, 2)) / pow(self.FDC, 2)  # Величина коэффициента согласования
        self.ZEK = self.ZCP + 0.5 * (self.BC + self.BP)  # Значение эквивалентного зазора между индуктором и заготовкой
        self.LCA()
        self.NCTC = pow(abs(self.K1 * self.LDC * self.LCA / (3.14 * mu * self.DCA * self.ZEK * (1 - self.K1))),
                        0.5)  # Количество витков индуктора
        self.NCT = round(self.NCTC)  # Целое количество рабочих витков
        self.LU = self.SC * self.NCT  # Длина индуктора
        self.SCIC = (self.LCA / self.NCT)  # Расчетный шаг витков индуктора
        self.SSC = self.SCIC - self.ZS  # Ширина медной шины по оси индуктора
        self.ROC = self.DCA / 2  # наружный радиус индуктора
        self.RIC = self.ROC - self.HSC  # Внутренний радиус индуктора
        self.KEC = pow(((2 * self.ROC / self.RIC) * (self.ZEK / self.RIC) - 1), 2)
        self.NCWC = self.LBT / self.SCIC  # Расчетное количество рабочих витков
        self.NCW = round(self.NCWC)
        self.NCF = round(self.NCT - self.NCW)  # Количество свободных витков
        if self.NCF == 0:
            self.NCT = self.NCT1
            self.LU = self.SC * self.NCT  # Длина индуктора
            self.SCIC = (self.LCA / self.NCT)  # Расчетный шаг витков индуктора
            self.SSC = self.SCIC - self.ZS  # Ширина медной шины по оси индуктора
            self.ROC = self.DCA / 2  # наружный радиус индуктора
            self.RIC = self.ROC - self.HSC  # Внутренний радиус индуктора
            self.KEC = pow(((2 * self.ROC / self.RIC) * (self.ZEK / self.RIC) - 1), 2)
            self.NCWC = self.LBT / self.SCIC  # Расчетное количество рабочих витков
            self.NCW = round(self.NCWC)
            self.NCF = round(self.NCT - self.NCW)  # Количество свободных витков
        self.LCC = (3.14 * mu * (self.DCA + self.ZCP) * self.NCT * self.ZCP * self.NCT) / (self.KEC * self.LU)
        self.LUC2 = self.LCC
        f = Form(self.DOT, self.ST, self.BCM, self.KDM, self.MM, self.LBT, self.KPD, geometry, self.operation)
        self.VCR = math.sqrt(
            2 * f.WYD / self.PLM)  # Расчет режима обработки. Средняя скорость по деформируемому участку заготовки.
        self.LUC()
        self.PM = 4.4 * self.VCR * self.FR * self.PLM * self.ST  # Амплитудное значение давления ИМП
        self.SPYR = 0.141 * self.VCR / self.FR  # Величина перемещений заготовки на участке разгона
        # ================Расчет коэффициентов===================================================
        BRC = self.BC
        BRP = self.BP
        BLC = self.BC / 2
        BLP = self.BP / 2
        # ===============Диаметры===============================================
        DRC = self.DCA - BRC
        DRP = f.DIB + BRP
        DLP = f.DIB + BLP
        # ==================Коэффициенты==========================================
        ALFA = self.LU / f.DIB
        F = 22.7 / (1 + 2.35 * ALFA)
        # ===================Индуктивность и сопротивление заготовки================
        LP = F * DLP * pow(10, -7)
        RP = 3.14 * DRP * self.YEMP / (BRP * LBT)
        # =========================================================================
        self.QP = 2 * 3.14 * self.FR * LP / RP  # Добротность заготовки
        self.KZ = self.SSC * self.NCT / self.LU  # Коэффициент заполнения индуктора
        self.RC = 3.14 * DRC * self.YEMC / (BRC * self.LU * self.KZ)  # Сопротивление индуктора
        # =индуктивность однородная
        LOC = 3.14 * mu * self.DCA * self.LCA / (4 * self.LU)
        L1S = F * (self.DCA + self.ZCP) * pow(10, -7)
        LOCS = LOC / (pow(self.NCT, 2))
        LZSD = L1S / (1 + (L1S / LOCS) - (L1S / LOC))
        # =====Взаимная индуктивность индуктора и заготовки================================================
        self.M = math.sqrt(LP * math.fabs(L1S - LZSD))  # !!!!!!!!! поставил модуль
        QQ = math.pow(self.QP, 2)
        LSDQ = (LZSD * QQ + L1S) / (QQ + 1)
        MDL = math.pow((self.M / LP), 2)
        RSDQ = self.RC + MDL * QQ * RP / (QQ + 1)
        # ==========Суммарная добротность контура========================================================================
        QS = 2 * 3.14 * self.FR * LSDQ / RSDQ
        LOZ = 3.14 * mu * self.DCA / self.LU
        DL05 = L1S / LOZ
        DEZ = self.ZCP / DL05
        # =====K1=====
        self.K1 = 1 - pow(self.FR / self.FDC,2)
        print(self.K1)
        # ====K2======
        self.K2 = math.exp(-math.atan(2 * QS) / QS)
        # ===Коэффициент К3
        self.K3 = 1 / (1 + DEZ)
        self.LK = L1S / LZSD
        self.K4 = QQ / (QQ + self.LK)
        # Площадь создаваемого давления ИМП
        self.SUMP = 3.14 * (self.DCA + self.ZCP) * self.LU
        # Необходимая энергия разряда МИУ
        self.WR = self.PM * self.SUMP * (self.ZPR + 0.5 * self.SPYR) * self.KEC * self.KEC / (
                    self.K1 * self.K2 * self.K3 * self.K4)
        # Параметры разрядного тока.Значение тока I0 = IOO
        self.IOO = math.sqrt(2 * math.fabs(self.WR) / math.fabs(self.LCC + self.LDC))
        # Частота разрядного  тока
        self.FP = F
        # Декремент затухания
        self.DZT = RSDQ / (2 * LSDQ)

    def VCR(self):
        return self.VCR
    def PM(self):
        return self.PM

    def NCF(self):
        return self.NCF

    def NCWC(self):
        return self.NCWC

    def WR(self):
        return self.WR

    def M(self):
        return self.M

    def LCA(self):  # Длина индуктора
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

    def LUC(self):  # суммарная индуктивность
        mu = 4 * 3.17 * pow(10, -7)  # магнитная проницаемость в вакууме
        self.REZ = 1
        self.I = 0
        while abs(self.REZ) >= 0.01:
            LCP = self.LUC2 + self.LDC
            LUC1 = self.LUC2
            self.BC = pow(self.YEMC / (3.14 * mu * self.FW), 0.5)  # Глубина проникновения ИМП в материал индуктор
            self.BP = pow(self.YEMP / (3.14 * mu * self.FW), 0.5)  # Глубина проникновения ИМП в материал заготовки
            self.FR = (1 / (2 * 3.14)) * math.sqrt((1 / (LCP * self.CCE)))
            self.ZEK = self.ZCP + 0.5 * (self.BC + self.BP)
            for i in range(self.NCF):
                self.I = self.I + (math.sqrt(pow(self.SC * (self.NCF - 1) + self.ZS, 2) + pow(self.ZEK, 2)))
            self.ZPR = (self.ZEK * self.NCW + self.I) / self.NCT
            LCC = 3.14 * mu * self.NCT * (self.DCA + self.ZCP) * self.NCT * self.ZPR / (self.LU * self.KEC)
            self.LUC2 = LCC
            self.REZ = (self.LUC2 - LUC1) / LUC1
            #print(self.REZ)
        return self.LUC2

    def PWS(self):  # Проверка
        self.PWS = self.WR / (self.SSC * self.HSC)
        if self.PWS > pow(10, 9): print("возможно вам нужно провести расчет с большим диаметром шины")

    def DDP(self, geometry):
        f = Form(self.DOT, self.ST, self.BCM, self.KDM, self.MM, self.LBT, self.KPD, geometry, self.operation)
        if self.operation == "a1":
            self.DDP = self.RC - f.RIB - self.SPYR
        elif self.operation == "a2":
            self.DDP = geometry - f.RIB - self.SPYR
        elif self.operation == "a3":
            self.DDP = geometry - f.RIB - self.SPYR
        elif self.operation == "a4":
            self.DDP = geometry - self.SPYR
        elif self.operation == "b1":
            self.DDP = self.RC - f.RIB - self.SPYR
        return self.DDP



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
        self.WYD = (self.BCMD / (1 + self.MM)) * pow(self.EPS, (1 + self.MM))  # Удельная работа деформации WYD
        self.DVB = 3.14 * (self.DOT - self.ST) * self.ST * self.LBT  # Деформируемый объем заготовки DVB
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
            #self.EPS = ((self.RIB / geometry) - 1)
            self.EPS=0.02
        elif self.operation == "b2":
            self.EPS = (((geometry / self.RIB - 1) / 2) - 1) / 2
        elif self.operation == "b3":
            self.EPS = ((self.RIB / geometry) - 1) / math.sqrt(2)
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
        F = f"Внутренний диаметр трубчатой заготовки:{round(self.DIB,4)},м"
        F += f"\nВнутренний радиус трубчатой заготовки:{round(self.RIB,4)} ,м"
        F += f"\nCредняя величина деформации заготовки:{round(self.EPS,4)} ,м"
        F += f"\nДинамическое значение коэффициента аппроксимации кривой упрочнения:{round(self.BCMD,4)}"
        F += f"\nУдельная работа деформации:{round(self.WYD,4)},Дж"
        F += f"\nДеформируемый объем заготовки:{round(self.DVB,4)},mm3"
        F += f"\nРабота деформации заготовки:{round(self.WDB,4)} ,Дж"
        F += f"\nНеобходимая энергия для выполнения операции:{round(self.WMIR,4)},Дж"
        F += f"\nЭнергоемкость установки:{round(self.WMUR,4)},Дж"
        return F