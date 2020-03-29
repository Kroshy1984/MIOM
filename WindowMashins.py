from tkinter import ttk
import sqlite3
from SQL12 import *
import EntranceData
from Terminator import Terminator
from EditorMashins import *
class Basad():
    def GUI (self):
        self.BasaM2 = Tk()
        self.BasaM2.geometry('1330x700')
        self.BasaM2.title("Выбор оборудования МИОМ")
        self.Tree = ttk.Treeview(self.BasaM2, columns=(
        "Name", "Max_change_energi", "Condenser_capasity", "Equipment_induct", "SccF", "K1", "K2"), height=20,
                                 show='headings')
        self.Tree.column("Name", width=250, anchor=tk.CENTER)
        self.Tree.column("Max_change_energi", width=190, anchor=tk.CENTER)
        self.Tree.column("Condenser_capasity", width=250, anchor=tk.CENTER)
        self.Tree.column("Equipment_induct", width=230, anchor=tk.CENTER)
        self.Tree.column("SccF", width=280, anchor=tk.CENTER)
        self.Tree.column("K1", width=60, anchor=tk.CENTER)
        self.Tree.column("K2", width=50, anchor=tk.CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name", text="Наименование оборудования")
        self.Tree.heading("Max_change_energi", text="Максимальная энергия")
        self.Tree.heading("Condenser_capasity", text="Емкость батареи кондецаторов")
        self.Tree.heading("Equipment_induct", text=" Собственная индуктивность")
        self.Tree.heading("SccF", text="Частота тока короткого замыкания")
        self.Tree.heading("K1", text="K1")
        self.Tree.heading("K2", text="K2")
        self.Tree.place(x=10, y=10)
        self.btn = Button(self.BasaM2, text="Добавить оборудование", bg="grey", fg="black",
                          command=self.AddMashins)  # описание объекта типа button названия кнопки
        self.btn.place(x=300, y=500)  # расположение кнопки
        self.btn5 = Button(self.BasaM2, text="Редактировать оборудование", bg="grey", fg="black",
                           command=self.clicked2)  # описание объекта типа button названия кнопки
        self.btn5.place(x=800, y=500)  # расположение кнопки
        self.btn2 = Button(self.BasaM2, text="Удалить оборудование", bg="grey", fg="black",
                           command=self.DellMashins)  # описание объекта типа button названия кнопки
        self.btn2.place(x=550, y=500)  # расположение кнопки
        self.btn1 = Button(self.BasaM2, text="Отменить", bg='pink', fg='red', command=self.BasaM2.destroy)
        self.btn1.place(x=1150, y=500)
        self.btn4 = Button(self.BasaM2, text="Взять данные в работу", bg='green', fg='black', command=self.GoToWork)
        self.btn4.place(x=50, y=500)
    def clicked2(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1 = self.slct2[0]
        self.field2 = self.slct2[1]
        self.field3 = self.slct2[2]
        self.field4 = self.slct2[3]
        self.field5 = self.slct2[4]
        self.field6 = self.slct2[5]
        self.field7 = self.slct2[6]
        NewWindow = Editor(self.field1, self.field2, self.field3, self.field4, self.field5, self.field6, self.field7)
    def AddMashins(self):
        self.field1 = ""
        self.field2 = ""
        self.field3 = ""
        self.field4 = ""
        self.field5 = ""
        self.field6 = ""
        self.field7 = ""
        NewWindow = Editor(self.field1, self.field2, self.field3, self.field4, self.field5, self.field6, self.field7)
    def DellMashins(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1=self.slct2[0]
        print(self.slct2)
        print(self.slct2[0])
        print(self.field1)
        NewWindow2 = Terminator(self.field1)
    def view_records(self):
        mt = sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cursor.execute(sql6)
        cursor.execute(sql6)
        for row in cursor.execute(sql6): print(row)
        cpt = 0
        for row in cursor.execute(sql6):
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1
    def GoToWork(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1 = self.slct2[0]
        self.BasaM2.destroy()
        f=EntranceData.EntranceDataFirst(self.field1, self.f2, self.f3,self.f4)
    def __init__(self, a, b,c,d):
        self.field1=a
        self.f2=b
        self.f3=c
        self.f4=d
        self.GUI()
        self.view_records()
        self.BasaM2.mainloop()