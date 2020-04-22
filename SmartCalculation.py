import tkinter
import WindowMashins
from SetSizes import SetSizes
from OperationSwitch import OperationSwitch
from Materials import Materials
import Computing


class SmartCalculation():
    def __init__(self):
        self.GUI()

    def GUI(self):
        self.Smart = tkinter.Tk()
        self.Smart.geometry('1000x1000')  # геометрия окна
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
        btn = tkinter.Button(self.Smart, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=550)
        btn = tkinter.Button(self.Smart, text="Рассчитать", bg="green", fg="black", command=self.CalculateIt)
        btn.place(x=280, y=550)
        self.text=tkinter.Text(self.Smart, height=20)
        self.text.place(x=10,y=600)
        self.Smart.mainloop()

    def CloseWindow(self):
        self.Smart.destroy()

    def CalculateIt(self):
        DOT = self.message_entry1.get()
        ST = self.message_entry2.get()
        LBT = self.message_entry3.get()
        RC = self.message_entry4.get()
        BCM1 = self.message_entry5.get()
        BCM = BCM1*pow(10,7)
        MM = self.message_entry6.get()
        KDM = self.message_entry7.get()
        KPD = self.message_entry8.get()
        operation = self.message_entry9.get()
        f = Computing.Form(DOT, ST, BCM, KDM, MM, LBT, KPD, RC, operation)
        DIB = Computing.Form.DIB(f)
        s="Внутренний диаметр трубчатой заготовки:" + str(DIB) + ",м"
        self.text.insert(1.0, s)
        RIB = Computing.Form.RIB(f)
        s1="Внутренний радиус трубчатой заготовки:" + str(RIB) + ",м"
        self.text.insert(1.0, s1)
        ESP = Computing.Form.ESP(f, RC)
        s2="Cредняя величина деформации заготовки:" + str(ESP) + ",м"
        self.text.insert(1.0, s2)
        BCMD = Computing.Form.BCMD(f)
        s3="Динамическое значение коэффициента аппроксимации кривой упрочнения:" + str(BCMD)
        self.text.insert(1.0, s3)
        WYD = Computing.Form.WYD(f)
        s4="Удельная работа деформации:" + str(WYD) + ",Дж"
        self.text.insert(1.0, s4)
        DVB = Computing.Form.DVB(f)
        s5="Деформируемый объем заготовки:" + str(DVB) + ",mm3"
        self.text.insert(1.0, s5)
        WDB = Computing.Form.WDB(f)
        s6="Работа деформации заготовки:" + str(WDB) + ",Дж"
        self.text.insert(1.0, s6)
        WMIR = Computing.Form.WMIR(f)
        s7='Необходимая энергия для выполнения операции:' + str(WMIR) + ",Дж"
        self.text.insert(1.0, s7)
        WMUR = Computing.Form.WMUR(f)
        s8="Энергоемкость установки:" + str(WMUR) + ",Дж"
        self.text.insert(1.0, s8)