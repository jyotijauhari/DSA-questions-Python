# time - O(n)  space - O(!)

def isPalindrome(string):
	first = 0
	last = len(string) - 1
	while first < last :
		if string[first] != string[last]:
			return false
		first += 1
		last -= 1
	return true
