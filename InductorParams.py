from tkinter import *
class InductorParams():
    def GUI(self):
        self.InductorParams = Tk()
        self.InductorParams.geometry('600x500')  # геометрия окна
        self.InductorParams.title("Параметры индуктора")  # название окна
        label4 = Label(self.InductorParams, text="Величина тока", bg="white", fg="black")
        label4.place(x=10, y=10)
        label5 = Label(self.InductorParams, text="КПД", bg="white", fg="black")
        label5.place(x=10, y=60)
        btn4 = Button(self.InductorParams, text="Выбор материала", bg="grey", fg="black", command=self.WindowMashins)
        btn4.place(x=10, y=110)
        self.message_entry3 = Entry(self.InductorParams, textvariable='')
        self.message_entry3.place(x=300, y=10)
        self.message_entry4 = Entry(self.InductorParams, textvariable='')
        self.message_entry4.place(x=300, y=60)
        btn2 = Button(self.InductorParams, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn2.place(x=10, y=450)
        btn3 = Button(self.InductorParams, text="Рассчитать", bg="green", fg="black", command=self.Results)
        btn3.place(x=350, y=450)
        self.InductorParams.mainloop()
    def __init__(self):
        self.GUI()
    def Results(self): pass
    def CloseWindow(self): self.InductorParams.destroy()
    def WindowMashins(self):pass