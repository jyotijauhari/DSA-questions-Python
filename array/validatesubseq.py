#time - O(N) , space - O(1)

def ValidateSubsquence(array, subseq):
	m = len(array)
	n = len(subseq)
	counter =0
	for i in range(len(array)):
		current = array[i]
		if current == subseq[counter] :
			counter++
		if counter == n :
			return true
	return false
