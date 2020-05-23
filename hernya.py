import Pascal
import matplotlib.pyplot
f=Pascal.Pascal()
Y0=Pascal.Pascal.Y0(f)
Y1=Pascal.Pascal.Y1(f)
Y2=Pascal.Pascal.Y2(f)
Y3=Pascal.Pascal.Y3(f)
Y4=Pascal.Pascal.Y4(f)
F0=Pascal.Pascal.F0(f)
F1=Pascal.Pascal.F1(f)
F2=Pascal.Pascal.F2(f)
F3=Pascal.Pascal.F3(f)
F4=Pascal.Pascal.F4(f)
Time=Pascal.Pascal.Time(f)
print(len(Y0))
print(len(Y1))
print(len(Y2))
print(len(Y3))
print(len(Y4))
print(len(Time))
fig=matplotlib.pyplot.figure()
p1=matplotlib.pyplot.plot(Time,Y0,label="Y0")
p2=matplotlib.pyplot.plot(Time,Y1, label="Y1")
p3=matplotlib.pyplot.plot(Time,Y2, label="Y2")
p4=matplotlib.pyplot.plot(Time,Y3, label="Y3")
p5=matplotlib.pyplot.plot(Time,Y4, label="Y4")
matplotlib.pyplot.ylabel("Y") # ось абсцисс
matplotlib.pyplot.xlabel("Time") # ось ординат
grid1 = matplotlib.pyplot.grid(True)
legend=matplotlib.pyplot.legend()
fig2=matplotlib.pyplot.figure()
p1=matplotlib.pyplot.plot(Time,F0, label="F0")
p2=matplotlib.pyplot.plot(Time,F1, label="F1")
p3=matplotlib.pyplot.plot(Time,F2, label="F2")
p4=matplotlib.pyplot.plot(Time,F3, label="F3")
p5=matplotlib.pyplot.plot(Time,F4, label="F4")
matplotlib.pyplot.ylabel("F") # ось абсцисс
matplotlib.pyplot.xlabel("Time") # ось ординат
grid1 = matplotlib.pyplot.grid(True)
legend=matplotlib.pyplot.legend()
matplotlib.pyplot.show()
