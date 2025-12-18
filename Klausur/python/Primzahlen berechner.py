## Primzahelen berechner
## lest einen Wert ein und berechnet alle Primaen, bis zu dieser a
## Berechnung der Primaen muss manuell erfolgen

num = input("Insert a natural number: ")
num = int(num)
i= 0
j = 2
prim = 1
prim_array = []
nonprim_array = []

for i in range(num):
    for k in range(num):
        if prim / j != 1:
            if prim % j == 0:
                nonprim_array.append(prim)
            j = j+1
        else:
            if prim not in nonprim_array:
                prim_array.append(prim)
            j = j+1
    prim = prim +1
    j = 2


print(prim_array)

