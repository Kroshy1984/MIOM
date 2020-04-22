import tkinter
import StartPage
import EntranceData
import SmartCalculation
from InductorParams import InductorParams


class SelectWay():
    def __init__(self):
        self.SelectWayWindow = tkinter.Tk()
        self.SelectWayWindow.geometry('640x500')  # геометрия окна
        self.SelectWayWindow.title("Выбор пути расчета  расчета технологического процесса МИОМ")  # название окна
        frame_top = tkinter.Frame(self.SelectWayWindow, bg='green', relief=tkinter.RAISED, borderwidth=5)
        frame_top.pack(fill=tkinter.BOTH, expand=tkinter.Y)
        frame_top.pack(side=tkinter.TOP, padx=10, pady=10, ipadx=5, ipady=5)
        frame_bottom = tkinter.Frame(self.SelectWayWindow, bg='lightblue', relief=tkinter.RAISED, borderwidth=5)
        frame_bottom.pack(fill=tkinter.BOTH)
        frame_bottom.pack(padx=10, pady=10, ipadx=30, ipady=30)
        btn = tkinter.Button(frame_bottom, text="Второй путь", bg="grey", fg="black",
                             command=self.SecondWay)  # описание объекта типа button названия кнопки
        btn.place(x=160, y=11)  # расположение кнопки
        btn2 = tkinter.Button(frame_bottom, text="Первый путь", bg="grey", fg="black", command=self.FirstWay)
        btn2.place(x=10, y=11)
        btn3 = tkinter.Button(frame_bottom, text="Назад", bg="red", fg="black", command=self.Exit)
        btn3.place(x=500, y=11)
        btn1 = tkinter.Button(frame_bottom, text="Простой расчет", bg="lightblue", fg="black", command=self.SmartCalculation)
        btn1.place(x=300, y=11)
        label1 = tkinter.Label(frame_top, text="Выберете путь для рассчета процессов МИОМ", bg="white", fg="black")
        label1.pack()
        self.SelectWayWindow.mainloop()

    def SmartCalculation(self):
        self.SelectWayWindow.destroy()
        Window=SmartCalculation.SmartCalculation()

    def FirstWay(self):
        a = ''
        b = ''
        c = ''
        d = ''
        self.SelectWayWindow.destroy()
        WindowMashings = EntranceData.EntranceDataFirst(a, b, c, d)

    def SecondWay(self):
        self.SelectWayWindow.destroy()
        WindowMashings = EntranceData.EntranceDataSecond()

    def Exit(self):
        self.SelectWayWindow.destroy()
        self.window2 = StartPage.StartPage()
