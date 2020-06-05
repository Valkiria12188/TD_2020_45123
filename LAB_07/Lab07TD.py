#bilbioteki
import matplotlib.pyplot as plt
import math as math

#Mateusz Proc
#nr 45123
# gr 20C Niestacjonarne 1st

#Do opracowania mieliśmy tylko dekoder i sygnał Manchaster 

##nr indeksu 4 5 1 2 3
##oznaczenia E D C B A

##parametry
a=3
b=2
c=1

#string to binary
def STB(slowo):
    binaryStream = []
    for i in slowo:
        bits = bin(ord(i))[2:]  #bit dwójkowy
        bits = '0000000'[len(bits):] + bits
        binaryStream.extend([int(b) for b in bits])
    return binaryStream



def tile(value, count):
    return [value for _ in range(int(count))]




#funkcja rysująca wykresu
def ShowPlot(time, samples, subplot, yLabel, color = 'b', xLimLeft = 0, xLimRight = None):
    if xLimRight is None:
        xLimRight = max(time)
    ax = plt.subplot(4, 1, subplot)
    ax.axhline(0, linestyle='--', c='k', alpha = 0.5)
    ax.plot(time, samples, color, label = yLabel)
    ax.set_ylabel(yLabel)
    ax.set_xlim(xLimLeft, xLimRight)
    plt.legend()










def Bits_and_Plot(bits, ):

    #dane do wykresu CLK
    clk = CLK(100, len(bits))

    #dane do wykresu informacyjnego
    t, ttl = informationSignal(0.1, bits, 100)

 
    #dane do wykresu manchaster i dekoder manchaster
    manchesterSamples = manchesterCoder(clk, ttl)
    manchesterBits = manchesterDecoder(clk, ttl, 100)
    tzz, manchestersTtl = informationSignal(0.1, manchesterBits, 100)


    #wykres
    plt.figure(figsize=(8, 4))

    #wykres CLK
    ShowPlot(t, clk, 1, 'CLK', 'k')

    #wykres TTL
    ShowPlot(t, ttl, 2, 'TTL', 'c')
    
    #wykres manchaster 
    ShowPlot(t, manchesterSamples, 3, 'Manchester', 'g')

    #wykres manchaster dekoder
    ShowPlot(tzz, manchestersTtl, 4, 'Manchester TTL', 'g')


    print(bits)
    
    print(manchesterBits)
    plt.tight_layout()
    




####################################################################################################################################################
############  Zadanie 1 ############################################################################################################################
####################################################################################################################################################
print("Sygnał CLK")

def CLK(samplesBit, Count):
    halfSamples = int(samplesBit / 2)

    clockSamples = samplesBit * Count * [None]
    for i in range(Count * 2):
        clockSamples[i * halfSamples:(i + 1) * halfSamples] = tile((i % 2) == 0, halfSamples)
    return clockSamples



####################################################################################################################################################
############  Zadanie 2 ############################################################################################################################
####################################################################################################################################################
print("Sygnał TTL (m(t))")



#oblicza czas dla sygnału informacjnego
def timeLine(low, high, stepCount):
    step = (high - low) / (stepCount - 1)
    values = [low + step * i for i in range(stepCount)]
    return values


def informationSignal(secondsPerBit, bits, samplesBit):
    time = timeLine(0, secondsPerBit * len(bits), samplesBit * len(bits))
    samples_Signal = samplesBit * len(bits) * [None]


    for i, bit in enumerate(bits):
        samples_Signal[i * samplesBit:(i + 1) * samplesBit] = tile(bit, samplesBit)
    return time, samples_Signal



####################################################################################################################################################
############  Zadanie 3 ############################################################################################################################
####################################################################################################################################################
print("Sygnał TTL i manchaster")

def manchesterCoder(clk, ttl):
    tab = [0]
    currentValue = 0

    for i in range(len(clk) - 1):
        if (clk[i] == 1 and clk[i + 1] == 0): #wzgórze malejące
            if (ttl[i] == 0):
                currentValue = 1
            else:
                currentValue = -1
        elif (clk[i] == 0 and clk[i + 1] == 1): #wzgórze narastające
            if (ttl[i] == ttl[i + 1]):
                currentValue *= -1
        tab.append(currentValue)
    return tab


####################################################################################################################################################
############  Zadanie 4 ############################################################################################################################
####################################################################################################################################################
print("Dekodery kodow manchaster i TTL")

def manchesterDecoder(clock, manchester, samplesbit):
    quarterSamplesPerBit = int(samplesbit / 4)
    clock = tile(1, quarterSamplesPerBit) + clock
    clock = clock[:int(len(clock) - quarterSamplesPerBit)]

    bits = []
    for i in range(len(clock) - 1):
        if (clock[i] == 1 and clock[i + 1] == 0): #wzgórze malejące
            bits.append(manchester[i])
    return bits

####################################################################################################################################################
############   Wykresy  ############################################################################################################################
####################################################################################################################################################

#Dane do wykresów
bits = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0]
test = STB('Slowo')



##############
#test funkcji#
##############

#dla podanych bitów
Bits_and_Plot(bits)

# dla bitów ze słowa podanych funkcją STB
Bits_and_Plot(test[0:16])

plt.show()




