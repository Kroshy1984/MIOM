from tkinter import *
class OperationSwitch():
    def __init__(self):
        self.OperationSwitch = Tk()
        self.OperationSwitch.geometry('500x300')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        lbl = Label(self.OperationSwitch, text="Выберите необходимую операцию:", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        selected = IntVar()
        rad1 = Radiobutton(self.OperationSwitch, text='Свободная раздача трубчатой заготовки', value=1, variable=selected)
        rad2 = Radiobutton(self.OperationSwitch, text='Формовка переходников', value=2, variable=selected)
        rad3 = Radiobutton(self.OperationSwitch, text='Формовка рифтов', value=3, variable=selected)
        rad4 = Radiobutton(self.OperationSwitch, text='Разделительные операции на трубах', value=4, variable=selected)
        rad5 = Radiobutton(self.OperationSwitch, text='Пробивка отверстий в плоских заготовках', value=5, variable=selected)
        rad6 = Radiobutton(self.OperationSwitch, text='Гибка бортов', value=6, variable=selected)
        rad7 = Radiobutton(self.OperationSwitch, text='Формовка плоских заготовок', value=7, variable=selected)
        rad8 = Radiobutton(self.OperationSwitch, text='Калибровка на отжим', value=8, variable=selected)
        rad9 = Radiobutton(self.OperationSwitch, text='Калибровка на раздачу', value=9, variable=selected)
        rad1.place(x=10, y=40)
        rad2.place(x=10, y=60)
        rad3.place(x=10, y=80)
        rad4.place(x=10, y=100)
        rad5.place(x=10, y=120)
        rad6.place(x=10, y=140)
        rad7.place(x=10, y=160)
        rad8.place(x=10, y=180)
        rad9.place(x=10, y=200)
        btn = Button(self.OperationSwitch , text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=250)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=300, y=250)
        self.OperationSwitch.mainloop()

    def Insertdata(self): pass

    def CloseWindow(self): self.OperationSwitch.destroy()