from tkinter import *
class SetSizes():
    def GUI(self):
        self.SetSizesWindow = Tk()
        self.SetSizesWindow.geometry('500x200')  # геометрия окна
        self.SetSizesWindow.title("Размеры заготовки")  # название окна
        label1 = Label(self.SetSizesWindow, text="Длина заготовки", bg="white", fg="black")
        label1.place(x=10, y=10)
        label2 = Label(self.SetSizesWindow, text="Внешний диаметр заготовки", bg="white", fg="black")
        label2.place(x=10, y=60)
        label3 = Label(self.SetSizesWindow, text="Внутренний диаметр заготовки", bg="white", fg="black")
        label3.place(x=10, y=110)
        self.message_entry = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry.place(x=250, y=10)
        self.message_entry1 = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry1.place(x=250, y=60)
        self.message_entry2 = Entry(self.SetSizesWindow, textvariable='')
        self.message_entry2.place(x=250, y=110)
        btn = Button(self.SetSizesWindow, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=150)
        btn = Button(self.SetSizesWindow, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=280, y=150)
    def __init__(self):
        self.GUI()
        self.SetSizesWindow.mainloop()
    def Insertdata(self):pass
    def CloseWindow(self): self.SetSizesWindow.destroy()
