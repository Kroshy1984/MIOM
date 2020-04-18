from tkinter import *
import EntranceData
from EntranceData import *


class OperationSwitch():
    def GoToWork(self):
        self.filed2 = "ничего не выбрано"
        a = self.sel.get()
        if a == 1:
            self.field2 = "Формовка цилиндра(обжим)"
        elif a == 2:
            self.field2 = 'Формовка конуса(обжим)'
        elif a == 3:
            self.field2 = 'Формовка сферы(обжим)'
        elif a == 4:
            self.field2 = 'Формовка рифта(обжим)'
        elif a == 5:
            self.field2 = "Формовка цилиндра(раздача)"
        elif a == 6:
            self.field2 = 'Формовка конуса(раздача)'
        elif a == 7:
            self.field2 = 'Формовка сферы(раздача)'
        elif a == 8:
            self.field2 = 'Формовка рифта(раздача)'

        self.OperationSwitch.destroy()
        f = EntranceData.EntranceDataFirst(self.field1, self.field2, self.field3, self.field4)

    def GUI(self):
        self.OperationSwitch = tkinter.Tk()
        self.OperationSwitch.geometry('500x500')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        lbl = tkinter.Label(self.OperationSwitch, text="Выберите необходимую операцию:", font=("Arial Bold", 20))
        lbl.pack(anchor=tkinter.N)
        frame = tkinter.Frame(self.OperationSwitch, relief=tkinter.RAISED, borderwidth=1)
        frame.pack(fill=tkinter.BOTH, expand=True)
        self.sel = tkinter.IntVar()
        operations = [('Формовка цилиндра (обжим)', 1),
                      ('Формовка конуса(обжим)', 2),
                      ('Формовка сферы (обжим)', 3),
                      ('Формовка рифта(обжим)', 4),
                      ('Формовка цилиндра (раздача)', 5),
                      ('Формовка конуса(раздача)', 6),
                      ('Формовка сферы (раздача)', 7),
                      ('Формовка рифта(раздача)', 8), ]

        for operation, val in operations:
            tkinter.Radiobutton(frame, activebackground="yellow", selectcolor='lightblue', text=operation,
                                indicatoron=0, variable=self.sel, value=val, command=self.GoToWork).pack(
                anchor=tkinter.N)
        btn = tkinter.Button(self.OperationSwitch, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=350)
        btn = tkinter.Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.GoToWork)
        btn.place(x=300, y=350)
        self.OperationSwitch.mainloop()

    def __init__(self, a, b, c, d):
        self.field1 = a
        self.field2 = b
        self.field3 = c
        self.field4 = d
        self.GUI()

    def CloseWindow(self):
        self.OperationSwitch.destroy()
