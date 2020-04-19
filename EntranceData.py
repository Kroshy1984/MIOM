import tkinter
import WindowMashins
from SetSizes import SetSizes
from OperationSwitch import OperationSwitch
from InductorParams import InductorParams
from Materials import Materials


class EntranceDataFirst():
    def __init__(self, a, b, c, d):
        self.bif1 = a
        self.bif2 = b
        self.bif3 = c
        self.bif4 = d
        self.GUI(self.bif1, self.bif2, self.bif3, self.bif4)

    def GUI(self, bif1, bif2, bif3, bif4):
        self.EntranceDataWindow = tkinter.Tk()
        self.EntranceDataWindow.geometry('1200x700')  # геометрия окна
        self.EntranceDataWindow.title("Параметры для расчета технологического процесса МИОМ")  # название окна
        self.frame = tkinter.Frame(self.EntranceDataWindow, relief=tkinter.RAISED, borderwidth=1)
        self.frame.pack(fill=tkinter.BOTH, expand=True)
        btn1 = tkinter.Button(self.frame, text="Выбор оборудования", bg="grey", fg="black", command=self.WindowMashins)
        btn2 = tkinter.Button(self.frame, text="Выбор операции", bg="grey", fg="black",
                              command=self.WindowOperationSwitch)
        btn3 = tkinter.Button(self.frame, text="Выбор материала", bg="grey", fg="black", command=self.WindowMaterials)
        btn4 = tkinter.Button(self.frame, text="Размер заготовки и детали", bg="grey", fg="black",
                              command=self.SetSizes)
        btn5 = tkinter.Button(self.frame, text="Параметры индуктора", bg="lightgreen", fg="black",
                              command=self.WindowInductorParams)
        self.message_entry = tkinter.Entry(self.frame, textvariable='')
        self.message_entry.insert(0, bif1)
        self.message_entry.place(x=350, y=100)
        self.message_entry1 = tkinter.Entry(self.frame, textvariable='')
        self.message_entry1.insert(0, bif2)
        self.message_entry1.place(x=350, y=200, width=400)
        self.message_entry2 = tkinter.Entry(self.frame, textvariable='')
        self.message_entry2.insert(0, bif4)
        self.message_entry2.place(x=350, y=300)
        self.message_entry3 = tkinter.Entry(self.frame, textvariable='')
        self.message_entry3.insert(0, bif3)
        self.message_entry3.place(x=350, y=400, width=700)
        btn1.place(x=50, y=100)
        btn2.place(x=50, y=200)
        btn3.place(x=50, y=300)
        btn4.place(x=50, y=400)
        btn5.place(x=50, y=500)
        closeButton = tkinter.Button(self.EntranceDataWindow, text="Close", command=quit)
        closeButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
        okButton = tkinter.Button(self.EntranceDataWindow, text="OK")
        okButton.pack(side=tkinter.RIGHT)
        self.EntranceDataWindow.mainloop()

    def WindowInductorParams(self):
        window3 = InductorParams()

    def WindowMashins(self):
        self.EntranceDataWindow.destroy()
        window = WindowMashins.Basad(self.bif1, self.bif2, self.bif3, self.bif4)

    def SetSizes(self):
        self.EntranceDataWindow.destroy()
        window1 = SetSizes(self.bif1, self.bif2, self.bif3, self.bif4)

    def WindowOperationSwitch(self):
        self.EntranceDataWindow.destroy()
        window2 = OperationSwitch(self.bif1, self.bif2, self.bif3, self.bif4)

    def WindowMaterials(self):
        self.EntranceDataWindow.destroy()
        window4 = Materials(self.bif1, self.bif2, self.bif3, self.bif4)


class EntranceDataSecond():
    def __init__(self):
        self.EntranceDataWindow = tkinter.Tk()
        self.EntranceDataWindow.geometry('640x700')  # геометрия окна
        self.EntranceDataWindow.title("Параметры для расчета технологического процесса МИОМ")  # название окна
        frame = tkinter.Frame(self.EntranceDataWindow, relief=tkinter.RAISED, borderwidth=1)
        frame.pack(fill=tkinter.BOTH, expand=True)
        btn1 = tkinter.Button(frame, text="Выбор оборудования", bg="blue", fg="black", command=self.WindMash)
        btn2 = tkinter.Button(frame, text="Выбор операции", bg="blue", fg="black", command=self.WindowOperationSwitch)
        btn3 = tkinter.Button(frame, text="Выбор материала", bg="blue", fg="black", command=self.WindowMaterials)
        btn4 = tkinter.Button(frame, text="Размер заготовки", bg="blue", fg="black", command=self.SetSizes)
        btn5 = tkinter.Button(frame, text="Параметры индуктора", bg="blue", fg="black",
                              command=self.WindowInductorParams)
        self.message_entry = tkinter.Entry(frame, textvariable='')
        self.message_entry.place(x=350, y=100)
        self.message_entry1 = tkinter.Entry(frame, textvariable='')
        self.message_entry1.place(x=350, y=200)
        self.message_entry2 = tkinter.Entry(frame, textvariable='')
        self.message_entry2.place(x=350, y=300)
        self.message_entry3 = tkinter.Entry(frame, textvariable='')
        self.message_entry3.place(x=350, y=400)
        self.message_entry4 = tkinter.Entry(frame, textvariable='')
        self.message_entry4.place(x=350, y=500)
        btn1.place(x=50, y=100)
        btn2.place(x=50, y=200)
        btn3.place(x=50, y=300)
        btn4.place(x=50, y=400)
        btn5.place(x=50, y=500)
        closeButton = tkinter.Button(self.EntranceDataWindow, text="Close", command=quit)
        closeButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
        okButton = tkinter.Button(self.EntranceDataWindow, text="OK")
        okButton.pack(side=tkinter.RIGHT)
        self.EntranceDataWindow.mainloop()

    def WindMash(self):
        self.EntranceDataWindow.destroy()
        window = WindowMashins.Basad()

    def SetSizes(self):
        window1 = SetSizes()

    def WindowOperationSwitch(self):
        self.EntranceDataWindow.destroy()
        window2 = OperationSwitch()

    def WindowInductorParams(self):
        window3 = InductorParams()

    def WindowMaterials(self):
        window4 = Materials()
