from ChromaticScale import *

#------------#
# test utils #
#------------#

# AlterSymbolFromValue
assert "" == Utils.AlterSymbolFromValue(0)
assert "" == Utils.AlterSymbolFromValue("0")
assert "#" == Utils.AlterSymbolFromValue("1")
assert "x" == Utils.AlterSymbolFromValue("2")
assert "b" == Utils.AlterSymbolFromValue("-1")
assert "bb" == Utils.AlterSymbolFromValue("-2")

# AlterValueFromSymbol
assert 0 == Utils.AlterValueFromSymbol("")
assert 1 == Utils.AlterValueFromSymbol("#")
assert 2 == Utils.AlterValueFromSymbol("x")
assert -1 == Utils.AlterValueFromSymbol("b")
assert -2 == Utils.AlterValueFromSymbol("bb")

# LetterAndAlterToAlteredNote
assert "A" == Utils.LetterAndAlterToAlteredNote("A", 0)
assert "B#" == Utils.LetterAndAlterToAlteredNote("B", 1)
assert "Cx" == Utils.LetterAndAlterToAlteredNote("C", 2)
assert "Db" == Utils.LetterAndAlterToAlteredNote("D", -1)
assert "Ebb" == Utils.LetterAndAlterToAlteredNote("E", -2)

# GetAlterValueFromAlteredNote
assert 0 == Utils.GetAlterValueFromAlteredNote("A")
assert 1 == Utils.GetAlterValueFromAlteredNote("B#")
assert 2 == Utils.GetAlterValueFromAlteredNote("Cx")
assert -1 == Utils.GetAlterValueFromAlteredNote("Db")
assert -2 == Utils.GetAlterValueFromAlteredNote("Ebb")

# GetScaleDegreeFromKeyAndNote
testAMajor = Key("A", Modes["Major"])
assert "1" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "A")
assert "1#" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "A#")
assert "2" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "B")
assert "3" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "C#")
assert "3#" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "Cx")
assert "4b" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "Db")
assert "4" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "D")
assert "5" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "E")
assert "5#" == Utils.GetScaleDegreeFromKeyAndNote(testAMajor, "E#")

# _findNoteFromBase
assert "A#" == Utils._findNoteFromBase(["A#", "B", "Cb"], "A")
assert "B" == Utils._findNoteFromBase(["A#", "B", "Cb"], "B")
assert "Cb" == Utils._findNoteFromBase(["A#", "B", "Cb"], "C")