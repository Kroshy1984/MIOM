import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import sqlite3
from SQL12 import *
from Basa_mashins2 import *
import Basa_mashins2
class Terminator():
    def shot_it(self):
        mt = sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cursor.execute(sql8, (self.shot,))
        mt.commit() #запомнить изменения в базе данных
        cursor.execute(sql6)
        b = Basa_mashins2.Bd()
        Basa_mashins2.Bd.view_records(b)# обновление содержимого таблицы
    def __init__(self,a):
        self.shot=a
        print('удаляем, где ', self.shot)
        self.SBasa = Tk()
        self.SBasa.geometry('600x200')
        self.SBasa.title("Удаление оборудования МИОМ")
        self.SBasa.lift() # команда выталкивает окно на верх
        self.SBasa.attributes('-topmost', True) #окно будет поверх окон
        label1 = Label(self.SBasa, text="Вы действительно хотите удалить это обрудование?  ", bg="grey", fg="black")
        label1.place(x=50, y=50)
        label1 = Label(self.SBasa, text="Внимание! Речь идет о "+ a + ". Это может быть важная запись!" , bg="grey", fg="black")
        label1.place(x=50, y=70)
        btn1 = Button(self.SBasa, text="Закрыть", bg='pink', fg='red', command=self.SBasa.destroy)
        btn1.place(x=30, y=150)
        btn2 = Button(self.SBasa, text="Я все понял. Удалить", bg='green', fg='black', command=self.shot_it)
        btn2.place(x=350, y=150)

        self.SBasa.mainloop()
