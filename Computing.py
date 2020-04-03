#Длина деформируемой зоны LBT
#Название операции operation
#Диаметр наружной трубы DOT
#Толщина стенки трубы ST
class Calculation():pass
class Inductor(Calculation):
    def __init__(self, LBT, operation, DOT, ST):
        self.LBT=LBT
        self.operation=operation
        self.DOT=DOT
        self.ST=ST
        print(self.LBT, self.operation)
        self.ZS=0.65 # Толщина изоляции медной шины
        self.ZB=1.0 # Толщина основной изоляции индуктора
        self.ZA=0.25 #Толщина воздушного зазора
        self.LTC=0.7*pow(10,-7)#Индуктивность токов индуктора
        self.ZCP = self.ZS + self.ZB + self.ZA
        self.DCA = self.DOT - 2 * self.ST - 2 * self.ZCP
    def LCA(self):
        if self.operation=="a1":self.LCA=1.1*self.LBT #формовка цилиндра
        elif self.operation=="a2":self.LCA=1.3*self.LBT#формовка конуса
        elif self.operation=="a3":self.LCA=self.LBT#формовка сферы
        elif self.operation=="a4":self.LCA=0.75*self.LBT#формовка рифта
    def ZCP(self):#Величина зазора между индуктором и заготовкой
        return self.ZSP
    def DCA(self):
        return self.DCA
class Form(Calculation):
    def __init__(self,DOT,ST,BCMD,BCM,KDM,MM,ESP,LBT,WYD,KPD,operation):
        self.operation=operation
        self.DOT=DOT
        self.ST=ST
        self.BCMD=BCMD
        self.BCM=BCM
        self.KDM=KDM
        self.MM=MM
        self.ESP=ESP
        self.LBT=LBT
        self.WYD=WYD
        self.KPD=KPD
        self.DIB = self.DOT - 2 * self.ST
        self.RIB = self.DIB / 2
        self.BCMD = self.BCM * self.KDM
        self.WYD = (self.BCMD / (1 + self.MM)) * pow(self.ESP, (1 + self.MM))
        self.DVB = 3.14 * (self.DOT - self.ST) * self.ST * self.LBT
        self.WDB = self.WYD * self.DVB
        self.WMIR = self.WDB / self.KPD
        self.WMIR = self.WDB / self.KPD
    def DIB(self):
        return self.DIB
    def RIB(self):
        return self.RIB
    def ESR(self,geometry):
        if self.operation=="a1":self.ESR=(geometry/self.RIB)-1
        elif self.operation=="a2":self.ESR=(geometry/(self.RIB-1))/2
        elif self.operation=="a3":self.ESR=(geometry/(self.RIB-1))/pow(2,0.5)
        elif self.operation=="a4":self.ESR=(3.14*geometry)/(self.RIB*4)
    def BCMD(self):
        return self.BCMD
    def WYD(self):
        return self.WYD
    def DVB(self):
        return self.DVB
    def WDB(self):
        return self.WDB
    def WMIR(self):
        return self.WMIR
    def WMUR(self):
        return self.WMUR