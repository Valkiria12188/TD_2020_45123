import math as m
import numpy as np
import matplotlib.pyplot as plt
####################################################################################################################################################
############  Zadanie 1 ############################################################################################################################
####################################################################################################################################################
##nr indeksu 4 5 1 2 3
##oznaczenia E D C B A
print("Zadanie 1")
##parametry
a=3
b=2
c=1

#delta
delta = (b**2) - (4*a*c)
print("Delta wynosi: ", delta)
if delta==0:
    t0 = (-b)/(2*a)
    print("Funkcja ma jedno miejsce zerowe: ", t0)
elif delta >0:
    t1 = (-b-m.sqrt(delta))/(2*a)
    t2 = (-b+m.sqrt(delta))/(2*a)
    print("Funkcja ma dwa miejsca zerowe: " ,round(t1,2) ,"i" ,round(t2,2))
else:
    print("Delta mniesza od 0 - brak rozwiązań")

#Ekstremum funkcji 
x = -b/(2*a)
y = a*x**2 + b*x + c
print("Ekstremum wynosi: " ,y ,"dla x równego: " ,x)

r=[]
l=[]
# t z zakresu <-10,10> z krokiem 1/100
for t in np.arange (-10,11,0.01):
        y=a*(t**2)+b*t+c
        r.append(t)
        l.append(y)
        
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(r,l)
axes.plot
plt.title("Wykres funkcji kwadratowej") 
plt.xlabel('Os X')
plt.ylabel('OS Y')
plt.legend('Funkcja kwadratowa')
plt.show()

####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################
print("Zadanie 2")
# Dane potrzebne do zadania 2
#diag( nasz wartość t <0,1> z krokiem 1/22050)
tData=np.linspace(0,1,22050)
def x(t):
     return a*t**2 + b*t + c

########### FUNKCJA Y(T)
def y(t):
    return 2*x(t)**2+12*np.cos(t)

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(tData,y(tData))
axes.plot
plt.title("Wykres funkcji y(t)") 
plt.xlabel('Os X')
plt.ylabel('OS Y')
plt.show()

########### FUNKCJA Z(T)
def z(t):
    return np.sin(2*m.pi*7*t)*x(t)-0.2*np.log10(np.abs(y(t))+(m.pi))


fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(tData,z(tData))
axes.plot
plt.title("Wykres z(t)") 
plt.xlabel('Os X')
plt.ylabel('OS Y')
plt.show()


########### FUNKCJA U(T)
def u(t):
    return np.sqrt(np.abs(y(t)*y(t)*z(t)))-1.8*np.sin(0.4*t*z(t)*x(t))


fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(tData,u(tData))
axes.plot
plt.title("Wykres funkcji u(t)") 
plt.xlabel('Os X')
plt.ylabel('OS Y')
plt.show()


########### FUNKCJA V(T)
def v(t):
    if (t<0.22)and(t>=0):
        return (1-7*t)*np.sin((2*m.pi*t*10)/(t+0.04))
    if(t>=0.22)and(t<0.7):
        return 0.63*t*np.sin(125*t)
    if(t<=1)and (t>=0.7):
        return (t**(-0.662))+0.77*np.sin(8*t)


o=[]
for i in tData:
        o.append(v(i))

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(tData,o)
axes.plot
plt.title("Wykres funkcji v(t)") 
plt.xlabel('Os X')
plt.ylabel('OS Y')
plt.show()   


########### FUNKCJA P(T)
def p(t,m):
     sum = 0
     for n in  np.arange(1, m+1):
         sum +=((np.cos(12*t*n**2)+np.cos(16*t*n))/n**2)
     return sum

 
def P_function(x,y):
     plt.plot(x,y)
     plt.title("Wykres funkcji p(t)") 
     plt.xlabel('Os X')
     plt.ylabel('OS Y')
     plt.show()   


P_function(tData,p(tData,2))
P_function(tData,p(tData,4))
P_function(tData,p(tData,32)) # AB =32

