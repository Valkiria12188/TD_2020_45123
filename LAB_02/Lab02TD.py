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
t=np.linspace(0,3,400)# dla A=3 

#funkcja rysująca wykres
def function(x,y,z):
     plt.plot(x,y,z)
     plt.title("Wykres funkcji") 
     plt.xlabel('Os X')
     plt.ylabel('OS Y')
     plt.show()   

#funkcja s(t)
def s(A,f,fi,t):
    return A*np.sin(2*np.pi *f*t+fi)

# wynik zadania 1   
function(t,s(A,f,fi,t),'g*')

####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################
q1=16
quantize1= pow(2,q1)

#quantization = q1*np.round(t/q1)
plt.step(t,np.round(s(A,f,fi,t)*quantize1+quantize1/2))
function(t,np.round(s(A,f,fi,t)*quantize1+quantize1/2),'g*')

####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################

q2= 8
t1=np.linspace(0,3,200)# dla A=3 , częstotliwość probkowania zmniejszona o o plowe
quantize2= pow(2,q2)

plt.step(t,np.round(s(A,f,fi,t)*quantize2+quantize2/2))
function(t,np.round(s(A,f,fi,t)*quantize2+quantize2/2),'g*')
plt.show()   
