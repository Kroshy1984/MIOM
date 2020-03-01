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
        "Name", "Max_change_energi", "Condenser_capasity", "Equipment_induct", "SccF", "K1", "K2"), height=50,
                                 show='headings')
        self.Tree.grid(padx=8, pady=15)
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