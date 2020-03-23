import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *
from WindowMashins import *
class EditorMaterials():
    def GUI(self):
        self.SBasa = Tk()
        self.SBasa.geometry('600x900')
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
        btn2 = Button(self.SBasa, text="Запомнить", bg='green', fg='black', command=self.clicked2)
        btn2.place(x=450, y=750)
        self.SBasa.mainloop()
    def __init__(self):
        self.GUI()