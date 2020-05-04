import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


class Materials():
    def GUI(self):
        self.Materials = Tk()
        self.Materials.geometry('1260x700')
        self.Materials.title("Выбор материала ")
        self.Tree = ttk.Treeview(self.Materials, columns=(
            "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B",
            "Specific_electric_resistance", "The_coefficient_of_dynamic", 'Еhe_dynamic_modulus_hardening','E_z','E_up'), height=30,
                              show='headings')
        self.Tree.column("Name_of_the_metalls", width=60, anchor=CENTER)
        self.Tree.column("Tensile_strength", width=70, anchor=CENTER)
        self.Tree.column("Yield_strength", width=50, anchor=CENTER)
        self.Tree.column("Material_density", width=50, anchor=CENTER)
        self.Tree.column("M_M", width=50, anchor=CENTER)
        self.Tree.column("B", width=50, anchor=CENTER)
        self.Tree.column("Specific_electric_resistance", width=50, anchor=CENTER)
        self.Tree.column("The_coefficient_of_dynamic", width=50, anchor=CENTER)
        self.Tree.column("Еhe_dynamic_modulus_hardening", width=50, anchor=CENTER)
        self.Tree.column("E_z", width=50, anchor=CENTER)
        self.Tree.column("E_up", width=50, anchor=CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name_of_the_metalls", text="Металл")
        self.Tree.heading("Tensile_strength", text="PPM")
        self.Tree.heading("Yield_strength", text="PYD")
        self.Tree.heading("Material_density", text="PLM")
        self.Tree.heading("M_M", text="M_M")
        self.Tree.heading("B", text="B")
        self.Tree.heading("Specific_electric_resistance", text="YEMP")
        self.Tree.heading("The_coefficient_of_dynamic", text="KDM")
        self.Tree.heading("Еhe_dynamic_modulus_hardening", text="MDM")
        self.Tree.heading("E_z", text="E_z")
        self.Tree.heading("E_up", text="E_up")
        self.Tree.place(x=50, y=10)
        label1 = Label(self.Materials, text="PPM-предел прочность материала", bg="lightgrey", fg="black")
        label1.place(x=650, y=30)
        label2 = Label(self.Materials, text="PYD-предел упругости материала", bg="lightgrey",
                               fg="black")
        label2.place(x=650, y=50)
        label3 = Label(self.Materials, text="PLM-плотность материала", bg="lightgrey", fg="black")
        label3.place(x=650, y=70)
        label4 = Label(self.Materials,
                               text="M_M и B-вкоэффициенты степенной аппроксимации кривой упрочнения материала",
                               bg="lightgrey", fg="black")
        label4.place(x=650, y=90)
        label6 = Label(self.Materials, text="YEMP-удельное электрическое сопротивление материала",
                               bg="lightgrey", fg="black")
        label6.place(x=650, y=110)
        label7 = Label(self.Materials, text="MDM-коэффициент динамичности материала", bg="lightgrey",
                               fg="black")
        label7.place(x=650, y=130)
        self.btn = Button(self.Materials, text="Добавить материал", bg="orange", fg="black",
                          command=self.AddMaterial)  # описание объекта типа button названия кнопки
        self.btn.place(x=650, y=150)  # расположение кнопки
        self.btn5 = Button(self.Materials, text="Редактировать материал", bg="orange", fg="black",
                           command=self.EditMaterial)  # описание объекта типа button названия кнопки
        self.btn5.place(x=650, y=200)  # расположение кнопки
        self.btn2 = Button(self.Materials, text="Удалить материал", bg="orange", fg="black",
                           command=self.DelMaterial)  # описание объекта типа button названия кнопки
        self.btn2.place(x=650, y=250)  # расположение кнопки
        self.btn1 = Button(self.Materials, text="Закрыть", bg='pink', fg='red', command=self.Materials.destroy)
        self.btn1.place(x=650, y=300)
        self.view_records()
        self.Materials.mainloop()

    def __init__(self):
        self.GUI()

    def view_records(self):
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        for row in cursor.execute("select* from material"): print(row)
        cpt = 0
        for row in cursor.execute("select* from material"):
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1

    def AddMaterial(self):
        self.SBasa2 = Toplevel(self.Materials)
        self.SBasa2.geometry('300x600+800+300')
        self.SBasa2.title("Добавить Материал")
        self.SBasa2.lift()
        self.SBasa2.attributes('-topmost', True)
        label1 = Label(self.SBasa2, text="Металл", bg="lightgrey", fg="black")
        self.message_entry = Entry(self.SBasa2, textvariable="")
        self.message_entry.place(x=100, y=10)
        label2 = Label(self.SBasa2, text="PPM", bg="lightgrey", fg="black")
        self.message_entry1 = Entry(self.SBasa2, textvariable="")
        self.message_entry1.place(x=100, y=60)
        label3 = Label(self.SBasa2, text="PYD", bg="lightgrey", fg="black")
        self.message_entry2 = Entry(self.SBasa2, textvariable="")
        self.message_entry2.place(x=100, y=110)
        label4 = Label(self.SBasa2, text="PLM", bg="lightgrey", fg="black")
        self.message_entry3 = Entry(self.SBasa2, textvariable="")
        self.message_entry3.place(x=100, y=160)
        label5 = Label(self.SBasa2, text="М_м", bg="lightgrey", fg="black")
        self.message_entry4 = Entry(self.SBasa2, textvariable="")
        self.message_entry4.place(x=100, y=210)
        label6 = Label(self.SBasa2, text="В", bg="lightgrey", fg="black")
        self.message_entry5 = Entry(self.SBasa2, textvariable="")
        self.message_entry5.place(x=100, y=260)
        label7 = Label(self.SBasa2, text="YEMP", bg="lightgrey", fg="black")
        self.message_entry6 = Entry(self.SBasa2, textvariable="")
        self.message_entry6.place(x=100, y=310)
        label8 = Label(self.SBasa2, text="MDM", bg="lightgrey", fg="black")
        self.message_entry7 = Entry(self.SBasa2, textvariable="")
        self.message_entry7.place(x=100, y=360)
        label9 = Label(self.SBasa2, text="KDM", bg="lightgrey", fg="black")
        self.message_entry8 = Entry(self.SBasa2, textvariable="")
        self.message_entry8.place(x=100, y=410)
        label10 = Label(self.SBasa2, text="E_z", bg="lightgrey", fg="black")
        self.message_entry9 = Entry(self.SBasa2, textvariable="")
        self.message_entry9.place(x=100, y=460)
        label11 = Label(self.SBasa2, text="E_up", bg="lightgrey", fg="black")
        self.message_entry10 = Entry(self.SBasa2, textvariable="")
        self.message_entry10.place(x=100, y=510)
        label1.place(x=10, y=10)
        label2.place(x=10, y=60)
        label3.place(x=10, y=110)
        label4.place(x=10, y=160)
        label5.place(x=10, y=210)
        label6.place(x=10, y=260)
        label7.place(x=10, y=310)
        label8.place(x=10, y=360)
        label9.place(x=10, y=410)
        label10.place(x=10, y=460)
        label11.place(x=10, y=510)
        btn1 = Button(self.SBasa2, text="Закрыть", bg='pink', fg='red', command=self.SBasa2.destroy)
        btn1.place(x=10, y=550)
        btn2 = Button(self.SBasa2, text="Запомнить", bg='green', fg='black', command=self.Insert)
        btn2.place(x=150, y=550)

    def Insert(self):
        f1 = self.message_entry.get()
        f2 = self.message_entry1.get()
        f3 = self.message_entry2.get()
        f4 = self.message_entry3.get()
        f5 = self.message_entry4.get()
        f6 = self.message_entry5.get()
        f7 = self.message_entry6.get()
        f8 = self.message_entry7.get()
        f9 = self.message_entry8.get()
        f10 = self.message_entry9.get()
        f11 = self.message_entry10.get()
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cursor.execute('''Insert into material values (?,?,?,?,?,?,?,?,?,?,?);''', (f1, f2, f3, f4, f5, f6, f7,f8,f9,f10,f11))
        mt.commit()
        self.Tree.delete(*self.Tree.get_children())
        self.view_records()
        self.SBasa2.destroy()

    def EditMaterial(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.name=self.slct2[0]
        PPM=self.slct2[1]
        PYD=self.slct2[2]
        PLM=self.slct2[3]
        M_m=self.slct2[4]
        B=self.slct2[5]
        YEMP=self.slct2[6]
        MDM=self.slct2[7]
        KDM=self.slct2[8]
        E_z=self.slct2[9]
        E_up=self.slct2[10]
        self.SBasa = Toplevel(self.Materials)
        self.SBasa.geometry('300x600+800+300')
        self.SBasa.title("Добавить Материал")
        self.SBasa.lift()
        self.SBasa.attributes('-topmost', True)
        label1 = Label(self.SBasa, text="Металл", bg="lightgrey", fg="black")
        self.message_entry = Entry(self.SBasa, textvariable="")
        self.message_entry.insert(0,self.name)
        self.message_entry.place(x=100, y=10)
        label2 = Label(self.SBasa, text="PPM", bg="lightgrey", fg="black")
        self.message_entry1 = Entry(self.SBasa, textvariable="")
        self.message_entry1.insert(0,PPM)
        self.message_entry1.place(x=100, y=60)
        label3 = Label(self.SBasa, text="PYD", bg="lightgrey", fg="black")
        self.message_entry2 = Entry(self.SBasa, textvariable="")
        self.message_entry2.insert(0, PYD)
        self.message_entry2.place(x=100, y=110)
        label4 = Label(self.SBasa, text="PLM", bg="lightgrey", fg="black")
        self.message_entry3 = Entry(self.SBasa, textvariable="")
        self.message_entry3.insert(0, PLM)
        self.message_entry3.place(x=100, y=160)
        label5 = Label(self.SBasa, text="М_м", bg="lightgrey", fg="black")
        self.message_entry4 = Entry(self.SBasa, textvariable="")
        self.message_entry4.insert(0, M_m)
        self.message_entry4.place(x=100, y=210)
        label6 = Label(self.SBasa, text="В", bg="lightgrey", fg="black")
        self.message_entry5 = Entry(self.SBasa, textvariable="")
        self.message_entry5.insert(0, B)
        self.message_entry5.place(x=100, y=260)
        label7 = Label(self.SBasa, text="YEMP", bg="lightgrey", fg="black")
        self.message_entry6 = Entry(self.SBasa, textvariable="")
        self.message_entry6.insert(0, YEMP)
        self.message_entry6.place(x=100, y=310)
        label8 = Label(self.SBasa, text="MDM", bg="lightgrey", fg="black")
        self.message_entry7 = Entry(self.SBasa, textvariable="")
        self.message_entry7.insert(0, MDM)
        self.message_entry7.place(x=100, y=360)
        label9 = Label(self.SBasa, text="KDM", bg="lightgrey", fg="black")
        self.message_entry8 = Entry(self.SBasa, textvariable="")
        self.message_entry8.insert(0, KDM)
        self.message_entry8.place(x=100, y=410)
        label10 = Label(self.SBasa, text="E_z", bg="lightgrey", fg="black")
        self.message_entry9 = Entry(self.SBasa, textvariable="")
        self.message_entry9.insert(0, E_z)
        self.message_entry9.place(x=100, y=460)
        label11 = Label(self.SBasa, text="E_up", bg="lightgrey", fg="black")
        self.message_entry10 = Entry(self.SBasa, textvariable="")
        self.message_entry10.insert(0,E_up)
        self.message_entry10.place(x=100, y=510)
        label1.place(x=10, y=10)
        label2.place(x=10, y=60)
        label3.place(x=10, y=110)
        label4.place(x=10, y=160)
        label5.place(x=10, y=210)
        label6.place(x=10, y=260)
        label7.place(x=10, y=310)
        label8.place(x=10, y=360)
        label9.place(x=10, y=410)
        label10.place(x=10, y=460)
        label11.place(x=10, y=510)
        btn1 = Button(self.SBasa, text="Закрыть", bg='pink', fg='red', command=self.SBasa.destroy)
        btn1.place(x=10, y=550)
        btn2 = Button(self.SBasa, text="Запомнить", bg='green', fg='black', command=self.Update)
        btn2.place(x=150, y=550)

    def Update(self):
        f1 = self.message_entry.get()
        f2 = self.message_entry1.get()
        f3 = self.message_entry2.get()
        f4 = self.message_entry3.get()
        f5 = self.message_entry4.get()
        f6 = self.message_entry5.get()
        f7 = self.message_entry6.get()
        f8 = self.message_entry7.get()
        f9 = self.message_entry8.get()
        f10 = self.message_entry9.get()
        f11 = self.message_entry10.get()
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cursor.execute('''Update material set name =?,PPM =?,PYD =?,PLM =?,M_m =?,B =?,YEMP =?,MDM=?,KDM=?,E_z=?,E_up=? where name =?''',
                       (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11,self.name))
        mt.commit()
        self.Tree.delete(*self.Tree.get_children())
        self.view_records()
        self.SBasa.destroy()

    def DelMaterial(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.shotit = self.slct2[0]
        self.T = Toplevel(self.Materials)
        self.T.geometry('600x200+1000+400')
        self.T.title("Удаление оборудования МИОМ")
        self.T.lift()  # команда выталкивает окно на верх
        self.T.attributes('-topmost', True)  # окно будет поверх окон
        label1 = Label(self.T, text="Вы действительно хотите удалить это обрудование?  ", bg="lightgrey",
                       fg="black")
        label1.place(x=50, y=50)
        label1 = Label(self.T, text="Внимание! Речь идет о " + self.shotit + ". Это может быть важная запись!",
                       bg="lightgrey",
                       fg="black")
        label1.place(x=50, y=70)
        btn1 = Button(self.T, text="Закрыть", bg='pink', fg='red', command=self.T.destroy)
        btn1.place(x=30, y=150)
        btn2 = Button(self.T, text="Я все понял. Удалить", bg='green', fg='black', command=self.Delete)
        btn2.place(x=350, y=150)

    def Delete(self):
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cursor.execute("Delete from material where name =?", (self.shotit,))
        mt.commit()
        self.Tree.delete(*self.Tree.get_children())
        self.view_records()
        self.T.destroy()
       
