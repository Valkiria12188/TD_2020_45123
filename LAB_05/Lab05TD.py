import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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

#rysowanie wykresow
def function(x,y,z):
     plt.plot(x,y,z)
     plt.title("Wykres funkcji") 
     plt.xlabel('X')
     plt.ylabel('Y')
     plt.show()  


def STB(slowo):
    wynik = []
    for i in slowo:
        bits = bin(ord(i))[2:]
        bits = '0000000'[len(bits):] + bits
        wynik.extend([int(b) for b in bits])
    return wynik

test1=np.array(STB('slowo'))
#slowo
#11100111101100110111111101111101111




####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################

#dane do zadania
fi0=0
fi1=np.pi
fi = np.pi
A1=1
A2=0.3
Tb=1 #przyjełąm 1
N=1/Tb

f = N * (Tb ** -1)
f1 = (N + 1)/Tb
f2 = (N + 2)/Tb

x=50
z1=len(test1)

prb=x*(z1/Tb)
prb1=int(prb) # konwertuje wartosc na int poniewaz linespace obraża się na wartości float i sprawiał mi problemy z wyświetleiem 

t = np.linspace(0,z1,prb1)
x = np.linspace(0,z1,z1)


interpolacja = interp1d(x, test1, kind='previous')
TBs = interpolacja(t)

function(t,TBs,'g')


################################################################################
#Za(t)
def zat1(t):
    return A1 * np.sin(2 * np.pi *f*t + fi)
   

def zat0(t):
    return A2 * np.sin(2 * np.pi *f*t + fi)
    

ASK=[]
for i,j in zip(TBs,t):
    if i == 1:
        ASK.append(zat1(j))
    if i==0:
         ASK.append(zat0(j))


function(t,ASK,'g')



################################################################################
#Zf(t)
def zft1(t):
    return A1 * np.sin(2 * np.pi *f2*t + fi)
  

def zft0(t):
    return  A1 * np.sin(2 * np.pi *f1*t + fi)
     

FSK=[]
for i,j in zip(TBs,t):
    if i == 1:
        FSK.append(zft1(j))
    if i==0:
         FSK.append(zft0(j))

function(t,FSK,'g')



################################################################################
#Zp(t)
def zpt1(t):
    return A1 * np.sin(2 * np.pi *f*t + fi0)
  

def zpt0(t):
    return A1 * np.sin(2 * np.pi *f*t + fi1)
    


PSK=[]
for i,j in zip(TBs,t):
    if i == 1:
        PSK.append(zpt1(j))
    if i==0:
        PSK.append(zpt0(j))

function(t,PSK,'g')



####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################

#dane 


def function1(x,y):
     plt.plot(x,y)
     plt.title("Wykres funkcji") 
     plt.xlabel('X')
     plt.ylabel('Y')
     plt.show()  

N=2 # N=2
# ograniczam liczbę bitów do 10 
t1=np.linspace(0,10,prb1)
x1=np.linspace(0,10,z1)   


interpolacja1 = interp1d(x1, test1, kind='previous')
TBs1 = interpolacja1(t1)
f1 = (N + 1)/Tb
f2 = (N + 2)/Tb

################################################################################
#Za(t)
def zat1(t):
    return A1 * np.sin(2 * np.pi *f*t + fi)
   

def zat0(t):
    return A2 * np.sin(2 * np.pi *f*t + fi)
    

ASK1=[]
for i,j in zip(TBs1,t1):
    if i == 1:
        ASK1.append(zat1(j))
    if i==0:
         ASK1.append(zat0(j))


function1(t1,ASK1)

################################################################################
#Zf(t)
def zft1(t):
    return A1 * np.sin(2 * np.pi *f2*t + fi)
  

def zft0(t):
    return  A1 * np.sin(2 * np.pi *f1*t + fi)
     

FSK1=[]
for i,j in zip(TBs1,t1):
    if i == 1:
        FSK1.append(zft1(j))
    if i==0:
         FSK1.append(zft0(j))

function1(t1,FSK1)



################################################################################
#Zp(t)

def zpt1(t):
    return A1 * np.sin(2 * np.pi *f*t + fi0)
  

def zpt0(t):
    return A1 * np.sin(2 * np.pi *f*t + fi1)
    


PSK1=[]
for i,j in zip(TBs1,t1):
    if i == 1:
        PSK1.append(zpt1(j))
    if i==0:
        PSK1.append(zpt0(j))

function1(t1,PSK1)






####################################################################################################################################################
############  Zadanie 4 ############################################################################################################################
####################################################################################################################################################

#Widmo ASK
Widmo_ASK=np.abs(ASK)

function(t,Widmo_ASK,'g')

#Widmo FSK
Widmo_FSK=np.abs(FSK)

function(t,Widmo_FSK,'g')


#Widmo PSK
Widmo_PSK=np.abs(PSK)

function(t,Widmo_PSK,'g')

####################################################################################################################################################
############  Zadanie 5 ############################################################################################################################
####################################################################################################################################################


def szerokosc_pasma(x):
    Fmin=np.min(x)
    Fmax=np.max(x)
    W=Fmax-Fmin
    return W


#szerokość pasme ASK
SzerokoscPasmaASK=szerokosc_pasma(ASK)
print(SzerokoscPasmaASK)
#W= 1.999999838826768

#szerokość pasme FSK
SzerokoscPasmaFSK=szerokosc_pasma(FSK)
print(SzerokoscPasmaFSK)
#W= 1.999999967765353

#szerokość pasme PSK
SzerokoscPasmaPSK=szerokosc_pasma(PSK)
print(SzerokoscPasmaPSK)
#W= 1.999999838826768