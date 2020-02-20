from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class EntranceData():
    def __init__(self):
        self.EntranceDataWindow = Tk()
        self.EntranceDataWindow.geometry('640x700')  # геометрия окна
        self.EntranceDataWindow.title("Параметры для расчета технологического процесса МИОМ")  # название окна
        frame = Frame(self.EntranceDataWindow, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        closeButton = Button(self.EntranceDataWindow, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self.EntranceDataWindow, text="OK")
        okButton.pack(side=RIGHT)
        self.EntranceDataWindow.mainloop()