import math

"""def gate(a,b):
    while True:
        a = input("Geben Sie 1 oder 0 ein: ")
        if a not in ['0', '1']:
            print("Ungültige Eingabe. Bitte geben Sie nur 1 oder 0 ein.")
            continue
        b = input("Geben Sie 1 oder 0 ein: ")
        if b not in ['0', '1']:
            print("Ungültige Eingabe. Bitte geben Sie nur 1 oder 0 ein.")
            continue
        return a, b 
        
pos = [[0,0],[0,1],[1,0],[1,1]]

def konjunktion(a, b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'

def disjunktion(a, b):
    if a == '0' and b == '0':
        return '0'
    else:
        return '1'
    
def ausgabe(a,b):
    print("a =", a)
    print("b =", b)
    print("a AND b =", konjunktion(a, b))
    print("a OR b =", disjunktion(a, b))

while True:
    gate('a','b')
    konjunktion('a','b')
    disjunktion('a','b')
    ausgabe('a','b')   
"""


pos = [[0,0],[0,1],[1,0],[1,1]]

def konjunktion(a, b):
    print("Konjunktion")
    for i in range(len(pos)):
        k = pos[i]
        g = k[0] and k[1]
        print(str(k[0]) + " | " + str(k[1]) + " = " + str(g)),
        i+=1

def disjunktion(a, b):
    i = 0
    print("Disjunktion")
    for i in range(len(pos)):
        k = pos[i]
        g = k[0] or k[1]
        try:
            g=g/g
        except ZeroDivisionError:
            g=0
        print(str(k[0]) + " | " + str(k[1]) + " = " + str(int(g))),
        i+=1


def antivalenz(a, b):
    i =  0
    print("Antivalenz")
    for i in range(len(pos)):
        k = pos[i]
        g = k[0] - k[1]
        if g < 0:
            g = g*-1
        print(str(k[0]) + " | " + str(k[1]) + " = " + str(int(g))),
        i+=1

def ambivalenz(a, b):
    i = 0
    print("Ambivalenz")
    for i in range(len(pos)):
        k = pos[i]
        g = k[0] - k[1]
        if g > 1:
            g = g*-1
        g = g -1
        if g < 0:
            g = g*-1
            
        print(str(k[0]) + " | " + str(k[1]) + " = " + str(int(g))),
        i+=1

def negation(a,b):
    i = 0
    print("Negation")
    for i in range(len(pos)):
        k = pos[i]
        g = k[0] - 1
        if g < 0:
            g = g*-1
        print(str(k[0]) +  " = " + str(int(g))),
        i+=1
    
konjunktion('a','b')
disjunktion('a','b')
antivalenz('a','b')
ambivalenz('a','b')
negation('a','b')