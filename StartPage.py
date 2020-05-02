import tkinter
from tkinter import filedialog as fd  # из библиотеке взяли класс диалог и присвоили индефикатор FD
import SmartCalculation
import Materials
import WindowMashins

class StartPage():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('640x500')  # геометрия окна
        self.window.title("Программа расчета технологического процесса МИОМ")  # название окна
        menu = tkinter.Menu(self.window)  # объект меню
        help = tkinter.Menu(menu)
        BD=tkinter.Menu(menu)
        self.window.config(menu=menu)  # конфигурируем окно с добавлением меню
        menu.add_command(label="Открыть файл")
        menu.add_cascade(label="Базы данных",menu=BD,underline=0)
        BD.add_command(label="База данных материалов", command=self.WindowMashins)
        BD.add_command(label="База данных установок", command=self.Materials)
        menu.add_command(label="О разработчиках", command=self.OnMenuClick)
        menu.add_cascade(label="F1 Help", menu=help, underline=0)  # добавления пункта меню
        help.add_command(label="Что вы хотите найти?")
        help.add_command(label="Обратиться к разработчикам")
        menu.add_command(label="Выход", command=quit)
        menu.add_separator()
        frame_top = tkinter.Frame(self.window, bg='lightgreen', relief=tkinter.RAISED, borderwidth=5)
        frame_top.pack(fill=tkinter.BOTH, expand=tkinter.Y)
        frame_top.pack(side=tkinter.TOP, padx=10, pady=10, ipadx=5, ipady=5)
        frame_bottom = tkinter.Frame(self.window, bg='lightblue', relief=tkinter.RAISED, borderwidth=5)
        frame_bottom.pack(fill=tkinter.BOTH)
        frame_bottom.pack(padx=10, pady=10, ipadx=30, ipady=30)
        btn = tkinter.Button(frame_bottom, text="Новый файл", bg="grey", fg="black",
                             command=self.NewFile)  # описание объекта типа button названия кнопки
        btn.place(x=10, y=11)  # расположение кнопки
        btn2 = tkinter.Button(frame_bottom, text="Открыть файл", bg="grey", fg="black", command=self.OpennFile)
        btn2.place(x=160, y=11)
        btn3 = tkinter.Button(frame_bottom, text="Закрыть окно", bg="red", fg="black", command=quit)
        btn3.place(x=460, y=11)
        label1 = tkinter.Label(frame_top, text="Приветствуем Вас в программе рассчета процессов МИОМ для цилиндрических изделий",
                               bg="white", fg="black")
        label1.pack()
        self.window.mainloop()

    def WindowMashins(self):
        f=WindowMashins.Basad()

    def Materials(self):
        f=Materials.Materials()

    def OnMenuClick(self):
        pass

    def NewFile(self):
        self.window.destroy()
        Window=SmartCalculation.SmartCalculation()

    def OpennFile(self):
        pass
