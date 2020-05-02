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
        label2 = tkinter.Label(self.Smart, text="Введите диаметр наружной трубы, м", bg="lightgrey", fg="red")
        label2.place(x=10, y=60)
        label3 = tkinter.Label(self.Smart, text="Введите толщину стенки трубы, м", bg="lightgrey", fg="red")
        label3.place(x=10, y=110)
        label4 = tkinter.Label(self.Smart, text="Введите длину деформируемой зоны, м", bg="lightgrey", fg="red")
        label4.place(x=10, y=160)
        self.LabelG = ["Выберете операцию","Введите радиус цилиндра, м","Максимальный радиус конуса, м","Радиус сферы, м", "Радиус рифта"]
        self.label5 = tkinter.Label(self.Smart, text=self.LabelG[0], bg="lightgrey", fg="red")
        self.label5.place(x=10, y=210)
        label6 = tkinter.Label(self.Smart, text="Коэффициент степенной аппроксимации кривой упрочнения материала BCM", bg="lightgrey", fg="black")
        label6.place(x=10, y=260)
        label7 = tkinter.Label(self.Smart, text="Коэффициент степенной аппроксимации кривой упрочнения материала MM", bg="lightgrey", fg="black")
        label7.place(x=10, y=310)
        label8 = tkinter.Label(self.Smart, text="Коэффициент динамичности материала KDM",
                               bg="lightgrey", fg="black")
        label8.place(x=10, y=360)
        label9 = tkinter.Label(self.Smart, text="КПД, ед.",
                               bg="lightgrey", fg="red")
        label9.place(x=10, y=410)
        label10 = tkinter.Label(self.Smart, text="Операция",
                               bg="lightgrey", fg="black")
        label10.place(x=10, y=460)
        label11 = tkinter.Label(self.Smart, text="Поиск материала для заготовки в базе",
                                bg="lightgrey", fg="black")
        label11.place(x=800, y=60)
        self.label24 = tkinter.Label(self.Smart, text="",
                                     bg="lightgrey", fg="red")
        self.label24.place(x=820, y=80)
        label12 = tkinter.Label(self.Smart, text="Удельное электрическое сопротивление материала индуктора",
                                bg="lightgrey", fg="black")
        label12.place(x=10, y=510)
        label13 = tkinter.Label(self.Smart, text="Частота колебаний разрядного тока МИУ в режиме короткого замыкания",
                                bg="lightgrey", fg="black")
        label13.place(x=10, y=560)
        label14 = tkinter.Label(self.Smart, text="Индуктивность",
                                bg="lightgrey", fg="black")
        label14.place(x=10, y=610)
        label15 = tkinter.Label(self.Smart, text="Ёмкость батареи конденсаторов МИУ",
                                bg="lightgrey", fg="black")
        label15.place(x=10, y=660)
        label16 = tkinter.Label(self.Smart, text="Длина индуктора",
                                bg="lightgrey", fg="red")
        label16.place(x=10, y=710)
        label17 = tkinter.Label(self.Smart, text="Высота индуктора",
                                bg="lightgrey", fg="red")
        label17.place(x=10, y=760)
        label18 = tkinter.Label(self.Smart, text="Плотность материала индуктора",
                                bg="lightgrey", fg="black")
        label18.place(x=10, y=810)
        label19 = tkinter.Label(self.Smart, text="Поиск материала для индуктора в базе",
                                bg="lightgrey", fg="black")
        label19.place(x=800, y=110)
        self.label23 = tkinter.Label(self.Smart, text="",
                                     bg="lightgrey", fg="red")
        self.label23.place(x=820, y=130)
        label20 = tkinter.Label(self.Smart, text="Поиск установки в базе",
                                bg="lightgrey", fg="black")
        label20.place(x=800, y=160)
        self.label22 = tkinter.Label(self.Smart, text="",
                                bg="lightgrey", fg="red")
        self.label22.place(x=820, y=180)
        label21 = tkinter.Label(self.Smart, text="Частота тока короткого замыкания",
                                bg="lightgrey", fg="black")
        label21.place(x=10, y=860)
        label21 = tkinter.Label(self.Smart, text="Введите количество витков",
                                bg="lightgrey", fg="red")
        label21.place(x=10, y=910)
        self.message_entry1 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry1.place(x=600, y=60)
        self.message_entry2 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry2.place(x=600, y=110)
        self.message_entry3 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry3.place(x=600, y=160)
        self.message_entry5 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry5.place(x=600, y=260)
        self.message_entry6 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry6.place(x=600, y=310)
        self.message_entry7 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry7.place(x=600, y=360)
        self.message_entry8 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry8.place(x=600, y=410)
        self.option= tkinter.StringVar(self.Smart)
        self.option.set("Выбери операцию тут")
        self.message_entry9=tkinter.OptionMenu(self.Smart,self.option,"a1","a2","a3","a4","b1","b2","b3","b4")# выбор операции
        self.message_entry9.place(x=600, y=460)
        btn5=tkinter.Button(self.Smart, text="Выбрать", bg="orange", fg="black", command=self.ChangeLabel)
        btn5.place(x=500,y=460)
        self.message_entry10 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry10.place(x=1100, y=60)
        self.message_entry11 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry11.place(x=600, y=510)
        self.message_entry12 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry12.place(x=600, y=560)
        self.message_entry13 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry13.place(x=600, y=610)
        self.message_entry14 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry14.place(x=600, y=660)
        self.message_entry15 = tkinter.Entry(self.Smart, textvariable='') #длинна индуктора
        self.message_entry15.place(x=600, y=710)
        self.message_entry16 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry16.place(x=600, y=760)
        self.message_entry17 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry17.place(x=600, y=810)
        self.message_entry18 = tkinter.Entry(self.Smart, textvariable='')#материал индукора
        self.message_entry18.place(x=1100,y=110)
        self.message_entry19 = tkinter.Entry(self.Smart, textvariable='')# установка
        self.message_entry19.place(x=1100, y=160)
        self.message_entry20 = tkinter.Entry(self.Smart, textvariable='')# частота тока короткого замыкания
        self.message_entry20.place(x=600, y=860)
        self.message_entry21 = tkinter.Entry(self.Smart, textvariable='')  # количество витков
        self.message_entry21.place(x=600, y=910)
        btn = tkinter.Button(self.Smart, text="Закрыть окно", bg="red", fg="black", command=self.CloseWindow)
        btn.place(x=10, y=950)
        btn1 = tkinter.Button(self.Smart, text="Рассчитать", bg="green", fg="black", command=self.CalculateIt)
        btn1.place(x=280, y=950)
        btn5 = tkinter.Button(self.Smart, text="Открыть базу установок", bg="lightgreen", fg="black",
                              command=self.WindowMashines)
        btn5.place(x=1300, y=160)
        btn6 = tkinter.Button(self.Smart, text="Открыть базу материалов", bg="lightgreen", fg="black",
                              command=self.SearchMaterials)
        btn6.place(x=1300, y=110)
        btn7 = tkinter.Button(self.Smart, text="Открыть базу материалов", bg="lightgreen", fg="black",
                              command=self.SearchMaterials)
        btn7.place(x=1300, y=60)
        self.text=tkinter.Text(self.Smart, height=35)
        self.text.place(x=800,y=450)

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
        self.Tree = Treeview(self.Materials, columns=(
            "Name_of_the_metalls", "Tensile_strength", "Yield_strength", "Material_density", "M_M", "B",
            "Specific_electric_resistance", "The_coefficient_of_dynamic", 'Еhe_dynamic_modulus_hardening'), height=30,
                                 show='headings')
        self.Tree.column("Name_of_the_metalls", width=60, anchor=tkinter.CENTER)
        self.Tree.column("Tensile_strength", width=70, anchor=tkinter.CENTER)
        self.Tree.column("Yield_strength", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Material_density", width=50, anchor=tkinter.CENTER)
        self.Tree.column("M_M", width=50, anchor=tkinter.CENTER)
        self.Tree.column("B", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Specific_electric_resistance", width=50, anchor=tkinter.CENTER)
        self.Tree.column("The_coefficient_of_dynamic", width=50, anchor=tkinter.CENTER)
        self.Tree.column("Еhe_dynamic_modulus_hardening", width=50, anchor=tkinter.CENTER)
        self.Tree['show'] = "headings"
        self.Tree.heading("Name_of_the_metalls", text="Металл")
        self.Tree.heading("Tensile_strength", text="PPM")
        self.Tree.heading("Yield_strength", text="PYD")
        self.Tree.heading("Material_density", text="PLM")
        self.Tree.heading("M_M", text="M_M")
        self.Tree.heading("B", text="B")
        self.Tree.heading("Specific_electric_resistance", text="YEMP")
        self.Tree.heading("The_coefficient_of_dynamic", text="KDM")
        self.Tree.heading("Еhe_dynamic_modulus_hardening", text="MDM")
        self.Tree.place(x=50, y=10)
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
        for row in cursor.execute("select* from Workpiece_material"):
            self.Tree.insert('', 'end', text=str(cpt), values=row)
            cpt += 1
        self.btn = tkinter.Button(self.Materials, text="Взять данные в работу", bg="green", fg="black")  # описание объекта типа button названия кнопки
        self.btn.place(x=550, y=150)
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
        self.message_entry13.delete(0, 10)
        self.LCE1 = self.slct2[3]
        self.message_entry13.insert(0, self.LCE1)
        self.message_entry14.delete(0, 10)
        self.CCE1 = self.slct2[2]
        self.message_entry14.insert(0, self.CCE1)
        self.message_entry12.delete(0, 10)
        self.FCE1 = self.slct2[4]
        self.message_entry12.insert(0, self.FCE1)
        self.message_entry20.delete(0, 10)
        self.FW = self.slct2[6]
        self.message_entry20.insert(0, self.FW)
        self.BasaM2.destroy()

    def ChangeLabel(self):
        self.operation=self.option.get()
        print(self.operation)
        if self.operation == "b1" or self.operation == "a1":
            self.label5["text"] = self.LabelG[1]
        elif self.operation == "b2" or self.operation == "a2":
            self.label5["text"] = self.LabelG[2]
        elif self.operation == "b3" or self.operation == "a3":
            self.label5["text"] = self.LabelG[3]
        elif self.operation == "b4" or self.operation == "a4":
            self.label5["text"] = self.LabelG[4]
        self.message_entry4 = tkinter.Entry(self.Smart, textvariable='')
        self.message_entry4.place(x=600, y=210)

    def SearchMaterialForInductor(self):
        self.label23["text"] = ""
        material = self.message_entry18.get()
        print(material)
        conn = sqlite3.connect("Metalls.db")
        cursor = conn.cursor()
        sql1 = "select Specific_electric_resistance, Material_density from Workpiece_material where Name_of_the_metalls ='"+material+"'"
        c=0
        for row in cursor.execute(sql1):
            c=+1
            self.message_entry11.delete(0, 10)
            self.YEMP1=row[0]
            self.message_entry11.insert(0,self.YEMP1)
            self.message_entry17.delete(0, 10)
            self.PLM = row[1]
            self.message_entry17.insert(0, self.PLM)
        if c == 0: self.label23["text"] = "По вашему запросу в базе ничего не найдено"

    def SearchMaterial(self):
        self.label24["text"] = ""
        material=self.message_entry10.get()
        print(material)
        conn = sqlite3.connect("Metalls.db")
        cursor = conn.cursor()
        sql="select M_M, B, The_coefficient_of_dynamic from Workpiece_material where Name_of_the_metalls ='" + material + "'"
        print(sql)
        sql1="select * from Workpiece_material "
        print(cursor.execute(sql))
        c=0
        for row in cursor.execute(sql):
            print(row)
            c=+1
            self.message_entry5.delete(0,10)
            self.message_entry6.delete(0,10)
            self.message_entry7.delete(0,10)
            self.MM=row[0]
            self.BCM1=row[1]
            self.KDM=row[2]
            self.message_entry5.insert(0,self.BCM1)
            self.message_entry6.insert(0,self.MM)
            self.message_entry7.insert(0,self.KDM)
        if c == 0: self.label24["text"] = "По вашему запросу в базе ничего не найдено"

    def CloseWindow(self):
        self.Smart.destroy()

    def CalculateIt(self):
        self.DOT = self.message_entry1.get()
        self.ST = self.message_entry2.get()
        self.LBT = self.message_entry3.get()
        self.RC = self.message_entry4.get()
        self.BCM = float(self.BCM1)*pow(10,7)
        self.KPD = self.message_entry8.get()
        self.operation = self.option.get()#операция
        self.SC = self.message_entry15.get()# длина индуктора
        self.HSC = self.message_entry16.get()# высота индуктора
        self.NCT1 = self.message_entry21.get()  # высота индуктора
        self.YEMP=self.YEMP1*pow(10,-8)
        self.FCE=self.FCE1*pow(10,3)
        self.LCE=self.LCE1*pow(10,-6)
        self.CCE=self.CCE1*pow(10, -6)
        f = Computing.Form(float(self.DOT), float(self.ST), float(self.BCM), float(self.KDM), float(self.MM), float(self.LBT), float(self.KPD), float(self.RC), self.operation)
        g = Computing.Inductor(float(self.LBT), self.operation, float(self.DOT), float(self.ST), float(self.FW), float(self.YEMP), float(self.FCE), float(self.LCE), 1* pow(10, -12),
                               float(self.CCE), float(self.SC), float(self.HSC), float(self.PLM), float(self.BCM), float(self.KDM), float(self.MM), float(self.KPD),
                               float(self.RC), float(self.NCT1))
        DIB = Computing.Form.DIB(f)
        s="Внутренний диаметр трубчатой заготовки:" + str(DIB) + ",м"
        self.text.insert(1.0, s)
        RIB = Computing.Form.RIB(f)
        s1="\n"+"Внутренний радиус трубчатой заготовки:" + str(RIB) + ",м"
        self.text.insert(2.0, s1)
        ESP = Computing.Form.ESP(f, self.RC)
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
