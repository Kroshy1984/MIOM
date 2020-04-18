import tkinter


class InductorParams():
    def GUI(self):
        self.InductorParams = tkinter.Tk()
        self.InductorParams.geometry('600x500')  # геометрия окна
        self.InductorParams.title("Параметры индуктора")  # название окна
        label5 = tkinter.Label(self.InductorParams, text="КПД", bg="white", fg="black")
        label5.place(x=10, y=60)
        btn4 = tkinter.Button(self.InductorParams, text="Выбор материала", bg="grey", fg="black", command=self.WindowMashins)
        btn4.place(x=10, y=110)
        self.message_entry4 = tkinter.Entry(self.InductorParams, textvariable='')
        self.message_entry4.place(x=300, y=60)
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
