import numpy as np
import matplotlib.pyplot as plt

#Mateusz Proc
#nr 45123
# gr 20C Niestacjonarne 1st

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



#funkcje rysujące wykres
def function(x,y,z):
     plt.plot(x,y,z)
     plt.title("Wykres funkcji") 
     plt.xlabel('t')
     plt.ylabel('m(t)')
     plt.show()  

    # funkcja do rys widma
def widmo(x,y):
     plt.plot(x,y)
     plt.title("Wykres funkcji") 
     plt.xlabel('Częstotliwość prążków')
     plt.ylabel('Amplituda')
     plt.show()  


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


#Skala czestotliwości
def sk_cz(x,fs):
    N=len(x)
    fk=[]
    for k in range(N):
        fk.append(k*(fs/N))
    return fk


#funkcja widma amplitudowego -> M(k)
def Mk(x):
    Re=np.real(DFT(x))
    Im=np.imag(DFT(x))
    Mk_tab=[]
    for i in range(0, len(Re)):
        Mk_tab.append(np.sqrt(Re[i]**2+Im[i]**2))
    return Mk_tab


#funkcja skali decybelowej -> M'(k)
def Mk_prim(x):   # M'(k)
    return 10*np.log10(x) 


#funkcja skali decybelowej -> M'(k)
def Mk_prim1(x,y):   # M'(k)
    return y*np.log10(x) 



def szerokosc_pasma(x):
    Fmin=np.min(x)
    Fmax=np.max(x)
    W=Fmax-Fmin
    print(W)



# 7 wykresów 
#Dane
Am=1  #  [V]
fm=2  # B= 2
fn=1  # C= 1
t=np.linspace(0,3,321) #dla ABC wgd indeksu  -> (0,A,ABC)

#Funkcje używane w zadaniu
def mt(t):
    return Am*np.sin(2*np.pi* fm*t)

def zat(t):
    return (ka*mt(t)+1)*np.cos(2*np.pi*fn*t)

def zpt(t):
    return np.cos(2*np.pi*fn*t+kp*mt(t))


#----------------------------------------------------------------------
#wykres sygnalu informacyjnego

function(t,mt(t),'g')
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres A
#a)  1>ka>0  -> ka=0.5 
#    kp<2    -> kp=1
ka=0.5
kp=1

#za(t)
function(t,zat(t),'g')
#zp(t)
function(t,zpt(t),'g')
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres B 
#b)  12>ka>2  -> ka=10 
#    pi>kp>0    -> kp=2
ka=10
kp=2

#za(t)
function(t,zat(t),'g')
#zp(t)
function(t,zpt(t),'g')
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres C 
#c)  ka>23  -> ka=25 
#    kp>32    -> kp=35
ka=25
kp=35

#za(t)
function(t,zat(t),'g')
#zp(t)
function(t,zpt(t),'g')
#----------------------------------------------------------------------



####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################
print("Zadanie 2")
#wykresy amplitudowe sygnałów zmodulowanych za(t) i zp(t)
#6 wykresow
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres A
#a)  1>ka>0  -> ka=0.5 
#    kp<2    -> kp=1
ka=0.5
kp=1

#za(t)
widmo(sk_cz(DFT(zat(t)),100),Mk_prim(Mk(zat(t))))


#zp(t)
widmo(sk_cz(DFT(zpt(t)),100),Mk_prim(Mk(zpt(t))))
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres B 
#b)  12>ka>2  -> ka=10 
#    pi>kp>0    -> kp=2
ka=10
kp=2

#za(t)
widmo(sk_cz(DFT(zat(t)),100),Mk_prim(Mk(zat(t))))


#zp(t)
widmo(sk_cz(DFT(zpt(t)),100),Mk_prim(Mk(zpt(t))))
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres C 
#c)  ka>23  -> ka=25 
#    kp>32    -> kp=35
ka=25
kp=35

#za(t)
widmo(sk_cz(DFT(zat(t)),100),Mk_prim(Mk(zat(t))))


#zp(t)
widmo(sk_cz(DFT(zpt(t)),100),Mk_prim(Mk(zpt(t))))
#----------------------------------------------------------------------


####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################
print("Zadanie 3")
#bez wykresów
#W=fmax-fmin
#szerokosc pasm poszczegolnych aproksymacji zapisac w komentarzu


#----------------------------------------------------------------------
#wykres A (dla poziomu -3dB)
#a)  1>ka>0    -> ka=0.5 
#    kp<2      -> kp=1
ka=0.5
kp=1

#za(t)
mk=Mk(zat(t))
mkp=Mk_prim1(mk,0.801)
szerokosc_pasma(mkp)

#W =3.003130418370645

#zp(t)
mk=Mk(zpt(t))
mkp=Mk_prim1(mk,0.472)
szerokosc_pasma(mkp)

#W = 3.0035286729889745
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres B  (dla poziomu -3dB)
#b)  12>ka>2    -> ka=10 
#    pi>kp>0    -> kp=2
ka=10
kp=2

#za(t)
mk=Mk(zat(t))
mkp=Mk_prim1(mk,0.955)
szerokosc_pasma(mkp)

#W = 3.000806199780511

#zp(t) (dla poziomu -3dB)
mk=Mk(zpt(t))
mkp=Mk_prim1(mk,0.490)
szerokosc_pasma(mkp)

#W = 3.0086990966293325
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#wykres C 
#c)  ka>23    -> ka=25 
#    kp>32    -> kp=35
ka=25
kp=35

#za(t)
mk=Mk(zat(t))
mkp=Mk_prim1(mk,0.908)
szerokosc_pasma(mkp)

#W = 3.000068464757507

#zp(t)
mk=Mk(zpt(t))
mkp=Mk_prim1(mk,0.931)
szerokosc_pasma(mkp)

#W = 3.001748278747142
#----------------------------------------------------------------------

