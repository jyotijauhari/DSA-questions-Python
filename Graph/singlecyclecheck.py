#ip = [2,3,1,-4,-4,2]
#op - true
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

def getNexyYdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)