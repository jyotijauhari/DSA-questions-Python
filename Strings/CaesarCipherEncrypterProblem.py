#time - O(N) || space - O(N)
def CaesarCipherEncrypter(string, key):
	newLetters = []
	newKey = key%26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key #ord returns ascii(unicode) of letter
	return chr [newLetterCode] if newLetterCode <= 122 else return chr [96 + (newLetterCode % 122)]

#input 
#string = abc
#key = 2
#output = def
