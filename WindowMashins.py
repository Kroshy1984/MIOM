from tkinter import *
import sqlite3
from tkinter.ttk import Treeview
from SQL12 import *
import EntranceData
import Terminator
import EditorMashins


class Basad():
    def GUI(self):
        self.BasaM2 = Tk()
        self.BasaM2.geometry('1330x700')
        self.BasaM2.title("Выбор оборудования МИОМ")
        self.Tree = Treeview(self.BasaM2, columns=(
            "Name", "Max_change_energi", "Condenser_capasity", "Equipment_induct", "SccF", "R0"), height=20,
                                               show='headings')
        self.Tree.column("Name", width=150, anchor=CENTER)
        self.Tree.column("Max_change_energi", width=70, anchor=CENTER)
        self.Tree.column("Condenser_capasity", width=50, anchor=CENTER)
        self.Tree.column("Equipment_induct", width=50, anchor=CENTER)
        self.Tree.column("SccF", width=60, anchor=CENTER)
        self.Tree.column("R0", width=50, anchor=CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name", text="Наименование")
        self.Tree.heading("Max_change_energi", text="W_mash")
        self.Tree.heading("Condenser_capasity", text="CCE")
        self.Tree.heading("Equipment_induct", text="LCE")
        self.Tree.heading("SccF", text="FW")
        self.Tree.heading("R0", text="R0")
        self.Tree.place(x=50, y=10)
        label1 = Label(self.BasaM2, text="W_mash-максимальная мощность разряда", bg="lightgrey", fg="black")
        label1.place(x=600, y=30)
        label2=Label(self.BasaM2, text="CCT-Емкость батареи конденсаторов установки", bg="lightgrey", fg="black")
        label2.place(x=600,y=50)
        label3 = Label(self.BasaM2, text="LCE-индуктивность", bg="lightgrey", fg="black")
        label3.place(x=600, y=70)
        label4 = Label(self.BasaM2, text="FW-величина тока короткого замыкания", bg="lightgrey", fg="black")
        label4.place(x=600, y=90)
        label7 = Label(self.BasaM2, text="R0-активное сопротивление установки", bg="lightgrey", fg="black")
        label7.place(x=600, y=150)
        self.btn = EditorMashins.Button(self.BasaM2, text="Добавить оборудование", bg="orange", fg="black",
                                        command=self.AddMashins)  # описание объекта типа button названия кнопки
        self.btn.place(x=300, y=500)  # расположение кнопки
        self.btn5 = EditorMashins.Button(self.BasaM2, text="Редактировать оборудование", bg="orange", fg="black",
                                         command=self.clicked2)  # описание объекта типа button названия кнопки
        self.btn5.place(x=800, y=500)  # расположение кнопки
        self.btn2 = EditorMashins.Button(self.BasaM2, text="Удалить оборудование", bg="orange", fg="black",
                                         command=self.DellMashins)  # описание объекта типа button названия кнопки
        self.btn2.place(x=550, y=500)  # расположение кнопки
        self.btn1 = EditorMashins.Button(self.BasaM2, text="Отменить", bg='pink', fg='red', command=self.BasaM2.destroy)
        self.btn1.place(x=1150, y=500)
        self.btn4 = EditorMashins.Button(self.BasaM2, text="Взять данные в работу", bg='green', fg='black',
                                         command=self.GoToWork)
        self.btn4.place(x=50, y=500)

    def clicked2(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1 = self.slct2[0]
        self.field2 = self.slct2[1]
        self.field3 = self.slct2[2]
        self.field4 = self.slct2[3]
        self.field5 = self.slct2[4]
        NewWindow = EditorMashins.Editor(self.field1, self.field2, self.field3, self.field4, self.field5)

    def AddMashins(self):
        self.field1 = ""
        self.field2 = ""
        self.field3 = ""
        self.field4 = ""
        self.field5 = ""
        NewWindow = EditorMashins.Editor(self.field1, self.field2, self.field3, self.field4, self.field5)

    def DellMashins(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1 = self.slct2[0]
        print(self.slct2)
        print(self.slct2[0])
        print(self.field1)
        NewWindow2 = EditorMashins.Terminator.Terminator(self.field1, "mashins.db", EditorMashins.sql8)

    def view_records(self):
        mt = EditorMashins.sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cursor.execute(EditorMashins.sql6)
        cursor.execute(EditorMashins.sql6)
        for row in cursor.execute(EditorMashins.sql6): print(row)
        cpt = 0
        for row in cursor.execute(EditorMashins.sql6):
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1

    def GoToWork(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1 = self.slct2[0]
        self.BasaM2.destroy()
        f = EditorMashins.EntranceData.EntranceDataFirst(self.field1, self.f2, self.f3, self.f4)

    def __init__(self, a, b, c, d):
        self.field1 = a
        self.f2 = b
        self.f3 = c
        self.f4 = d
        self.GUI()
        self.view_records()
        self.BasaM2.mainloop()
