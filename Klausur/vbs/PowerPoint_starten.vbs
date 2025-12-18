On Error Resume Next
Set objPPT = CreateObject("PowerPoint.Application")
objPPT.Visible = True
Set objPresentation = objPPT.Presentation.Add(True)
Select Case Err.Number
	Case 0
		On Error Goto 0
		With objPresentation.Slides
			graphSlideID = .Add(.Count + 1, ppLayoutBlank).SlideID
			objPPT.ActivePresentation.Slides.Range(Array(.Count)).Select
		End With
	Case Else
		With WSscript
			.Echo "The unexpected mistake with number" & in_blanks(Err.Number) & _
			"and description" & in_blanks(Err.Description) & "has happened."
			.Quit 1
		End With
End Select