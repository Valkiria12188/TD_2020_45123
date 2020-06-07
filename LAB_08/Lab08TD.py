
  
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

#funkcja S2B2 z laboratorium 5
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


#Dane:
G = np.array([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
H = np.array([[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]])

#wrzucenie w tablice
arr = []
for i in range(0,1):
    for j in test1:
            arr.append(j)
      
            
# podzielenie na dwie częsci (2 tablice z 1)
arr1 = np.array(arr[0:4]) 
arr2 = np.array(arr[4:8])

print('tab: ', arr)
print('pierwsza część: ', arr1)
print('druga część: ', arr2)


#funkcja do obliczania wektorów
def wektor(x,y):
    v_tab=(np.dot(x,y)).transpose()%2
    return v_tab


#Pierwsza część (wektor 1)
v_tab1=wektor(G, arr1)


#Druga część (wektor 2)
v_tab2=wektor(G, arr2)



print("Wektor 1: ",v_tab1)
print("Wektor 2: ",v_tab2)
print("\n")
print("Wektor 1 i 2 łącznie: ",v_tab1,v_tab2)

####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################
print("\n")
print("---------------------------------------------------------------------------------------------------")
print("\n")
print("Zadanie 2")

#funkcja negująca wskazany numer bitu w strumienu binarnym z zadanai pierwszego
def negation(x):  
    negation_word = np.logical_not(x).astype(int)
    return negation_word

#test1=np.array(STB('slowo'))
#slowo
#11100111101100110111111101111101111

test2=np.array(negation(test1))
print("Zanegowanie wskazanego strumienia binarnego: ",test2)


####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################
print("\n")
print("---------------------------------------------------------------------------------------------------")
print("\n")
print("Zadanie 3")

def decoder(x,y):
    h=np.dot(x,y.T)%2
    print("h: ",h)
    h0=h[0]
    h1=h[1]
    h2=h[2]
    
    #sprawdzenie czy bity parzystości są zerowe
    if h0 != 0 & h1 != 0 & h2 != 0:
        print('Indeks korekty nie jest zerowy')
    else:
        print('Znaleiono indeks róny zero')
        p1 = (arr[0] + arr[1] + arr[3] + arr[4] + arr[6]) % 2
        p2 = (arr[0] + arr[2] + arr[3] + arr[5] + arr[6]) % 2
        p3 = (arr[1] + arr[2] + arr[3] + arr[7]) % 2
        p4 = (arr[4] + arr[5] + arr[6] + arr[7]) % 2
    print("Wektor danych: ", p1,p2,p3,p4)
    print("\n")
    print("Kod Hamminga: ", p1, p2, arr[0], p3, arr[1], arr[2], arr[3], p4, arr[4], arr[5],arr[6], arr[7])


Decoding=decoder(H,v_tab1)





####################################################################################################################################################
############  Zadanie 4 ############################################################################################################################
####################################################################################################################################################
print("\n")
print("---------------------------------------------------------------------------------------------------")
print("\n")
print("Zadanie 4")


#Dane macierz G i H: 
G_S = np.array([[1,1,1,0,0,0,0,1], [1,0,0,1,1,0,0,1], [0,1,0,1,0,1,0,1], [1,1,0,1,0,0,1,0]])
H_S = np.array([[1,0,1,0,1,0,1,0], [0,1,1,0,0,1,1,0], [0,0,0,1,1,1,1,0,], [1,1,1,1,1,1,1,1]])


#funkcja do obliczania wektorów
def wektor1(x,y):
    v_tab_S=(np.dot(x.T,y)).transpose()%2
    return v_tab_S


#Pierwsza część (wektor 1)
v_tab1_S=wektor1(G_S, arr1)


#Druga część (wektor 2)
v_tab2_S=wektor1(G_S, arr2)


print("Wektor 1: ",v_tab1_S)
print("Wektor 2: ",v_tab2_S)
print("\n")
print("Wektor 1 i 2 łącznie: ",v_tab1_S,v_tab2_S)
print("\n")


#dekodowanie z bitem parzystości
def decoder_SECDED(x,y):
    h_S=np.dot(x,y.T)%2
    print("h_S: ",h_S)
    h0_S=h_S[0]
    h1_S=h_S[1]
    h2_S=h_S[2]
    
    #sprawdzenie czy bity parzystości są zerowe
    if h0_S!= 0 & h1_S != 0 & h2_S != 0:
        print('Indeks korekty nie jest zerowy')
    else:
        print('Znaleiono indeks róny zero')
        p1_S = (arr[0] + arr[1] + arr[3] + arr[4] + arr[6]) % 2
        p2_S = (arr[0] + arr[2] + arr[3] + arr[5] + arr[6]) % 2
        p3_S = (arr[1] + arr[2] + arr[3] + arr[7]) % 2
        p4_S = (arr[4] + arr[5] + arr[6] + arr[7]) % 2
        c = (p1_S + p2_S + arr[0] + p3_S + arr[1] + arr[2] + arr[3] + p4_S + arr[4] + arr[5] + arr[6] + arr[7]) % 2
        negation_c = negation(c)

    print('Wektor danych z bitem parzystości: ', p1_S, p2_S, p3_S, p4_S, negation_c)
    print("\n")
    print('Kod Hamminga z bitem parzystości: ', p1_S, p2_S, arr[0], p3_S, arr[1], arr[2], arr[3], p4_S, arr[4], arr[5],arr[6], arr[7], negation_c)


decoder_SECDED(H_S,v_tab1_S)