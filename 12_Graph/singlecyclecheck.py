#ip = [2,3,1,-4,-4,2]
#op - true

# O(N) time and O(1) space
def hasSingleCycle(array):
    # Write your code here.
	i = 0
    while array[i] != None:
		jump = array[i]
		array[i] = None
		if jump >= 0:
			i = (jump + i) % len(array)
		else:
			jump = abs(jump) % len(array)
			if i - jump < 0:
				i = len(array) + (i - jump)
			else:
				i -= jump
	
	if i != 0:
		return False
	print(array)
	for x in array:
		if x != None:
			return False
		
	return True



#t- O(N) and space = O(1)
def hasSingleCycle(array):
	numElementsVisited = 0
	currentIdx = 0 
	while numElemetsVisisted < len(array):
		if numElementsVisited > 0 and currentIdx == 0 :
			return False
		numElementsVisited += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == 0

def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)
