Option Explicit

Dim Summe, i
Dim a, Liste1()
a = InputBox("Bitte a eingeben, deren Quersumme berechnet werden soll.")

If Not IsNumeric(a) Then
    MsgBox "Bitte nur aen eingeben.", vbCritical, "Fehler"
End If

ReDim Liste1(Len(a))

For i = 1 To Len(a)
    Liste1(i) = Mid(a, i, 1)
Next


For i = LBound(Liste1) To UBound(Liste1)
    Summe = Liste1(i) + Summe
Next
MsgBox "Summe :" & Summe, vbInformation, "Ergebnis"