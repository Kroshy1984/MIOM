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
        self.OperationSwitch.geometry('500x500')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        lbl = Label(self.OperationSwitch, text="Выберите необходимую операцию:", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        self.selected = IntVar()
        self.selected.set(3)
        operations=[('Свободная раздача трубчатой заготовки',1),('Формовка переходников',2),('Формовка рифтов',3),('Разделительные операции на трубах',4),('Пробивка отверстий в плоских заготовках',5),('Гибка бортов',6),('Формовка плоских заготовок',7),('Калибровка на отжим',8),('Калибровка на раздачу',9)]
        for operation,val in operations:
            Radiobutton(self.OperationSwitch, text=operation, variable=self.selected, value=val).place(x=10, y=val*35)
        btn = Button(self.OperationSwitch, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=350)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.GoToWork)
        btn.place(x=300, y=350)
        self.OperationSwitch.mainloop()
    def __init__(self):
        self.GUI()
        print(self.selected.get())


    def CloseWindow(self): self.OperationSwitch.destroy()