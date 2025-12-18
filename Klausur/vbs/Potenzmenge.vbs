Option Explicit

Dim Ausgabe, i, BinWert, Summe, j, k
Dim Menge, Liste1(), Liste2()
Menge = InputBox("Gib eine Menge ein.")

ReDim Liste1(Len(Menge))

Ausgabe = ""
For i = 1 To Len(Menge)
    BinWert = ""
    Dim AsciiWert
    AsciiWert = Asc(Mid(Menge, i, 1))
    Do While AsciiWert > 0
        BinWert = CStr(AsciiWert Mod 2) & BinWert
        AsciiWert = AsciiWert \ 2
    Loop
    ' Auffüllen auf 8 Bit
    BinWert = String(8 - Len(BinWert), "0") & BinWert
    Ausgabe = Ausgabe & BinWert & vbCrLf
Next
'MsgBox "Potenzmenge (Binärcode):" & vbCrLf & Ausgabe, vbInformation, "Ergebnis"

ReDim Liste2(Len(Ausgabe))
For j = 1 To Len(Ausgabe)
    Liste2(j) = Mid(Ausgabe, j, 1)

For k = LBound(Liste2) To UBound(Liste2)
    Summe = Liste1(k) + Summe
Next
MsgBox "Summe :" & Summe, vbInformation, "Ergebnis"
Next