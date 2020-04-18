import tkinter as tk
import tkinter
from tkinter import ttk
import sqlite3
from SQL12 import *
from WindowMashins import *


class EditorMaterials():
    def GUI(self):
        self.SBasa = tkinter.Tk()
        self.SBasa.geometry('600x900')
        self.SBasa.title("Добавить Материал")
        self.SBasa.lift()
        self.SBasa.attributes('-topmost', True)
        label1 = tkinter.Label(self.SBasa, text="Металл", bg="grey", fg="black")
        self.message_entry = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry.place(x=400, y=50)
        label2 = tkinter.Label(self.SBasa, text="Предел прочности", bg="grey", fg="black")
        self.message_entry1 = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry1.place(x=400, y=150)
        label3 = tkinter.Label(self.SBasa, text="Предел текучести", bg="grey", fg="black")
        self.message_entry2 = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry2.place(x=400, y=250)
        label4 = tkinter.Label(self.SBasa, text="Плотность", bg="grey", fg="black")
        self.message_entry3 = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry3.place(x=400, y=350)
        label5 = tkinter.Label(self.SBasa, text="М_м", bg="grey", fg="black")
        self.message_entry4 = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry4.place(x=400, y=450)
        label6 = tkinter.Label(self.SBasa, text="В", bg="grey", fg="black")
        self.message_entry5 = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry5.place(x=400, y=550)
        label7 = tkinter.Label(self.SBasa, text="Удельное сопротивление", bg="grey", fg="black")
        self.message_entry6 = tkinter.Entry(self.SBasa, textvariable="")
        self.message_entry6.place(x=400, y=650)
        label1.place(x=10, y=50)
        label2.place(x=10, y=150)
        label3.place(x=10, y=250)
        label4.place(x=10, y=350)
        label5.place(x=10, y=450)
        label6.place(x=10, y=550)
        label7.place(x=10, y=650)
        btn1 = tkinter.Button(self.SBasa, text="Закрыть", bg='pink', fg='red', command=self.SBasa.destroy)
        btn1.place(x=30, y=750)
        btn2 = tkinter.Button(self.SBasa, text="Запомнить", bg='green', fg='black', command=self.clicked2)
        btn2.place(x=450, y=750)
        self.SBasa.mainloop()

    def __init__(self):
        self.GUI()
