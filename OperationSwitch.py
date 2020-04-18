from tkinter import *
import EntranceData
from EntranceData import *
class OperationSwitch():
    def GoToWork(self):
        self.filed2="ничего не выбрано"
        a=self.sel.get()
        if a==1:
            self.field2="Формовка цилиндра"
        elif a==2:
            self.field2='Формовка конуса'
        elif a==3:
            self.field2='Формовка сферы'
        elif a==4:
            self.field2 = 'Формовка рифта'
        elif a==5:
            self.field2 = "Отбортовка наружного контура заготовки"
        elif a==6:
            self.field2='Формовка тороидального рифта'
        elif a==7:
            self.field2='Формовка сферической пуклевки'
        elif a==8:
            self.field2='Формовка конусной пуклевки'
        elif a==9:
            self.field2 ='Формовка плоской пуклевки'
        elif a==10:
            self.field2 ='Гибка прямолинейного борта'
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
        operations=[('Формовка цилиндра',1),
                    ('Формовка конуса',2),
                    ('Формовка сферы',3),
                    ('Формовка рифта',4),
                    ('Отбортовка наружного контура заготовки',5),
                    ('Формовка тороидального рифта',6),
                    ('Формовка сферической пуклевки',7),
                    ('Формовка конусной пуклевки',8),
                    ('Формовка плоской пуклевки',9),
                    ('Гибка прямолинейного борта',10)]
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