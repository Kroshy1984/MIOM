import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *


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
        self.btn1 = Button(self.Materials, text="Отменить", bg='pink', fg='red', command=self.GoToPrevious)
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
        self.SBasa2.geometry('350x400+800+300')
        self.SBasa2.title("Добавить Материал")
        self.SBasa2.lift()
        self.SBasa2.attributes('-topmost', True)
        label1 = Label(self.SBasa2, text="Металл", bg="grey", fg="black")
        self.message_entry = Entry(self.SBasa2, textvariable="")
        self.message_entry.place(x=150, y=10)
        label2 = Label(self.SBasa2, text="Предел прочности", bg="grey", fg="black")
        self.message_entry1 = Entry(self.SBasa2, textvariable="")
        self.message_entry1.place(x=150, y=60)
        label3 = Label(self.SBasa2, text="Предел текучести", bg="grey", fg="black")
        self.message_entry2 = Entry(self.SBasa2, textvariable="")
        self.message_entry2.place(x=150, y=110)
        label4 = Label(self.SBasa2, text="Плотность", bg="grey", fg="black")
        self.message_entry3 = Entry(self.SBasa2, textvariable="")
        self.message_entry3.place(x=150, y=160)
        label5 = Label(self.SBasa2, text="М_м", bg="grey", fg="black")
        self.message_entry4 = Entry(self.SBasa2, textvariable="")
        self.message_entry4.place(x=150, y=210)
        label6 = Label(self.SBasa2, text="В", bg="grey", fg="black")
        self.message_entry5 = Entry(self.SBasa2, textvariable="")
        self.message_entry5.place(x=150, y=260)
        label7 = Label(self.SBasa2, text="Удельное сопротивление", bg="grey", fg="black")
        self.message_entry6 = Entry(self.SBasa2, textvariable="")
        self.message_entry6.place(x=150, y=310)
        label1.place(x=10, y=10)
        label2.place(x=10, y=60)
        label3.place(x=10, y=110)
        label4.place(x=10, y=160)
        label5.place(x=10, y=210)
        label6.place(x=10, y=260)
        label7.place(x=10, y=310)
        btn1 = Button(self.SBasa2, text="Закрыть", bg='pink', fg='red', command=self.SBasa2.destroy)
        btn1.place(x=30, y=750)
        btn2 = Button(self.SBasa2, text="Запомнить", bg='green', fg='black')
        btn2.place(x=450, y=750)


    def EditMaterial(self):
        self.SBasa = Toplevel(self.Materials)
        self.SBasa.geometry('350x400+800+300')
        self.SBasa.title("Добавить Материал")
        self.SBasa.lift()
        self.SBasa.attributes('-topmost', True)
        label1 = Label(self.SBasa, text="Металл", bg="grey", fg="black")
        self.message_entry = Entry(self.SBasa, textvariable="")
        self.message_entry.place(x=400, y=50)
        label2 = Label(self.SBasa, text="Предел прочности", bg="grey", fg="black")
        self.message_entry1 = Entry(self.SBasa, textvariable="")
        self.message_entry1.place(x=400, y=150)
        label3 = Label(self.SBasa, text="Предел текучести", bg="grey", fg="black")
        self.message_entry2 = Entry(self.SBasa, textvariable="")
        self.message_entry2.place(x=400, y=250)
        label4 = Label(self.SBasa, text="Плотность", bg="grey", fg="black")
        self.message_entry3 = Entry(self.SBasa, textvariable="")
        self.message_entry3.place(x=400, y=350)
        label5 = Label(self.SBasa, text="М_м", bg="grey", fg="black")
        self.message_entry4 = Entry(self.SBasa, textvariable="")
        self.message_entry4.place(x=400, y=450)
        label6 = Label(self.SBasa, text="В", bg="grey", fg="black")
        self.message_entry5 = Entry(self.SBasa, textvariable="")
        self.message_entry5.place(x=400, y=550)
        label7 = Label(self.SBasa, text="Удельное сопротивление", bg="grey", fg="black")
        self.message_entry6 = Entry(self.SBasa, textvariable="")
        self.message_entry6.place(x=400, y=650)
        label1.place(x=10, y=50)
        label2.place(x=10, y=150)
        label3.place(x=10, y=250)
        label4.place(x=10, y=350)
        label5.place(x=10, y=450)
        label6.place(x=10, y=550)
        label7.place(x=10, y=650)
        btn1 = Button(self.SBasa, text="Закрыть", bg='pink', fg='red', command=self.SBasa.destroy)
        btn1.place(x=30, y=750)
        btn2 = Button(self.SBasa, text="Запомнить", bg='green', fg='black')
        btn2.place(x=450, y=750)

    def DelMaterial(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.f4 = self.slct2[0]
        print(self.slct2)
        print(self.slct2[0])
        print(self.f4)
       
    def GoToPrevious(self):pass


