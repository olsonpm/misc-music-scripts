from modify_musicxml import MusicXML

test = MusicXML('input.xml')
test.RemoveAllFingerings()
test.RemoveAllRehearsalLetters()
test.InsertScaleDegrees()
test.SetStaffSpacing(140)
test.WriteToFile('output.xml')
	
input('Press enter to exit')