from tkinter import *
import sqlite3
from tkinter.ttk import Treeview
from SQL12 import *
import Terminator
import SmartCalculation
import EditorMashins

class Basad():
    def GUI(self):
        self.BasaM2 = Toplevel()
        self.BasaM2.geometry('1100x450+700+200')
        self.BasaM2.title("Выбор оборудования МИОМ")
        self.Tree = Treeview(self.BasaM2, columns=(
            "Name", "Max_change_energi", "Condenser_capasity", "Equipment_induct", "SccF", "R0","FW"), height=20,
                                               show='headings')
        self.Tree.column("Name", width=120, anchor=CENTER)
        self.Tree.column("Max_change_energi", width=70, anchor=CENTER)
        self.Tree.column("Condenser_capasity", width=50, anchor=CENTER)
        self.Tree.column("Equipment_induct", width=50, anchor=CENTER)
        self.Tree.column("SccF", width=60, anchor=CENTER)
        self.Tree.column("R0", width=50, anchor=CENTER)
        self.Tree.column("FW", width=50, anchor=CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name", text="Наименование")
        self.Tree.heading("Max_change_energi", text="W_mash")
        self.Tree.heading("Condenser_capasity", text="CCE")
        self.Tree.heading("Equipment_induct", text="LCE")
        self.Tree.heading("SccF", text="FCE")
        self.Tree.heading("R0", text="R0")
        self.Tree.heading("FW", text="FW")
        self.Tree.place(x=50, y=10)
        label1 = Label(self.BasaM2, text="W_mash-максимальная мощность разряда", bg="lightgrey", fg="black")
        label1.place(x=510, y=30)
        label2=Label(self.BasaM2, text="CCЕ-Емкость батареи конденсаторов установки", bg="lightgrey", fg="black")
        label2.place(x=510,y=50)
        label3 = Label(self.BasaM2, text="LCE-индуктивность", bg="lightgrey", fg="black")
        label3.place(x=510, y=70)
        label4 = Label(self.BasaM2, text="FW-величина тока короткого замыкания", bg="lightgrey", fg="black")
        label4.place(x=510, y=90)
        label7 = Label(self.BasaM2, text="R0-активное сопротивление установки", bg="lightgrey", fg="black")
        label7.place(x=510, y=110)
        label8 = Label(self.BasaM2, text="FCE-частота колебаний разрядного тока МИУ в режиме короткого замыкания", bg="lightgrey", fg="black")
        label8.place(x=510, y=110)
        btn = Button(self.BasaM2, text="Добавить оборудование", bg="orange", fg="black",
                                        command=self.AddMashins)  # описание объекта типа button названия кнопки
        btn.place(x=510, y=200)  # расположение кнопки
        btn5 = Button(self.BasaM2, text="Редактировать оборудование", bg="orange", fg="black",
                                         command=self.Edit)  # описание объекта типа button названия кнопки
        btn5.place(x=510, y=250)  # расположение кнопки
        btn2 = Button(self.BasaM2, text="Удалить оборудование", bg="orange", fg="black",
                                         command=self.DellMashins)  # описание объекта типа button названия кнопки
        btn2.place(x=510, y=300)  # расположение кнопки
        btn1 = Button(self.BasaM2, text="Отменить", bg='pink', fg='red', command=self.BasaM2.destroy)
        btn1.place(x=510, y=350)

    def Edit(self):
        sel = self.Tree.focus()
        slct2 = self.Tree.item(sel, option='values')
        field1 = slct2[0]
        field2 = slct2[1]
        field3 = slct2[2]
        field4 = slct2[3]
        field5 = slct2[4]
        field6 = slct2[5]
        field7 = slct2[4]
        self.Editor = Toplevel(self.BasaM2)
        self.Editor.geometry('350x400+1200+400')
        self.Editor.title("Редактировать Материал")
        self.Editor.lift()
        self.Editor.attributes('-topmost', True)
        label1 = Label(self.Editor, text="Наименование", bg="lightgrey", fg="black")
        self.message_entry = Entry(self.Editor, textvariable="")
        self.message_entry.place(x=150, y=10)
        self.message_entry.insert(0,str(field1))
        label2 = Label(self.Editor, text="W_mash", bg="lightgrey", fg="black")
        self.message_entry1 = Entry(self.Editor, textvariable="")
        self.message_entry1.place(x=150, y=60)
        self.message_entry1.insert(0, str(field2))
        label3 = Label(self.Editor, text="CCE", bg="lightgrey", fg="black")
        self.message_entry2 = Entry(self.Editor, textvariable="")
        self.message_entry2.place(x=150, y=110)
        self.message_entry2.insert(0, str(field3))
        label4 = Label(self.Editor, text="LCE", bg="lightgrey", fg="black")
        self.message_entry3 = Entry(self.Editor, textvariable="")
        self.message_entry3.place(x=150, y=160)
        self.message_entry3.insert(0, str(field4))
        label5 = Label(self.Editor, text="FCE", bg="lightgrey", fg="black")
        self.message_entry4 = Entry(self.Editor, textvariable="")
        self.message_entry4.place(x=150, y=210)
        self.message_entry4.insert(0, str(field5))
        label6 = Label(self.Editor, text="R0", bg="lightgrey", fg="black")
        self.message_entry5 = Entry(self.Editor, textvariable="")
        self.message_entry5.place(x=150, y=260)
        self.message_entry5.insert(0, str(field6))
        label7 = Label(self.Editor, text="Fw", bg="lightgrey", fg="black")
        self.message_entry6 = Entry(self.Editor, textvariable="")
        self.message_entry6.place(x=150, y=310)
        self.message_entry6.insert(0, str(field7))
        label1.place(x=10, y=10)
        label2.place(x=10, y=60)
        label3.place(x=10, y=110)
        label4.place(x=10, y=160)
        label5.place(x=10, y=210)
        label6.place(x=10, y=260)
        label7.place(x=10, y=310)
        btn1 = Button(self.Editor, text="Закрыть", bg='red', fg='black', command=self.Editor.destroy)
        btn1.place(x=30, y=350)
        self.a = self.message_entry.get()
        btn2 = Button(self.Editor, text="Запомнить", bg='lightgreen', fg='black', command=self.Update)
        btn2.place(x=200, y=350)

    def Update(self):
        f1 = self.message_entry.get()
        f2 = self.message_entry1.get()
        f3 = self.message_entry2.get()
        f4 = self.message_entry4.get()
        f5 = self.message_entry4.get()
        f6 = self.message_entry5.get()
        f7 = self.message_entry6.get()
        print(f1)
        mt = sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cursor.execute('''Update Mashines set Name=?,W_mash =?,CCE =?,LCE =?,FCE =?,Ro =?,FW =? where Name =?''', (f1, f2, f3, f4, f5, f6, f7,self.a))
        mt.commit()
        self.Tree.delete(*self.Tree.get_children())
        self.view_records()
        self.Editor.destroy()

    def AddMashins(self):
        self.Editor = Toplevel(self.BasaM2)
        self.Editor.geometry('350x400+1200+400')
        self.Editor.title("Добавить Материал")
        self.Editor.lift()
        self.Editor.attributes('-topmost', True)
        label1 = Label(self.Editor, text="Наименование", bg="lightgrey", fg="black")
        self.message_entry = Entry(self.Editor, textvariable="")
        self.message_entry.place(x=150, y=10)
        label2 = Label(self.Editor, text="W_mash", bg="lightgrey", fg="black")
        self.message_entry1 = Entry(self.Editor, textvariable="")
        self.message_entry1.place(x=150, y=60)
        label3 = Label(self.Editor, text="CCE", bg="lightgrey", fg="black")
        self.message_entry2 = Entry(self.Editor, textvariable="")
        self.message_entry2.place(x=150, y=110)
        label4 = Label(self.Editor, text="LCE", bg="lightgrey", fg="black")
        self.message_entry3 = Entry(self.Editor, textvariable="")
        self.message_entry3.place(x=150, y=160)
        label5 = Label(self.Editor, text="FCE", bg="lightgrey", fg="black")
        self.message_entry4 = Entry(self.Editor, textvariable="")
        self.message_entry4.place(x=150, y=210)
        label6 = Label(self.Editor, text="R0", bg="lightgrey", fg="black")
        self.message_entry5 = Entry(self.Editor, textvariable="")
        self.message_entry5.place(x=150, y=260)
        label7 = Label(self.Editor, text="Fw", bg="lightgrey", fg="black")
        self.message_entry6 = Entry(self.Editor, textvariable="")
        self.message_entry6.place(x=150, y=310)
        label1.place(x=10, y=10)
        label2.place(x=10, y=60)
        label3.place(x=10, y=110)
        label4.place(x=10, y=160)
        label5.place(x=10, y=210)
        label6.place(x=10, y=260)
        label7.place(x=10, y=310)
        btn1 = Button(self.Editor, text="Закрыть", bg='red', fg='black', command=self.Editor.destroy)
        btn1.place(x=30, y=350)
        btn2 = Button(self.Editor, text="Запомнить", bg='lightgreen', fg='black',command=self.Insert)
        btn2.place(x=200, y=350)

    def Insert(self):
        f1 = self.message_entry.get()
        f2 = self.message_entry1.get()
        f3 = self.message_entry2.get()
        f4 = self.message_entry4.get()
        f5 = self.message_entry4.get()
        f6 = self.message_entry5.get()
        f7 = self.message_entry6.get()
        mt = sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cursor.execute('''Insert into Mashines values (?,?,?,?,?,?,?);''', (f1, f2, f3, f4, f5, f6, f7))
        mt.commit()
        self.Tree.delete(*self.Tree.get_children())
        self.view_records()
        self.Editor.destroy()

    def DellMashins(self):
        sel = self.Tree.focus()
        slct2 = self.Tree.item(sel, option='values')
        field1 = slct2[0]
        self.SBasa = Toplevel(self.BasaM2)
        self.SBasa.geometry('600x200+1000+400')
        self.SBasa.title("Удаление оборудования МИОМ")
        self.SBasa.lift()  # команда выталкивает окно на верх
        self.SBasa.attributes('-topmost', True)  # окно будет поверх окон
        label1 = Label(self.SBasa, text="Вы действительно хотите удалить это обрудование?  ", bg="lightgrey", fg="black")
        label1.place(x=50, y=50)
        label1 = Label(self.SBasa, text="Внимание! Речь идет о " + field1 + ". Это может быть важная запись!", bg="lightgrey",
                   fg="black")
        label1.place(x=50, y=70)
        btn1 = Button(self.SBasa, text="Закрыть", bg='pink', fg='red', command=self.SBasa.destroy)
        btn1.place(x=30, y=150)
        btn2 = Button(self.SBasa, text="Я все понял. Удалить", bg='green', fg='black')
        btn2.place(x=350, y=150)


    def view_records(self):
        mt = EditorMashins.sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cpt = 0
        for row in cursor.execute("select* from Mashines"):
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1

    def __init__(self):
        self.GUI()
        self.view_records()

