import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *

class Bd():
    def clicked2(self):pass
    def AddMashins(self):
        NewWindow1 = Smashins()
    def DellMashins(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        NewWindow2 = Terminator(self.slct2[0])
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
    def EditeMashins(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.field1 = self.slct2[0]
        self.field2 = self.slct2[1]
        self.field3 = self.slct2[2]
        self.field4 = self.slct2[3]
        self.field5 = self.slct2[4]
        self.field6 = self.slct2[5]
        self.field7 = self.slct2[6]
        NewWindow3 = Editor(self.field1, self.field2, self.field3, self.field4, self.field5, self.field6, self.field7)
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
    def __init__(self):

        self.BasaM2 = Tk()
        self.BasaM2.geometry('1800x1000')
        self.BasaM2.title("Выбор оборудования МИОМ")
        container = Frame(self.BasaM2, height=1750, width=950, bg='lightgreen', relief=RAISED, borderwidth=3)
        container.pack(fill=BOTH, expand=Y)
        container.pack(padx=10, pady=10, ipadx=5, ipady=5)
        frame_bottom = Frame(self.BasaM2, bg='lightblue', relief=RAISED, borderwidth=5)
        frame_bottom.pack(fill=BOTH)
        #frame_bottom.pack(padx=10, pady=10, ipadx=30, ipady=30)
        self.Tree = ttk.Treeview(container, columns=("Name", "Max_change_energi", "Condenser_capasity", "Equipment_induct", "SccF", "K1", "K2"), show='headings')
        self.vsb = Scrollbar(self.Tree, orient="vertical")
        self.vsb.place(x=1300, y=21,height=140)
        self.Tree.configure(yscrollcommand=self.vsb.set, height=140)
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
        self.vsb.config(command = self.Tree.yview)
        self.view_records()
        self.Tree.pack(side='bottom')
        self.slct2 = ['Выбери из таблицы','Выбери из таблицы','Выбери из таблицы','Выбери из таблицы','Выбери из таблицы','Выбери из таблицы','Выбери из таблицы']
        self.field1 = self.slct2[0]
        self.field2 = self.slct2[1]
        self.field3 = self.slct2[2]
        self.field4 = self.slct2[3]
        self.field5 = self.slct2[4]
        self.field6 = self.slct2[5]
        self.field7 = self.slct2[6]

        print(self.slct2)

        self.btn = Button(frame_bottom, text="Добавить оборудования", bg="grey", fg="black",command=self.AddMashins)  # описание объекта типа button названия кнопки
        self.btn.place(x=250, y=800)  # расположение кнопки
        self.btn2 = Button(frame_bottom, text="Удалить оборудование", bg="grey", fg="black",command=self.DellMashins)  # описание объекта типа button названия кнопки
        self.btn2.place(x=470, y=800)  # расположение кнопки
        self.btn3 = Button(frame_bottom, text="Применить", bg="grey", fg="black",command=self.SelectlMashins)  # описание объекта типа button названия кнопки
        self.btn3.place(x=1050, y=800)  # расположение кнопки
        self.btn1 = Button(frame_bottom, text="Отменить", bg='pink', fg='red', command=self.BasaM2.destroy)
        self.btn1.place(x=1250, y=800)
        self.btn5 = Button(frame_bottom, text="Редактировать", bg='grey', fg='black', command=self.EditeMashins)
        self.btn5.place(x=750, y=800)
        self.btn4 = Button(frame_bottom, text="Взять данные в работу", bg='green', fg='black', command=self.clicked2)
        self.btn4.place(x=50, y=800)
        if self.field1 == 'Выбери из таблицы': self.btn4['state']='disabled'
        label1 = Label(frame_bottom, text="Название оборудования", bg="grey", fg="black")
        self.message_entry = Entry(frame_bottom, textvariable='')
        self.message_entry.insert(0,self.field1)
        self.message_entry.place(x=150, y=575)
        label2 = Label(frame_bottom, text="Максимальная энергия заряда", bg="grey", fg="black")
        self.message_entry1 = Entry(frame_bottom, textvariable='')
        self.message_entry1.place(x=450, y=575)
        self.message_entry1.insert(0, self.field2)
        label3 = Label(frame_bottom, text="Емкость батареи кондецаторов", bg="grey", fg="black")
        self.message_entry2 = Entry(frame_bottom, textvariable='')
        self.message_entry2.place(x=750, y=575)
        self.message_entry2.insert(0, self.field3)
        label4 = Label(frame_bottom, text="Собственная индуктивность разрядного контура", bg="grey", fg="black")
        self.message_entry3 = Entry(frame_bottom, textvariable='')
        self.message_entry3.place(x=1050, y=575)
        self.message_entry3.insert(0, self.field4)
        label5 = Label(frame_bottom, text="Частота тока короткого замыкания", bg="grey", fg="black")
        self.message_entry4 = Entry(frame_bottom, textvariable='')
        self.message_entry4.place(x=450, y=675)
        self.message_entry4.insert(0, self.field5)
        label6 = Label(frame_bottom, text="K1", bg="grey", fg="black")
        self.message_entry5 = Entry(frame_bottom, textvariable='')
        self.message_entry5.place(x=750, y=675)
        self.message_entry5.insert(0, self.field6)
        label7 = Label(frame_bottom, text="K2", bg="grey", fg="black")
        self.message_entry6 = Entry(frame_bottom, textvariable=self.field7)
        self.message_entry6.place(x=1050, y=675)
        self.message_entry6.insert(0, self.field7)
        label1.place(x=150, y=550)
        label2.place(x=450, y=550)
        label3.place(x=750, y=550)
        label4.place(x=1050, y=550)
        label5.place(x=450, y=650)
        label6.place(x=750, y=650)
        label7.place(x=1050, y=650)
        self.BasaM2.mainloop()