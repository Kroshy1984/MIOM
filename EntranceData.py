from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class EntranceData():
    def __init__(self):
        self.EntranceDataWindow = Tk()
        self.EntranceDataWindow.geometry('640x700')  # геометрия окна
        self.EntranceDataWindow.title("Параметры для расчета технологического процесса МИОМ")  # название окна
        frame = Frame(self.EntranceDataWindow, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        btn1=Button(frame,text="Выбор оборудоания")
        btn2=Button(frame,text="Выбор операции")
        btn3=Button(frame, text = "Выбор материала")
        btn4=Button(frame,text = "Размер заготовки")
        btn5=Button(frame, text = "Параметры индуктора")
        btn1.place(x=50,y=100)
        btn2.place(x=50,y=200)
        btn3.place(x=50,y=300)
        btn4.place(x=50,y=400)
        btn5.place(x=50,y=500)
        closeButton = Button(self.EntranceDataWindow, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self.EntranceDataWindow, text="OK")
        okButton.pack(side=RIGHT)
        self.EntranceDataWindow.mainloop()