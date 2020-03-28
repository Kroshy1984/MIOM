from tkinter import *
import EntranceData
from EntranceData import *
class OperationSwitch():
    def GoToWork(self):
        self.filed2="ничего не выбрано"
        a=self.sel.get()
        if a==1:
            self.field2="Свободная раздача трубчатой заготовки"
        elif a==2:
            self.field2='Формовка переходников'
        elif a==3:
            self.field2='Формовка рифтов'
        elif a==4:
            self.field2 = 'Разделительные операции на трубах'
        elif a==5:
            self.field2 = "Пробивка отверстий в плоских заготовках"
        elif a==6:
            self.field2='Гибка бортов'
        elif a==7:
            self.field2='Формовка плоских заготовок'
        elif a==8:
            self.field2='Калибровка на отжим'
        elif a==9:
            self.field2 ='Калибровка на раздачу'
        self.OperationSwitch.destroy()
        f = EntranceData.EntranceDataFirst(self.field1,self.field2,self.field3,self.field4)
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
            Radiobutton(frame,activebackground="yellow", selectcolor='lightblue', text=operation, indicatoron=0, variable=self.sel, value=val,command=self.GoToWork).pack(anchor=N)
        btn = Button(self.OperationSwitch, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=350)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.GoToWork)
        btn.place(x=300, y=350)
        self.OperationSwitch.mainloop()
    def __init__(self,a,b,c,d):
        self.field1=a
        self.field2=b
        self.field3=c
        self.field4=d
        self.GUI()
    def CloseWindow(self): self.OperationSwitch.destroy()