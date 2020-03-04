from tkinter import *
class OperationSwitch():
    def GoToWork(self):
        Ttext="ничего не выбрано"
        if self.selected.get()==1:
            Ttext="Свободная раздача трубчатой заготовки"
            print(self.selected.get())
        elif self.selected.get()==2:
            Ttext='Формовка переходников'
        elif self.selected.get()==3:
            Ttext='Формовка рифтов'
        elif self.selected.get()==4:
            Ttext = 'Разделительные операции на трубах'
        elif self.selected.get()==5:
            Ttext = "Пробивка отверстий в плоских заготовках"
        elif self.selected.get()==6:
            Ttext='Гибка бортов'
        elif self.selected.get()==7:
            Ttext='Формовка плоских заготовок'
        elif self.selected.get()==8:
            Ttext='Калибровка на отжим'
        elif self.selected.get()==9:
            Ttext ='Калибровка на раздачу'
        print(Ttext)
        print(self.selected.get())

    def GUI (self):
        self.OperationSwitch = Tk()
        self.OperationSwitch.geometry('500x300')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        lbl = Label(self.OperationSwitch, text="Выберите необходимую операцию:", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        self.selected = IntVar()
        self.selected.set(10)
        rad1 = Radiobutton(self.OperationSwitch, text='Свободная раздача трубчатой заготовки', variable=self.selected, value=1,command=self.GoToWork)
        rad2 = Radiobutton(self.OperationSwitch, text='Формовка переходников', variable=self.selected,value=2, command=self.GoToWork)
        rad3 = Radiobutton(self.OperationSwitch, text='Формовка рифтов',  variable=self.selected, value=3, command=self.GoToWork)
        rad4 = Radiobutton(self.OperationSwitch, text='Разделительные операции на трубах', variable=self.selected,value=4, command=self.GoToWork)
        rad5 = Radiobutton(self.OperationSwitch, text='Пробивка отверстий в плоских заготовках', variable=self.selected,value=5, command =self.GoToWork)
        rad6 = Radiobutton(self.OperationSwitch, text='Гибка бортов', variable=self.selected, value=6, command = self.GoToWork)
        rad7 = Radiobutton(self.OperationSwitch, text='Формовка плоских заготовок', variable=self.selected,value=7, command=self.GoToWork)
        rad8 = Radiobutton(self.OperationSwitch, text='Калибровка на отжим', variable=self.selected,value=8, command=self.GoToWork)
        rad9 = Radiobutton(self.OperationSwitch, text='Калибровка на раздачу', variable=self.selected,value=9, command=self.GoToWork)
        rad1.place(x=10, y=40)
        rad2.place(x=10, y=60)
        rad3.place(x=10, y=80)
        rad4.place(x=10, y=100)
        rad5.place(x=10, y=120)
        rad6.place(x=10, y=140)
        rad7.place(x=10, y=160)
        rad8.place(x=10, y=180)
        rad9.place(x=10, y=200)
        btn = Button(self.OperationSwitch, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=250)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=300, y=250)
    def __init__(self):
        self.GUI()
        self.OperationSwitch.mainloop()

    def Insertdata(self): pass

    def CloseWindow(self): self.OperationSwitch.destroy()