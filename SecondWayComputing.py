import math

def topy(poisk,pro,R0,lm,c0, h0,p3,mod_upr,pm,dh,l0,v,l1,dv,kn,mm):
    if poisk==1:  # ручной поиск
        print("***"+ pro+ "***")  # pro это либо обжим или раздача
        flag = 0
        mu0 = 4 * math.pi * 1e-7
        r2l = R0 * R0 / 4 / lm / lm
        lmc = lm * c0
    if 1 / lmc < r2l:
        print("*** РАЗРЯД АПЕРИОДИЧЕСКИЙ ***")  # вместо данной операции необходимо вызвать окно с этой надписью и выходом в главное мен
        f0 = 0.5 / math.pi * math.pow((1 / lmc - r2l), 0.5)
        over_f0 = 0.5 / math.pi * math.pow(lmc, 0.5)
        fz = p3 / math.pi / mu0 / h0 / h0  # минимальная рабочая частота разряда, Гц
        # {для недопущения эффекта "магнитной подушки"}
        w3 = math.pow(mod_upr / pm, 0.5) * 2 / dh
        f3 = w3 / 2 / math.pi  # { собственная частота }
    #     { колебаний заготовки, Гц }
    # _____________________________________________________________________________________________________________________________
    #     { dh-НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
        db = dh - 2 * h0  # { db-ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ
        if v == 1:  # раздача }
            ly = l0 / db

    else:  # { ОБЖИМ }
        ly = l1 / dv
        if kn < 0.1:
            if poisk==1:
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
    if poisk==1:
        print(" Фактор поля , Кн = ",kn)
        if fz < f0 / 2:
            fp = 0.5 * f0
        if abs(fz - f0) < f0 / 2:
            fp = 0.8 * f0
        if fz > 1.5 * f0:
            print(" ОБРАБОТКА НА МИУ НЕЦЕЛЕСООБРАЗНА ")  # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных
        if poisk==1 or mm==0:  # {miom=0}

{2}
print(' КОНТРОЛЬ ПАРАМЕТРОВ [ 1 - ДА ], [ 0 - НЕТ ] ? ')  # необходимо вывести окно с данным вопросом
kp1=input()  # { gotoxy(1,1)} Until{2}((kp1=1) or (kp1=0))

    else:
        kp1 = 0
        if poisk==1 and mm > 0:
            U0 = u1
# print prikid
# print
# print(' Uo , кВ = ',u0/1000:12:5) выести окно с расчитанным U0 из процедуры Prikid с корректировкой U0
# print
# print print (' ЗАДАЙТЕ Uo , кВ ==> ') ReadLn(U1)
    u1 = u1 * 1000
    U0 = u1
    if poisk==0 and mmm > 0:
        prikid()

U0 = uu0

# {1} Repeat {начало}
    wq = fp * 2.0 * math.pi
    if w3 > wq * 3:
        ef = 0.5 * ek
    else:
    if w3 < wq / 3:
        ef = 0
    else:
        ef = 0.25 * ek
    if v == 1:
        vg = 1
    if l0 / db < 1.0:
        l3 = l0  # {/sqrt(1.0+ef)}
        h3 = h0  # {/sqrt(1.0+ef)}
    else:
        l3 = l0
    h3 = h0  # {/(1.0+ef)}
    dz = dh
#{*(1.0 + ef)}  # { СРЕДНИЙ НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
    dm = dz - 2.0 * h3  # { СРЕДНИЙ ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ }
    wr = (db - dn) / 2.0
    else:  # РАЗДАЧА
# { ОБЖИМ }
        vg = 1 * (-1)
    if l0 / dh < 1:
        l3 = l0 / math.pow((1 - ef), 0.5)
        h3 = h0 / sqrt(1 - ef)
    else:
        l3 = l0
        h3 = h0 / (1 - ef)
        dz = dh * (1 - ef)  # { СРЕДНИЙ НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
        dm = dz - 2.0 * h3  # { СРЕДНИЙ ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ }
        wr = (dv - dh) / 2.0

        x3 = math.pow((p3 / math.pi / mu0 / fp), 0.5)
        x1 = math.pow((p1 / mu0 / math.pi / fp), 0.5)
    if x1 < 2 * a / 3:
        xb = x1
    else:
        xb = 2 * a / 3
        z = b / (hb + xb)  # {hb - ЗАЗОР МЕЖДУ ТОКОПОДВОДАМИ }
        lb = (0.5 * l1 * math.log((2.0 * l1) / (a + b) + 0.5) + (
                math.log((hb + xb) / (b + xb)) + (z * z - 1) * math.log(1 + z * z) / (2.0 * z * z) + (
                    2.0 / z * ArcTan(z))) * lv) * 1e-7
    rb = p1 * (l1 + 2.0 * lv) / (a * b)
    xi = 0
    if v == 0:
# begin { ОБЖИМ }
    if 0.5 * x1 < h1 / 3.0:
        xi = 0.5 * x1
    else:
        xi = h1 / 3.0
        di = dv + 2.0 * xi
    else:  # обжим
        di = dn - h1  # { РАЗДАЧА }
# {Если .... }
# { индуктор средний }
    if l1 / di < 1.0 and l1 / di > 0.3:
        Lind = di * di / l1 * (4.1 + 3.9 * (l1 / di - 0.3)) * n1 * n1 * 1e-7
        else:
    if l1 / di > 1:  # then { индуктор длинный }
        Lind = di * di / l1 * (9.9 - (3.2 * di) / l1) * n1 * n1 * 1e-7
    else:  # { индуктор короткий }
        Lind = di * di / l1 * (4.1 + 3.9 * (l1 / di - 0.3)) * n1 * n1 * 1e-7
    if x1 <= h1:
        xr = x1
    else:
        xr = h1
    if 3 <= h3 / 3.0:
        xz = x3 / 2.0
    else:
        xz = h3 / 3.0
    if v == 1:
        dr = dm + 2.0 * xz  # { РАЗДАЧА }
# { dr - РАСЧЕТНЫЙ ДИАМЕТР ЗАГОТОВКИ}
    else:
        dr = dz - 2.0 * xz  # { ОБЖИМ }
    if l3 / dr < 1.0 and l3 / dr > 0.3:
        vb = 1
        q0 = 2.0 / math.pow(3.0, 0.5)
    # { заготовка средняя }
    Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * 1e-7
    else:  # { begin else }
        vb = 0
        q0 = 1
    if l3 / dr > 1.0:  # then { заготовка длинная }
        Lzag = dr * dr / l3 * (9.9 - 3.2 * dr / l3) * 1e-7
    else:
        print("... Обработка на МИУ нецелесообразна...")  # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных
    # Delay(3000) Задержка
    vb = 1
    q0 = 2.0 / math.pow(3.0, 0.5)
# { заготовка короткая }
    Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * 1e-7
# end
# end { end else }
    if x3 < h3:
        xs = x3
    else:
        xs = h3
        Rzag = p3 * math.pi * dr / (l3 * xs)  # { Rzag - АКТИВНОЕ СОПРОТИВЛЕНИЕ ЗАГОТОВКИ }
        hm = (l1 - H_izol * (n1 - 1)) * 1000 / n1  # { hm - ВЫСОТА ВИТКА ИНДУКТОРА }
    if hm < 0:
# begin
# print(' кУ-кУ !! кУ-кУ !! кУ-кУ !!') Требуется вывести окно
# print(' ВЫСОТА ВИТКА ИНДУКТОРА < 0 !! ')
# Delay(3000) Задержка
# end
        Rind = p1 * math.pi * di * n1 * n1 / l1 / xr  # { Rind - АКТИВНОЕ СОПРОТИВЛЕНИЕ ИНДУКТОРА }
    if l1 / di > 1.0:
        Lind = di * di / l1 * (9.9 - 3.2 * di / l1) * n1 * n1 * 1e-7
    else:
        Lind = di * di / l1 * (4.1 + 3.9 * (l1 / di - 0.3)) * n1 * n1 * 1e-7
# Case v+1 Выбор оператора
# 1:begin { ОБЖИМ }
    if l1 / di < 1.0:
        fb = 4.8
    else:
        fb = 5.0
        m9 = fb * math.pow((1 + (l1 + l3) * (l1 + l3) / di / di), 0.5) - 4.5 * math.pow(
        (1 + (l1 - l3) * (l1 - l3) / di / di), 0.5) * n1 * 1e-7)
        m8 = dr * dr * di / (l1 * l3)
        M_ind_zag = m9 * m8
    # end
    # 2:begin { РАЗДАЧА }
    if l3 / dr < 1: fb = 4.8
    else:
        fb = 5.0
        m9 = fb * math.pow((1 + (l1 + l3) * (l1 + l3) / dr / dr), 0.5) - 4.5 * math.pow(
        (1 + (l1 - l3) * (l1 - l3) / dr / dr), 0.5) * n1 * 1e-7)
        m8 = dr * di * di / (l3 * l1)
        M_ind_zag = m8 * m9
    # End{case}
        kq = M_ind_zag / Lzag
        qq = 2.0 * math.pi * fp * Lzag / Rzag
        k2 = qq / math.pow((1 + qq * qq), 0.5)
        lnn = Lzag * kq * kq * k2 * k2
        rn = Rzag * kq * kq * k2 * k2
        lo = Lind - lnn
        ro = Rind + rn
        ls = lm + lb + lo
        rs = R0 + rb + ro
        s1 = rs / (2.0 * ls)
        ww = math.pow((abs(1.0 / (c0 * ls) - s1 * s1)), 0.5)
        c9 = (1.0 / (c0 * ls) - s1 * s1)
    if c9 < 0 and flag > 1:
        print("Ку ку разряд апериодический")  # then
    # begin
    # print(' кУ-кУ !! кУ-кУ !! кУ-кУ !!')
    # print(' Разряд апериодический !! ')
    # Delay(5000)
    # Halt(1)
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
        E0 = 0.5 * c0 * U0 * U0
    if (v == 0):  # then { ОБЖИМ }
        pw = mu0 * E0 * (n1 * kn / l3) * (n1 * kn / l3) / ls
    else:
    # { РАЗДАЧА }
        pw = (mu0 * E0 * kq * kq * kn * kn) / (ls * l3 * l3)
        pq = pw * exp(0 - Pi / (2.0 * q1))
    if c9 < 0:  # then
        fq = 10
    else:
        fq = ww / 2.0 / math.pi
    if kp1 == 1:
        print("радиальная ширина витка индуктора, мм < "+str(5000*x1))
        print(" Fo= "+str(f0)+ "Fz="+ str(fz)+"Fp= "+ str(fp)+ "f3= "+str(f3))
        print('│ h3='+str(h3 * 1e3)+ ' l3='+ str(l3 * 1e3: 10:2)+' vg='+str(vg: 2)+ ' │ ')
        print('│ dz=', dz * 1e3: 10:2, ' ef%=', ef * 100: 9:2, ' wr=', wr * 1e3: 10:2, ' db=', db * 1e3: 10:2, '│')
        print('│ dm=', dm * 1e3: 10:2, ' x3=', x3 * 1e3: 10:2, ' x1=', x1 * 1e3: 10:2, ' xb=', xb * 1e3: 10:2, '│')
        print('│ z=', z: 10, 'Lтп=', lb: 10, ' xi=', xi * 1e3: 10:2, ' di=', di * 1e3: 10:2, '│ ')
        print('│ Li=', Lind: 10, ' xr=', xr * 1e3: 10:2, ' Ri=', Rind: 10, ' xz=', xz * 1e3: 10:2, '│ ')
        print('│ dr=', dr * 1e3: 10:2, ' Lz=', Lzag: 10, ' xs=', xs * 1e3: 10:2, ' Rz=', Rzag: 10, '│ ')
        print('│ Ms=', M_ind_zag: 10, ' k=', kq: 10, ' qq=', qq: 10, ' k2=', k2: 10, '│ ')
        print('│ Ln=', lnn: 10, ' Rn=', rn: 10, ' Lo=', lo: 10, ' Ro=', ro: 10, '│ ')
        print('│ Ls=', ls: 10, ' Rs=', rs: 10, ' s1=', s1: 10, ' ww=', ww: 10, '│ ')
        print('│ q3=', q3: 10, ' q1=', q1: 10, ' Kн=', kn: 10, ' f1=', f1: 10, '│ ')
        print('│ s3=', s3: 10, ' k3=', k3: 10, ' Eo=', E0: 10:2, ' Pw=', pw / 1e6: 10:2, '│')
        print('│Rтп=', rb: 10, ' n1=', n1: 10, ' Uo=', U0: 10:2, ' Pmax=', pq / 1e6: 8:2, '│')
        print('│ H_вит= ', hm: 10:2, ' Fr0= ', over_f0: 10:2, ' │ ')
        print('fq = ', fq: 10:2)
    # Repeat{3}
        print(' Для продолжения ===> Жми на <Enter> >>')
        klav = ReadKey
        q0q = Ord(klav)
        gotoxy(1, 1)
    Until
    {3}(q0q=13)
    end
    {end if (kp1 = 1)}
    abt = abs(fp - fq)
    if (abt > 1): fp = fq
        flag = flag + 1
    Until{1} (abt < 1) {конец}
    if poisk = 1 then
    begin
        print(brus, ' Контроль текущих параметров')
        print(brus, '')
        print(brus, ' радиальная ширина витка индуктора, мм < ', 5000 * x1:6: 3)
        print(brus, '┌────────────────────────────────────────────────────────┐')
        print(brus, '│ Fo=', f0: 10:2, ' Fz=', fz: 10:2, ' Fp=', fp: 10:2, ' f3=', f3: 10:2, '│ ')
        print(brus, '│ h3=', h3 * 1e3: 10:2, ' l3=', l3 * 1e3: 10:2, ' vg=', vg: 2, ' │')
        print(brus, '│ dz=', dz * 1e3: 10:2, ' ef%=', ef * 100: 9:2, ' wr=', wr * 1e3: 10:2, ' db=', db * 1e3: 10:2, '│')
        print(brus, '│ dm=', dm * 1e3: 10:2, ' x3=', x3 * 1e3: 10:2, ' x1=', x1 * 1e3: 10:2, ' xb=', xb * 1e3: 10:2, '│')
        print(brus, '│ z=', z: 10, 'Lтп=', lb: 10, ' xi=', xi * 1e3: 10:2, ' di=', di * 1e3: 10:2, '│')
        print(brus, '│ Li=', Lind: 10, ' xr=', xr * 1e3: 10:2, ' Ri=', Rind: 10, ' xz=', xz * 1e3: 10:2, '│')
        print(brus, '│ dr=', dr * 1e3: 10:2, ' Lz=', Lzag: 10, ' xs=', xs * 1e3: 10:2, ' Rz=', Rzag: 10, '│')
        print(brus, '│ Ms=', M_ind_zag: 10, ' k=', kq: 10, ' qq=', qq: 10, ' k2=', k2: 10, '│ ')
        print(brus, '│ Ln=', lnn: 10, ' Rn=', rn: 10, ' Lo=', lo: 10, ' Ro=', ro: 10, '│ ')
        print(brus, '│ Ls=', ls: 10, ' Rs=', rs: 10, ' s1=', s1: 10, ' ww=', ww:
            10, '│ ')
        print(brus, '│ q3=', q3: 10, ' q1=', q1: 10, ' Kн=', kn: 10, ' f1=', f1: 10, '│ ')
        print(brus, '│ s3=', s3: 10, ' k3=', k3: 10, ' Eo=', E0: 10:2, ' Pw=', pw / 1e6: 10:2, '│')
        print(brus, '│Rтп=', rb: 10, ' n1=', n1: 10, ' Uo=', U0: 10:2, ' Pmax=', pq / 1e6: 8:2, '│')
        print(brus, '│ H_вит= ', hm: 10:2, ' Fr0= ', over_f0: 10:2, ' │')
        print(brus, '└────────────────────────────────────────────────────────┘')
        print(brus, '')

        io = 1  # { МИОМ(Э) , c. 79 }
        lw = lm + lb
        alfa1 = Lind / lw
        alfa3 = Lzag * n1 * n1 / lw
        m13 = M_ind_zag * n1 / lw
        Gamma0 = R0 * math.pow((c0 / lw), 0.5)
        Gamma1 = Rind * math.pow((c0 / lw), 0.5)
        Gamma3 = Rzag * n1 * n1 * math.pow((c0 / lw), 0.5)
        ka = 4 * ey * lw * c0 / pm / dh / dh
        dd = 4 * sp * lw * c0 / pm / dh / dh
        bb = mu0 * (c0 * U0 * n1 * kn) * (c0 * U0 * n1 * kn) / (pm * dh * h0 * l0 * l0)
        b1 = mu0 * c0 / 2.0 / lw * n1 * U0 * kn / l3 * n1 * U0 * kn / l3


