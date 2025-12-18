Option Explicit

Dim Summe, i
Dim Liste1(5)
Liste1(1) = 2
Liste1(2) = 10
Liste1(3) = 2
Liste1(4) = 5
Liste1(5) = 8

For i = LBound(Liste1) To UBound(Liste1)
    Summe = Liste1(i) + Summe
Next
MsgBox "Summe :" & Summe, vbInformation, "Ergebnis"