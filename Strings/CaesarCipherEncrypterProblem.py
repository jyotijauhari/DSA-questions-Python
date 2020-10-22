#time - O(N) || space - O(N)
def CaesarCipherEncrypter(string, key):
	newLetters = []
	newKey = key%26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key #ord returns ascii(unicode) of letter
	return alphabet[newLetterCode] if newLetterCode <= 26 else return alphabet[26 + newLetterCode%2]

#input 
#string = abc
#key = 2
#output = def
