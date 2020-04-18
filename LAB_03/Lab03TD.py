#Mateusz Proc
#nr 45123
# Informatyka N1 GR. 20C


#bilbioteki użyte w programie
import math as m
import numpy as np
import matplotlib.pyplot as plt
####################################################################################################################################################
############  Zadanie 1 ############################################################################################################################
####################################################################################################################################################
##nr indeksu 4 5 1 2 3
##oznaczenia E D C B A
#Dane do zadań
A= 1.0 #               [V]
f= 2 # dla A=2 ,       [HZ]
fi= 1 * np.pi #dla C =1 [rad]
n=np.linspace(0,321)# dla ABC=321

#funkcja rysująca wykres
def function(x,y,z):
     plt.plot(x,y,z)
     plt.title("Wykres funkcji") 
     plt.xlabel('Os X')
     plt.ylabel('OS Y')
     plt.show()   


#funkcja s(n)
def s(A,f,fi,n):
    return A*np.sin(2*np.pi *f*n+fi)


#Funkcja Dyskretnej Transformaty Fouriera
def DFT(x):                           #transformata furiera
    N= len(x)                         # N -> liczba próbek
    x_k= []                           # x(k) wartosc harmonicznej
    wn=np.exp(1j * 2*np.pi / N)      #definicja wn współczynnika skrętu, j->l.urojon(zapis pythona)
    for k in range(N):                #k -> numer harmonicznej
        suma=0                        #EPSILON (SUMA)
        for n in range(N):            # n -> numer probki sygnału 
            suma += x[n]* wn **(-k*n) # wzor na dft podstawiam wn i poteguje przez (-k*n)
        x_k.append(suma)                
    return x_k


#Funkcja Odwrotnej Dyskretnej Transformaty Fouriera
def IDFT(x):                                #odwrotna transformata furiera
     N= len(x)                              # N -> liczba próbek
     x_n=[]                                 # x(k) wartosc próbki sygnału
     wn=np.exp(1j * 2*np.pi / N)            #definicja wn współczynnika skrętu, j->l.urojon(zapis pythona)
     for n in range(N):                     #n -> numer probki sygnału 
         suma=0                             #EPSILON (SUMA)
         for k in range(N):                 # k -> numer harmonicznej
             suma += x[n]* wn **(k*n)       # wzor na idft, podstawiam wn i poteguje przez (k*n)
         x_n.append(suma/N)                 # do sume mnoże razy 1/N czyli dziele przez N(liczbe próbek)
     return x_n




####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################

function(n,s(A,f,fi,n),'g')  #wykres tonu prostego

function(n,DFT(s(A,f,fi,n)),'g') # wykres DFT dla tonu prostego


#Widmo aplitudowe M(k)
#Re=np.real(DFT(s(A,f,fi,n)))
#Im=np.imag(DFT(s(A,f,fi,n)))
#Mk=np.sqrt(Re**2+Im**2)

#funkcja widma amplitudowego -> M(k)
def Mk():
    Re=np.real(DFT(s(A,f,fi,n)))
    Im=np.imag(DFT(s(A,f,fi,n)))
    Mk_tab=[]
    for i in range(0, len(Re)):
        Mk_tab.append(np.sqrt(Re[i]**2+Im[i]**2))
    return Mk_tab


#funkcja skali decybelowej -> M'(k)
def Mk_prim(x):   # M'(k)
    return 10*np.log10(x) 


#Skala czestotliwości
def sk_cz(x,fs):
    N=len(x)
    fk=[]
    for k in range(N):
        fk.append(k*(fs/N))
    return fk


#wykres widma amplitudowego M'(k)

plt.title('wykres widma amplitudowego Mk_prim')
plt.bar(sk_cz(DFT(s(A,f,fi,n)),100),Mk_prim(Mk())) #wykres słupkowy, poniewaz na plt.plot nie mogłem osiągnąć pożądanego efektu
plt.show() 


####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################
#nr indeksu 4 5 1 2 3
#           E D C B A
a=3
b=2
c=1

#widmo amplitudowe dla funkcji x(t)
t_x=np.linspace(-10,10,50)
        
def x(t):
     return a*t**2 + b*t + c

function(sk_cz(x(t_x),10),DFT(x(t_x)),'g')

#----------------------------------------------------------------------
#widmo amplitudowe dla funkcji y(t)
t_y=np.linspace(-10,1,20)

def y(t):
   return 2*x(t)**2+12*np.cos(t)

function(sk_cz(y(t_y),100),DFT(y(t_y)),'g')

#----------------------------------------------------------------------
#widmo amplitudowe dla funkcji z(t)
t_z=np.linspace(-10,1,420)

def z(t):
    return np.sin(2*m.pi*7*t)*x(t)-0.2*np.log10(np.abs(y(t))+(m.pi))

function(sk_cz(z(t_z),100),DFT(z(t_z)),'g')

#----------------------------------------------------------------------
#widmo amplitudowe dla funkcji u(t)
t_u=np.linspace(-10,1,420)

def u(t):
    return np.sqrt(np.abs(y(t)*y(t)*z(t)))-1.8*np.sin(0.4*t*z(t)*x(t))

function(sk_cz(u(t_u),100),DFT(u(t_u)),'g')

#----------------------------------------------------------------------
#widmo amplitudowe dla funkcji v(t)
t_v=np.linspace(0,1,420)

def v(t):
    if (t<0.22)and(t>=0):
        return (1-7*t)*np.sin((2*m.pi*t*10)/(t+0.04))
    if(t>=0.22)and(t<0.7):
        return 0.63*t*np.sin(125*t)
    if(t<=1)and (t>=0.7):
        return (t**(-0.662))+0.77*np.sin(8*t)

o=[]
for i in t_v:
        o.append(v(i))

v1=np.abs(DFT(o)) # obl wartosc bezwzgledną

function(sk_cz(o,100),v1,'g')

#----------------------------------------------------------------------
#widmo amplitudowe dla funkcji p(t)

t_p=np.linspace(-10,1,420)

def p(t,m):
     sum = 0
     for n in  np.arange(1, m+1):
         sum +=((np.cos(12*t*n**2)+np.cos(16*t*n))/n**2)
     return sum

def P_function(x,y):
     plt.plot(x,y)
     plt.title("Wykres funkcji ") 
     plt.xlabel('Os X')
     plt.ylabel('OS Y')
     plt.show()   


p1=np.abs(DFT(p(t_p, 2))) # obl wartosc bezwzgledną
p2=np.abs(DFT(p(t_p,4))) # obl wartosc bezwzgledną
p3=np.abs(DFT(p(t_p,32))) # obl wartosc bezwzgledną

P_function(sk_cz(p(t_p,2),100),p1)
P_function(sk_cz(p(t_p,4),100),p2)
P_function(sk_cz(p(t_p,32),100),p3) # AB =32
####################################################################################################################################################
############  Zadanie 4 ############################################################################################################################
####################################################################################################################################################

function(n,IDFT(DFT(s(A,f,fi,n))),'g') # wykres IDFT dla sygnału z zadania 2 czyli dft(s(n))
