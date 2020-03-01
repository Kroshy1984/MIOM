import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *

class Materials():
    def __init__(self):
        self.Materials = Tk()
        self.Materials.geometry('1800x1000')
        self.Materials.title("Выбор материала ")
        self.Tree = ttk.Treeview(self.Materials, columns=(
        "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B", "Specific_electric_resistance","The_coefficient_of_dynamic",'Еhe_dynamic_modulus_hardening'), height=50,
                                 show='headings')
        self.Tree.grid(padx=8, pady=15)
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
        self.Tree.pack()
        self.view_records()
        self.Materials.mainloop()
    def view_records(self):
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cursor.execute(sql6)
        cursor.execute(sql6)
        for row in cursor.execute(sql6): print(row)
        cpt = 0  # Counter representing the ID of your code.
        for row in cursor.execute(sql6):
            # I suppose the first column of your table is ID
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1  # increment the I