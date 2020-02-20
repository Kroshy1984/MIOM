from tkinter import * #вызов библиотеки ткинтер
from tkinter import filedialog as fd #из библиотеке взяли класс диалог и присвоили индефикатор FD
from SelectWay import SelectWay

class StartPage():
    def __init__(self):
        self.window = Tk()
        self.window.geometry('640x500')  # геометрия окна
        self.window.title("Программа расчета технологического процесса МИОМ")  # название окна
        menu = Menu(self.window)  # объект меню
        help = Menu(menu)
        self.window.config(menu=menu)  # конфигурируем окно с добавлением меню
        menu.add_cascade(label="Помощь", menu=help, underline=0)  # добавления пункта меню
        help.add_command(label="Что вы хотите найти?")
        help.add_command(label="Обратиться к разработчикам")
        menu.add_command(label="Открыть файл")
        menu.add_command(label="О разработчиках", command=self.OnMenuClick)
        menu.add_command(label="Выход", command=quit)
        menu.add_separator()
        frame_top = Frame(self.window, bg='lightgreen', relief=RAISED, borderwidth=5)
        frame_top.pack(fill=BOTH, expand=Y)
        frame_top.pack(side=TOP, padx=10, pady=10, ipadx=5, ipady=5)
        frame_bottom = Frame(self.window, bg='lightblue', relief=RAISED, borderwidth=5)
        frame_bottom.pack(fill=BOTH)
        frame_bottom.pack( padx=10, pady=10, ipadx=30, ipady=30)
        btn = Button(frame_bottom, text="Новый файл", bg="grey", fg="black",
                     command=self.NewFile)  # описание объекта типа button названия кнопки
        btn.place(x=10, y=11)  # расположение кнопки
        btn2 = Button(frame_bottom, text="Открыть файл", bg="grey", fg="black", command=self.OpennFile)
        btn2.place(x=160,y=11)
        btn3 = Button(frame_bottom, text="Закрыть окно", bg="red", fg="black", command=quit)
        btn3.place(x=460, y=11)
        label1 = Label(frame_top, text="Приветствуем Вас в программе рассчета процессов МИОМ", bg="white", fg="black")
        label1.pack()
        self.window.mainloop()
    def OnMenuClick(self):
        pass
    def NewFile(self):
        self.window.destroy()
        SelectWaywindow = SelectWay()
    def OpennFile(self):
        pass

