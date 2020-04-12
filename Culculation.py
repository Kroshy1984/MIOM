from Computing import *
operation="b1"
DOT=0.1514#int(input("введите диаметр наружной трубы"))
ST=0.0012#int(input("введите толщину стенки трубы"))
LBT=0.03#int(input("введите длину деформируемой зоны"))
RC=0.074#int(input("введите радиус цилиндра"))
BCM=57.4*pow(10,7)
MM=0.23
KDM=1.660
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
print("Удельная работа деформации:"+str(WYD)+",Дж")
DVB=Form.DVB(f)
print("Деформируемый объем заготовки:"+str(DVB)+",mm3")
WDB=Form.WDB(f)
print("Работа деформации заготовки:"+str(WDB)+",Дж")
WMIR=Form.WMIR(f)
print("Необходимая энергия для выполнения операции:"+str(WMIR)+",Дж")
WMUR=Form.WMUR(f)
print("Энергоемкость установки:"+str(WMUR)+",Дж")
FW=32.5*pow(10,3) #частота тока
YEMP=1.78*pow(10,-8)#дельного электрического сопротивления материала индуктора
FCE=2400*pow(10,3)#частота колебаний разрядного тока МИУ в режиме короткого замыкания
LCE=0.17*pow(10,-6)#индуктивность
LCB=1#индуктивность кабеля
CCE=254*pow(10,-3)#емкость батареи конденсаторов МИУ
SC=0.004#Длина индуктора??????
HSC=0.008#высота индуктора
PLM=2.64
g=Inductor(LBT,operation,DOT,ST,FW,YEMP,FCE,LCE,LCB,CCE,SC,HSC,PLM,BCM,KDM,MM,KPD,RC)
LCA=Inductor.LCA(g)
print("Длина индуктора:"+str(LCA)+",м")
ZCP=Inductor.ZCP(g)
print("Величина зазора между индуктором и заготовкой:"+str(ZCP)+",м")
DCA=Inductor.DCA(g)
print("Диаметр индуктора:"+str(DCA)+",м")
BP=Inductor.BP(g)
print("Глубина проникновения ИМП в материал заготовки: "+str(BP)+" ,м")
BC=Inductor.BC(g)
print("Глубина проникновения ИМП в материал индуктор: "+str(BP)+" ,м")
LDC=Inductor.LDC(g)
print("Паразитная индуктивность разрядного контура: "+str(LDC)+" ,Гн")
FDC=Inductor.FDC(g)
print("Частота разряда при наличии только паразитных индуктивностей: "+str(FDC)+" ,Гц")
K1=Inductor.K1(g)
print("Коэффициент К1: "+str(K1))
ZEK=Inductor.ZEK(g)
print("Значение эквивалентного зазора между индуктором и заготовкой: "+str(ZEK))
NCTC=Inductor.NCTC(g)
print("Количество витков индуктора: "+str(NCTC))
NCW=Inductor.NCW(g)
print("Целое количество витков индуктора: "+str(NCW))