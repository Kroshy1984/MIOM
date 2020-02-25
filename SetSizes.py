from tkinter import *
class SetSizes():
    def __init__(self):
        self.SetSizesWindow = Tk()
        self.SetSizesWindow.geometry('200x200')  # геометрия окна
        self.SetSizesWindow.title("Размеры заготовки")  # название окна
        label1 = Label(self.SetSizesWindow, text="Длина заготовки", bg="white", fg="black")
        label1.place(x=10, y=10)
        label2 = Label(self.SetSizesWindow, text="Ширина заготовки", bg="white", fg="black")
        label2.place(x=10, y=60)
        label3 = Label(self.SetSizesWindow, text="Высота заготовки", bg="white", fg="black")
        label3.place(x=10, y=110)
        self.SetSizesWindow.main.loop()