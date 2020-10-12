#time-O(N) 
#space - O(N)

def moveEleToEnd(array, ele):
	i = 0
	j = len(array) - 1
	while i < j:
		while i < j and array[j] == ele:
			j = j-1
		if array[i] == ele
			array[i], array[j] = array[j], array[i]		
		i += 1
	return array
	
