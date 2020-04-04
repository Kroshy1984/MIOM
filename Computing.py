#Длина деформируемой зоны LBT
#Название операции operation
#Диаметр наружной трубы DOT
#Толщина стенки трубы ST
#астота разрядного тока FW
#Глубина проникновения ИМП в материал заготовки BP
class Inductor():
    def __init__(self,LBT,operation,DOT,ST,FW,YEMP,mu):
        self.LBT=LBT
        self.operation=operation
        self.DOT=DOT
        self.ST=ST
        self.ZS=0.65 # Толщина изоляции медной шины
        self.ZB=1.0 # Толщина основной изоляции индуктора
        self.ZA=0.25 #Толщина воздушного зазора
        self.LTC=0.7*pow(10,-7)#Индуктивность токов индуктора
        self.ZCP = self.ZS + self.ZB + self.ZA
        self.DCA = self.DOT - 2 * self.ST - 2 * self.ZCP
        self.FW=FW#Частота разрядного тока
        self.BP = pow((YEMP / (3.14 * mu * FW),0.5)#Глубина проникновения ИМП в материал заготовки
    def LCA(self):
        if self.operation=="a1":self.LCA=1.1*self.LBT #формовка цилиндра
        elif self.operation=="a2":self.LCA=1.3*self.LBT#формовка конуса
        elif self.operation=="a3":self.LCA=self.LBT#формовка сферы
        elif self.operation=="a4":self.LCA=0.75*self.LBT#формовка рифта
        return self.LCA
    def ZCP(self):#Величина зазора между индуктором и заготовкой
        return self.ZSP
    def DCA(self):
        return self.DCA
    def BP(self):#Глубина проникновения ИМП в материал заготовки
        return self.BP


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