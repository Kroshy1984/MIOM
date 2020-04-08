from Computing import *
operation="b1"
DOT=151.4*0.001#int(input("введите диаметр наружной трубы"))
ST=1.2*0.001#int(input("введите толщину стенки трубы"))
LBT=30*0.001#int(input("введите длину деформируемой зоны"))
RC=74*0.001#int(input("введите радиус цилиндра"))
BCM=57.4*pow(10,7)
MM=0.23
KDM=2.402
KPD=0.13
f=Form(DOT,ST,BCM,KDM,MM,LBT,KPD,RC,operation)
DIB=Form.DIB(f)
print("Внутренний диаметр трубчатой заготовки:"+str(DIB)+",м")
RIB=Form.RIB(f)
print("Внутренний радиус трубчатой заготовки:"+str(RIB)+",м")
ESP=Form.ESP(f,RC)
print("Cредняя величина деформации заготовки:"+str(ESP)+",м")
BCMD=Form.BCMD(f)
print("Динамическое значение коэффициента аппроксимации кривой упрочнения:"+str(BCMD))
WYD=Form.WYD(f)
print("Удельная работа деформации:"+str(WYD)+",кДж")
DVB=Form.DVB(f)
print("Деформируемый объем заготовки:"+str(DVB)+",mm3")
WDB=Form.WDB(f)
print("Работа деформации заготовки:"+str(WDB)+",кДж")
WMIR=Form.WMIR(f)
print("Необходимая энергия для выполнения операции:"+str(WMIR)+",кДж")
WMUR=Form.WMUR(f)
print("Энергоемкость установки:"+str(WMUR)+",кДж")
FW=13.4 #частота тока
YEMP=7.1*pow(10,-7)#дельного электрического сопротивления материала индуктора
FCE=30#частота колебаний разрядного тока МИУ в режиме короткого замыкания
LCE=110#индуктивность
LCB=30#индуктивность кабеля
CCE=253.3#емкость батареи конденсаторов МИУ
SC=4#Длина индуктора??????
HSC=8#высота индуктора
PLM=2.64
g=Inductor(LBT,operation,DOT,ST,FW,YEMP,FCE,LCE,LCB,CCE,SC,HSC,PLM)