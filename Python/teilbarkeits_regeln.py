x = input("Bitte eine Zahl eingeben: ")

#Hauprtfunktion der Teilbarkeitsregeln
def scanf(x):
    i = 2
    for i in range(9):
        i = i + 1
        try:
            int(x) % int(i) == 0
        except ZeroDivisionError:
            i = 2
        if int(x) % int(i) == 0:
            print(str(x) + " ist durch " + str(i) + " teilbar.")
        else:
            print(str(x) + " ist nicht durch " + str(i) + " teilbar.")


#Durchfuehrung der Funktion
scanf(x)