import tkinter
import WindowMashins
from SetSizes import SetSizes
from OperationSwitch import OperationSwitch
from Materials import Materials


class SmartCalculation():
    def __init__(self):
        self.GUI()

    def GUI(self):
        self.Smart = tkinter.Tk()
        self.Smart.geometry('1000x1000')  # геометрия окна
        self.Smart.title("Простой расчет формовки и параметров индуктора")  # название окна
        label2 = tkinter.Label(self.Smart, text="Введите диаметр наружной трубы, м", bg="white", fg="black")
        label2.place(x=10, y=60)
        label2 = tkinter.Label(self.Smart, text="Введите толщину стенки трубы, м", bg="white", fg="black")
        label2.place(x=10, y=110)
        label3 = tkinter.Label(self.Smart, text="Введите длину деформируемой зоны, м", bg="white", fg="black")
        label3.place(x=10, y=160)
        label4 = tkinter.Label(self.Smart, text="Введите радиус цилиндра, м", bg="white", fg="black")
        label4.place(x=10, y=210)
        label5 = tkinter.Label(self.Smart, text="Коэффициент степенной аппроксимации кривой упрочнения материала BCM", bg="white", fg="black")
        label5.place(x=10, y=260)
        label5 = tkinter.Label(self.Smart, text="Коэффициент степенной аппроксимации кривой упрочнения материала MM", bg="white", fg="black")
        label5.place(x=10, y=310)
        label5 = tkinter.Label(self.Smart, text="Коэффициент динамичности материала KDM",
                               bg="white", fg="black")
        label5.place(x=10, y=360)
        label6 = tkinter.Label(self.Smart, text="КПД, ед.",
                               bg="white", fg="black")
        label6.place(x=10, y=410)
        label7 = tkinter.Label(self.Smart, text="Операция",
                               bg="white", fg="black")
        label7.place(x=10, y=460)
        self.message_entry1 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry1.place(x=600, y=60)
        self.message_entry1 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry1.place(x=600, y=110)
        self.message_entry2 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry2.place(x=600, y=160)
        self.message_entry3 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry3.place(x=600, y=210)
        self.message_entry4 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry4.place(x=600, y=260)
        self.message_entry5 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry5.place(x=600, y=310)
        self.message_entry5 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry5.place(x=600, y=360)
        self.message_entry5 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry5.place(x=600, y=410)
        self.message_entry5 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry5.place(x=600, y=460)
        self.Smart.mainloop()