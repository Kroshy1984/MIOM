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
        self.Materials.mainloop()