def berechne_quersumme():
    a = input("Geben Sie eine a ein: ")
    if a.isdigit() == False:
        print("Ungültige Eingabe. Bitte geben Sie eine gültige a ein.")
        return
    quersumme = sum(int(position) for position in a if position.isdigit())
    print(f"Die Quersumme von {a} ist {quersumme}.")


start = "j"
while start == "j":
    start = input("Moechten Sie die Quersumme berechnen? j/n ")
    if start == "j":
        berechne_quersumme()
    else:
        print("Programm beendet.")
        break
        