import tkinter


class InductorParams():
    def GUI(self):
        self.InductorParams = tkinter.Tk()
        self.InductorParams.geometry('500x500')  # геометрия окна
        self.InductorParams.title("Параметры индуктора")  # название окна
        btn4 = tkinter.Button(self.InductorParams, text="Выбор материала индуктора", bg="grey", fg="black", command=self.WindowMashins)
        btn4.place(x=10, y=60)
        label2 = tkinter.Label(self.InductorParams, text="Высота индуктора, м", bg="white", fg="black")
        label2.place(x=10, y=110)
        label3 = tkinter.Label(self.InductorParams, text="Длина индуктора, м", bg="white", fg="black")
        label3.place(x=10, y=160)
        label4 = tkinter.Label(self.InductorParams, text="Толщина изоляции шины, м", bg="white", fg="black")
        label4.place(x=10, y=210)
        label5 = tkinter.Label(self.InductorParams, text="Толщина изоляции индуктора, м", bg="white", fg="black")
        label5.place(x=10, y=260)
        label5 = tkinter.Label(self.InductorParams, text="Толщина воздушного зазора, м", bg="white", fg="black")
        label5.place(x=10, y=310)
        self.message_entry1 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry1.place(x=300, y=60)
        self.message_entry1 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry1.place(x=300, y=110)
        self.message_entry2 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry2.place(x=300, y=160)
        self.message_entry3 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry3.place(x=300, y=210)
        self.message_entry4 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry4.place(x=300, y=260)
        self.message_entry5 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry5.place(x=300, y=310)

        btn2 = tkinter.Button(self.InductorParams, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn2.place(x=10, y=450)
        btn3 = tkinter.Button(self.InductorParams, text="Рассчитать", bg="green", fg="black", command=self.Results)
        btn3.place(x=350, y=450)
        self.InductorParams.mainloop()

    def __init__(self):
        self.GUI()

    def Results(self): pass

    def CloseWindow(self): self.InductorParams.destroy()

    def WindowMashins(self): pass
