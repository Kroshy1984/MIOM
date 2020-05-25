import math


class Pascal():
    def __init__(self):

        self.defold = 0
        self.miom = 0
        self.mmm = 0
        F=True
        while F:

            self.poisk = 0
            v = 0
            kn = 0
            # mc=1
            # r2l=1
            # mm = 0
            # u1 = 1
            # self.U0 = 1
            ek = 0.02  # TODO: точтно ли такое значение дб?
            fb = 1
            self.l1 = 1
            l3 = 1
            # self.di = 1
            # self.c0 = 1
            lm = 120e-9  # * math.pow(10, -7) # Lm_у СОБСТВ. ИНДУКТИВНОСТЬ УСТАНОВКИ
            self.c0 = 254e-6  # * math.pow(10, -6) # Co_у ЕМКОСТЬ КОНДЕНСАТОРОВ УСТАНОВКИ
            self.p3 = 7.1e-8  # * math.pow(10, -8) # RO_з УДЕЛ. Э/СОПРОТИВЛЕНИЕ ЗАГОТОВКИ,
            self.mod_upr = 68e9  # * math.pow(10, 9) # E_з МОДУЛЬ УПРУГОСТИ ЗАГОТОВКИ,
            pm = 2640  # Pm_з ПЛОТНОСТЬ ЗАГОТОВКИ, ( кг/м3)
            self.l0 = 30e-3  # lo_з ДЛИНА ЗАГОТОВКИ, м
            self.dh = 151.4e-3  # Dн_з НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ, м
            self.h0 = 1.2e-3  # Ho_з ТОЛЩИНА СТЕНКИ ЗАГОТОВКИ, м
            p1 = 1.78e-8  # * math.pow(10, -8) # RO_и УДЕЛ. Э/СОПРОТИВЛЕНИЕ ИНДУКТОРА, (Ом*м)
            a = 50e-3
            b = 6e-3
            hb = 10e-3
            lv = 270e-3
            dv = 153e-3  # Dи_в ВНУТРЕННИЙ ДИАМЕТР ИНДУКТОРА , м
            self.n1 = 7  # self.n1_и ЧИСЛО ВИТКОВ ИНДУКТОРА
            self.l1 = 0.036  # self.l1_и ДЛИНА (ВЫСОТА) ИНДУКТОРА, м
            R0 = 24.0e-3  # * math.pow(10, -3) # Ro_у СОПРОТИВЛЕНИЕ УСТАНОВКИ, Ом
            self.dn = 0.169  # Dн_и НАРУЖНЫЙ ДИАМЕТР ИНДУКТОРА , м
            self.sp = 165 * math.pow(10, 6)  # SP_з ПРЕДЕЛ ТЕКУЧЕСТИ ЗАГОТОВКИ, Н/м2
            h1 = 0.008  # Hи_1 ВЫСОТА ВИТКА ИНДУКТОРА (ПО ДЛИНЕ), м
            self.ey = 700 * math.pow(10, 6)  # e'_з МОДУЛЬ УПРОЧНЕНИЯ ЗАГОТОВКИ, Н/м2
            ek = 0.03  # TODO:убрать ? это похоже на правильное значение
            eps = 0.0001  # eo_з КОНЕЧНАЯ ОТНОСИТЕЛЬНАЯ ДЕФОРМАЦИЯ ЗАГОТОВКИ - 𝑒𝜑𝑘
            H_izol = 0.0009  # Hизол_и - ТОЛЩИНА ИЗОЛЯЦИИ МЕЖДУ ВИТКАМИ, м
            H_izol = 1.33e-3  # TODO: по данным
            self.U0 = 6000  # Uo_у НАЧАЛЬНОЕ НАПРЯЖЕНИЕ УСТАНОВКИ, В
            kn = 0.32  # TODO: убрать ? во входных данных указано данное значение
            eps = 0.03  # TODO: по исходным данным
            self.kappa = 1
            self.ek = ek
            flag = 0
            mu0 = 4 * math.pi * 1e-7
            r2l = R0 * R0 / (4 * lm * lm)
            lmc = lm * self.c0
            if 1 / lmc < r2l:
                print("Разряд апериодический")
            f0 = 0.5 / math.pi * math.pow((1 / lmc - r2l), 0.5)
            over_f0 = 0.5 / (math.pi * math.pow(lmc, 0.5))
            fz = self.p3 / (math.pi * mu0 * self.h0 * self.h0)  # минимальная рабочая частота разряда, Гц
            # {для недопущения эффекта "магнитной подушки"}
            w3 = math.pow(self.mod_upr / pm, 0.5) * 2 / self.dh
            f3 = w3 / 2 / math.pi  # { собственная частота }
            #     { колебаний заготовки, Гц }
            # _____________________________________________________________________________________________________________________________
            #     { self.dh-НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
            db = self.dh - 2 * self.h0  # { db-ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ

            if v == 1:  # раздача }
                ly = self.l0 / db
            else:  # { ОБЖИМ }
                ly = self.l1 / dv
            if kn < 0.1:
                if self.poisk == 1:
                    print("L/D = ", ly)
                if ly < 1:  # TODO:внесла условие под условие kn < 0.1
                    kn = 3.783890521981891 * ly - 7.795224937947945 * ly * ly \
                         + 4.714887625113096 * math.pow(ly, 3) + 6.984777813396215 * math.pow(ly, 4) \
                         - 13.53957485592525 * math.pow(ly, 5) + 9.187983184383594 * math.pow(ly, 6) \
                         - 3.048218155556006 * math.pow(ly, 7) + 0.4929535896014099 * math.pow(ly, 8) \
                         - 3.094887626324646E-2 * math.pow(ly, 9)
                else:
                    if ly < 2:
                        kn = 0.69026 + 0.06 * ly
                    else:
                        kn = 0.7669266667 + 0.021666667 * ly
                if self.poisk == 1:  # TODO:внесла условие под условие kn < 0.1
                    print(" Фактор поля , Кн = ", kn)

            if fz < (f0 / 2):
                fp = 0.5 * f0
            if abs(fz - f0) < f0 / 2:  # TODO:раскомментировала условие
                fp = 0.8 * f0
            if fz > (1.5 * f0):
                # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных
                print(" ОБРАБОТКА НА МИУ НЕЦЕЛЕСООБРАЗНА ")


            if (self.poisk == 1) or (self.mmm == 0):
                while True:
                    kp1 = int(input("КОНТРОЛЬ ПАРАМЕТРОВ [ 1 - ДА ], [ 0 - НЕТ ] ? "))
                    # kp1 = 0
                    if kp1 in [0, 1]:
                        break
            else:
                kp1 = 0
                if ((self.poisk==1) and (self.mmm > 0)):
                    self.U0 = self.u1
                    self.prikid()
                    self.u1 = float(input("ЗАДАЙТЕ  Uo , кВ  ==> "))
                    self.u1 = self.u1 * 1000
                    self.U0 = self.u1
                if ((self.poisk==0) and (self.mmm > 0)):
                    uu0 = self.prikid()
                    self.U0 = uu0




            flag = 0
            # fp = 5201.75  # TODO:убрать
            while True:
                wq = fp * 2.0 * math.pi
                if w3 > (wq * 3):
                    ef = 0.5 * ek
                else:
                    if w3 < (wq / 3):
                        ef = 0
                    else:
                        ef = 0.25 * ek



                # ___________________________________________________________________________________________________________________
                if v == 1:  # РАЗДАЧА
                    self.vg = 1  # TODO: vg -> self.vg
                    if (self.l0 / db < 1.0):
                        l3 = self.l0  # { / sqrt(1.0 + ef)};
                        h3 = self.h0  # { / sqrt(1.0 + ef)};
                    else:
                        l3 = self.l0
                        h3 = self.h0  # { / (1.0 + ef)};
                    dz = self.dh  # {*(1.0 + ef)}; {СРЕДНИЙ НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ}
                    dm = dz - 2.0 * h3  # {СРЕДНИЙ ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ}
                    wr = (db - self.dn) / 2.0
                else:  # { ОБЖИМ }
                    self.vg = 1 * (-1)
                    if self.l0 / self.dh < 1:
                        l3 = self.l0 / math.sqrt(1 - ef)
                        h3 = self.h0 / math.sqrt(1 - ef)
                    else:
                        l3 = self.l0
                        h3 = self.h0 / (1 - ef)
                    dz = self.dh * (1 - ef)  # { СРЕДНИЙ НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
                    dm = dz - 2.0 * h3  # { СРЕДНИЙ ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ }
                    wr = (dv - self.dh) / 2.0

                self.x3 = pow((self.p3 / (math.pi * mu0 * fp)), 0.5)
                x1 = pow((p1 / (mu0 * math.pi * fp)), 0.5)
                if x1 < 2 * a / 3:
                    xb = x1
                else:
                    xb = 2 * a / 3
                z = b / (hb + xb)  # {hb - ЗАЗОР МЕЖДУ ТОКОПОДВОДАМИ }
                lb = (0.5 * self.l1 * math.log((2.0 * self.l1) / (a + b) + 0.5) +
                      (math.log((hb + xb) / (b + xb)) + (z * z - 1) * math.log(1 + z * z) / (2.0 * z * z)
                       + (2.0 / z * math.atan(z))) * lv) * pow(10, -7)
                rb = p1 * (self.l1 + 2.0 * lv) / (a * b)
                xi = 0
                # ======================================================================================================================
                if v == 0:  # { ОБЖИМ }
                    if 0.5 * x1 < h1 / 3.0:
                        xi = 0.5 * x1
                    else:
                        xi = h1 / 3.0
                    self.di = dv + 2.0 * xi
                else:  # { РАЗДАЧА }
                    self.di = self.dn - h1

                # { индуктор средний }
                Lind = 0  # TODO: добавила
                if (self.l1 / self.di < 1.0) and (self.l1 / self.di > 0.3):
                    Lind = self.di * self.di / self.l1 * (4.1 + 3.9 * (self.l1 / self.di - 0.3)) * self.n1 * self.n1 * pow(10,
                                                                                                                           -7)
                else:
                    if self.l1 / self.di > 1:  # then { индуктор длинный }
                        Lind = self.di * self.di / self.l1 * (9.9 - (3.2 * self.di) / self.l1) * self.n1 * self.n1 * pow(10, -7)
                    else:  # { индуктор короткий }
                        Lind = self.di * self.di / self.l1 * (4.1 + 3.9 * (self.l1 / self.di - 0.3)) * self.n1 * self.n1 * pow(
                            10, -7)
                if x1 <= h1:
                    xr = x1
                else:
                    xr = h1
                if self.x3 <= h3 / 3.0:
                    xz = self.x3 / 2.0
                else:
                    xz = h3 / 3.0
                if v == 1:
                    dr = dm + 2.0 * xz  # { РАЗДАЧА }
                # { dr - РАСЧЕТНЫЙ ДИАМЕТР ЗАГОТОВКИ}
                else:
                    dr = dz - 2.0 * xz  # { ОБЖИМ }
                if 1.0 > l3 / dr > 0.3:  # TODO: python упростил условие
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
                Rzag = self.p3 * math.pi * dr / (l3 * xs)  # { Rzag - АКТИВНОЕ СОПРОТИВЛЕНИЕ ЗАГОТОВКИ }
                hm = (self.l1 - H_izol * (self.n1 - 1)) * 1000 / self.n1  # { hm - ВЫСОТА ВИТКА ИНДУКТОРА }
                # ========================================================================================================================
                if hm < 0:
                    # begin
                    print("кУ-кУ !! кУ-кУ !! кУ-кУ !!")  # Требуется вывести окно
                    print(" ВЫСОТА ВИТКА ИНДУКТОРА < 0 !!")
                # Delay(3000) Задержка
                # end
                Rind = p1 * math.pi * self.di * self.n1 * self.n1 / self.l1 / xr  # { Rind - АКТИВНОЕ СОПРОТИВЛЕНИЕ ИНДУКТОРА }
                if self.l1 / self.di > 1.0:
                    Lind = self.di * self.di / self.l1 * (9.9 - 3.2 * self.di / self.l1) * self.n1 * self.n1 * pow(10, -7)
                else:
                    Lind = self.di * self.di / self.l1 * (4.1 + 3.9 * (self.l1 / self.di - 0.3)) * self.n1 * self.n1 * pow(10,
                                                                                                                           -7)

                if v + 1 == 1:  # TODO: v -> v+1
                    if self.l1 / self.di < 1.0:
                        fb = 4.8
                    else:
                        fb = 5.0
                    # TODO:кусок помещен под нужное условие
                    m9 = (fb * math.sqrt(1 + (self.l1 + l3) ** 2 / self.di ** 2)
                          - 4.5 * math.sqrt(1 + (self.l1 - l3) ** 2 / self.di ** 2)) * self.n1 * 10 ** (-7)

                    # m9 = fb * pow((1 + (self.l1 + l3) * (self.l1 + l3)) / (self.di * self.di), 0.5) \
                    #      - 4.5 * pow(((1 + (self.l1 - l3) * (self.l1 - l3) / self.di / self.di), 0.5) * (self.n1 * pow(10, -7)))
                    m8 = (dr * dr * self.di) / (self.l1 * l3)
                    M_ind_zag = m9 * m8
                    # TODO:кусок помещен под нужное условие

                if v + 1 == 2:  # TODO: v -> v+1
                    if l3 / dr < 1:
                        fb = 4.8
                    else:
                        fb = 5.0
                    # TODO:кусок помещен под нужное условие
                    m9 = (fb * math.sqrt(1 + (self.l1 + l3) ** 2 / dr ** 2)
                          - 4.5 * math.sqrt(1 + (self.l1 - l3) ** 2 / dr ** 2)) * self.n1 * 10 ** (-7)
                    # m9 = fb * pow(1 + (self.l1 + l3) * (self.l1 + l3) / dr * dr, 0.5) - 4.5 * pow(
                    #     1 + (self.l1 - l3) * (self.l1 - l3) / (dr * dr),
                    #     0.5) * self.n1 * pow(10, -7)
                    m8 = dr * self.di * self.di / (l3 * self.l1)
                    M_ind_zag = m8 * m9
                    # TODO:кусок помещен под нужное условие

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                kq = M_ind_zag / Lzag
                qq = 2.0 * 3.14 * fp * Lzag / Rzag
                k2 = qq / math.pow((1 + qq * qq), 0.5)
                lnn = Lzag * kq * kq * k2 * k2
                rn = Rzag * kq * kq * k2 * k2
                lo = Lind - lnn
                # print(Lind, lnn)
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
                if v == 0:  # then { ОБЖИМ }
                    pw = mu0 * E0 * (self.n1 * kn / l3) * (self.n1 * kn / l3) / ls
                else:  # { РАЗДАЧА }
                    pw = (mu0 * E0 * kq * kq * kn * kn) / (ls * l3 * l3)
                pq = pw * math.exp(0 - math.pi / (2.0 * q1))
                if c9 < 0:  # then
                    fq = 10
                else:
                    fq = ww / (2.0 * math.pi)
                if kp1 == 1:
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
                abt = abs(fp - fq)
                if abt > 1:
                    fp = fq
                flag = flag + 1

                if abt < 1:
                    break


            if self.poisk == 1:
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
            self.ka = 4 * self.ey * self.lw * self.c0 / pm / self.dh / self.dh
            self.dd = 4 * self.sp * self.lw * self.c0 / pm / self.dh / self.dh
            self.bb = mu0 * (self.c0 * self.U0 * self.n1 * kn) * (self.c0 * self.U0 * self.n1 * kn) / (
                    pm * self.dh * self.h0 * self.l0 * self.l0)
            self.b1 = mu0 * self.c0 / 2.0 / self.lw * self.n1 * self.U0 * kn / l3 * self.n1 * self.U0 * kn / l3
            pstrag = h3 * 2 * self.sp / dz * (self.vb + (1 - self.vb) * self.q0)
            print("Давление страгивания====>(МПа)", pstrag / 1e6)
            self.pstrag = pstrag
            # print(self.io, self.lw, self.alfa1, self.alfa3, self.m13, self.Gamma0, self.Gamma1, self.Gamma3)
            # print(self.ka, self.dd, self.bb, self.b1)
            # _________________________________________end TOPY_________________________________________________________________
            # +++++++++++++++++++++++++++++++++++++++++++++++++self.difur++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            k0 = 0.02 * math.pi * pow((1 + self.alfa1), 0.5) * pow((self.lw * self.c0), 0.5)
            print("Рекомендуемый шаг счета============>", k0 * 1e6)
            k0 = float(input("Задайте шаг счета"))
            self.NS = float(input("Задайте кратность печати"))
            self.Time_h = k0 / math.sqrt(self.lw * self.c0) / pow(10, 6)  # TODO: убрала неправильные скобки
            self.Time_x = 0
            self.NI = 0
            self.y = [0, 0, 1, 0, 0]
            self.w = [0, 0, 1, 0, 0]
            self.f = [0, 0, 1, 0, 0]
            self.k = [0, 0, 1, 0, 0]
            self.k0 = k0
            self.N_Y = 5
            print("Time_h=", self.Time_h)
            print("vb=", self.vb, "q0=", self.q0, "dd=", self.dd, "bb=", self.bb)
            # инициализация доп переменных
            self.i2 = 0
            self.i4 = 0
            self.S_tek = 0
            self.pc = 0
            self.Iind = 0
            self.U_tek = 0
            self.Izag = 0
            self.P_tek = 0
            self.Time_tek = 0
            self.V_tek = 0
            self.SSS_tek = 0
            self.Sig_tek = 0
            # инициализация доп переменных
            # +++++++++++++++++++++++++++++++++++++++++++++++++self.difur end+++++++++++++++++++++++++++++++++++++++++++++++++++++++
            self.NI = 0
            self.Y3 = []
            self.Time = []
            self.Y0 = []
            self.Y1 = []
            self.Y2 = []
            self.Y4 = []
            self.F0 = []
            self.F1 = []
            self.F2 = []
            self.F3 = []
            self.F4 = []
            self.W0 = []
            self.W1 = []
            self.W2 = []
            self.W3 = []
            self.W4 = []
            self.SS1 = []
            self.SS2 = []
            self.SS3 = []
            self.SS6 = []
            self.SS7 = []
            while True:

                self.rezult()
                # chance
                self.var1()
                if self.io == 2:
                    self.var2()

                # chance
                # if self.io == 1:
                #     self.var1()
                # elif self.io == 2:
                #     # self.var1()
                #     self.var2()
                # else:
                #     self.var1()
                # dolay
                self.Ston()
                self.zub1()
                self.Time_x = self.Time_x + self.Time_h / 2.0
                self.Ston()
                self.zub2()
                self.Ston()
                self.zub3()
                self.Time_x = self.Time_x + self.Time_h / 2.0
                self.Ston()
                for j in range(self.N_Y):
                    self.y[j] = self.w[j] + (self.k[j] + self.Time_h * self.f[j]) / 6.0
                    self.w[j] = self.y[j]
                if self.io == 3:
                    print("Заготовка остановилась")
                    print("&#39; Финиш !!!&#39;")
                    break
                # dolay
                self.Time.append(self.Time_tek)
                self.Y0.append(self.y[0])
                self.Y1.append(self.y[1])
                self.Y2.append(self.y[2])
                self.Y3.append(self.y[3])
                self.Y4.append(self.y[4])
                self.F0.append(self.f[0])
                self.F1.append(self.f[1])
                self.F2.append(self.f[2])
                self.F3.append(self.f[3])
                self.F4.append(self.f[4])
                self.W0.append(self.w[0])
                self.W1.append(self.w[1])
                self.W2.append(self.w[2])
                self.W3.append(self.w[3])
                self.W4.append(self.w[4])
                if self.io!=2:
                    self.SS1.append(0)
                    self.SS2.append(0)
                    self.SS3.append(0)
                else:
                    self.SS1.append(self.ss1)
                    self.SS2.append(self.ss2)
                    self.SS3.append(self.ss3)
                self.SS6.append(self.ss6)
                self.SS7.append(self.ss7)

            self.mmm = self.mmm + 1
            print("""Считается  вариант - {0:3} 
                        Задана   деформация, %  - {1:15.7f}
                        Получена    деформация, %  - {2:15.7f}
                        ПОГРЕШНОСТЬ, %  - {3:15.7f}
                        при  [ кВ ]      Uo  = {4:15.7f}""".format(self.mmm, self.ek * 100, self.y[0] * 100,
                                                                   abs(self.y[0] - self.ek) * 100, self.U0 / 1000))
            if abs(self.y[0] - self.ek)*100 < eps:
                self.miom = 1
            else:
                if self.poisk == 1:
                    self.miom = int(input("Будем уточнять  Uo ( 1 - Нет, 0 - Да) ==> "))

            self.u1 = self.U0
            if self.miom == 1:
                break
            print(f"Time_tek - {int(self.Time_tek * pow(10, 6))},U_tek- {self.U_tek},Iind- {self.Iind},Izag - {self.Izag},P_tek - {self.P_tek}, {self.y[1] * 100},.y[2]- {self.y[2] * 1000}, S_tek - {self.S_tek},V_tek- {self.V_tek}")
            f=input("Продолжить - Y/N")
            if f=="y":F=True
            else:F=False

    def Y0(self):
        return self.Y0
    def Y1(self):
        return self.Y1
    def Y3(self):
        return self.Y3
    def Y2(self):
        return self.Y2
    def Y4(self):
        return self.Y4
    def F0(self):
        return self.F0
    def F1(self):
        return self.F1
    def F3(self):
        return self.F3
    def F2(self):
        return self.F2
    def F4(self):
        return self.F4
    def W0(self):
        return self.W0
    def W1(self):
        return self.W1
    def W3(self):
        return self.W3
    def W2(self):
        return self.W2
    def W4(self):
        return self.W4
    def SS1(self):
        return self.SS1
    def SS2(self):
        return self.SS2
    def SS3(self):
        return self.SS3
    def SS6(self):
        return self.SS6
    def SS7(self):
        return self.SS7


    def Time(self):
        return self.Time

    def var1(self):
        self.ss6 = (self.vb + (1.0 - self.vb) * self.q0) * self.dd
        self.ss7 = self.bb * self.pc
        if (self.ss7 - self.ss6) > 0:
            self.io = 2
            dr = math.modf(round(self.Time_tek * 10 ** 6, 2) / self.NS)
            if dr[0] < 1e-6:
                print("заготовка движется")
        if ((self.ss7 - self.ss6) < 0) and ((self.Time_tek * 1e6) > 100):
            self.io = 3
            # print("заготовка остановилась")
            # print("&#39; Финиш !!!&#39;")

    def var2(self):
        # z1 = self.y[1]  # TODO: проверить соотношение индексации (массивы в Pascal нумеруются с 1)
        z1 = self.y[0]  # TODO: проверить соотношение индексации (массивы в Pascal нумеруются с 1)
        h_tek = self.h0 * (self.vb / math.sqrt(1.0 + self.vg * z1) + (1.0 - self.vb) / (1.0 + self.vg * z1))
        if self.x3 <= (h_tek / 3.0):  # TODO:(x3 == h_tek/3.0) -> (x3 <= h_tek/3.0)
            xx = self.x3 / 2.0
        else:
            xx = h_tek / 3.0
        if self.x3 <= h_tek:  # TODO:(self.x3 == h_tek) -> (self.x3 <= h_tek)
            xe = self.x3
        else:
            xe = h_tek

        if self.vb == 0:  # Короткая заготовка}
            h_zag = self.h0 / (1 + self.vg * z1)
        else:  # Длинная заготовка}
            h_zag = self.h0 / math.sqrt(1 + self.vg * z1)
        # TODO: все последующие операторы были выведены из блока else
        zn = self.dh * (1.0 + self.vg * z1)
        zb = zn - 2 * h_zag
        d_tek = (1.0 - self.vg) / 2.0 * (zn - 2.0 * xx) + (1.0 + self.vg) / 2.0 * (zb + 2.0 * xx)
        l_tek = self.l0 * (self.vb / math.sqrt(1.0 + self.vg * z1) + 1.0 - self.vb)

        if self.vb == 0:  # Короткая заготовка}
            L_zag_tek = d_tek * d_tek / l_tek * (9.9 - 3.2 * d_tek / l_tek) * 1e-7
        else:  # Длинная заготовка}
            L_zag_tek = d_tek * d_tek / l_tek * (4.15 + 3.96 * (l_tek / d_tek - 0.32)) * 1e-7

        if self.vg > 0:  # self.vg = 1 раздача } # TODO: (self.vg == 0) -> (self.vg > 0)
            if (l_tek / d_tek) > 1:  # TODO: (l_tek / d_tek == 1) ->(l_tek / d_tek) > 1
                fb = 5.0
            else:
                fb = 4.8
            # TODO: все последующие операторы были выведены из блока else
            # TODO: проверила расчет m8 и m9
            m8 = d_tek * self.di * self.di / l_tek / self.l1
            # m9 = (fb * math.sqrt(1 + (self.l1 + l_tek) * (self.l1 + l_tek) / d_tek / d_tek)
            #       - 4.5 * math.sqrt(1 + (self.l1 - l_tek) * (self.l1 - l_tek) / d_tek / d_tek)) * self.n1 * 1e-7
            m9 = (fb * math.sqrt(1.0 + (self.l1 + l_tek) ** 2 / d_tek ** 2)
                  - 4.5 * math.sqrt(1.0 + (self.l1 - l_tek) ** 2 / d_tek ** 2)) * self.n1 * 10 ** (-7)
            # TODO: все последующие операторы были выведены из блока else
        else:  # self.vg = -1 обжим }
            if (self.l1 / self.di) > 1:
                fb = 5.0
            else:
                fb = 4.8
            # TODO: все последующие операторы были выведены из блока else
            # TODO: проверила расчет m8 и m9
            m9 = (fb * math.sqrt(1.0 + (self.l1 + l_tek) ** 2 / self.di ** 2)
                  - 4.5 * math.sqrt(1.0 + (self.l1 - l_tek) ** 2 / self.di ** 2)) * self.n1 * 10 ** (-7)

            # m9 = (fb * math.sqrt(1.0 + (self.l1 + l_tek) * (self.l1 + l_tek) / self.di / self.di)
            #       - 4.5 * math.sqrt(
            #             1.0 + (self.l1 - l_tek) * (self.l1 - l_tek) / self.di / self.di)) * self.n1 * 1e-7
            m8 = d_tek * d_tek * self.di / self.l1 / l_tek
            # TODO: все последующие операторы были выведены из блока else

        M_ind_zag_tek = m9 * m8
        self.alfa3 = self.n1 * self.n1 * L_zag_tek / self.lw
        R_zag_tek = math.pi * self.p3 * d_tek / (l_tek * xe)
        self.m13 = M_ind_zag_tek * self.n1 / self.lw
        self.Gamma3 = R_zag_tek * math.sqrt(self.c0 / self.lw) * self.n1 * self.n1
        # if (z1 == 0):  # TODO : (z1 == 0) -> z1 <= 0
        #     print("&#39; Финиш !!!&#39;")
        if self.y[1] < 0:  # TODO :  (self.y[1] == 0)->
            self.io = 3

    def rezult(self):
        dc = self.dh - self.h0
        zaz = self.dh - 2 * self.h0 - self.dn
        self.i2 = (self.y[3] * self.alfa3 - self.y[4] * self.m13) / \
                  ((1 + self.alfa1) * self.alfa3 - self.m13 * self.m13)
        self.i4 = (self.y[3] * self.m13 - self.y[4] * (1 + self.alfa1)) / (
                (1 + self.alfa1) * self.alfa3 - self.m13 * self.m13) * (-1.0)
        self.S_tek = dc * self.y[0] * 1000
        self.pc = 0.5 * ((self.vg - 1) * (2.0 * self.i2 + self.i4) * self.i4 + (self.vg + 1) * self.i4 ** 2) * \
                  (zaz / (zaz + self.kappa * self.S_tek / 1000))
        self.Iind = self.i2 * self.U0 / math.sqrt(self.lw / self.c0)
        self.U_tek = self.y[2] * self.U0
        self.Izag = self.i4 * self.n1 * self.U0 / math.sqrt(self.lw / self.c0)
        self.P_tek = self.pc * self.b1
        self.Time_tek = self.Time_x * math.sqrt(self.lw * self.c0)
        self.V_tek = dc * self.y[1] / math.sqrt(self.c0 * self.lw)
        self.SSS_tek = self.y[0] * self.mod_upr
        if self.SSS_tek > self.sp:
            self.Sig_tek = self.sp + self.y[0] * self.ey
        else:
            self.Sig_tek = self.SSS_tek
        if self.poisk == 0:
            if (self.NI == self.NS):
                self.NI = 0
        self.NI = self.NI + 1
        dr = math.modf(round(self.Time_tek * 10**6, 2) / self.NS)
        if dr[0] < 1e-6:
        # if ((self.NI * self.k0) % self.NS) == 0:
            print("{0:>6}|{1:>8}|{2:>10}|{3:>10}|{4:>7}|{5:>7}|{6:>6}|{7:>8}|{8:>8}".format(
                "Time", "U_tek", "Iind", "Izag", "P_tek", "y[0]", "y[1]", "S_tek", "V_tek"))
            print("{0:>6.2f}|{1:>8.0f}|{2:>10.0f}|{3:>10.0f}|{4:>7.2f}|{5:>7.3f}|{6:>6.3f}|{7:>8.3f}|{8:>8.2f}".format(
                self.Time_tek * pow(10, 6), self.U_tek, self.Iind, self.Izag, self.P_tek / 10 ** 6,
                                                                                   self.y[0] * 100, self.y[1] * 1000,
                self.S_tek, self.V_tek))

    def Ston(self):
        if self.io == 1:
            self.f[0] = 0
            self.f[1] = 0
        elif self.io == 3:
            self.f[0] = 0
            self.f[1] = 0
            self.y[1] = 0
        else:
            # TODO: проверила формулы
            self.f[0] = self.y[1]
            # self.ss1 = (4.0 / 3.0 - self.vb / 3.0) * self.ka * self.vg * \
            #       math.log1p(1 + self.vg * self.y[0]) / (1.0 + self.vg * self.y[0])
            self.ss1 = (4.0 / 3.0 - self.vb / 3.0) * self.ka * self.vg * \
                  math.log(1 + self.vg * self.y[0]) / (1.0 + self.vg * self.y[0])
            self.ss2 = (self.vb + (1.0 - self.vb) * self.q0) * self.dd / (1.0 + self.vg * self.y[0])
            self.ss3 = self.bb * self.pc * (
                    self.vb * math.sqrt(1.0 + self.vg * self.y[0]) + (1.0 - self.vb) * (1.0 + self.vg * self.y[0]))
            self.f[1] = self.ss3 - self.ss1 - self.ss2
            # TODO: проверила формулы
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

    def prikid(self):
        def1 = self.y[0]
        zoloto = (math.sqrt(5) - 1) / 2.0
        defold = def1
        if def1 < self.ek:
            def1 = defold + zoloto * abs(defold - self.ek)
        else:
            def1 = self.ek + (1 - zoloto) * abs(defold - self.ek)
        drob = (def1 + self.ek) / self.ek / 2.0
        if (defold - self.ek) > 0:
            if drob < 1:
                uu0 = self.u1 * drob
            else:
                uu0 = self.u1 / drob
        else:
            if drob < 1:
                uu0 = self.u1 / drob
            else:
                uu0 = self.u1 * drob
        if (defold / self.ek) < 0.01:
            uu0 = 2 * self.u1 / drob
        print("Предлагаемое значение [кВ]  Uo = ", uu0 / 1000)

        return uu0