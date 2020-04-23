import tkinter
import WindowMashins
from SetSizes import SetSizes
from OperationSwitch import OperationSwitch
from Materials import Materials
import Computing
import sqlite3


class SmartCalculation():
    def __init__(self):
        self.GUI()

    def GUI(self):
        self.Smart = tkinter.Tk()
        self.Smart.geometry('1500x1000')  # геометрия окна
        self.Smart.title("Простой расчет формовки и параметров индуктора")  # название окна
        label2 = tkinter.Label(self.Smart, text="Введите диаметр наружной трубы, м", bg="white", fg="black")
        label2.place(x=10, y=60)
        label3 = tkinter.Label(self.Smart, text="Введите толщину стенки трубы, м", bg="white", fg="black")
        label3.place(x=10, y=110)
        label4 = tkinter.Label(self.Smart, text="Введите длину деформируемой зоны, м", bg="white", fg="black")
        label4.place(x=10, y=160)
        label5 = tkinter.Label(self.Smart, text="Введите радиус цилиндра, м", bg="white", fg="black")
        label5.place(x=10, y=210)
        label6 = tkinter.Label(self.Smart, text="Коэффициент степенной аппроксимации кривой упрочнения материала BCM", bg="white", fg="black")
        label6.place(x=10, y=260)
        label7 = tkinter.Label(self.Smart, text="Коэффициент степенной аппроксимации кривой упрочнения материала MM", bg="white", fg="black")
        label7.place(x=10, y=310)
        label8 = tkinter.Label(self.Smart, text="Коэффициент динамичности материала KDM",
                               bg="white", fg="black")
        label8.place(x=10, y=360)
        label9 = tkinter.Label(self.Smart, text="КПД, ед.",
                               bg="white", fg="black")
        label9.place(x=10, y=410)
        label10 = tkinter.Label(self.Smart, text="Операция",
                               bg="white", fg="black")
        label10.place(x=10, y=460)
        label11 = tkinter.Label(self.Smart, text="Поиск материала для заготовки в базе",
                                bg="white", fg="black")
        label11.place(x=800, y=60)
        label12 = tkinter.Label(self.Smart, text="Удельное электрическое сопротивление материала индуктора",
                                bg="white", fg="black")
        label12.place(x=10, y=510)
        label13 = tkinter.Label(self.Smart, text="Частота колебаний разрядного тока МИУ в режиме короткого замыкания",
                                bg="white", fg="black")
        label13.place(x=10, y=560)
        label14 = tkinter.Label(self.Smart, text="Индуктивность",
                                bg="white", fg="black")
        label14.place(x=10, y=610)
        label15 = tkinter.Label(self.Smart, text="Ёмкость батареи конденсаторов МИУ",
                                bg="white", fg="black")
        label15.place(x=10, y=660)
        label16 = tkinter.Label(self.Smart, text="Длина индуктора",
                                bg="white", fg="black")
        label16.place(x=10, y=710)
        label17 = tkinter.Label(self.Smart, text="Высота индуктора",
                                bg="white", fg="black")
        label17.place(x=10, y=760)
        label18 = tkinter.Label(self.Smart, text="Плотность материала индуктора",
                                bg="white", fg="black")
        label18.place(x=10, y=810)
        label19 = tkinter.Label(self.Smart, text="Поиск материала для индуктора в базе",
                                bg="white", fg="black")
        label19.place(x=800, y=110)
        label20 = tkinter.Label(self.Smart, text="Поиск установки в базе",
                                bg="white", fg="black")
        label20.place(x=800, y=160)
        self.message_entry1 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry1.place(x=600, y=60)
        self.message_entry2 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry2.place(x=600, y=110)
        self.message_entry3 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry3.place(x=600, y=160)
        self.message_entry4 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry4.place(x=600, y=210)
        self.message_entry5 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry5.place(x=600, y=260)
        self.message_entry6 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry6.place(x=600, y=310)
        self.message_entry7 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry7.place(x=600, y=360)
        self.message_entry8 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry8.place(x=600, y=410)
        self.message_entry9 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry9.place(x=600, y=460)
        self.message_entry10 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry10.place(x=1100, y=60)
        self.message_entry11 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry11.place(x=600, y=510)
        self.message_entry12 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry12.place(x=600, y=560)
        self.message_entry13 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry13.place(x=600, y=610)
        self.message_entry14 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry14.place(x=600, y=660)
        self.message_entry15 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry15.place(x=600, y=710)
        self.message_entry16 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry16.place(x=600, y=760)
        self.message_entry17 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry17.place(x=600, y=810)
        self.message_entry18 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry18.place(x=1100,y=110)
        self.message_entry19 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry19.place(x=1100, y=160)
        btn = tkinter.Button(self.Smart, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=950)
        btn1 = tkinter.Button(self.Smart, text="Рассчитать", bg="green", fg="black", command=self.CalculateIt)
        btn1.place(x=280, y=950)
        btn2 = tkinter.Button(self.Smart, text="Найти", bg="lightgreen", fg="black", command=self.SearchMaterial)
        btn2.place(x=1300, y=60)
        btn3 = tkinter.Button(self.Smart, text="Найти", bg="lightgreen", fg="black", command=self.SearchMaterialForInductor)
        btn3.place(x=1300, y=110)
        btn4 = tkinter.Button(self.Smart, text="Найти", bg="lightgreen", fg="black",
                              command=self.SearchEquipment)
        btn4.place(x=1300, y=160)
        self.text=tkinter.Text(self.Smart, height=20)
        self.text.place(x=800,y=600)
        self.Smart.mainloop()

    def SearchEquipment(self):pass

    def SearchMaterialForInductor(self):pass

    def SearchMaterial(self):
        material=self.message_entry10.get()
        print(material)
        conn = sqlite3.connect("Metalls.db")
        cursor = conn.cursor()
        sql="select M_M, B, The_coefficient_of_dynamic from Workpiece_material where Name_of_the_metalls ='"+material+"'"
        print(sql)
        sql1="select * from Workpiece_material "
        print(cursor.execute(sql))
        for row in cursor.execute(sql):
            self.message_entry5.delete(0,10)
            self.message_entry6.delete(0,10)
            self.message_entry7.delete(0,10)
            self.MM=row[0]
            self.BCM1=row[1]
            self.KDM=row[2]
            self.message_entry5.insert(0,self.BCM1)
            self.message_entry6.insert(0,self.MM)
            self.message_entry7.insert(0,self.KDM)

    def CloseWindow(self):
        self.Smart.destroy()

    def CalculateIt(self):
        self.DOT = self.message_entry1.get()
        self.ST = self.message_entry2.get()
        self.LBT = self.message_entry3.get()
        self.RC = self.message_entry4.get()
        self.BCM1 = self.message_entry5.get()
        self.BCM = float(self.BCM1)*pow(10,7)
        self.MM = self.message_entry6.get()
        self.KDM = self.message_entry7.get()
        self.KPD = self.message_entry8.get()
        operation = self.message_entry9.get()
        #print(float(DOT),float(ST),float(LBT),float(RC),float(BCM),float(MM),float(KDM),float(KPD),operation)
        f = Computing.Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM), float(self.LBT), float(self.KPD), float(self.RC), operation)
        DIB = Computing.Form.DIB(f)
        s="Внутренний диаметр трубчатой заготовки:" + str(DIB) + ",м"
        self.text.insert(1.0, s)
        RIB = Computing.Form.RIB(f)
        #print(RIB)
        s1="\n"+"Внутренний радиус трубчатой заготовки:" + str(RIB) + ",м"
        self.text.insert(2.0, s1)
        ESP = Computing.Form.ESP(f, self.RC)
        #print(ESP)
        s2="\n"+"Cредняя величина деформации заготовки:" + str(ESP) + ",м"
        self.text.insert(3.0, s2)
        BCMD = Computing.Form.BCMD(f)
        #print(BCMD)
        s3="\n"+"Динамическое значение коэффициента аппроксимации кривой упрочнения:" + str(BCMD)
        self.text.insert(4.0, s3)
        WYD = Computing.Form.WYD(f)
        #print(WYD)
        s4="\n"+"Удельная работа деформации:" + str(WYD) + ",Дж"
        self.text.insert(5.0, s4)
        DVB = Computing.Form.DVB(f)
        #print(DVB)
        s5="\n"+"Деформируемый объем заготовки:" + str(DVB) + ",mm3"
        self.text.insert(6.0, s5)
        WDB = Computing.Form.WDB(f)
        #print(WDB)
        s6="\n"+"Работа деформации заготовки:" + str(WDB) + ",Дж"
        self.text.insert(7.0, s6)
        WMIR = Computing.Form.WMIR(f)
        #print(WMIR)
        s7="\n"+'Необходимая энергия для выполнения операции:' + str(WMIR) + ",Дж"
        self.text.insert(8.0, s7)
        WMUR = Computing.Form.WMUR(f)
        #print(WMUR)
        s8="\n"+"Энергоемкость установки:" + str(WMUR) + ",Дж"
        self.text.insert(9.0, s8)