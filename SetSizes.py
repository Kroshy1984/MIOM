from tkinter import *
import EntranceData
from EntranceData import *
class SetSizes():
    def GUI(self):
        self.SetSizesWindow = Tk()
        self.SetSizesWindow.geometry('500x300')  # геометрия окна
        self.SetSizesWindow.title("Размеры заготовки и детали (в метрах)")  # название окна
        label1 = Label(self.SetSizesWindow, text="Длина деформируемой зоны", bg="white", fg="black")
        label1.place(x=10, y=10)
        label2 = Label(self.SetSizesWindow, text="Внешний диаметр заготовки", bg="white", fg="black")
        label2.place(x=10, y=60)
        label3 = Label(self.SetSizesWindow, text="Толщина стенки", bg="white", fg="black")
        label3.place(x=10, y=110)
        label4 = Label(self.SetSizesWindow, text="Радиус цилинда", bg="white", fg="black")
        label4.place(x=10, y=160)
        self.message_entry = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry.place(x=250, y=10)
        self.message_entry1 = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry1.place(x=250, y=60)
        self.message_entry2 = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry2.place(x=250, y=110)
        self.message_entry2 = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry2.place(x=250, y=160)
        btn = Button(self.SetSizesWindow, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=250)
        btn = Button(self.SetSizesWindow, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=280, y=250)
    def __init__(self, a, b, c, d):
        self.f1=a
        self.f2=b
        self.f3=c
        self.f4=d
        self.GUI()
        self.SetSizesWindow.mainloop()
    def Insertdata(self):
        self.field1=self.message_entry.get()
        self.field2=self.message_entry1.get()
        self.field3=self.message_entry2.get()
        print(self.field1,self.field2, self.field3)
        self.f3="Длина заготовки - "+self.field1+"мм, Внешний диаметр заготовки - "+self.field2+"мм, Внутренний диаметр заготовки- "+self.field3+"мм"
        print(self.f3)
        self.SetSizesWindow.destroy()
        f = EntranceData.EntranceDataFirst(self.f1, self.f2, self.f3,self.f4)
    def CloseWindow(self):
        self.SetSizesWindow.destroy()
        f = EntranceData.EntranceDataFirst(self.f1, self.f2, self.f3, self.f4)