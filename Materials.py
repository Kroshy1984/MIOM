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
        self.Tree = ttk.Treeview(self.Materials, columns=(
            "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B",
            "Specific_electric_resistance", "The_coefficient_of_dynamic", 'Еhe_dynamic_modulus_hardening'), height=30,
                                 show='headings')
        self.Tree.column("Name_of_the_metalls", width=60, anchor=tk.CENTER)
        self.Tree.column("Tensile_strength", width=170, anchor=tk.CENTER)
        self.Tree.column("Yield_strength", width=150, anchor=tk.CENTER)
        self.Tree.column("Material_density", width=100, anchor=tk.CENTER)
        self.Tree.column("M_M", width=50, anchor=tk.CENTER)
        self.Tree.column("B", width=50, anchor=tk.CENTER)
        self.Tree.column("Specific_electric_resistance", width=200, anchor=tk.CENTER)
        self.Tree.column("The_coefficient_of_dynamic", width=230, anchor=tk.CENTER)
        self.Tree.column("Еhe_dynamic_modulus_hardening", width=270, anchor=tk.CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name_of_the_metalls", text="Металл")
        self.Tree.heading("Tensile_strength", text="Предел прочности")
        self.Tree.heading("Yield_strength", text="Предел текучести")
        self.Tree.heading("Material_density", text="Плотность")
        self.Tree.heading("M_M", text="M_M")
        self.Tree.heading("B", text="B")
        self.Tree.heading("Specific_electric_resistance", text="Удельное Сопротивление")
        self.Tree.heading("The_coefficient_of_dynamic", text="Динамический коэффициент")
        self.Tree.heading("Еhe_dynamic_modulus_hardening", text="Модуль коэффициента жесткости")
        self.Tree.place(x=50, y=10)
        self.btn = Button(self.Materials, text="Добавить материал", bg="grey", fg="black",
                          command=self.AddMaterial)  # описание объекта типа button названия кнопки
        self.btn.place(x=900, y=650)  # расположение кнопки
        self.btn5 = Button(self.Materials, text="Редактировать материал", bg="grey", fg="black",
                           command=self.EditMaterial)  # описание объекта типа button названия кнопки
        self.btn5.place(x=650, y=650)  # расположение кнопки
        self.btn2 = Button(self.Materials, text="Удалить материал", bg="grey", fg="black",
                           command=self.DelMaterial)  # описание объекта типа button названия кнопки
        self.btn2.place(x=400, y=650)  # расположение кнопки
        self.btn3 = Button(self.Materials, text="Применить", bg="green", fg="black",
                           command=self.GoToWork)  # описание объекта типа button названия кнопки
        self.btn3.place(x=150, y=650)  # расположение кнопки
        self.btn1 = Button(self.Materials, text="Отменить", bg='pink', fg='red', command=self.GoToPrevious)
        self.btn1.place(x=1150, y=650)
        self.view_records()
        self.Materials.mainloop()

    def __init__(self, a, b, c, d):
        self.f1 = a
        self.f2 = b
        self.f3 = c
        self.f4 = d
        self.GUI()

    def view_records(self):
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cursor.execute(sql10)
        cursor.execute(sql10)
        for row in cursor.execute(sql10): print(row)
        cpt = 0
        for row in cursor.execute(sql10):
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

    def GoToPrevious(self):
        self.f4 = ''
        self.Materials.destroy()
        f = EntranceData.EntranceDataFirst(self.f1, self.f2, self.f3, self.f4)

    def GoToWork(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.f4 = self.slct2[0]
        print(self.slct2)
        print(self.slct2[0])
        print(self.f4)
        self.Materials.destroy()
        f = EntranceData.EntranceDataFirst(self.f1, self.f2, self.f3, self.f4)
