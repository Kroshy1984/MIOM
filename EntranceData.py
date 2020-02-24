from tkinter import *
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
        self.message_entry = Entry(frame,textvariable='')
        self.message_entry.place(x=350, y=100)
        self.message_entry1 = Entry(frame, textvariable='')
        self.message_entry1.place(x=350, y=200)
        self.message_entry2 = Entry(frame, textvariable='')
        self.message_entry2.place(x=350, y=300)
        self.message_entry3 = Entry(frame, textvariable='')
        self.message_entry3.place(x=350, y=400)
        self.message_entry4 = Entry(frame, textvariable='')
        self.message_entry4.place(x=350, y=500)
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