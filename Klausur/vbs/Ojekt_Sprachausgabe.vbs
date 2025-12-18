Option Explicit

Dim message, sapi
Dim read_aloud

message = InputBox("Bitte Text eingeben, der vorgelesen werden soll.")
Set sapi = CreateObject("SAPI.SpVoice")
sapi.Speak message
'read_aloud= "Heute ist " & WeekdayName(Weekday(Date, vbMonday), False, vbMonday)
sapi.Speak read_aloud
