import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *
from EntranceData import *
import EntranceData
class Basad():
    def GUI (self):
        self.BasaM2 = Tk()
        self.BasaM2.geometry('1800x1000')
        self.BasaM2.title("Выбор оборудования МИОМ")
        self.Tree = ttk.Treeview(self.BasaM2, columns=(
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
        self.slct2 = ['Выбери из таблицы', 'Выбери из таблицы', 'Выбери из таблицы', 'Выбери из таблицы',
                      'Выбери из таблицы', 'Выбери из таблицы', 'Выбери из таблицы']
        self.field1 = self.slct2[0]
        self.field2 = self.slct2[1]
        self.field3 = self.slct2[2]
        self.field4 = self.slct2[3]
        self.field5 = self.slct2[4]
        self.field6 = self.slct2[5]
        self.field7 = self.slct2[6]
        self.btn = Button(self.BasaM2, text="Добавить оборудование", bg="grey", fg="black",
                          command=self.AddMashins)  # описание объекта типа button названия кнопки
        self.btn.place(x=250, y=800)  # расположение кнопки
        self.btn5 = Button(self.BasaM2, text="Редактировать оборудование", bg="grey", fg="black",
                           command=self.clicked2)  # описание объекта типа button названия кнопки
        self.btn5.place(x=750, y=800)  # расположение кнопки
        self.btn2 = Button(self.BasaM2, text="Удалить оборудование", bg="grey", fg="black",
                           command=self.DellMashins)  # описание объекта типа button названия кнопки
        self.btn2.place(x=500, y=800)  # расположение кнопки
        self.btn3 = Button(self.BasaM2, text="Применить", bg="grey", fg="black",
                           command=self.SelectlMashins)  # описание объекта типа button названия кнопки
        self.btn3.place(x=1000, y=800)  # расположение кнопки
        self.btn1 = Button(self.BasaM2, text="Отменить", bg='pink', fg='red', command=self.BasaM2.destroy)
        self.btn1.place(x=1250, y=800)
        self.btn4 = Button(self.BasaM2, text="Взять данные в работу", bg='green', fg='black', command=self.GoToWork)
        self.btn4.place(x=50, y=800)
        if self.field1 == 'Выбери из таблицы': self.btn4['state'] = 'disabled'
        label1 = Label(self.BasaM2, text="Название оборудования", bg="grey", fg="black")
        self.message_entry = Entry(self.BasaM2, textvariable='')
        self.message_entry.insert(0, self.field1)
        self.message_entry.place(x=50, y=75)
        label2 = Label(self.BasaM2, text="Максимальная энергия заряда", bg="grey", fg="black")
        self.message_entry1 = Entry(self.BasaM2, textvariable='')
        self.message_entry1.place(x=50, y=175)
        self.message_entry1.insert(0, self.field2)
        label3 = Label(self.BasaM2, text="Емкость батареи кондецаторов", bg="grey", fg="black")
        self.message_entry2 = Entry(self.BasaM2, textvariable='')
        self.message_entry2.place(x=50, y=275)
        self.message_entry2.insert(0, self.field3)
        label4 = Label(self.BasaM2, text="Собственная индуктивность разрядного контура", bg="grey", fg="black")
        self.message_entry3 = Entry(self.BasaM2, textvariable='')
        self.message_entry3.place(x=50, y=375)
        self.message_entry3.insert(0, self.field4)
        label5 = Label(self.BasaM2, text="Частота тока короткого замыкания", bg="grey", fg="black")
        self.message_entry4 = Entry(self.BasaM2, textvariable='')
        self.message_entry4.place(x=50, y=475)
        self.message_entry4.insert(0, self.field5)
        label6 = Label(self.BasaM2, text="K1", bg="grey", fg="black")
        self.message_entry5 = Entry(self.BasaM2, textvariable='')
        self.message_entry5.place(x=50, y=575)
        self.message_entry5.insert(0, self.field6)
        label7 = Label(self.BasaM2, text="K2", bg="grey", fg="black")
        self.message_entry6 = Entry(self.BasaM2, textvariable=self.field7)
        self.message_entry6.place(x=50, y=675)
        self.message_entry6.insert(0, self.field7)
        label1.place(x=50, y=50)
        label2.place(x=50, y=150)
        label3.place(x=50, y=250)
        label4.place(x=50, y=350)
        label5.place(x=50, y=450)
        label6.place(x=50, y=550)
        label7.place(x=50, y=650)
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
        NewWindow = Smashins()
    def DellMashins(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        NewWindow = Terminator(self.slct2[0])
    def SelectlMashins(self):
        self.btn4['state'] = 'active'
        sel=self.Tree.focus()
        self.message_entry.delete(0, END)
        self.message_entry1.delete(0, END)
        self.message_entry2.delete(0, END)
        self.message_entry3.delete(0, END)
        self.message_entry4.delete(0, END)
        self.message_entry5.delete(0, END)
        self.message_entry6.delete(0, END)
        self.slct2=self.Tree.item(sel, option='values')
        self.field1=self.slct2[0]
        self.message_entry.insert(0, self.field1)
        self.field2=self.slct2[1]
        self.message_entry1.insert(0, self.field2)
        self.field3=self.slct2[2]
        self.message_entry2.insert(0, self.field3)
        self.field4=self.slct2[3]
        self.message_entry3.insert(0, self.field4)
        self.field5=self.slct2[4]
        self.message_entry4.insert(0, self.field5)
        self.field6=self.slct2[5]
        self.message_entry5.insert(0, self.field6)
        self.field7=self.slct2[6]
        self.message_entry6.insert(0, self.field7)
        print("наименование оборудования "+self.field1)
        print("максимальная энергия"+self.field2)
        print('Емкость батарей конденсаторов ' + self.field3)
        print('Собственная индуктивность ' + self.field4)
        print('Частота тока короткого замыкания '+self.field5)
        print('K1 '+ self.field6)
        print("K2 "+ self.field7)
        print(self.slct2)
    def view_records(self):
        mt = sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cursor.execute(sql6)
        cursor.execute(sql6)
        for row in cursor.execute(sql6): print(row)
        cpt = 0  # Counter representing the ID of your code.
        for row in cursor.execute(sql6):
            # I suppose the first column of your table is ID
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1  # increment the I
    def GoToWork(self):
        self.BasaM2.destroy()
        WindowMashings=EntranceData.EntranceDataFirst()
        EntranceData.EntranceDataFirst.GUI(WindowMashings,self.field1)
    def __init__(self):
        self.GUI()
        self.view_records()
        self.BasaM2.mainloop()