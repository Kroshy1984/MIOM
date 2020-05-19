import math

class Pascal():
    def __init__(self):
        # def maiself.n1
        self.poisk = 1
        v = 0
        kn = 0
        # mc=1
        # r2l=1
        mm = 0
        u1 = 1
        mmm = 0
        self.U0 = 1
        ek = 0.02
        fb = 1
        self.l1 = 1
        l3 = 1
        self.di = 1
        # self.c0 = 1
        lm = 1.2 * math.pow(10, -7)  # Lm_у СОБСТВ. ИНДУКТИВНОСТЬ УСТАНОВКИ
        self.c0 = 254 * math.pow(10, -6)  # Co_у ЕМКОСТЬ КОНДЕНСАТОРОВ УСТАНОВКИ
        self.p3 = 7.1 * math.pow(10, -8)  # RO_з УДЕЛ. Э/СОПРОТИВЛЕНИЕ ЗАГОТОВКИ,
        mod_upr = 68 * math.pow(10, 9)  # E_з МОДУЛЬ УПРУГОСТИ ЗАГОТОВКИ,
        pm = 2640  # Pm_з ПЛОТНОСТЬ ЗАГОТОВКИ, ( кг/м3)
        self.l0 = 0.030  # lo_з ДЛИНА ЗАГОТОВКИ, м
        self.dh = 0.1514  # Dн_з НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ, м
        self.h0 = 0.0012  # Ho_з ТОЛЩИНА СТЕНКИ ЗАГОТОВКИ, м
        p1 = 1.78 * math.pow(10, -8)  # RO_и УДЕЛ. Э/СОПРОТИВЛЕНИЕ ИНДУКТОРА, (Ом*м)
        a = 0.004
        b = 0.008
        hb = 0.005
        lv = 0.150
        dv = 0.153  # Dи_в ВНУТРЕННИЙ ДИАМЕТР ИНДУКТОРА , м
        self.n1 = 7  # self.n1_и ЧИСЛО ВИТКОВ ИНДУКТОРА
        self.l1 = 0.036  # self.l1_и ДЛИНА (ВЫСОТА) ИНДУКТОРА, м
        R0 = 4.25 * math.pow(10, -3)  # Ro_у СОПРОТИВЛЕНИЕ УСТАНОВКИ, Ом
        self.dn = 0.169  # Dн_и НАРУЖНЫЙ ДИАМЕТР ИНДУКТОРА , м
        sp = 700 * math.pow(10, 6)  # SP_з ПРЕДЕЛ ТЕКУЧЕСТИ ЗАГОТОВКИ, Н/м2
        h1 = 0.004  # Hи_1 ВЫСОТА ВИТКА ИНДУКТОРА (ПО ДЛИНЕ), м
        ey = 700 * math.pow(10, 6)  # e'_з МОДУЛЬ УПРОЧНЕНИЯ ЗАГОТОВКИ, Н/м2
        eps = 0.0001  # eo_з КОНЕЧНАЯ ОТНОСИТЕЛЬНАЯ ДЕФОРМАЦИЯ ЗАГОТОВКИ - 𝑒𝜑𝑘
        H_izol = 0.0009  # Hизол_и - ТОЛЩИНА ИЗОЛЯЦИИ МЕЖДУ ВИТКАМИ, м
        self.U0 = 7000  # Uo_у НАЧАЛЬНОЕ НАПРЯЖЕНИЕ УСТАНОВКИ, В
        self.kappa = 1

        flag = 0
        mu0 = 4 * math.pi * 1e-7
        r2l = R0 * R0 / 4 / lm / lm
        lmc = lm * self.c0
        if 1 / lmc < r2l:
            print("Разряд апериодический")
        f0 = 0.5 / (3.14 * math.pow((1 / lmc - r2l), 0.5))
        over_f0 = 0.5 / (3.14 * math.pow(lmc, 0.5))
        fz = self.p3 / (3.14 * mu0 * self.h0 * self.h0)  # минимальная рабочая частота разряда, Гц
        # {для недопущения эффекта "магнитной подушки"}
        w3 = math.pow(mod_upr / pm, 0.5) * 2 / self.dh
        f3 = w3 / 2 / 3.14  # { собственная частота }
        #     { колебаний заготовки, Гц }
        # _____________________________________________________________________________________________________________________________
        #     { self.dh-НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
        db = self.dh - 2 * self.h0  # { db-ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ

        """def Prikids(y,ek,u1):
                ZOLOTO = (pow(5, 0.5)-1)/2
                def1 = y
                defold = def1
                if def1 < ek: def1 = defold + ZOLOTO*abs(defold-ek)
                else: def1 = ek + (1-ZOLOTO)*abs(defold-ek)
                drob = (def1 + ek) / ek/2
                if defold-ek > 0:
                    if drob < 1:
                     uself.U0 = u1 * drob
                    else: uself.U0 = u1 / drob
                else:
                    if drob < 1: uself.U0 = u1 / drob
                    else: uself.U0 = u1 * drob
                if (defold/ek) < 0.01:
                    uself.U0 = 2 * u1 / drob
                print("Предлагаемое значение [кВ] Uo = "+str(uself.U0)+" кВ")"""

        if v == 1:  # раздача }
            ly = self.l0 / db

        else:  # { ОБЖИМ }
            ly = self.l1 / dv
        if kn < 0.1:
            if self.poisk == 1:
                print("L/D = ", ly)
        if ly < 1:
            kn = 3.783890521981891 * ly - 7.795224937947945 * ly * ly + 4.714887625113096 * math.pow(ly,
                                                                                                     3) + 6.984777813396215 * math.pow(
                ly, 4) - 13.53957485592525 * math.pow(ly, 5) + 9.187983184383594 * math.pow(ly,
                                                                                            6) - 3.048218155556006 * math.pow(
                ly, 7) + 0.4929535896014099 * math.pow(ly, 8) - 3.094887626324646E-2 * math.pow(ly, 9)
        else:
            if ly < 2:
                kn = 0.69026 + 0.06 * ly
            else:
                kn = 0.7669266667 + 0.021666667 * ly
        if self.poisk == 1:
            print(" Фактор поля , Кн = ", kn)
        if fz < (f0 / 2):
            fp = 0.5 * f0
        else:  # if abs(fz - f0) < f0 / 2:
            fp = 0.8 * f0
        if fz > 1.5 * f0:
            print(
                " ОБРАБОТКА НА МИУ НЕЦЕЛЕСООБРАЗНА ")  # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных
        # <<<<<<< HEAD
        # if self.poisk==1 or mm==0:
        #   print(' КОНТРОЛЬ ПАРАМЕТРОВ [ 1 - ДА ], [ 0 - НЕТ ] ? ')  # необходимо вывести окно с данным вопросом
        #  kp1 = input()
        # else:
        #   kp1 = 0
        if self.poisk == 1 and mm > 0:
            self.U0 = u1
            u1 = u1 * 1000
            self.U0 = u1
        if self.poisk == 0 and mmm > 0:
            self.U0 = self.U0

        # {1} Repeat {начало}
        wq = fp * 2.0 * 3.14
        if w3 > wq * 3:
            ef = 0.5 * ek
        else:
            if w3 < wq / 3:
                ef = 0
            else:
                ef = 0.25 * ek
        # =======
        """if self.poisk==1 or mm==0:
                    print(' КОНТРОЛЬ ПАРАМЕТРОВ [ 1 - ДА ], [ 0 - НЕТ ] ? ')  # необходимо вывести окно с данным вопросом
                    kp1=input()
                 else: """
        kp1 = 0
        if self.poisk == 1 and mm > 0:
            self.U0 = u1
            u1 = u1 * 1000
            self.U0 = u1
        if self.poisk == 0 and mmm > 0:
            self.U0 = self.U0

        # ___________________________________________________________________________________________________________________
        else:  # РАЗДАЧА
            # { ОБЖИМ }
            self.vg = 1 * (-1)
        if self.l0 / self.dh < 1:
            l3 = self.l0 / math.pow((1 - ef), 0.5)
            h3 = self.h0 / math.sqrt(1 - ef)
        else:
            l3 = self.l0
            h3 = self.h0 / (1 - ef)
        dz = self.dh * (1 - ef)  # { СРЕДНИЙ НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
        dm = dz - 2.0 * h3  # { СРЕДНИЙ ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ }
        wr = (dv - self.dh) / 2.0
        self.x3 = pow((self.p3 / (3.14 * mu0 * fp)), 0.5)
        x1 = pow((p1 / (mu0 * 3.14 * fp)), 0.5)
        if x1 < 2 * a / 3:
            xb = x1
        else:
            xb = 2 * a / 3
        z = b / (hb + xb)  # {hb - ЗАЗОР МЕЖДУ ТОКОПОДВОДАМИ }
        lb = (0.5 * self.l1 * math.log((2.0 * self.l1) / (a + b) + 0.5) + (
                math.log((hb + xb) / (b + xb)) + (z * z - 1) * math.log(1 + z * z) / (2.0 * z * z) + (
                2.0 / z * math.atan(z))) * lv) * pow(10, -7)
        rb = p1 * (self.l1 + 2.0 * lv) / (a * b)
        xi = 0
        # ======================================================================================================================
        if v == 0:
            # begin { ОБЖИМ }
            if 0.5 * x1 < h1 / 3.0:
                xi = 0.5 * x1
            else:
                xi = h1 / 3.0
            self.di = dv + 2.0 * xi
        else:  # обжим
            self.di = self.dn - h1  # { РАЗДАЧА }

        # { индуктор средний }
        if self.l1 / self.di < 1.0 and self.l1 / self.di > 0.3:
            Lind = self.di * self.di / self.l1 * (4.1 + 3.9 * (self.l1 / self.di - 0.3)) * self.n1 * self.n1 * pow(10, -7)
        else:
            if self.l1 / self.di > 1:  # then { индуктор длинный }
                Lind = self.di * self.di / self.l1 * (9.9 - (3.2 * self.di) / self.l1) * self.n1 * self.n1 * pow(10, -7)
            else:  # { индуктор короткий }
                Lind = self.di * self.di / self.l1 * (4.1 + 3.9 * (self.l1 / self.di - 0.3)) * self.n1 * self.n1 * pow(10, -7)
        if x1 <= h1:
            xr = x1
        else:
            xr = h1
        if 3 <= h3 / 3.0:
            xz = self.x3 / 2.0
        else:
            xz = h3 / 3.0
        if v == 1:
            dr = dm + 2.0 * xz  # { РАЗДАЧА }
        # { dr - РАСЧЕТНЫЙ ДИАМЕТР ЗАГОТОВКИ}
        else:
            dr = dz - 2.0 * xz  # { ОБЖИМ }
        if l3 / dr < 1.0 and l3 / dr > 0.3:
            self.vb = 1
            self.q0 = 2.0 / math.pow(3.0, 0.5)
            # { заготовка средняя }
            Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * pow(10, -7)
        else:  # { begin else }
            self.vb = 0
            self.q0 = 1
        if l3 / dr > 1.0:  # then { заготовка длинная }
            Lzag = dr * dr / l3 * (9.9 - 3.2 * dr / l3) * pow(10, -7)
        else:
            print(
                "... Обработка на МИУ нецелесообразна...")  # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных

        self.vb = 1
        self.q0 = 2.0 / math.pow(3.0, 0.5)

        Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * pow(10, -7)

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if self.x3 < h3:
            xs = self.x3
        else:
            xs = h3
        Rzag = self.p3 * 3.14 * dr / (l3 * xs)  # { Rzag - АКТИВНОЕ СОПРОТИВЛЕНИЕ ЗАГОТОВКИ }
        hm = (self.l1 - H_izol * (self.n1 - 1)) * 1000 / self.n1  # { hm - ВЫСОТА ВИТКА ИНДУКТОРА }
        # ========================================================================================================================
        if hm < 0:
            # begin
            print("кУ-кУ !! кУ-кУ !! кУ-кУ !!")  # Требуется вывести окно
            print(" ВЫСОТА ВИТКА ИНДУКТОРА < 0 !!")
        # Delay(3000) Задержка
        # end
        Rind = p1 * 3.14 * self.di * self.n1 * self.n1 / self.l1 / xr  # { Rind - АКТИВНОЕ СОПРОТИВЛЕНИЕ ИНДУКТОРА }
        if self.l1 / self.di > 1.0:
            Lind = self.di * self.di / self.l1 * (9.9 - 3.2 * self.di / self.l1) * self.n1 * self.n1 * pow(10, -7)
        else:
            Lind = self.di * self.di / self.l1 * (4.1 + 3.9 * (self.l1 / self.di - 0.3)) * self.n1 * self.n1 * pow(10, -7)

        if v == 1:
            if self.l1 / self.di < 1.0:
                fb = 4.8
            else:
                fb = 5.0
                m9 = fb * pow((1 + (self.l1 + l3) * (self.l1 + l3)) / (self.di * self.di), 0.5) - 4.5 * pow(
                    ((1 + (self.l1 - l3) * (self.l1 - l3) / self.di / self.di), 0.5) * (self.n1 * pow(10, -7)))
                m8 = (dr * dr * self.di) / (self.l1 * l3)
                M_ind_zag = m9 * m8

        if v == 2:
            if l3 / dr < 1:
                fb = 4.8
            else:
                fb = 5.0
        m9 = fb * pow(1 + (self.l1 + l3) * (self.l1 + l3) / dr * dr, 0.5) - 4.5 * pow(1 + (self.l1 - l3) * (self.l1 - l3) / (dr * dr),
                                                                            0.5) * self.n1 * pow(10, -7)
        m8 = dr * self.di * self.di / (l3 * self.l1)
        M_ind_zag = m8 * m9

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        kq = M_ind_zag / Lzag
        qq = 2.0 * 3.14 * fp * Lzag / Rzag
        k2 = qq / math.pow((1 + qq * qq), 0.5)
        lnn = Lzag * kq * kq * k2 * k2
        rn = Rzag * kq * kq * k2 * k2
        lo = Lind - lnn
        ro = Rind + rn
        ls = lm + lb + lo
        rs = R0 + rb + ro
        s1 = rs / (2.0 * ls)
        ww = pow((abs(1.0 / (self.c0 * ls) - s1 * s1)), 0.5)
        c9 = (1.0 / (self.c0 * ls) - s1 * s1)
        if c9 < 0 and flag > 1:
            print("Ку ку разряд апериодический")  # then
        # _______________________________________________________________________________
        if c9 < 0:
            ww = 1
        q1 = ww / s1
        q3 = ww * (Lzag / Rzag)
        if c9 < 0:
            f1 = 0
        else:
            f1 = math.atan(q1 / (q1 * q3 - q3 / q1 - 1.0))
        s3 = ww / q3
        k3 = 1  # {sqrt((1+1/q1/q1)/(1-(1/q1-1/q3)*(1/q1-1/q3)))}
        E0 = 0.5 * self.c0 * self.U0 * self.U0
        # _____________________________________________________________________________________________________________________
        if (v == 0):  # then { ОБЖИМ }
            pw = mu0 * E0 * (self.n1 * kn / l3) * (self.n1 * kn / l3) / ls
        else:
            # { РАЗДАЧА }
            pw = (mu0 * E0 * kq * kq * kn * kn) / (ls * l3 * l3)
        pq = pw * math.exp(0 - 3.14 / (2.0 * q1))
        if c9 < 0:  # then
            fq = 10
        else:
            fq = ww / (2.0 * 3.14)
        """        # Repeat{3}
        print(' Для продолжения ===> Жми на <Enter> >>')"""
        print("F0=", f0)
        print("Fz=", fz)
        print("Fp=", fp)
        print("f3=", f3)
        print("h3=", h3)
        print("l3=", l3)
        print("self.vg=", self.vg)
        print("dz=", dz)
        print("ef=", ef)
        print("wr=", wr)
        print("db=", db)
        print("dm=", dm)
        print("self.x3=", self.x3)
        print("x1=", x1)
        print("xb=", xb)
        print("z=", z)
        print("xi=", xi)
        print("self.di=", self.di)
        print("Li=", Lind)
        print("xr=", xr)
        print("Ri=", Rind)
        print("xz=", xz)
        print("dr=", dr)
        print("Lz=", Lzag)
        print("xs=", xs)
        print("Rz=", Rzag)
        print("Ms=", M_ind_zag)
        print("k=", kq)
        print("qq=", qq)
        print("k2=", k2)
        print("Ln=", lnn)
        print("Rn=", rn)
        print("self.l0=", lo)
        print("Ro=", ro)
        print("Ls=", ls)
        print("Rs=", rs)
        print("s1=", s1)
        print("ww=", ww)
        print("q3=", q3)
        print("q1=", q1)
        print("Kн=", kn)
        print("f1=", f1)
        print("s3=", s3)
        print("k3=", k3)
        print("E0=", E0)
        print("Pw=", pw)
        print("Rтп=", rb)
        print("self.n1=", self.n1)
        print("Uo=", self.U0)
        print("Pmax=", pq)
        print("Hвит=", hm)
        print("Fr0=", over_f0)
        print("fq=", fq)
        self.io = 1  # { МИОМ(Э) , c. 79 }
        self.lw = lm + lb
        self.alfa1 = Lind / self.lw
        self.alfa3 = Lzag * self.n1 * self.n1 / self.lw
        self.m13 = M_ind_zag * self.n1 / self.lw
        self.Gamma0 = R0 * math.pow((self.c0 / self.lw), 0.5)
        self.Gamma1 = Rind * math.pow((self.c0 / self.lw), 0.5)
        self.Gamma3 = Rzag * self.n1 * self.n1 * math.pow((self.c0 / self.lw), 0.5)
        self.ka = 4 * ey * self.lw * self.c0 / pm / self.dh / self.dh
        self.dd = 4 * sp * self.lw * self.c0 / pm / self.dh / self.dh
        self.bb = mu0 * (self.c0 * self.U0 * self.n1 * kn) * (self.c0 * self.U0 * self.n1 * kn) / (pm * self.dh * self.h0 * self.l0 * self.l0)
        self.b1 = mu0 * self.c0 / 2.0 / self.lw * self.n1 * self.U0 * kn / l3 * self.n1 * self.U0 * kn / l3
        pstrag = h3 * 2 * sp / dz * (self.vb + (1 - self.vb) * self.q0)
        print("Давление страгивания====>(МПа)", pstrag / 1e6)
        print(self.io, self.lw, self.alfa1, self.alfa3, self.m13, self.Gamma0, self.Gamma1, self.Gamma3)
        print(self.ka, self.dd, self.bb, self.b1)
        # _________________________________________end TOPY_________________________________________________________________
        # +++++++++++++++++++++++++++++++++++++++++++++++++self.difur++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        k0 = 0.02 * math.pi * pow((1 + self.alfa1), 0.5) * pow((self.lw * self.c0), 0.5)
        print("Рекомендуемый шаг счета============>", k0 * 1e6)
        k0 = float(input("Задайте шаг счета"))
        self.NS = float(input("Задайте кратность печати"))
        self.Time_h = k0 / (math.sqrt(self.lw * self.c0) * pow(10, 6))
        self.Time_x = 0
        self.y = [0, 0, 1, 0, 0]
        self.w = [0, 0, 1, 0, 0]
        self.f = [0, 0, 1, 0, 0]
        self.k = [0, 0, 1, 0, 0]
        self.i2 = (self.y[3] * self.alfa3 - self.y[4] * self.m13) / ((1 + self.alfa1) * self.alfa3 - self.m13 * self.m13)
        self.i4 = (self.y[3] * self.m13 - self.y[4] * (1 + self.alfa1)) / ((1 + self.alfa1) * self.alfa3 - self.m13 * self.m13) * (-1.0)
        self.N_Y = 5
        print(self.Time_h)
        # +++++++++++++++++++++++++++++++++++++++++++++++++self.difur end+++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.NI = 0
        while self.io != 3:
            #print(f"io - {self.io}")
            self.rezult()
            if self.io==1: self.var1()
            else: self.var2()
            self.Ston()
            self.zub1()
            self.Time_x = self.Time_x + self.Time_h / 2.0
            self.Ston()
            self.zub2()
            self.Ston()
            self.zub3()
            self.Time_x = self.Time_x + self.Time_h / 2.0
            #print(f"Time_x - {self.Time_x} мс")
            self.Ston()
            for j in range(self.N_Y):
                self.y[j] = self.w[j] + (self.k[j] + self.Time_h * self.f[j]) / 6.0
                #print(f"j - {j}, y[j] - {self.y[j]}")
                self.w[j] = self.y[j]
            #print(f"y -{self.y}")

    def var1(self):
        ss6 = (self.vb + (1.0 - self.vb) * self.q0) * self.dd
        ss7 = self.bb * self.pc
        '''print(f"bb - {self.bb}")
        print(f"pc - {self.pc}")
        print(f"ss6 - {ss6},ss7 - {ss7}")
        print(f"разница - {ss7-ss6}")'''
        if (ss7-ss6 > 0):
            self.io = 2

        if (ss7-ss6 < 0) and (self.Time_tek * 1e6 > 100): self.io = 3
        print(f"Time_tek - {self.Time_tek},U_tek- {self.U_tek},Iind- {self.Iind}, - {self.Izag},P_tek - {self.P_tek}, {self.y[1] * 100},.y[2]- {self.y[2] * 1000}, S_tek - {self.S_tek},V_tek- {self.V_tek}")

    def var2(self):
            z1 = self.y[1]
            h_tek = self.h0 * (self.vb / math.sqrt(1.0 + self.vg * z1) + (1.0 - self.vb) / (1.0 + self.vg * z1))
            if (self.x3 == h_tek / 3.0):
                xx = self.x3 / 2.0
            else:
                xx = h_tek / 3.0
            if (self.x3 == h_tek):
                xe = self.x3
            else:
                xe = h_tek
            if (self.vb == 0):  # Короткая заготовка}
                h_zag = self.h0 / (1 + self.vg * z1)
            else:  # Длинная заготовка}
                h_zag = self.h0 / math.sqrt(1 + self.vg * z1)
                zn = self.dh * (1.0 + self.vg * z1)
                zb = zn - 2 * h_zag
                d_tek = (1.0 - self.vg) / 2.0 * (zn - 2.0 * xx) + (1.0 + self.vg) / 2.0 * (zb + 2.0 * xx)
                l_tek = self.l0 * (self.vb / math.sqrt(1.0 + self.vg * z1) + 1.0 - self.vb)
                if (self.vb == 0):  # Короткая заготовка}
                    L_zag_tek = d_tek * d_tek / l_tek * (9.9 - 3.2 * d_tek / l_tek) * 1e-7
                else:  # Длинная заготовка}
                    L_zag_tek = d_tek * d_tek / l_tek * (4.15 + 3.96 * (l_tek / d_tek - 0.32)) * 1e-7
                if (self.vg == 0):  # self.vg = 1 раздача }
                    if (l_tek / d_tek == 1):
                        fb = 5.0
                    else:
                        fb = 4.8
                        m8 = d_tek * self.di * self.di / l_tek / self.l1
                        m9 = (fb * math.sqrt(1 + (self.l1 + l_tek) * (self.l1 + l_tek) / d_tek / d_tek)
                          - 4.5 * math.sqrt(1 + (self.l1 - l_tek) * (self.l1 - l_tek) / d_tek / d_tek)) * self.n1 * 1e-7
                else:  # self.vg = -1 обжим }
                    if (self.l1 / self.di == 1):
                        fb = 5.0
                    else:
                        fb = 4.8
                        m9 = (fb * math.sqrt(1.0 + (self.l1 + l_tek) * (self.l1 + l_tek) / self.di / self.di)
                          - 4.5 * math.sqrt(1.0 + (self.l1 - l_tek) * (self.l1 - l_tek) / self.di / self.di)) * self.n1 * 1e-7
                        m8 = d_tek * d_tek * self.di / self.l1 / l_tek

                self.alfa3 = self.n1 * self.n1 * L_zag_tek / self.lw
                M_ind_zag_tek = m9 * m8
                R_zag_tek = 3.14 * self.p3 * d_tek / (l_tek*xe)
                self.m13 = M_ind_zag_tek * self.n1 / self.lw
                self.Gamma3 = R_zag_tek * math.sqrt(self.c0 / self.lw) * self.n1 * self.n1
            if (z1 == 0):
                print("&#39; Финиш !!!&#39;")
            if (self.y[1] == 0):
                self.io = 3

    def rezult(self):
        dc = self.dh - self.h0
        zaz = self.dh - 2 * self.h0 - self.dn
        self.i2 = (self.y[3] * self.alfa3 - self.y[4] * self.m13) / ((1 + self.alfa1) * self.alfa3 - self.m13 * self.m13)
        self.i4 = (self.y[3] * self.m13 - self.y[4  ] * (1 + self.alfa1)) / ((1 + self.alfa1) * self.alfa3 - self.m13 * self.m13) * (-1.0)
        self.S_tek = dc * self.y[1] * 1000
        self.pc = 0.5 * ((self.vg - 1) * (2.0 * self.i2 + self.i4) * self.i4 + (self.vg + 1) * self.i4 * self.i4) * (zaz / ((zaz + self.kappa * self.S_tek * 1000)))
        '''print(f" vg - {self.vg}, i2 - {self.i2}, i4 - {self.i4}, vg - {self.vg}, zaz - {zaz}, kappa - {self.kappa}, S.tek - {self.S_tek}")
        print(f"1 -{((self.vg - 1) * (2.0 * self.i2 + self.i4) * self.i4 + (self.vg + 1) * self.i4 * self.i4)}")
        print(f"pc -{self.pc}")'''
        self.Iind = self.i2 * self.U0 / math.sqrt(self.lw / self.c0)
        self.U_tek = self.y[2] * self.U0
        self.Izag = self.i4 * self.n1 * self.U0 / math.sqrt(self.lw / self.c0)
        self.P_tek = self.pc * self.b1
        self.Time_tek = self.Time_x * math.sqrt(self.lw * self.c0)
        self.V_tek = dc * self.y[1] / math.sqrt(self.c0 * self.lw)
        if self.poisk == 0:
            if (self.NI == self.NS):
                self.NI = 0
        self.NI = self.NI + 1

    def Ston(self):
        if (self.io == 1):
            self.f[0] = 0
            self.f[1] = 0
        elif (self.io == 3):
            self.f[0] = 0
            self.f[1] = 0
            self.y[1] = 0
        else:
            self.f[0] = self.y[1]
            ss1 = ((4.0 / 3.0 - self.vb / 3.0) * self.ka * self.vg * math.log1p(1 + self.vg * self.y[1]) / (1.0 + self.vg * self.y[1]))
            ss2 = (self.vb + (1.0 - self.vb) * self.q0) * self.dd / (1.0 + self.vg * self.y[1])
            ss3 = self.bb * self.pc * (self.vb * math.sqrt(1.0 + self.vg * self.y[1]) + (1.0 - self.vb) * (1.0 + self.vg * self.y[1]))
            self.f[1] = ss3 - ss1 - ss2
        self.f[2] = self.i2 * (-1.0)
        self.f[3] = self.y[2] - self.i2 * (self.Gamma0 + self.Gamma1)
        self.f[4] = self.Gamma3 * (-self.i4)


    def zub1(self):
        for j in range(self.N_Y):
            vk = self.Time_h * self.f[j]
            self.k[j] = vk
            self.y[j] = self.w[j] + vk / 2.0

    def zub2(self):
        for j in range(self.N_Y):
            vk = self.Time_h * self.f[j]
            self.k[j] = self.k[j] + 2.0 * vk
            self.y[j] = self.w[j] + vk / 2.0

    def zub3(self):
        for j in range(self.N_Y):
            vk = self.Time_h * self.f[j]
            self.k[j] = self.k[j] + vk * 2.0
            self.y[j] = self.w[j] + vk




