
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
    return A1 * np.sin(2 * np.pi *f*t + fi)
  

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
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################
print("Zadanie 2")


################ Demodulacja ASK dla x(t) ##################

def dzat(i,t):
    return i* A1 * np.sin(2 * np.pi *f*t + fi)
    
demodulatorASK=[]
for i,j in zip(ASK,t):
    demodulatorASK.append(dzat(i,j))
    
function(t,demodulatorASK,'r')

################ Demodulacja PSK dla x(t) ##################

def dzpt(i,t):
    return i* A1 * np.sin(2 * np.pi *f*t + fi)
    
demodulatorPSK=[]
for i,j in zip(PSK,t):
    demodulatorPSK.append(dzpt(i,j))

function(t,demodulatorPSK,'r')

################ Demodulacja FSK dla x1(t) ###################

def dzft0(i,t):
    return i* A1 * np.sin(2 * np.pi *f1*t + fi)
    
demodulatoFSK0=[]
for i,j in zip(FSK,t):
    demodulatoFSK0.append(dzft0(i,j))

function(t,demodulatoFSK0,'r')

################ Demodulacja FSK dla x2(t) ###################
def dzft1(i,t):
    return i* A1 * np.sin(2 * np.pi *f2*t + fi)
    
demodulatoFSK1=[]
for i,j in zip(FSK,t):
    demodulatoFSK1.append(dzft1(i,j))

function(t,demodulatoFSK1,'r')

################## Interpolate func ##################################
#dane napisane na gorze
x=50
z1=len(test1)

prb=x*(z1/Tb)
prb1=int(prb) # konwertuje wartosc na int poniewaz linespace obraża się na wartości float i sprawiał mi problemy z wyświetleiem 

t = np.linspace(0,z1,prb1)
x = np.linspace(0,z1,z1)



################ Demodulacja Amplitudy ASK dla p(t) ###################

integralASK = []
for i in range(z1):
    xi = 0
    for j in range(50):
        xi = xi + demodulatorASK[(i * 50) + j]
    integralASK.append(xi)
        


interpolatingASK=interp1d(x, integralASK, kind='previous')
ASK_pt=interpolatingASK(t)
function(t,ASK_pt,'g')


################ Demodulacja Amplitudy PSK dla p(t) ###################


integralPSK = []
for i in range(z1):
    xi = 0
    for j in range(50):
        xi = xi + demodulatorPSK[(i * 50) + j]
    integralPSK.append(xi)
   

interpolatingPSK=interp1d(x, integralPSK, kind='previous')
PSK_pt=interpolatingPSK(t)
function(t,PSK_pt,'g')

################ Demodulacja Amplitudy FSK dla p(t) ###################


integralFSK0 = []
for i in range(z1):
    x0 = 0
    for j in range(50):
        x0 = x0 + demodulatoFSK0[(i * 50) + j]
    integralFSK0.append(x0)
   



integralFSK1 = []
for i in range(z1):
    x1 = 0
    for j in range(50):
        x1 = x1 + demodulatoFSK1[(i * 50) + j]
    integralFSK1.append(x1)
 



integral_FULL_FSK = []
for i in range(z1):
    integral_FULL_FSK.append(integralFSK0[i] - integralFSK1[i])
    



interpolatingFSK=interp1d(x, integral_FULL_FSK, kind='previous')
FSK_pt=interpolatingFSK(t)
function(t,FSK_pt,'g')


####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################
print("Zadanie 3")

#Dane 
h=10
#funkc do wyznaczenia wart progowej
def wartoscProgowa (pt_key,h):
    tab_wart_prog = []
    for p in pt_key:
        if p < h:
            p = 0
            tab_wart_prog.append(p)
        else:
            p = 1
            tab_wart_prog.append(p)
    return tab_wart_prog



#wartość progowa dla ASK
ASK_wart_progowa=wartoscProgowa(ASK_pt,h)

#wartość progowa dla PSK
PSK_wart_progowa=wartoscProgowa(PSK_pt,h)

#wartość progowa dla FSK
FSK_wart_progowa=wartoscProgowa(FSK_pt,h)




####################################################################################################################################################
############  Zadanie 4 ############################################################################################################################
####################################################################################################################################################
print("Zadanie 4")


#wykresy przedstawiające wynik demodulacji

#ASK
function(t,ASK_wart_progowa,'r')

#PSK
function(t,PSK_wart_progowa,'r')

#FSK
function(t,FSK_wart_progowa,'r')