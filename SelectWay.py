from tkinter import * #вызов библиотеки ткинтер
import StartPage
from EntranceData import EntranceDataFirst, EntranceDataSecond
class SelectWay():
    def __init__(self):
        self.SelectWayWindow = Tk()
        self.SelectWayWindow.geometry('640x500')  # геометрия окна
        self.SelectWayWindow.title("Выбор пути расчета  расчета технологического процесса МИОМ")  # название окна
        frame_top = Frame(self.SelectWayWindow, bg='green', relief=RAISED, borderwidth=5)
        frame_top.pack(fill=BOTH, expand=Y)
        frame_top.pack(side=TOP, padx=10, pady=10, ipadx=5, ipady=5)
        frame_bottom = Frame(self.SelectWayWindow, bg='lightblue', relief=RAISED, borderwidth=5)
        frame_bottom.pack(fill=BOTH)
        frame_bottom.pack(padx=10, pady=10, ipadx=30, ipady=30)
        btn = Button(frame_bottom, text="Второй путь", bg="grey", fg="black", command = self.SecondWay)  # описание объекта типа button названия кнопки
        btn.place(x=160, y=11)  # расположение кнопки
        btn2 = Button(frame_bottom, text="Первый путь", bg="grey", fg="black", command=self.FirstWay)
        btn2.place(x=10, y=11)
        btn3 = Button(frame_bottom, text="Назад", bg="red", fg="black", command=self.Exit)
        btn3.place(x=460, y=11)
        label1 = Label(frame_top, text="Выберете путь для рассчета процессов МИОМ", bg="white", fg="black")
        label1.pack()
        self.SelectWayWindow.mainloop()
    def FirstWay(self):
        a=''
        b=''
        c=''
        self.SelectWayWindow.destroy()
        WindowMashings=EntranceDataFirst(a,b, c)
    def SecondWay(self):
        self.SelectWayWindow.destroy()
        WindowMashings=EntranceDataSecond()
    def Exit(self):
        self.SelectWayWindow.destroy()
        self.window2= StartPage.StartPage()
