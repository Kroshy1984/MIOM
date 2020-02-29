from tkinter import *
class OperationSwitch():
    def __init__(self):
        self.OperationSwitch = Tk()
        self.OperationSwitch.geometry('400x200')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        btn = Button(self.OperationSwitch , text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=150)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=200, y=150)
        self.OperationSwitch.mainloop()

    def Insertdata(self): pass

    def CloseWindow(self): self.OperationSwitch.destroy()