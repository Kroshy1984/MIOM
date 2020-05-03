import tkinter
import Computing
import sqlite3
from tkinter.ttk import Treeview
import WindowMashins
import Materials


class SmartCalculation():
    def __init__(self):
        self.GUI()
        self.Smart.mainloop()

    def GUI(self):
        self.Smart = tkinter.Tk()
        self.Smart.geometry('1700x1000')  # геометрия окна
        self.Smart.title("Простой расчет формовки и параметров индуктора")  # название окна
        menu = tkinter.Menu(self.Smart)  # объект меню
        help = tkinter.Menu(menu)
        BD = tkinter.Menu(menu)
        self.Smart.config(menu=menu)  # конфигурируем окно с добавлением меню
        menu.add_command(label="Открыть файл")
        menu.add_cascade(label="Базы данных", menu=BD, underline=0)
        BD.add_command(label="База данных материалов", command=self.WindowMashins)
        BD.add_command(label="База данных установок", command=self.Materials)
        menu.add_command(label="О разработчиках", command=self.OnMenuClick)
        menu.add_cascade(label="F1 Help", menu=help, underline=0)  # добавления пункта меню
        help.add_command(label="Что вы хотите найти?")
        help.add_command(label="Обратиться к разработчикам")
        menu.add_command(label="Выход", command=quit)
        label=tkinter.Label(self.Smart, text="Введите наименование детали", bg="lightgrey", fg="red")
        label.place(x=15,y=10)
        label2 = tkinter.Label(self.Smart, text="Введите диаметр наружной трубы, м", bg="lightgrey", fg="red")
        label2.place(x=10, y=60)
        label3 = tkinter.Label(self.Smart, text="Введите толщину стенки трубы, м", bg="lightgrey", fg="red")
        label3.place(x=10, y=110)
        label4 = tkinter.Label(self.Smart, text="Введите длину деформируемой зоны, м", bg="lightgrey", fg="red")
        label4.place(x=10, y=160)
        self.LabelG = ["Выберете операцию","Введите радиус цилиндра, м","Максимальный радиус конуса, м","Радиус сферы, м", "Радиус рифта"]
        self.label5 = tkinter.Label(self.Smart, text=self.LabelG[0], bg="lightgrey", fg="red")
        self.label5.place(x=10, y=210)
        label9 = tkinter.Label(self.Smart, text="КПД, ед.",
                               bg="lightgrey", fg="red")
        label9.place(x=10, y=260)
        label10 = tkinter.Label(self.Smart, text="Операция",
                               bg="lightgrey", fg="green")
        label10.place(x=10, y=310)
        label11 = tkinter.Label(self.Smart, text="Поиск материала для заготовки в базе",
                                bg="lightgrey", fg="black")
        label11.place(x=600, y=60)
        label16 = tkinter.Label(self.Smart, text="Длина индуктора, м",
                                bg="lightgrey", fg="red")
        label16.place(x=10, y=360)
        label17 = tkinter.Label(self.Smart, text="Высота индуктора, м",
                                bg="lightgrey", fg="red")
        label17.place(x=10, y=410)
        label19 = tkinter.Label(self.Smart, text="Поиск материала для индуктора в базе",
                                bg="lightgrey", fg="black")
        label19.place(x=600, y=110)
        label20 = tkinter.Label(self.Smart, text="Поиск установки в базе",
                                bg="lightgrey", fg="black")
        label20.place(x=600, y=160)
        label21 = tkinter.Label(self.Smart, text="Введите количество витков, шт.",
                                bg="lightgrey", fg="red")
        label21.place(x=10, y=460)
        label23 = tkinter.Label(self.Smart, text="R0",
                                bg="lightgrey", fg="red")
        label23.place(x=850, y=210)
        label24 = tkinter.Label(self.Smart, text="Толщина изоляции витка, м",
                                bg="lightgrey", fg="red")
        label24.place(x=690, y=260)
        label25 = tkinter.Label(self.Smart, text="Толщина основной изоляции индуктора, м",
                                bg="lightgrey", fg="red")
        label25.place(x=590, y=310)
        label26 = tkinter.Label(self.Smart, text="Толщина воздушного зазора, м",
                                bg="lightgrey", fg="red")
        label26.place(x=620, y=360)
        label27 = tkinter.Label(self.Smart, text="Удельное сопротивление шины, Ом х Е-07",
                                bg="lightgrey", fg="red")
        label27.place(x=580, y=410)
        label28 = tkinter.Label(self.Smart, text="Индуктивность токоподводов индуктора Гн х E-08",
                                bg="lightgrey", fg="red")
        label28.place(x=530, y=460)
        label29 = tkinter.Label(self.Smart, text="А_ТП",
                                bg="lightgrey", fg="red")
        label29.place(x=1350, y=60)
        label30 = tkinter.Label(self.Smart, text="B_ТП",
                                bg="lightgrey", fg="red")
        label30.place(x=1350, y=110)
        label31 = tkinter.Label(self.Smart, text="HB_ТП",
                                bg="lightgrey", fg="red")
        label31.place(x=1350, y=160)
        label32 = tkinter.Label(self.Smart, text="LB_ТП",
                                bg="lightgrey", fg="red")
        label32.place(x=1350, y=210)
        label33 = tkinter.Label(self.Smart, text="Кп_3%",
                                bg="lightgrey", fg="red")
        label33.place(x=1350, y=260)
        label33 = tkinter.Label(self.Smart, text="Kappa",
                                bg="lightgrey", fg="red")
        label33.place(x=1350, y=310)
        self.message_entry=tkinter.Entry(self.Smart, textvariable='')
        self.message_entry.place(x=300, y=10)
        self.message_entry1 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry1.place(x=300, y=60)
        self.message_entry2 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry2.place(x=300, y=110)
        self.message_entry3 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry3.place(x=300, y=160)
        self.message_entry8 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry8.place(x=300, y=260)
        self.option= tkinter.StringVar(self.Smart)
        self.option.set("Выбери операцию тут")
        self.message_entry9=tkinter.OptionMenu(self.Smart,self.option,"a1-раздача цилиндра","a2 - раздача конуса","a3 - раздача сферы","a4 - раздача рифта","b1 - обжим цилиндра","b2 - обжим конуса","b3 - обжим сферы","b4 - обжим рифта")# выбор операции
        self.message_entry9.place(x=300, y=310)
        btn5=tkinter.Button(self.Smart, text="Выбрать", bg="orange", fg="black", command=self.ChangeLabel)
        btn5.place(x=200,y=310)
        self.message_entry10 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry10.place(x=900, y=60) #оиск материала заготовки в базе
        self.message_entry15 = tkinter.Entry(self.Smart, textvariable='') #длина индуктора
        self.message_entry15.place(x=300, y=360)
        self.message_entry16 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry16.place(x=300, y=410)
        self.message_entry18 = tkinter.Entry(self.Smart, textvariable='')#материал индукора
        self.message_entry18.place(x=900,y=110)#поиск материала индуктора в базе
        self.message_entry19 = tkinter.Entry(self.Smart, textvariable='')# установка
        self.message_entry19.place(x=900, y=160)
        self.message_entry21 = tkinter.Entry(self.Smart, textvariable='')  # количество витков
        self.message_entry21.place(x=300, y=460)
        self.message_entry23 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry23.place(x=900, y=210) # R0
        self.message_entry24 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry24.place(x=900, y=260)  # Толщина изоляции витка ZS
        self.message_entry25 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry24.insert(0, "0.00065")
        self.ZS=self.message_entry24.get()
        self.message_entry25.place(x=900, y=310)  # Толщина основной изоляции индуктора ZB
        self.message_entry25.insert(0, "0.001")
        self.ZB = self.message_entry25.get()
        self.message_entry26 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry26.place(x=900, y=360)  # Толщина воздушного зазора ZA
        self.message_entry26.insert(0, "0.00025")
        self.ZA=self.message_entry26.get()
        self.message_entry27 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry27.place(x=900, y=410)  # YEMC
        self.message_entry27.insert(0, "1.78")
        self.YEMC=self.message_entry27.get()
        self.YEMC=float(self.YEMC)*pow(10,-8)
        self.message_entry28 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry28.place(x=900, y=460)  # Толщина воздушного зазора ZA
        self.message_entry28.insert(0, "0.7")#LTC
        self.LTC=self.message_entry28.get()
        self.LTC=float(self.LTC)*pow(10,-7)
        self.message_entry29 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry29.place(x=1400, y=60)  # A_ТП
        self.message_entry30 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry30.place(x=1400, y=110)  # B_ТП
        self.message_entry31 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry31.place(x=1400, y=160)  # B_ТП
        self.message_entry32 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry32.place(x=1400, y=210)  # B_ТП
        self.message_entry33 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry33.place(x=1400, y=260)  # B_ТП
        self.message_entry34 = tkinter.Entry(self.Smart, textvariable='')  #
        self.message_entry34.place(x=1400, y=310)  # B_ТП
        btn = tkinter.Button(self.Smart, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=550)
        btn1 = tkinter.Button(self.Smart, text="Рассчитать индуктор", bg="green", fg="black", command=self.CalculateIt)
        btn1.place(x=280, y=550)
        btn5 = tkinter.Button(self.Smart, text="Открыть базу установок", bg="lightgreen", fg="black",
                              command=self.WindowMashines)
        btn5.place(x=1100, y=160)
        btn6 = tkinter.Button(self.Smart, text="Открыть базу материалов", bg="lightgreen", fg="black",
                              command=self.SearchMaterials)
        btn6.place(x=1100, y=110)
        btn7 = tkinter.Button(self.Smart, text="Открыть базу материалов", bg="lightgreen", fg="black",
                              command=self.SearchMaterials2)
        btn7.place(x=1100, y=60)
        btn8=tkinter.Button(self.Smart, text="Рассчитать EPS",bg="yellow", fg="black", command=self.CulculateEPS)
        btn8.place(x=600, y=550)
        btn9 = tkinter.Button(self.Smart, text="Рассчитать формовку", bg="brown", fg="black", command=self.CalculateForm)
        btn9.place(x=280, y=600)
        self.text=tkinter.Text(self.Smart, height=35)
        self.text.place(x=1100,y=360)

    def CulculateEPS(self):
        self.DOT = self.message_entry1.get()
        self.ST = self.message_entry2.get()
        self.LBT = self.message_entry3.get()
        self.RC = self.message_entry4.get()
        self.BCM = float(self.BCM1) * pow(10, 7)
        self.KPD = self.message_entry8.get()
        f = Computing.Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                           float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        EPS=Computing.Form.EPS(f,float(self.RC))
        self.message_entry22 = tkinter.Entry(self.Smart, textvariable=str(EPS))  # EPS
        self.message_entry22.place(x=600, y=580)
        self.message_entry22.delete(0, 10)
        self.message_entry22.insert(0, EPS)

    def OnMenuClick(self):
        pass

    def WindowMashins(self):
        f=WindowMashins.Basad()

    def Materials(self):
        f=Materials.Materials()

    def SearchMaterials(self):
        self.Materials = tkinter.Toplevel(self.Smart)
        self.Materials.geometry('1200x700+600+200')
        self.Materials.title("Выбор материала ")
        self.Tree2 = Treeview(self.Materials, columns=(
            "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B",
            "Specific_electric_resistance", "The_coefficient_of_dynamic", 'Еhe_dynamic_modulus_hardening'), height=30,
                                 show='headings')
        self.Tree2.column("Name_of_the_metalls", width=60, anchor=tkinter.CENTER)
        self.Tree2.column("Tensile_strength", width=70, anchor=tkinter.CENTER)
        self.Tree2.column("Yield_strength", width=50, anchor=tkinter.CENTER)
        self.Tree2.column("Material_density", width=50, anchor=tkinter.CENTER)
        self.Tree2.column("M_M", width=50, anchor=tkinter.CENTER)
        self.Tree2.column("B", width=50, anchor=tkinter.CENTER)
        self.Tree2.column("Specific_electric_resistance", width=50, anchor=tkinter.CENTER)
        self.Tree2.column("The_coefficient_of_dynamic", width=50, anchor=tkinter.CENTER)
        self.Tree2.column("Еhe_dynamic_modulus_hardening", width=50, anchor=tkinter.CENTER)
        self.Tree2['show'] = "headings"
        self.Tree2.heading("Name_of_the_metalls", text="Металл")
        self.Tree2.heading("Tensile_strength", text="PPM")
        self.Tree2.heading("Yield_strength", text="PYD")
        self.Tree2.heading("Material_density", text="PLM")
        self.Tree2.heading("M_M", text="M_M")
        self.Tree2.heading("B", text="B")
        self.Tree2.heading("Specific_electric_resistance", text="YEMP")
        self.Tree2.heading("The_coefficient_of_dynamic", text="KDM")
        self.Tree2.heading("Еhe_dynamic_modulus_hardening", text="MDM")
        self.Tree2.place(x=50, y=10)
        label1 = tkinter.Label(self.Materials, text="PPM-предел прочность материала", bg="lightgrey", fg="black")
        label1.place(x=550, y=30)
        label2 = tkinter.Label(self.Materials, text="PYD-предел упругости материала", bg="lightgrey",
                               fg="black")
        label2.place(x=550, y=50)
        label3 = tkinter.Label(self.Materials, text="PLM-плотность материала", bg="lightgrey", fg="black")
        label3.place(x=550, y=70)
        label4 = tkinter.Label(self.Materials, text="M_M и B-вкоэффициенты степенной аппроксимации кривой упрочнения материала", bg="lightgrey", fg="black")
        label4.place(x=550, y=90)
        label6 = tkinter.Label(self.Materials, text="YEMP-удельное электрическое сопротивление материала", bg="lightgrey", fg="black")
        label6.place(x=550, y=110)
        label7 = tkinter.Label(self.Materials, text="MDM-коэффициент динамичности материала", bg="lightgrey", fg="black")
        label7.place(x=550, y=130)
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cpt=0
        for row in cursor.execute("select* from material"):
            self.Tree2.insert('', 'end', text=str(cpt), values=row)
            cpt += 1
        self.btn = tkinter.Button(self.Materials, text="Взять данные в работу", bg="green", fg="black", command=self.GoToWork_in)  # описание объекта типа button названия кнопки
        self.btn.place(x=550, y=150)

    def SearchMaterials2(self):
        self.Materials2 = tkinter.Toplevel(self.Smart)
        self.Materials2.geometry('1200x700+600+200')
        self.Materials2.title("Выбор материала заготовки")
        self.Tree3 = Treeview(self.Materials2, columns=(
            "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B",
            "Specific_electric_resistance", "The_coefficient_of_dynamic", 'Еhe_dynamic_modulus_hardening'), height=30,
                                 show='headings')
        self.Tree3.column("Name_of_the_metalls", width=60, anchor=tkinter.CENTER)
        self.Tree3.column("Tensile_strength", width=70, anchor=tkinter.CENTER)
        self.Tree3.column("Yield_strength", width=50, anchor=tkinter.CENTER)
        self.Tree3.column("Material_density", width=50, anchor=tkinter.CENTER)
        self.Tree3.column("M_M", width=50, anchor=tkinter.CENTER)
        self.Tree3.column("B", width=50, anchor=tkinter.CENTER)
        self.Tree3.column("Specific_electric_resistance", width=50, anchor=tkinter.CENTER)
        self.Tree3.column("The_coefficient_of_dynamic", width=50, anchor=tkinter.CENTER)
        self.Tree3.column("Еhe_dynamic_modulus_hardening", width=50, anchor=tkinter.CENTER)
        self.Tree3['show'] = "headings"
        self.Tree3.heading("Name_of_the_metalls", text="Металл")
        self.Tree3.heading("Tensile_strength", text="PPM")
        self.Tree3.heading("Yield_strength", text="PYD")
        self.Tree3.heading("Material_density", text="PLM")
        self.Tree3.heading("M_M", text="M_M")
        self.Tree3.heading("B", text="B")
        self.Tree3.heading("Specific_electric_resistance", text="YEMP")
        self.Tree3.heading("The_coefficient_of_dynamic", text="KDM")
        self.Tree3.heading("Еhe_dynamic_modulus_hardening", text="MDM")
        self.Tree3.place(x=50, y=10)
        label1 = tkinter.Label(self.Materials2, text="PPM-предел прочность материала", bg="lightgrey", fg="black")
        label1.place(x=550, y=30)
        label2 = tkinter.Label(self.Materials2, text="PYD-предел упругости материала", bg="lightgrey",
                               fg="black")
        label2.place(x=550, y=50)
        label3 = tkinter.Label(self.Materials2, text="PLM-плотность материала", bg="lightgrey", fg="black")
        label3.place(x=550, y=70)
        label4 = tkinter.Label(self.Materials2, text="M_M и B-вкоэффициенты степенной аппроксимации кривой упрочнения материала", bg="lightgrey", fg="black")
        label4.place(x=550, y=90)
        label6 = tkinter.Label(self.Materials2, text="YEMP-удельное электрическое сопротивление материала", bg="lightgrey", fg="black")
        label6.place(x=550, y=110)
        label7 = tkinter.Label(self.Materials2, text="MDM-коэффициент динамичности материала", bg="lightgrey", fg="black")
        label7.place(x=550, y=130)
        mt = sqlite3.connect("Metalls.db")
        cursor = mt.cursor()
        cpt=0
        for row in cursor.execute("select* from material"):
            self.Tree3.insert('', 'end', text=str(cpt), values=row)
            cpt += 1
        self.btn = tkinter.Button(self.Materials2, text="Взять данные в работу", bg="green", fg="black", command=self.GoToWork_z)  # описание объекта типа button названия кнопки
        self.btn.place(x=550, y=150)

    def GoToWork_z(self):
        sel = self.Tree3.focus()
        self.slct = self.Tree3.item(sel, option='values')
        row = self.slct
        self.MM = row[4]
        self.BCM1 = row[5]
        self.KDM = row[7]
        self.message_entry10.delete(0, 10)
        self.message_entry10.insert(0, row[0])
        self.Materials2.destroy()

    def GoToWork_in(self):
        sel = self.Tree2.focus()
        self.slct = self.Tree2.item(sel, option='values')
        row = self.slct
        self.YEMP1 = row[6]
        self.PLM = row[3]
        self.message_entry18.delete(0, 10)
        self.message_entry18.insert(0, row[0])
        self.Materials.destroy()

    def WindowMashines(self):
        self.BasaM2 = tkinter.Toplevel(self.Smart)
        self.BasaM2.geometry('1070x450+700+200')
        self.BasaM2.title("Выбор оборудования МИОМ")
        self.Tree = Treeview(self.BasaM2, columns=(
            "Name", "Max_change_energi", "Condenser_capasity", "Equipment_induct", "SccF", "R0", "FW"), height=20,
                             show='headings')
        self.Tree.column("Name", width=120, anchor=tkinter.CENTER)
        self.Tree.column("Max_change_energi", width=70, anchor=tkinter.CENTER)
        self.Tree.column("Condenser_capasity", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Equipment_induct", width=50, anchor=tkinter.CENTER)
        self.Tree.column("SccF", width=60, anchor=tkinter.CENTER)
        self.Tree.column("R0", width=50, anchor=tkinter.CENTER)
        self.Tree.column("FW", width=50, anchor=tkinter.CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name", text="Наименование")
        self.Tree.heading("Max_change_energi", text="W_mash")
        self.Tree.heading("Condenser_capasity", text="CCE")
        self.Tree.heading("Equipment_induct", text="LCE")
        self.Tree.heading("SccF", text="FCE")
        self.Tree.heading("R0", text="R0")
        self.Tree.heading("FW", text="FW")
        self.Tree.place(x=50, y=10)
        mt = sqlite3.connect("mashins.db")
        cursor = mt.cursor()
        cpt = 0
        for row in cursor.execute("select* from mashines"):
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1
        self.Tree.place(x=50, y=10)
        label1 = tkinter.Label(self.BasaM2, text="W_mash-максимальная мощность разряда", bg="lightgrey", fg="black")
        label1.place(x=510, y=30)
        label2 = tkinter.Label(self.BasaM2, text="CCT-Емкость батареи конденсаторов установки", bg="lightgrey", fg="black")
        label2.place(x=510, y=50)
        label3 = tkinter.Label(self.BasaM2, text="LCE-индуктивность", bg="lightgrey", fg="black")
        label3.place(x=510, y=70)
        label4 = tkinter.Label(self.BasaM2, text="FW-величина тока короткого замыкания", bg="lightgrey", fg="black")
        label4.place(x=510, y=90)
        label7 = tkinter.Label(self.BasaM2, text="R0-активное сопротивление установки", bg="lightgrey", fg="black")
        label7.place(x=510, y=110)
        label8 = tkinter.Label(self.BasaM2, text="FCE-частота колебаний разрядного тока МИУ в режиме короткого замыкания",
                       bg="lightgrey", fg="black")
        label8.place(x=510, y=130)
        btn4 = tkinter.Button(self.BasaM2, text="Взять данные в работу", bg='green', fg='black',
                                    command=self.GoToWork)
        btn4.place(x=510, y=180)

    def GoToWork(self):
        sel = self.Tree.focus()
        self.slct2 = self.Tree.item(sel, option='values')
        self.row = self.slct2[0]
        print(self.row)
        print(self.slct2)
        self.message_entry19.delete(0, 10)
        self.message_entry19.insert(0, self.row)
        self.LCE1 = self.slct2[3]
        self.CCE1 = self.slct2[2]
        self.FCE1 = self.slct2[4]
        self.FW = self.slct2[6]
        self.BasaM2.destroy()

    def ChangeLabel(self):
        self.operation=self.option.get()
        print(self.operation)
        if self.operation == "b1 - обжим цилиндра" or self.operation == "a1-раздача цилиндра":
            self.label5["text"] = self.LabelG[1]
        elif self.operation == "b2 - обжим конуса" or self.operation == "a2 - раздача конуса":
            self.label5["text"] = self.LabelG[2]
        elif self.operation == "b3 - обжим сферы" or self.operation == "a3 - раздача сферы":
            self.label5["text"] = self.LabelG[3]
        elif self.operation == "b4 - обжим рифта" or self.operation == "a4 - раздача рифта":
            self.label5["text"] = self.LabelG[4]
        self.operation=self.operation[0:2]
        print(self.operation)
        self.message_entry4 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry4.place(x=300, y=210)

    def CloseWindow(self):
        self.Smart.destroy()

    def CalculateForm(self):
        self.text.delete(1.0, tkinter.END)
        self.DOT = self.message_entry1.get()
        self.ST = self.message_entry2.get()
        self.LBT = self.message_entry3.get()
        self.RC = self.message_entry4.get()
        self.BCM = float(self.BCM1) * pow(10, 7)
        self.KPD = self.message_entry8.get()
        f = Computing.Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM),
                           float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        DIB = Computing.Form.DIB(f)
        s = "Внутренний диаметр трубчатой заготовки:" + str(DIB) + ",м"
        self.text.insert(1.0, s)
        RIB = Computing.Form.RIB(f)
        s1 = "\n" + "Внутренний радиус трубчатой заготовки:" + str(RIB) + ",м"
        self.text.insert(2.0, s1)
        ESP = Computing.Form.EPS(f, self.RC)
        s2 = "\n" + "Cредняя величина деформации заготовки:" + str(ESP) + ",м"
        self.text.insert(3.0, s2)
        BCMD = Computing.Form.BCMD(f)
        s3 = "\n" + "Динамическое значение коэффициента аппроксимации кривой упрочнения:" + str(BCMD)
        self.text.insert(4.0, s3)
        WYD = Computing.Form.WYD(f)
        s4 = "\n" + "Удельная работа деформации:" + str(WYD) + ",Дж"
        self.text.insert(5.0, s4)
        DVB = Computing.Form.DVB(f)
        s5 = "\n" + "Деформируемый объем заготовки:" + str(DVB) + ",mm3"
        self.text.insert(6.0, s5)
        WDB = Computing.Form.WDB(f)
        s6 = "\n" + "Работа деформации заготовки:" + str(WDB) + ",Дж"
        self.text.insert(7.0, s6)
        WMIR = Computing.Form.WMIR(f)
        s7 = "\n" + 'Необходимая энергия для выполнения операции:' + str(WMIR) + ",Дж"
        self.text.insert(8.0, s7)
        WMUR = Computing.Form.WMUR(f)
        s8 = "\n" + "Энергоемкость установки:" + str(WMUR) + ",Дж"
        self.text.insert(9.0, s8)
    def CalculateIt(self):
        self.text.delete(1.0, tkinter.END)
        self.DOT = self.message_entry1.get()
        self.ST = self.message_entry2.get()
        self.LBT = self.message_entry3.get()
        self.RC = self.message_entry4.get()
        self.BCM = float(self.BCM1)*pow(10,7)
        self.KPD = self.message_entry8.get()
        self.SC = self.message_entry15.get()# длина индуктора
        self.HSC = self.message_entry16.get()# высота индуктора
        self.NCT1 = self.message_entry21.get()  # высота индуктора
        self.YEMP=float(self.YEMP1)*pow(10,-8)
        self.FCE=float(self.FCE1)*pow(10,3)
        self.LCE=float(self.LCE1)*pow(10,-6)
        self.CCE=float(self.CCE1)*pow(10, -6)
        f = Computing.Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM), float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        g = Computing.Inductor(float(self.LBT), self.operation, float(self.DOT), float(self.ST), float(self.FW), float(self.YEMP), float(self.FCE), float(self.LCE), 1* pow(10, -12),
                               float(self.CCE), float(self.SC), float(self.HSC), float(self.PLM), float(self.BCM), float(self.KDM), float(self.MM), float(self.KPD),
                               float(self.RC), float(self.NCT1), float(self.ZS),float(self.ZB),float(self.ZA),float(self.YEMC),float(self.LTC))
        DIB = Computing.Form.DIB(f)
        s="Внутренний диаметр трубчатой заготовки:" + str(DIB) + ",м"
        self.text.insert(1.0, s)
        RIB = Computing.Form.RIB(f)
        s1="\n"+"Внутренний радиус трубчатой заготовки:" + str(RIB) + ",м"
        self.text.insert(2.0, s1)
        ESP = Computing.Form.EPS(f, self.RC)
        s2="\n"+"Cредняя величина деформации заготовки:" + str(ESP) + ",м"
        self.text.insert(3.0, s2)
        BCMD = Computing.Form.BCMD(f)
        s3="\n"+"Динамическое значение коэффициента аппроксимации кривой упрочнения:" + str(BCMD)
        self.text.insert(4.0, s3)
        WYD = Computing.Form.WYD(f)
        s4="\n"+"Удельная работа деформации:" + str(WYD) + ",Дж"
        self.text.insert(5.0, s4)
        DVB = Computing.Form.DVB(f)
        s5="\n"+"Деформируемый объем заготовки:" + str(DVB) + ",mm3"
        self.text.insert(6.0, s5)
        WDB = Computing.Form.WDB(f)
        s6="\n"+"Работа деформации заготовки:" + str(WDB) + ",Дж"
        self.text.insert(7.0, s6)
        WMIR = Computing.Form.WMIR(f)
        s7="\n"+'Необходимая энергия для выполнения операции:' + str(WMIR) + ",Дж"
        self.text.insert(8.0, s7)
        WMUR = Computing.Form.WMUR(f)
        s8="\n"+"Энергоемкость установки:" + str(WMUR) + ",Дж"
        self.text.insert(9.0, s8)
        LCA = Computing.Inductor.LCA(g)
        s9="\n"+"Длина индуктора:" + str(LCA) + ",м"
        self.text.insert(10.0, s9)
        ZCP = Computing.Inductor.ZCP(g)
        s10="\n"+"Величина зазора между индуктором и заготовкой:" + str(ZCP) + ",м"
        self.text.insert(11.0, s10)
        DCA = Computing.Inductor.DCA(g)
        s11="\n"+"Диаметр индуктора:" + str(DCA) + ",м"
        self.text.insert(12.0, s11)
        BP = Computing.Inductor.BP(g)
        s12="\n"+"Глубина проникновения ИМП в материал заготовки: " + str(BP) + " ,м"
        self.text.insert(13.0, s12)
        BC = Computing.Inductor.BC(g)
        s13="\n"+"Глубина проникновения ИМП в материал индуктор: " + str(BC) + " ,м"
        self.text.insert(14.0, s13)
        LDC = Computing.Inductor.LDC(g)
        s14="\n"+"Паразитная индуктивность разрядного контура: " + str(LDC) + " ,Гн"
        self.text.insert(15.0, s14)
        FDC = Computing.Inductor.FDC(g)
        s15="\n"+"Частота разряда при наличии только паразитных индуктивностей: " + str(FDC) + " ,Гц"
        self.text.insert(16.0, s15)
        K1 = Computing.Inductor.K1(g)
        s16="\n"+"Коэффициент К1: " + str(K1)
        self.text.insert(17.0, s16)
        K2 = Computing.Inductor.K2(g)
        s17="\n"+"Коэффициент К2: " + str(K2)
        self.text.insert(18.0, s17)
        K3 = Computing.Inductor.K3(g)
        s18="\n"+"Коэффициент К3: " + str(K3)
        self.text.insert(19.0, s18)
        K4 = Computing.Inductor.K4(g)
        s19="\n"+"Коэффициент К4: " + str(K4)
        self.text.insert(20.0, s19)
        ZEK = Computing.Inductor.ZEK(g)
        s20="\n"+"Значение эквивалентного зазора между индуктором и заготовкой: " + str(ZEK)
        self.text.insert(21.0, s20)
        NCTC = Computing.Inductor.NCTC(g)
        s21="\n"+"Количество витков индуктора: " + str(NCTC)
        self.text.insert(22.0, s21)
        NCW = Computing.Inductor.NCW(g)
        s22="\n"+"Целое количество витков индуктора: " + str(NCW)
        self.text.insert(23.0, s22)
        NCWC = Computing.Inductor.NCWC(g)
        s23="\n"+"Расчетное количество рабочих витков" + str(NCWC)
        self.text.insert(24.0, s23)
        NCF = Computing.Inductor.NCF(g)
        s24="\n"+"Количество свободных витков" + str(NCF)
        self.text.insert(25.0, s24)
        SCIC = Computing.Inductor.SCIC(g)
        s25="\n"+"Расчетный шаг витков индуктора: " + str(SCIC)
        self.text.insert(26.0, s25)
        WR = Computing.Inductor.WR(g)
        s26="\n"+"Необходимая энергия разряда МИУ: " + str(WR) + ",Дж"
        self.text.insert(27.0, s26)
        LUC = Computing.Inductor.LUC(g)
        s27="\n"+"Суммарная индуктивность: " + str(LUC) + " ,Гн"
        self.text.insert(28.0, s27)
        PM = Computing.Inductor.PM(g)
        s28="\n"+"Давление  " + str(PM) + "Па"
        self.text.insert(29.0, s28)
        VCR = Computing.Inductor.VCR(g)
        s29="\n"+"Скорость  " + str(VCR) + "м\с"
        self.text.insert(30.0, s29)
