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
        if self.operation=="a1":self.LCA=1.1*self.LBT
        elif self.operation=="a2":self.LCA=1.3*self.LBT
        elif self.operation=="a3":self.LCA=self.LBT
        elif self.operation=="a4":self.LCA=0.75*self.LBT
    def ZCP(self):#Величина зазора между индуктором и заготовкой
        self.ZCP = self.ZS + self.ZB + self.ZA
    def DCA(self):
        self.DCA=self.DOT-2*self.ST-2*self.ZCP
