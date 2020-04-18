from tkinter import *
class InductorParams():
    def GUI(self):
        self.InductorParams = Tk()
        self.InductorParams.geometry('500x400')  # геометрия окна
        self.InductorParams.title("Параметры индуктора")  # название окна
        label1 = Label(self.InductorParams, text="Диаметр наружной трубы", bg="white", fg="black")
        label1.place(x=10, y=10)
        label2 = Label(self.InductorParams, text="Толщина стенки", bg="white", fg="black")
        label2.place(x=10, y=60)
        label3 = Label(self.InductorParams, text="Диаметр деформированной зоны", bg="white", fg="black")
        label3.place(x=10, y=110)
        btn1 = Button(self.InductorParams, text="Выбор оборудования", bg="grey", fg="black", command=self.WindowMashins)
        btn1.place(x=10, y=170)
        btn4 = Button(self.InductorParams, text="Выбор материала", bg="grey", fg="black", command=self.WindowMashins)
        btn4.place(x=10, y=220)
        btn5 = Button(self.InductorParams, text="Выбор операции", bg="grey", fg="black", command=self.WindowMashins)
        btn5.place(x=10, y=280)
        self.message_entry = Entry(self.InductorParams, textvariable='')
        self.message_entry.place(x=250, y=10)
        self.message_entry1 = Entry(self.InductorParams, textvariable='')
        self.message_entry1.place(x=250, y=60)
        self.message_entry2 = Entry(self.InductorParams, textvariable='')
        self.message_entry2.place(x=250, y=110)
        btn2 = Button(self.InductorParams, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn2.place(x=10, y=350)
        btn3 = Button(self.InductorParams, text="Рассчитать", bg="green", fg="black", command=self.Insertdata)
        btn3.place(x=350, y=350)
        self.InductorParams.mainloop()
    def __init__(self):
        self.GUI()
    def Insertdata(self): pass
    def CloseWindow(self): self.InductorParams.destroy()
    def WindowMashins(self):pass