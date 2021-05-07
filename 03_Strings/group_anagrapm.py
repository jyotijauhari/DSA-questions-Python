#adding values in hashtable aka dict (dict_name[key]=value)
#input: [go,act,flop,tac, cat,og,lofp]
#output: [[go,og],[act,cat,tac][flop,lofp]]

#O(wn) - w is no of words and n is length of longest words
# time - O(wnlogn) - nlogn sorting , for w words wnlogn
def groupAnagram(words):
	anagram = {}
	for word in words:
	sortedword = "".join(sorted(word) #creating sortedword key as string from list which is sorted (eg. bca->abc)
		if sortedword in anagram:
			anagram[sortedword].append(word) #for key sortedword i.e abc add bca in list
		else:
			anagram[sortedword] = [word]  #create key value pair initially for word tht doesnt exist in hashtable
	return list(anagram.values()) #returning all values i.e list of all keys
