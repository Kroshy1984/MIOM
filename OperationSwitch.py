from tkinter import *
class OperationSwitch():
    def __init__(self):
        self.OperationSwitch = Tk()
        self.OperationSwitch.geometry('500x200')  # геометрия окна
        self.OperationSwitch.title("Выбор операции")  # название окна
        lbl = Label(self.OperationSwitch, text="Выберите необходимую операцию:", font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        selected = IntVar()
        rad1 = Radiobutton(self.OperationSwitch, text='Формовка цилиндра, конуса, сферы', value=1, variable=selected)
        rad2 = Radiobutton(self.OperationSwitch, text='Формовка рифтов', value=2, variable=selected)
        rad3 = Radiobutton(self.OperationSwitch, text='Гибка бортов', value=3, variable=selected)
        rad4 = Radiobutton(self.OperationSwitch, text='Формовка плоских заготовок', value=4, variable=selected)
        rad1.place(x=10, y=40)
        rad2.place(x=10, y=60)
        rad3.place(x=10, y=80)
        rad4.place(x=10, y=100)
        btn = Button(self.OperationSwitch , text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=150)
        btn = Button(self.OperationSwitch, text="Внести данные", bg="green", fg="black", command=self.Insertdata)
        btn.place(x=300, y=150)
        self.OperationSwitch.mainloop()

    def Insertdata(self): pass

    def CloseWindow(self): self.OperationSwitch.destroy()