import Computing

operation = "b1"
DOT = 0.1514  # int(input("введите диаметр наружной трубы"))
ST = 0.0012  # int(input("введите толщину стенки трубы"))
LBT = 0.03  # int(input("введите длину деформируемой зоны"))
RC = 0.074  # int(input("введите радиус цилиндра"))
BCM = 57.4 * pow(10, 7)
MM = 0.23
KDM = 1.660
KPD = 0.04
f = Computing.Form(DOT, ST, BCM, KDM, MM, LBT, KPD, RC, operation)
DIB = Computing.Form.DIB(f)
print("Внутренний диаметр трубчатой заготовки:" + str(DIB) + ",м")
RIB = Computing.Form.RIB(f)
print("Внутренний радиус трубчатой заготовки:" + str(RIB) + ",м")
ESP = Computing.Form.ESP(f, RC)
print("Cредняя величина деформации заготовки:" + str(ESP) + ",м")
BCMD = Computing.Form.BCMD(f)
print("Динамическое значение коэффициента аппроксимации кривой упрочнения:" + str(BCMD))
WYD = Computing.Form.WYD(f)
print("Удельная работа деформации:" + str(WYD) + ",Дж")
DVB = Computing.Form.DVB(f)
print("Деформируемый объем заготовки:" + str(DVB) + ",mm3")
WDB = Computing.Form.WDB(f)
print("Работа деформации заготовки:" + str(WDB) + ",Дж")
WMIR = Computing.Form.WMIR(f)
print('Необходимая энергия для выполнения операции:' + str(WMIR) + ",Дж")
WMUR = Computing.Form.WMUR(f)
print("Энергоемкость установки:" + str(WMUR) + ",Дж")
FW = 10728  # частота тока
YEMP = 1.78 * pow(10, -8)  # дельного электрического сопротивления материала индуктора
FCE = 2400 * pow(10, 3)  # частота колебаний разрядного тока МИУ в режиме короткого замыкания
LCE = 0.17 * pow(10, -6)  # индуктивность
LCB = 1 * pow(10, -12)  # индуктивность кабеля
CCE = 254 * pow(10, -6)  # емкость батареи конденсаторов МИУ
SC = 0.004  # Длина индуктора??????
HSC = 0.008  # высота индуктора
PLM = 2.64
g = Computing.Inductor(LBT, operation, DOT, ST, FW, YEMP, FCE, LCE, LCB, CCE, SC, HSC, PLM, BCM, KDM, MM, KPD, RC)
LCA = Computing.Inductor.LCA(g)
print("Длина индуктора:" + str(LCA) + ",м")
ZCP = Computing.Inductor.ZCP(g)
print("Величина зазора между индуктором и заготовкой:" + str(ZCP) + ",м")
DCA = Computing.Inductor.DCA(g)
print("Диаметр индуктора:" + str(DCA) + ",м")
BP = Computing.Inductor.BP(g)
print("Глубина проникновения ИМП в материал заготовки: " + str(BP) + " ,м")
BC = Computing.Inductor.BC(g)
print("Глубина проникновения ИМП в материал индуктор: " + str(BC) + " ,м")
LDC = Computing.Inductor.LDC(g)
print("Паразитная индуктивность разрядного контура: " + str(LDC) + " ,Гн")
FDC = Computing.Inductor.FDC(g)
print("Частота разряда при наличии только паразитных индуктивностей: " + str(FDC) + " ,Гц")
K1 = Computing.Inductor.K1(g)
print("Коэффициент К1: " + str(K1))
K2 = Computing.Inductor.K2(g)
print("Коэффициент К2: " + str(K2))
K3 = Computing.Inductor.K3(g)
print("Коэффициент К3: " + str(K3))
K4 = Computing.Inductor.K4(g)
print("Коэффициент К4: " + str(K4))
ZEK = Computing.Inductor.ZEK(g)
print("Значение эквивалентного зазора между индуктором и заготовкой: " + str(ZEK))
NCTC = Computing.Inductor.NCTC(g)
print("Количество витков индуктора: " + str(NCTC))
NCW = Computing.Inductor.NCW(g)
print("Целое количество витков индуктора: " + str(NCW))
NCWC = Computing.Inductor.NCWC(g)
print("Расчетное количество рабочих витков" + str(NCWC))
NCF = Computing.Inductor.NCF(g)
print("Количество свободных витков" + str(NCF))
SCIC = Computing.Inductor.SCIC(g)
print("Расчетный шаг витков индуктора: " + str(SCIC))
WR = Computing.Inductor.WR(g)
print("Необходимая энергия разряда МИУ: " + str(WR) + ",Дж")
LUC = Computing.Inductor.LUC(g)
print("Суммарная индуктивность: " + str(LUC) + " ,Гн")
