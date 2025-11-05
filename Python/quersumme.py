def berechne_quersumme():
    zahl = input("Geben Sie eine Zahl ein: ")
    if zahl.isdigit() == False:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")
        return
    quersumme = sum(int(position) for position in zahl if position.isdigit())
    print(f"Die Quersumme von {zahl} ist {quersumme}.")


start = "j"
while start == "j":
    start = input("Moechten Sie die Quersumme berechnen? j/n ")
    if start == "j":
        berechne_quersumme()
    else:
        print("Programm beendet.")
        break
        