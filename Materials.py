import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *
from EditorMaterials import *


class Materials():
    def GUI(self):
        self.Materials = Tk()
        self.Materials.geometry('1350x700')
        self.Materials.title("Выбор материала ")
        self.Tree = Treeview(self.Materials, columns=(
            "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B",
            "Specific_electric_resistance", "The_coefficient_of_dynamic", 'Еhe_dynamic_modulus_hardening'), height=30,
                              show='headings')
        self.Tree.column("Name_of_the_metalls", width=60, anchor=tkinter.CENTER)
        self.Tree.column("Tensile_strength", width=70, anchor=tkinter.CENTER)
        self.Tree.column("Yield_strength", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Material_density", width=50, anchor=tkinter.CENTER)
        self.Tree.column("M_M", width=50, anchor=tkinter.CENTER)
        self.Tree.column("B", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Specific_electric_resistance", width=50, anchor=tkinter.CENTER)
        self.Tree.column("The_coefficient_of_dynamic", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Еhe_dynamic_modulus_hardening", width=50, anchor=tkinter.CENTER)
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
        self.Tree.place(x=50, y=10)
        label1 = tkinter.Label(self.Materials, text="PPM-предел прочность материала", bg="lightgrey", fg="black")
        label1.place(x=550, y=30)
        label2 = tkinter.Label(self.Materials, text="PYD-предел упругости материала", bg="lightgrey",
                               fg="black")
        label2.place(x=550, y=50)
        label3 = tkinter.Label(self.Materials, text="PLM-плотность материала", bg="lightgrey", fg="black")
        label3.place(x=550, y=70)
        label4 = tkinter.Label(self.Materials,
                               text="M_M и B-вкоэффициенты степенной аппроксимации кривой упрочнения материала",
                               bg="lightgrey", fg="black")
        label4.place(x=550, y=90)
        label6 = tkinter.Label(self.Materials, text="YEMP-удельное электрическое сопротивление материала",
                               bg="lightgrey", fg="black")
        label6.place(x=550, y=110)
        label7 = tkinter.Label(self.Materials, text="MDM-коэффициент динамичности материала", bg="lightgrey",
                               fg="black")
        label7.place(x=550, y=130)
        self.btn = Button(self.Materials, text="Добавить материал", bg="grey", fg="black",
                          command=self.AddMaterial)  # описание объекта типа button названия кнопки
        self.btn.place(x=900, y=650)  # расположение кнопки
        self.btn5 = Button(self.Materials, text="Редактировать материал", bg="grey", fg="black",
                           command=self.EditMaterial)  # описание объекта типа button названия кнопки
        self.btn5.place(x=650, y=650)  # расположение кнопки
        self.btn2 = Button(self.Materials, text="Удалить материал", bg="grey", fg="black",
                           command=self.DelMaterial)  # описание объекта типа button названия кнопки
        self.btn2.place(x=400, y=650)  # расположение кнопки
        self.btn1 = Button(self.Materials, text="Отменить", bg='pink', fg='red', command=self.GoToPrevious)
        self.btn1.place(x=1150, y=650)
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
        NewWindow = EditorMaterials()

    def EditMaterial(self):
        NewWindow = EditorMaterials()

    def DelMaterial(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.f4 = self.slct2[0]
        print(self.slct2)
        print(self.slct2[0])
        print(self.f4)
        NewWindow2 = Terminator(self.f4, "Metalls.db", materials_sql8)

    def GoToPrevious(self):pass


