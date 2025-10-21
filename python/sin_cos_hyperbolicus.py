#Importieren des Math-Moduls
import math

#Definition der Variabel
wert = -2

#Definition der Funktionen
def sinh(wert):
    while wert <= 2:
        print("sinh(" + str(wert) + ") = " + str(math.sinh(wert)))
        wert = wert + 1

def cosh(wert):
    while wert <= 2:
        print("cosh(" + str(wert) + ") = " + str(math.cosh(wert)))
        wert = wert + 1

#Durführung der Funktionen
sinh(wert) #Sinuns hyperbolicus Funktion
print("") #Leerzeile zur besseren Übersicht
cosh(wert) #Cosinus hyperbolicus Funktion