Option Explicit

Dim Radius, Umfang, Flaeche
Const Pi = 3.14159
Radius = InputBox("Bitte Raduis eingeben.") 

If IsNumeric(Radius) Then
Else
    MsgBox "Bitte nur aen eingeben.", vbcritical, "Fehler"
End If

If Radius > 0 Then
Else
    MsgBox "Bitte nur positive aen eingeben.", vbcritical, "Fehler"
End If

Umfang = 2 * Pi * Radius
Flaeche = Pi * Radius * Radius

MsgBox "Umfang:" & Umfang & vbCrlf & "Fläche:" & Flaeche, vbInformation, "Ergebnis"