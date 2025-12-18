#Import
import math

#Funktionen der Rechenoperationen

def add(a, b):
    return int(a) + int(b)
def substract1(a, b):
    return int(a) - int(b)
def substract2(a, b):
    return int(b) - int(a)
def multiply(a, b):
    result = 0
    for i in range(int(b)):
        result = add(result, a)
    return result
def divide(a, b):
    return int(a) / int(b)
def modulo(a, b):
    return int(a) % int(b)
def exponation(a,b):
    return int(a) ** int(b)
def falcutaet(n: int) -> int:
    if n == 1:
        return 1
    else:
        return falcutaet(n-1)*n




#Hauptfunktion des Rechners

def rechner():
    operation = input("Gib die Rechenoperation an (Addition(+), Subtraktion(-), Multiplikation(*), Division(/), Modulo(%), Potenzieren(**), Fakultaet(!)): ")  #Variabelen definieren
    
#Abfangen von ungültigen Eingaben
    while True:
        a = input("a 1 = ")
        if a.isdigit():
            break
        else:
            print("Ungültige Eingabe. Bitte erneut eingeben.")

    while True:
        if operation == "!":
            b = 0
            break
        b = input("a 2 = ")
        if b.isdigit():
            break
        else:
            print("Ungültige Eingabe. Bitte erneut eingeben.")

    result = 0
    a = float(a)
    b = float(b)

#Auswahl und durchführung der Rechenoperation    

    if operation not in ["+", "-", "*", "/", "%", "**", "!"]:                       
        print("Ungültige Rechenoperation. Bitte erneut eingeben.")
        operation = input("Gib die Rechenoperation an (Addition(+), Subtraktion(-), Multiplikation(*), Division(/), Modulo(%), Potenzieren(**), Fakultaet(!)): ")
    if operation == "+":                                            #Addition
        result = add(a, b)
        print("Ergebnis: " + str(result))
    elif operation == "-":                                          #Subtraktion
        if a > b:
            result = substract1(a, b)
            print("Ergebnis: " + str(result))
        else:
            result = substract2(a, b)
            print("Ergebnis: " + str(result))
    elif operation == "*":                                          #Multiplikation   
        result = multiply(a, b)
        print("Ergebnis: " + str(result))
    elif operation == "/":                                          #Division     
        if b == 0:
            print("Fehler: Division durch Null ist nicht erlaubt.")
        else:
            result = divide(a, b)
            print("Ergebnis: " + str(result))
    elif operation == "%":                                          #Modulo
        if b == 0:
            print("Fehler: Division durch Null ist nicht erlaubt.")
        else:
            result = modulo(a, b)
            print("Ergebnis: " + str(result))
    elif operation == "**":                                         #Exponation
        result = exponation(a, b)
        print("Ergebnis: " + str(result))
    elif operation == "!":                                          #Fakultaet
        if a < 1:
            print("Fehler: Fakultaet ist nur für positive ganze aen definiert.")
        else:
            result = falcutaet(int(a))
            print("Ergebnis: " + str(result))

#Hauptprogramm
start = "j"
while True:
    start = input("Möchten Sie den Rechner benutzen? (j/n) ")
    if start == "j":
        rechner()
    elif start == "n":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte 'j' oder 'n' eingeben.")
        start = "j"