#Длина деформируемой зоны LBT
#Название операции operation
#Диаметр наружной трубы DOT
#Толщина стенки трубы ST
#астота разрядного тока FW
#Глубина проникновения ИМП в материал заготовки BP
#обозначение удельного электрического сопротивления заготовки YEMP
#обозначение удельного электрического сопротивления материала индуктора YEMC
#собственное значение индукционного тока FWE
import math
class Inductor():
    def __init__(self,LBT,operation,DOT,ST,FW,YEMP,YEMC,FCE,FWE,LCE, LCB,CCE,SC, HSC,PLM):
        mu = 4 * 3.17 * pow(10, -7)# магнитная проницаемость в вакууме
        self.LBT=LBT
        self.operation=operation
        self.DOT=DOT
        self.ST=ST
        self.ZS=0.65 # Толщина изоляции медной шины
        self.ZB=1.0 # Толщина основной изоляции индуктора
        self.ZA=0.25 #Толщина воздушного зазора
        self.LTC=0.7*pow(10,-7)#Индуктивность токов индуктора
        self.YEMP=YEMP#обозначение удельного электрического сопротивления заготовки
        self.YEMC=YEMC
        self.FCE=FCE
        self.FWE=FWE
        self.CCE=CCE# емкость батареи конденсаторов МИУ
        self.LCE=LCE#индуктивность собственная
        self.LCB=LCB#индуктивность кабеля
        self.SC=SC # шина изоляции
        self.HSC=HSC#высота шины
        self.PLM=PLM#плотность
        self.ZCP = self.ZS + self.ZB + self.ZA
        self.DCA = self.DOT - 2 * self.ST - 2 * self.ZCP
        self.FW=FW#Частота разрядного тока
        self.BC = pow((self.YEMC / (3.14 * mu *self.FW),0.5))#Глубина проникновения ИМП в материал индуктор
        self.BP=pow((self.YEMP / (3.14 * mu * self.FW),0.5))#Глубина проникновения ИМП в материал заготовки
        if self.BP>self.ST:self.FW = self.YEMP / (3.14 * mu * pow(self.ST, 2))
        if self.FW > self.FWE:print("Значение Частоты разрядного тока превышает собственное значение индукционного тока")
        self.LU = self.SC * self.NCT#Длина индуктора
        self.LDC=self.LCE + self.LCB + self.LTC#Паразитная индуктивность разрядного контура
        self.FDC = pow((1 / (self.LDC * self.CCE)),0.5) / 2 * 3.14#Частота разряда при наличии только паразитных индуктивностей
        self.K1 = (pow(self.FDC, 2) - pow(self.FW, 2)) /pow(self.FDC,2)#Величина коэффициента согласования
        self.ZEK = self.ZCP + 0.5*(self.BC + self.BP)#Значение эквивалентного зазора между индуктором и заготовкой
        self.NCTC = pow(self.K1 * self.LDC * self.LCA / (3.14 * mu * self.DCA * self.ZEK * (1-self.K1)),0.5)#Количество витков индуктора
        self.NCT = round(self.NCTC)#Целое количество рабочих витков
        self.SCIC = self.LCA / self.NCT#Расчетный шаг витков индуктора
        self.SSC = self.SCIC - self.ZS#Ширина медной шины по оси индуктора
        self.ROC = self.DCA / 2# наружный радиус индуктора
        self.RIC = self.ROC - self.HSC#Внутренний радиус индуктора
        self.KEC =pow(((2*self.ROC / self.RIC) * (self.ZEK / self.RIC)- 1), 2)
        self.NCWC = self.LBT / self.SCIC#Расчетное количество рабочих витков
        self.NCW = round(self.NCWC)#Целое количество рабочих витков
        self.NCF = self.NCT - self.NCW#Количество свободных витков
        self.LCC = (3.14 * mu * (self.DCA +self.ZCP) * self.NCT * self.ZCP *self.NCT) / (self.KEC * self.LU)
        self.LUC2 = self.LCC
        f=Form()
        self.VCR = math.sqrt(2 *f.WYD / self.PLM)#Расчет режима обработки. Средняя скорость по деформируемому участку заготовки.
        self.LUC()
        self.PM = 4.4 * self.VCR * self.FR * self.PLM * self.ST#Амплитудное значение давления ИМП
        self.SPYR = 0.141 * self.VCR / self.FR#Величина перемещений заготовки на участке разгона
        #================Расчет коэффициентов===================================================
        BRC = self.BC
        BRP = self.BP
        BLC = self.BC / 2
        BLP = self.BP / 2
        #===============Диаметры==================================================================
        DRC = self.DCA - 2 * BRC
        DRP = self.DIB + 2 * BRP
        DLC = self.DCA - BLC
        DLP = self.DIB + BLP
        #==================Коэффициенты==========================================
        ALFA = self.LU / self.DIB
        F = 22.7 / (1 + 2.35 * ALFA)
    def LCA(self):
        if self.operation=="a1":self.LCA=1.1*self.LBT #формовка цилиндра
        elif self.operation=="a2":self.LCA=1.3*self.LBT#формовка конуса
        elif self.operation=="a3":self.LCA=self.LBT#формовка сферы
        elif self.operation=="a4":self.LCA=0.75*self.LBT#формовка рифта
        return self.LCA
    def ZCP(self):#Величина зазора между индуктором и заготовкой
        return self.ZCP
    def DCA(self):
        return self.DCA
    def BP(self):#Глубина проникновения ИМП в материал заготовки
        return self.BP
    def BC(self):#Глубина проникновения ИМП в материал индуктор
        return self.BC
    def LDC(self):#Паразитная индуктивность разрядного контура
        return self.LDC
    def FDC(self):#Частота разряда при наличии только паразитных индуктивностей
        return self.FDC
    def K1(self):#Частота разряда при наличии только паразитных индуктивностей
        return self.K1
    def ZEK(self):#Значение эквивалентного зазора между индуктором и заготовкой
        return self.ZEK
    def NCTC(self):#Количество витков индуктора
        return self.NCTC
    def NCW(self):
        return self.NCW#Целое количество рабочих витков
    def NCF(self):
        return self.NCF#Количество свободных витков
    def SCIC(self):#Расчетный шаг витков индуктора
        return self.SCIC
    def SSC(self):#Ширина медной шины по оси индуктора
        return self.SSC
    def ROC(self):# наружный радиус индуктора
        return self.ROC
    def LUC(self):#суммарная индективность
        mu = 4 * 3.17 * pow(10, -7)  # магнитная проницаемость в вакууме
        while abs(self.REZ)>0.01:
            LCP = self.LUC2 +self.LDC
            LUC1 = self.LUC2
            self.FR = (1 / (2 * 3.14)) * math.sqrt(1 / (LCP * self.CCE))
            BC=self.BC()
            BP=self.BP()
            ZEK = self.ZCP + 0.5 * (BC + BP)
            I=0
            for i in range(self.NCF):
                I=i+(math.sqrt(pow(self.SC*(self.NCF-1)+self.ZS),2)+pow(self.ZEK,2))/self.NCT
            ZPR=self.ZEK*self.NCW+I
            LCC = 3.14 * mu * self.NCT * (self.DCA + self.ZCP) * self.NCT * ZPR / (self.LU * self.KEC)
            self.LUC2=LCC
            self.REZ = (self.LUC2 - LUC1) / LUC1
        return self.LUC2
#Диаметр наружной трубы DOT
#Толщина стенки трубы ST
#Коэффициент динамичности материала KDM
#коэффициенты степенной аппроксимации кривой упрочнения материала MM
#длина деформированной зоны LBT
# коэффициент полезного действия  KPD
class Form():
    def __init__(self,DOT,ST,BCM,KDM,MM,LBT,KPD,operation):
        self.operation=operation
        self.DOT=DOT
        self.ST=ST
        self.BCM=BCM
        self.KDM=KDM
        self.MM=MM
        self.LBT=LBT
        self.KPD=KPD
        self.DIB = self.DOT - 2 * self.ST #Внутренний диаметр трубчатой заготовки
        self.RIB = self.DIB / 2 #Внутренний радиус трубчатой заготовки
        self.BCMD = self.BCM * self.KDM #Динамическое значение коэффициента аппроксимации кривой упрочнения
        self.WYD = (self.BCMD / (1 + self.MM)) * pow(self.ESP, (1 + self.MM)) #Удельная работа деформации WYD
        self.DVB = 3.14 * (self.DOT - self.ST) * self.ST * self.LBT #Деформируемый объем заготовки DVB
        self.WDB = self.WYD * self.DVB #Работа деформации заготовки WDB
        self.WMIR = self.WDB / self.KPD #Необходимая энергия для выполнения операции WMIR
        self.WMUR = self.WDB / 1.2 #Энергоемкость установки WMUR
    def DIB(self):#Внутренний диаметр трубчатой заготовки
        return self.DIB
    def RIB(self):#Внутренний радиус трубчатой заготовки
        return self.RIB
    def ESP(self,geometry):
        if self.operation=="a1":self.ESP=(geometry/self.RIB)-1
        elif self.operation=="a2":self.ESP=(geometry/(self.RIB-1))/2
        elif self.operation=="a3":self.ESP=(geometry/(self.RIB-1))/pow(2,0.5)
        elif self.operation=="a4":self.ESP=(3.14*geometry)/(self.RIB*4)
        return self.ESP
    def BCMD(self):#Динамическое значение коэффициента аппроксимации кривой упрочнения
        return self.BCMD
    def WYD(self):#Удельная работа деформации WYD
        return self.WYD
    def DVB(self):#Деформируемый объем заготовки DVB
        return self.DVB
    def WDB(self):#Работа деформации заготовки WDB
        return self.WDB
    def WMIR(self):#Необходимая энергия для выполнения операции WMIR
        return self.WMIR
    def WMUR(self):
        return self.WMUR