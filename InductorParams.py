from tkinter import *
class InductorParams():
    def __init__(self):
        self.InductorParams = Tk()
        self.InductorParams.geometry('400x200')  # геометрия окна
        self.InductorParams.title("Параметры индуктора")  # название окна
        btn = Button(self.InductorParams , text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=150)
        btn = Button(self.InductorParams, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=200, y=150)
        self.InductorParams.mainloop()

    def Insertdata(self): pass

    def CloseWindow(self): self.InductorParams.destroy()