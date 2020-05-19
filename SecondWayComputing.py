import math
#def main1
poisk = 1
v = 0
kn = 0
#mc=1
#r2l=1
mm = 0
u1 = 1
mmm = 0
uu0 = 1
ek = 0.02
fb = 1
l1 = 1
l3 = 1
di = 1
#c0 = 1
lm = 1.2 * math.pow(10, -7) #Lm_у СОБСТВ. ИНДУКТИВНОСТЬ УСТАНОВКИ
c0 = 254*math.pow(10, -6)#Co_у ЕМКОСТЬ КОНДЕНСАТОРОВ УСТАНОВКИ
p3 = 7.1*math.pow(10, -8)#RO_з УДЕЛ. Э/СОПРОТИВЛЕНИЕ ЗАГОТОВКИ,
mod_upr = 68*math.pow(10, 9)#E_з МОДУЛЬ УПРУГОСТИ ЗАГОТОВКИ,
pm = 2640 # Pm_з ПЛОТНОСТЬ ЗАГОТОВКИ, ( кг/м3)
l0 = 0.030 # lo_з ДЛИНА ЗАГОТОВКИ, м
dh = 0.1514 # Dн_з НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ, м
h0 = 0.0012 # Ho_з ТОЛЩИНА СТЕНКИ ЗАГОТОВКИ, м
p1 = 1.78*math.pow(10, -8) #RO_и УДЕЛ. Э/СОПРОТИВЛЕНИЕ ИНДУКТОРА, (Ом*м)
a = 0.004
b = 0.008
hb = 0.005
lv = 0.150
dv = 0.153 #Dи_в ВНУТРЕННИЙ ДИАМЕТР ИНДУКТОРА , м
n1 = 7 #N1_и ЧИСЛО ВИТКОВ ИНДУКТОРА
l1 = 0.036 #l1_и ДЛИНА (ВЫСОТА) ИНДУКТОРА, м
R0 = 4.25*math.pow(10, -3) #Ro_у СОПРОТИВЛЕНИЕ УСТАНОВКИ, Ом
dn = 0.169 #Dн_и НАРУЖНЫЙ ДИАМЕТР ИНДУКТОРА , м
sp = 700*math.pow(10, 6) #SP_з ПРЕДЕЛ ТЕКУЧЕСТИ ЗАГОТОВКИ, Н/м2
h1 = 0.004 # Hи_1 ВЫСОТА ВИТКА ИНДУКТОРА (ПО ДЛИНЕ), м
ey = 700 *math.pow(10, 6) #e'_з МОДУЛЬ УПРОЧНЕНИЯ ЗАГОТОВКИ, Н/м2
eps = 0.0001 #eo_з КОНЕЧНАЯ ОТНОСИТЕЛЬНАЯ ДЕФОРМАЦИЯ ЗАГОТОВКИ - 𝑒𝜑𝑘
H_izol = 0.0009#Hизол_и - ТОЛЩИНА ИЗОЛЯЦИИ МЕЖДУ ВИТКАМИ, м
U0 = 7000 #Uo_у НАЧАЛЬНОЕ НАПРЯЖЕНИЕ УСТАНОВКИ, В
kappa = 1


flag=0
mu0=4*math.pi*1e-7
r2l = R0*R0/4/lm/lm
lmc = lm*c0
if 1/lmc<r2l:
    print("Разряд апериодический")
f0 = 0.5 / (3.14 * math.pow((1 / lmc - r2l), 0.5))
over_f0 = 0.5 / (3.14 * math.pow(lmc, 0.5))
fz = p3 / (3.14 * mu0 * h0 * h0)  # минимальная рабочая частота разряда, Гц
# {для недопущения эффекта "магнитной подушки"}
w3 = math.pow(mod_upr / pm, 0.5) * 2 / dh
f3 = w3 / 2 / 3.14  # { собственная частота }
    #     { колебаний заготовки, Гц }
    # _____________________________________________________________________________________________________________________________
    #     { dh-НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
db = dh - 2 * h0  # { db-ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ

"""def Prikids(y,ek,u1):
        ZOLOTO = (pow(5, 0.5)-1)/2
        def1 = y
        defold = def1
        if def1 < ek: def1 = defold + ZOLOTO*abs(defold-ek)
        else: def1 = ek + (1-ZOLOTO)*abs(defold-ek)
        drob = (def1 + ek) / ek/2
        if defold-ek > 0:
            if drob < 1:
             uu0 = u1 * drob
            else: uu0 = u1 / drob
        else:
            if drob < 1: uu0 = u1 / drob
            else: uu0 = u1 * drob
        if (defold/ek) < 0.01:
            uu0 = 2 * u1 / drob
        print("Предлагаемое значение [кВ] Uo = "+str(uu0)+" кВ")"""

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
    print(" Фактор поля , Кн = ", kn)
if fz < (f0/2):
    fp = 0.5 * f0
else: #if abs(fz - f0) < f0 / 2:
    fp = 0.8 * f0
if fz > 1.5 * f0:
    print(" ОБРАБОТКА НА МИУ НЕЦЕЛЕСООБРАЗНА ")  # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных
#<<<<<<< HEAD
#if poisk==1 or mm==0:
 #   print(' КОНТРОЛЬ ПАРАМЕТРОВ [ 1 - ДА ], [ 0 - НЕТ ] ? ')  # необходимо вывести окно с данным вопросом
  #  kp1 = input()
#else:
 #   kp1 = 0
if poisk==1 and mm > 0:
    U0 = u1
    u1 = u1 * 1000
    U0 = u1
if poisk==0 and mmm > 0:
    U0 = uu0

# {1} Repeat {начало}
wq = fp * 2.0 * 3.14
if w3 > wq * 3: ef = 0.5 * ek
else:
    if w3 < wq / 3:
        ef = 0
    else: ef = 0.25 * ek
#=======
"""if poisk==1 or mm==0:
            print(' КОНТРОЛЬ ПАРАМЕТРОВ [ 1 - ДА ], [ 0 - НЕТ ] ? ')  # необходимо вывести окно с данным вопросом
            kp1=input()
         else: """
kp1 = 0
if poisk==1 and mm > 0:
    U0 = u1
    u1 = u1 * 1000
    U0 = u1
if poisk==0 and mmm > 0:U0 = uu0

#___________________________________________________________________________________________________________________
else:  # РАЗДАЧА
# { ОБЖИМ }
    vg = 1 * (-1)
if l0 / dh < 1:
    l3 = l0 / math.pow((1 - ef), 0.5)
    h3 = h0 / math.sqrt(1 - ef)
else:
    l3 = l0
    h3 = h0 / (1 - ef)
dz = dh * (1 - ef)  # { СРЕДНИЙ НАРУЖНЫЙ ДИАМЕТР ЗАГОТОВКИ }
dm = dz - 2.0 * h3  # { СРЕДНИЙ ВНУТРЕННИЙ ДИАМЕТР ЗАГОТОВКИ }
wr = (dv - dh) / 2.0
x3 = pow((p3 / (3.14 * mu0 * fp)), 0.5)
x1 = pow((p1 / (mu0 * 3.14 * fp)), 0.5)
if x1 < 2 * a / 3:
    xb = x1
else:
    xb = 2 * a / 3
z = b / (hb + xb)  # {hb - ЗАЗОР МЕЖДУ ТОКОПОДВОДАМИ }
lb = (0.5 * l1 * math.log((2.0 * l1) / (a + b) + 0.5) + (
                math.log((hb + xb) / (b + xb)) + (z * z - 1) * math.log(1 + z * z) / (2.0 * z * z) + (
                    2.0 / z * math.atan(z))) * lv) * pow(10,-7)
rb = p1 * (l1 + 2.0 * lv) / (a * b)
xi = 0
#======================================================================================================================
if v == 0:
# begin { ОБЖИМ }
    if 0.5 * x1 < h1 / 3.0:
        xi = 0.5 * x1
    else:
        xi = h1 / 3.0
    di = dv + 2.0 * xi
else:  # обжим
    di = dn - h1  # { РАЗДАЧА }

# { индуктор средний }
if l1 / di < 1.0 and l1 / di > 0.3:
    Lind = di * di / l1 * (4.1 + 3.9 * (l1 / di - 0.3)) * n1 * n1 * pow(10,-7)
else:
    if l1 / di > 1:  # then { индуктор длинный }
        Lind = di * di / l1 * (9.9 - (3.2 * di) / l1) * n1 * n1 * pow(10,-7)
    else:  # { индуктор короткий }
        Lind = di * di / l1 * (4.1 + 3.9 * (l1 / di - 0.3)) * n1 * n1 * pow(10,-7)
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
    Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * pow(10,-7)
else:  # { begin else }
    vb = 0
    q0 = 1
if l3 / dr > 1.0:  # then { заготовка длинная }
    Lzag = dr * dr / l3 * (9.9 - 3.2 * dr / l3) * pow(10,-7)
else:
    print("... Обработка на МИУ нецелесообразна...")  # вместо данной команды необходимо выдать окно с данной надписью и вернуться в ввод данных

vb = 1
q0 = 2.0 / math.pow(3.0, 0.5)

Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * pow(10,-7)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if x3 < h3:
    xs = x3
else:
    xs = h3
Rzag = p3 * 3.14 * dr / (l3 * xs)  # { Rzag - АКТИВНОЕ СОПРОТИВЛЕНИЕ ЗАГОТОВКИ }
hm = (l1 - H_izol * (n1 - 1)) * 1000 / n1  # { hm - ВЫСОТА ВИТКА ИНДУКТОРА }
#========================================================================================================================
if hm < 0:
# begin
    print("кУ-кУ !! кУ-кУ !! кУ-кУ !!") #Требуется вывести окно
    print(" ВЫСОТА ВИТКА ИНДУКТОРА < 0 !!")
# Delay(3000) Задержка
# end
Rind = p1 * 3.14 * di * n1 * n1 / l1 / xr  # { Rind - АКТИВНОЕ СОПРОТИВЛЕНИЕ ИНДУКТОРА }
if l1 / di > 1.0:
    Lind = di * di / l1 * (9.9 - 3.2 * di / l1) * n1 * n1 * pow(10,-7)
else:
    Lind = di * di / l1 * (4.1 + 3.9 * (l1 / di - 0.3)) * n1 * n1 * pow(10,-7)

if v == 1:
    if l1 / di < 1.0:
        fb = 4.8
    else:
        fb = 5.0
        m9 = fb * pow((1 + (l1 + l3) * (l1 + l3)) / (di*di), 0.5) - 4.5 * pow(((1 + (l1 - l3) * (l1 - l3) / di / di), 0.5) * (n1 * pow(10,-7)))
        m8 = (dr * dr * di) / (l1 * l3)
        M_ind_zag = m9 * m8

if v == 2:
    if l3 / dr < 1:
        fb = 4.8
    else:
        fb = 5.0
m9 = fb* pow(1 + (l1 + l3) * (l1 + l3) / dr*dr,0.5)-4.5*pow(1 + (l1 - l3) * (l1 - l3) / (dr*dr),0.5)*n1*pow(10,-7)
m8 = dr * di * di / (l3 * l1)
M_ind_zag = m8 * m9

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
ww = pow((abs(1.0 / (c0 * ls) - s1 * s1)), 0.5)
c9 = (1.0 / (c0 * ls) - s1 * s1)
if c9 < 0 and flag > 1:
    print("Ку ку разряд апериодический")  # then
 #_______________________________________________________________________________
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
#_____________________________________________________________________________________________________________________
if (v == 0):  # then { ОБЖИМ }
    pw = mu0 * E0 * (n1 * kn / l3) * (n1 * kn / l3) / ls
else:
    # { РАЗДАЧА }
    pw = (mu0 * E0 * kq * kq * kn * kn) / (ls * l3 * l3)
pq = pw * math.exp(0 - 3.14 / (2.0 * q1))
if c9 < 0:  # then
    fq = 10
else:
    fq = ww/(2.0 * 3.14)
"""        # Repeat{3}
print(' Для продолжения ===> Жми на <Enter> >>')"""
print("F0=", f0)
print("Fz=", fz)
print("Fp=", fp)
print("f3=", f3)
print("h3=", h3)
print("l3=", l3)
print("vg=", vg)
print("dz=", dz)
print("ef=", ef)
print("wr=", wr)
print("db=", db)
print("dm=", dm)
print("x3=", x3)
print("x1=", x1)
print("xb=", xb)
print("z=", z)
print("xi=", xi)
print("di=", di)
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
print("L0=", lo)
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
print("n1=", n1)
print("Uo=", U0)
print("Pmax=", pq)
print("Hвит=", hm)
print("Fr0=", over_f0)
print("fq=", fq)

"""q0q = Ord(klav)
        gotoxy(1, 1)
    Until
    {3}(q0q=13)
    end
    {end if (kp1 ==1)}
        abt = abs(fp - fq)
        if (abt > 1):
            fp = fq
            flag = flag + 1
        while (abt < 1):"""
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
pstrag =h3*2*sp/dz*(vb+(1-vb)*q0)
print("Давление страгивания====>(МПа)", pstrag/1e6)
print(io, lw, alfa1, alfa3, m13, Gamma0, Gamma1, Gamma3)
print(ka, dd, bb, b1)
#_________________________________________end TOPY_________________________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++Difur++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
k0 = 0.02*math.pi*pow((1+alfa1), 0.5)*pow((lw*c0), 0.5)
print("Рекомендуемый шаг счета============>", k0*1e6)
k0 = float(input("Задайте шаг счета"))
NS = float(input("Задайте кратность печати"))
Time_h = k0/(math.sqrt(lw*c0)*pow(10,6))
Time_x=0
y=[0, 0, 1, 0, 0]
w=[0, 0, 1, 0, 0]
f=[0,0,1,0,0]
k=[0,0,1,0,0]
i2 = ( y[3]*alfa3-y[4]*m13 ) / ( (1+alfa1)*alfa3-m13*m13 )
i4 = (y[3]*m13-y[4]*(1+alfa1))/( (1+alfa1)*alfa3-m13*m13 )*(-1.0)
N_Y=0
print(Time_h)
#+++++++++++++++++++++++++++++++++++++++++++++++++Difur end+++++++++++++++++++++++++++++++++++++++++++++++++++++++
def var1(pc, Time_tek,U_tek,Iind,Izag,P_tek, S_tek, V_tek):
    ss6 = (vb+(1.0-vb)*q0)*dd
    ss7 = bb*pc
    if (ss7-ss6==0):
        io = 2
        if poisk == 1:
            print(Time_tek,U_tek,Iind,Izag,P_tek,y[1]*100,y[2]*1000,S_tek,V_tek)
        if (ss7-ss6 == 0) and ( Time_tek*1e6 == 100):
            io = 3
def var2():
    z1 = y[1]
    h_tek = h0*(vb/math.sqrt(1.0+vg*z1)+(1.0-vb)/(1.0+vg*z1))
    if(x3 == h_tek/3.0) :
        xx = x3/2.0
    else:
        xx = h_tek/3.0
    if(x3 == h_tek):
        xe = x3
    else:
        xe = h_tek
    if(vb == 0) : # Короткая заготовка}
        h_zag = h0/(1+vg*z1)
    else: # Длинная заготовка}
        h_zag = h0/math.sqrt(1+vg*z1)
        zn = dh*(1.0+vg*z1)
        zb = zn-2*h_zag
        d_tek = (1.0-vg)/2.0*(zn-2.0*xx)+(1.0+vg)/2.0*(zb+2.0*xx)
        l_tek = l0*(vb/math.sqrt(1.0+vg*z1)+1.0-vb)
    if(vb == 0) : # Короткая заготовка}
        L_zag_tek = d_tek*d_tek/l_tek*(9.9-3.2*d_tek/l_tek)*1e-7
    else: # Длинная заготовка}
        L_zag_tek = d_tek*d_tek/l_tek*(4.15+3.96*(l_tek/d_tek-0.32))*1e-7
    if (vg == 0) : # vg = 1 раздача }
        if (l_tek/d_tek == 1) :
            fb = 5.0
        else:
            fb = 4.8
            m8 = d_tek*di*di/l_tek/l1
            m9 = ( fb*math.sqrt(1+(l1+l_tek)*(l1+l_tek)/d_tek/d_tek)
            - 4.5*math.sqrt(1+(l1-l_tek)*(l1-l_tek)/d_tek/d_tek) )*n1*1e-7
            M_ind_zag_tek = m8 * m9
    else: # vg = -1 обжим }
        if (l1/di == 1) :
            fb = 5.0
        else:
            fb = 4.8
            m9 = ( fb*math.sqrt(1.0+(l1+l_tek)*(l1+l_tek)/di/di)
            - 4.5*math.sqrt(1.0+(l1-l_tek)*(l1-l_tek)/di/di) )*n1*1e-7
            m8 = d_tek*d_tek*di/l1/l_tek
            M_ind_zag_tek = m9*m8
    alfa3 = n1*n1* L_zag_tek /lw
    R_zag_tek = 3.14*p3*d_tek/l_tek/xe
    m13 = M_ind_zag_tek *n1/lw
    Gamma3 = R_zag_tek *math.sqrt(c0/lw)*n1*n1
    if(z1 == 0) :
        print("&#39; Финиш !!!&#39;")
    if(y[1] == 0) :
        io = 3
    print(io)

def rezult(NI):
    dc = dh-h0
    zaz= dh-2*h0-dn
    i2 = ( y[3]*alfa3-y[4]*m13 ) / ( (1+alfa1)*alfa3-m13*m13 )
    i4 = (y[3]*m13-y[4]*(1+alfa1))/( (1+alfa1)*alfa3-m13*m13 )*(-1.0)
    S_tek = dc*y[1]*1000
    pc = 0.5*((vg-1)*(2.0*i2+i4)*i4+(vg+1)*i4*i4)*(zaz/(zaz+kappa*S_tek/1000))
    Iind = i2*U0/math.sqrt(lw/c0)
    U_tek = y[2]*U0
    Izag = i4*n1*U0/math.sqrt(lw/c0)
    P_tek = pc*b1
    Time_tek = Time_x*math.sqrt(lw*c0)
    V_tek = dc*y[1]/math.sqrt(c0*lw)
    if poisk == 0:
        if (NI == NS): NI = 0
        NI = NI + 1

def Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4,f,y):

    if (io == 1):
        f[0]=0
        f[1]=0
    elif (io == 3):
        f[0]=0
        f[1]=0
        y[1]=0
    else:
        f[0]=y[1]
        ss1 =((4.0/3.0-vb/3.0)*ka*vg*math.log(1+vg*y[1])/(1.0+vg*y[1]),math.exp(1))
        ss2 =(vb+(1.0-vb)*q0)*dd/(1.0+vg*y[1])
        ss3 =bb*pc*(vb*math.sqrt(1.0+vg*y[1])+(1.0-vb)*(1.0+vg*y[1]))
        f[1]=ss3-ss1-ss2
    f[2] = i2*(-1.0)
    f[3] = y[2]-i2*(Gamma0+Gamma1)
    f[4] = Gamma3*(-i4)
    print(f)
    print(y)

def zub1(N_Y,Time_h,f,w,k,y):
    for j in range(N_Y):
        vk = Time_h * f[j]
        k[j] = vk
        y[j] = w[j] + vk / 2.0

def zub2(N_Y,Time_h,w,f,k,y):
    for j in range(N_Y):
        vk = Time_h * f[j]
        k[j] = k[j] + 2.0 * vk
        y[j] = w[j] + vk / 2.0

def zub3(N_Y,Time_h,f,k,y,w):
    for j in range(N_Y):
        vk = Time_h * f[j]
        k[j] = k[j] + vk * 2.0
        y[j] = w[j] + vk

NI=0

while io!=3:
    rezult(NI)
    #var1(pc,Time_tek,U_tek,Iind,Izag,P_tek, S_tek, V_tek)
    var2()
    Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4,f,y)
    zub1(N_Y,Time_h,f,w,k,y)
    Time_x = Time_x + Time_h/2.0
    Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4,f,y)
    zub2(N_Y,Time_h,w,f,k,y)
    Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4,f,y)
    zub3(N_Y,Time_h,f,k,y,w)
    Time_x = Time_x + Time_h/2.0
    Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4,f,y)
    for j in range (N_Y):
        y[j] = w[j] + (k[j] + Time_h*f[j])/6.0
        w[j] = y[j]


