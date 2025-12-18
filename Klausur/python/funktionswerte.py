import math

def f(x):
    wert= -5
    while wert <= 5:
        funktionswert= wert * wert
        print("f(" + str(wert) + ") = " + str(funktionswert))
        wert += 1

def f1(x):
    wert= -5
    while wert <= 5:
        funktionswert= 2 * wert
        print("f'(" + str(wert) + ") = " + str(funktionswert))
        wert += 1

def f2(x):
    print("f''(x) = 2")

x = 0
f(x)
f1(x)
f2(x)








