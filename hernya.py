import Pascal
import matplotlib.pyplot
f=Pascal.Pascal()
Y0=Pascal.Pascal.Y0(f)
Y1=Pascal.Pascal.Y1(f)
Y2=Pascal.Pascal.Y2(f)
#Y3=Pascal.Pascal.Y3(f)
Y4=Pascal.Pascal.Y4(f)
Time=Pascal.Pascal.Time(f)
print(len(Y0))
print(len(Y1))
print(len(Y2))
#print(len(Y3))
print(len(Y4))
print(len(Time))
p1=matplotlib.pyplot.plot(Time,Y0)
p2=matplotlib.pyplot.plot(Time,Y1)
p3=matplotlib.pyplot.plot(Time,Y2)
#p4=matplotlib.pyplot.plot(Time,Y3)
p5=matplotlib.pyplot.plot(Time,Y4)
matplotlib.pyplot.ylabel("Y") # ось абсцисс
matplotlib.pyplot.xlabel("Time") # ось ординат

matplotlib.pyplot.show()
