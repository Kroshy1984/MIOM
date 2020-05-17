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
ka= 4 * ey * lw * c0 /(pm*dh*dh)
vg=-1
q0 = 2.0 / math.pow(3.0, 0.5)
dd = 4 * sp * lw * c0 / pm / dh / dh
bb = mu0 * (c0 * U0 * n1 * kn) * (c0 * U0 * n1 * kn) / (pm * dh * h0 * l0 * l0)
pc = 0.5*((vg-1)*(2.0*i2+i4)*i4+(vg+1)*i4*i4)*(zaz/(zaz+kappa*S_tek/1000))
i2 = ( y[4]*alfa3-y[5]*m13 ) / ( (1+alfa1)*alfa3-m13*m13 )
Gamma0 = R0 * math.pow((c0 / lw), 0.5)
Gamma1 = Rind * math.pow((c0 / lw), 0.5)
Gamma3 = Rzag * n1 * n1 * math.pow((c0 / lw), 0.5)
i4 = (y[4]*m13-y[5]*(1+alfa1))/( (1+alfa1)*alfa3-m13*m13 )*(-1.0)

Ston(io,vb,ka,vg,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
zub1(N_Y,Time_h,f,w)
Time_x = Time_x + Time_h/2.0
Ston(io,vb,ka,vg,Ln,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
zub2(N_Y,Time_h,w,f,k,y)
Ston(io,vb,ka,vg,Ln,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
zub3(N_Y,Time_h,f,k,y,w)
Time_x = Time_x + Time_h/2.0
Ston(io,vb,ka,vg,Ln,q0,dd,bb,pc,i2,Gamma0,Gamma1,Gamma3,i4)
for j in range (N_Y):
    y[j] := w[j] + (k[j] + Time_h*f[j])/6.0;
    w[j] := y[j];
