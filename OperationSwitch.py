from tkinter import *
class OperationSwitch():
    def GoToWork(self):
        Ttext="ничего не выбрано"
        a=self.sel.get()
        if a==1:
            Ttext="Свободная раздача трубчатой заготовки"
            print(self.sel.get())
        elif a==2:
            Ttext='Формовка переходников'
        elif a==3:
            Ttext='Формовка рифтов'
        elif a==4:
            Ttext = 'Разделительные операции на трубах'
        elif a==5:
            Ttext = "Пробивка отверстий в плоских заготовках"
        elif a==6:
            Ttext='Гибка бортов'
        elif a==7:
            Ttext='Формовка плоских заготовок'
        elif a==8:
            Ttext='Калибровка на отжим'
        elif a==9:
            Ttext ='Калибровка на раздачу'
        print(Ttext)
        print(a)

    def GUI (self):
        self.OperationSwitch = Tk()
        self.OperationSwitch.geometry('500x500')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        lbl = Label(self.OperationSwitch, text="Выберите необходимую операцию:", font=("Arial Bold", 20))
        lbl.pack(anchor=N)
        frame = Frame(self.OperationSwitch, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.sel = IntVar()
        operations=[('Свободная раздача трубчатой заготовки',1),('Формовка переходников',2),('Формовка рифтов',3),('Разделительные операции на трубах',4),('Пробивка отверстий в плоских заготовках',5),('Гибка бортов',6),('Формовка плоских заготовок',7),('Калибровка на отжим',8),('Калибровка на раздачу',9)]
        for operation,val in operations:
            print(val)
            Radiobutton(frame,activebackground="yellow", selectcolor='lightblue', text=operation, indicatoron=0, variable=self.sel, value=val,command=self.GoToWork).pack(anchor=N)
        btn = Button(self.OperationSwitch, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=350)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.GoToWork)
        btn.place(x=300, y=350)
        self.OperationSwitch.mainloop()
    def __init__(self):
        self.GUI()
        print(self.sel.get())

    def CloseWindow(self): self.OperationSwitch.destroy()