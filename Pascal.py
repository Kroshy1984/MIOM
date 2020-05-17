import math
def Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4):
    f=[]
    y=[]
    if (io == 1):
        f[0]=0
        f[1]=0
    else:
        if (io == 3):
            f[0]=0
            f[1]=0
            y[1]=0
        else:
            f[0]=y[1]
            ss1 =((4.0/3.0-vb/3.0)*ka*vg*math.log(1+vg*y[1])/(1.0+vg*y[1]),math.exp(1))
            ss2 =(vb+(1.0-vb)*q0)*dd/(1.0+vg*y[1])
            ss3 =bb*pc*(vb*math.sqrt(1.0+vg*y[1])+(1.0-vb)*(1.0+vg*y[1]))
            f[2]=ss3-ss1-ss2
    f[3] = i2*(-1.0)
    f[4] = y[3]-i2*(Gamma0+Gamma1)
    f[5] = Gamma3*(-i4)

def zub1(N_Y,Time_h,f,w):
    k=[]
    y=[]
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

io=1
vb=1
l1 = 1
ek = 0.02
a = 0.004
b = 0.008
ey = 700 *math.pow(10, 6)
lm = 1.2 * math.pow(10, -7)
hb = 0.005
xb = 2 * a / 3
lv = 0.150
z = b / (hb + xb)
lb = (0.5 * l1 * math.log((2.0 * l1) / (a + b) + 0.5) + (
                math.log((hb + xb) / (b + xb)) + (z * z - 1) * math.log(1 + z * z) / (2.0 * z * z) + (
                    2.0 / z * math.atan(z))) * lv) * pow(10,-7)
lw = lm + lb
c0 = 254*math.pow(10, -6)
U0 = 1
pm = 2640
dh = 0.1514
ka= 4 * ey * lw * c0 /(pm*dh*dh)
vg=-1
n1 = 7
mu0=4*math.pi*1e-7
q0 = 2.0 / math.pow(3.0, 0.5)
kn = 0
l0 = 0.030
h0 = 0.0012
sp = 700*math.pow(10, 6)
dd = 4 * sp * lw * c0 / pm / dh / dh
bb = mu0 * (c0 * U0 * n1 * kn) * (c0 * U0 * n1 * kn) / (pm * dh * h0 * l0 * l0)
ef = 0
dz = dh * (1 - ef)
h3 = h0 / math.sqrt(1 - ef)
dm = dz - 2.0 * h3  #
p3 = 7.1*math.pow(10, -8)
lmc = lm*c0
R0 = 4.25*math.pow(10, -3)
r2l = R0*R0/4/lm/lm
f0 = 0.5 / (3.14 * math.pow((1 / lmc - r2l), 0.5))
fp = 0.5 * f0
x3 = pow((p3 / (3.14 * mu0 * fp)), 0.5)
xz = x3 / 2.0
dr = dm + 2.0 * xz
l3 = 1
Lzag = dr * dr / l3 * (4.1 + 3.9 * (l3 / dr - 0.3)) * pow(10,-7)
di = dv + 2.0 * xi
Lind = di * di / l1 * (9.9 - 3.2 * di / l1) * n1 * n1 * pow(10,-7)
alfa1 = Lind/lw
alfa3 = Lzag*n1*n1/lw
i2 = ( y[4]*alfa3-y[5]*m13 ) / ( (1+alfa1)*alfa3-m13*m13 )
i4 = (y[4]*m13-y[5]*(1+alfa1))/( (1+alfa1)*alfa3-m13*m13 )*(-1.0)
pc = 0.5*((vg-1)*(2.0*i2+i4)*i4+(vg+1)*i4*i4)*(zaz/(zaz+kappa*S_tek/1000))
i2 = (y[4]*alfa3-y[5]*m13 ) / ( (1+alfa1)*alfa3-m13*m13 )
Gamma0 = R0 * math.pow((c0 / lw), 0.5)
Gamma1 = Rind * math.pow((c0 / lw), 0.5)
Gamma3 = Rzag * n1 * n1 * math.pow((c0 / lw), 0.5)
i4 = (y[4]*m13-y[5]*(1+alfa1))/( (1+alfa1)*alfa3-m13*m13 )*(-1.0)
N_Y=5
Time_h = k0/(math.sqrt(lw*c0)*pow(10,6))
Time_x=0

Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
zub1(N_Y,Time_h,f,w)
Time_x = Time_x + Time_h/2.0
Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
zub2(N_Y,Time_h,w,f,k,y)
Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
zub3(N_Y,Time_h,f,k,y,w)
Time_x = Time_x + Time_h/2.0
Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
for j in range (N_Y):
    y[j] = w[j] + (k[j] + Time_h*f[j])/6.0
    w[j] = y[j]
