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
        self.slct2 = ['Выбери из таблицы', 'Выбери из таблицы', 'Выбери из таблицы', 'Выбери из таблицы',
                      'Выбери из таблицы', 'Выбери из таблицы', 'Выбери из таблицы']
        self.field1 = self.slct2[0]
        self.field2 = self.slct2[1]
        self.field3 = self.slct2[2]
        self.field4 = self.slct2[3]
        self.field5 = self.slct2[4]
        self.field6 = self.slct2[5]
        self.field7 = self.slct2[6]
        self.btn = Button(self.Materials, text="Добавить материал", bg="grey", fg="black")  # описание объекта типа button названия кнопки
        self.btn.place(x=250, y=800)  # расположение кнопки
        self.btn5 = Button(self.Materials, text="Редактировать материал", bg="grey", fg="black")  # описание объекта типа button названия кнопки
        self.btn5.place(x=750, y=800)  # расположение кнопки
        self.btn2 = Button(self.Materials, text="Удалить материал", bg="grey", fg="black")  # описание объекта типа button названия кнопки
        self.btn2.place(x=500, y=800)  # расположение кнопки
        self.btn3 = Button(self.Materials, text="Применить", bg="grey", fg="black")  # описание объекта типа button названия кнопки
        self.btn3.place(x=1000, y=800)  # расположение кнопки
        self.btn1 = Button(self.Materials, text="Отменить", bg='pink', fg='red')
        self.btn1.place(x=1250, y=800)
        self.btn4 = Button(self.Materials, text="Взять данные в работу", bg='green', fg='black')
        self.btn4.place(x=50, y=800)
        if self.field1 == 'Выбери из таблицы': self.btn4['state'] = 'disabled'
        label1 = Label(self.Materials, text="Металл", bg="grey", fg="black")
        self.message_entry = Entry(self.Materials, textvariable='')
        self.message_entry.insert(0, self.field1)
        self.message_entry.place(x=50, y=75)
        label2 = Label(self.Materials, text="Предел прочности", bg="grey", fg="black")
        self.message_entry1 = Entry(self.Materials, textvariable='')
        self.message_entry1.place(x=50, y=175)
        self.message_entry1.insert(0, self.field2)
        label3 = Label(self.Materials, text="Предел текучести", bg="grey", fg="black")
        self.message_entry2 = Entry(self.Materials, textvariable='')
        self.message_entry2.place(x=50, y=275)
        self.message_entry2.insert(0, self.field3)
        label4 = Label(self.Materials, text="Плотность", bg="grey", fg="black")
        self.message_entry3 = Entry(self.Materials, textvariable='')
        self.message_entry3.place(x=50, y=375)
        self.message_entry3.insert(0, self.field4)
        label5 = Label(self.Materials, text="М_м", bg="grey", fg="black")
        self.message_entry4 = Entry(self.Materials, textvariable='')
        self.message_entry4.place(x=50, y=475)
        self.message_entry4.insert(0, self.field5)
        label6 = Label(self.Materials, text="В", bg="grey", fg="black")
        self.message_entry5 = Entry(self.Materials, textvariable='')
        self.message_entry5.place(x=50, y=575)
        self.message_entry5.insert(0, self.field6)
        label7 = Label(self.Materials, text="Предел прочности", bg="grey", fg="black")
        self.message_entry6 = Entry(self.Materials, textvariable=self.field7)
        self.message_entry6.place(x=50, y=675)
        self.message_entry6.insert(0, self.field7)
        label1.place(x=50, y=50)
        label2.place(x=50, y=150)
        label3.place(x=50, y=250)
        label4.place(x=50, y=350)
        label5.place(x=50, y=450)
        label6.place(x=50, y=550)
        label7.place(x=50, y=650)
        self.view_records()

        self.Materials.mainloop()
    def view_records(self):
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cursor.execute(sql10)
        cursor.execute(sql10)
        for row in cursor.execute(sql10): print(row)
        cpt = 0  # Counter representing the ID of your code.
        for row in cursor.execute(sql10):
            # I suppose the first column of your table is ID
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1  # increment the I