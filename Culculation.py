from Computing import *
operation="b1"
DOT=151.4#int(input("введите диаметр наружной трубы"))
ST=1.2#int(input("введите толщину стенки трубы"))
LBT=30#int(input("введите длину деформируемой зоны"))
RC=75.2#int(input("введите радиус цилиндра"))
BCM=57.4
MM=0.23
KDM=2.402
KPD=0.13
f=Form(DOT,ST,BCM,KDM,MM,LBT,KPD,RC,operation)
DIB=Form.DIB(f)
print("Внутренний диаметр трубчатой заготовки:"+str(DIB)+",мм")
RIB=Form.RIB(f)
print("Внутренний радиус трубчатой заготовки:"+str(RIB)+",мм")
ESP=Form.ESP(f,RC)
print("Cредняя величина деформации заготовки:"+str(ESP)+",мм")
BCMD=Form.BCMD(f)
print("Динамическое значение коэффициента аппроксимации кривой упрочнения:"+str(BCMD))
WYD=Form.WYD(f)
print("Удельная работа деформации:"+str(WYD)+",Дж")
DVB=Form.DVB(f)
print("Деформируемый объем заготовки:"+str(DVB)+",mm3")
WDB=Form.WDB(f)
print("Работа деформации заготовки:"+str(WDB)+",Дж")
WMIR=Form.WMIR(f)
print("Необходимая энергия для выполнения операции:"+str(WMIR)+",Дж")
WMUR=Form.WMUR(f)
print("Энергоемкость установки:"+str(WMUR)+",Дж")