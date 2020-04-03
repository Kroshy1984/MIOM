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
    def LCA(self):
        if self.operation=="a1":self.LCA=1.1*self.LBT #формовка цилиндра
        elif self.operation=="a2":self.LCA=1.3*self.LBT#формовка конуса
        elif self.operation=="a3":self.LCA=self.LBT#формовка сферы
        elif self.operation=="a4":self.LCA=0.75*self.LBT#формовка рифта
    def ZCP(self):#Величина зазора между индуктором и заготовкой
        self.ZCP = self.ZS + self.ZB + self.ZA
    def DCA(self):
        self.DCA=self.DOT-2*self.ST-2*self.ZCP
class Form(Calculation):
    def __init__(self,DOT,ST,RC,RCF,PR,BCMD,RMK,BCM,KDM,MM,ESP,LBT,WYD,operation):
        self.operation=operation
        self.DOT=DOT
        self.ST=ST
        self.RC=RC
        self.RCF=RCF
        self.PR=PR
        self.BCMD=BCMD
        self.RMK=RMK
        self.BCM=BCM
        self.KDM=KDM
        self.MM=MM
        self.ESP=ESP
        self.LBT=LBT
        self.WYD=WYD
    def DIB(self):
        self.DIB=self.DOT-2*self.ST
    def RIB(self):
        self.RIB=self.DIB/2
    def ESR(self):
        if self.operation=="a1":self.ESR=(self.RC/self.RIB)-1
        elif self.operation=="a2":self.ESR=(self.RMK/(self.RIB-1))/2
        elif self.operation=="a3":self.ESR=(self.RCF/(self.RIB-1))/pow(2,0.5)
        elif self.operation=="a4":self.ESR=(3.14*self.PR)/(self.RIB*4)
    def BCMD(self):
        self.BCMD=self.BCM*self.KDM
    def WYD(self):
        self.WYD=(self.BCMD/(1+self.MM))*pow(self.ESP,(1+self.MM))
    def DVB(self):
        self.DVB=3.14*(self.DOT-self.ST)*self.ST*self.LB
    def WDB(self):
        self.WDB=self.WYD*self.DVB