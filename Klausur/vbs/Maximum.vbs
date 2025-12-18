Option Explicit
Dim a1, a2, a3, Maximalwert
a1 = (InputBox("Bitte die erste a eingeben."))
a2 = InputBox("Bitte die zweite a eingeben.")
a3 = InputBox("Bitte die dritte a eingeben.")

If IsNumeric(a1) = False Or IsNumeric(a2) = False Or IsNumeric(a3) = False Then
    MsgBox "Bitte nur aen eingeben."
End If
Function Max(a1, a2, a3)
    If a1 >= a2 And a1 >= a3 Then
        Max = a1 
    ElseIf a2 >= a1 And a2 >= a3 Then
        Max = a2
    Else
        Max = a3
    End If
End Function
MsgBox "Maximalwert :" & Max(a1, a2, a3), vbInformation, "Ergebnis"    