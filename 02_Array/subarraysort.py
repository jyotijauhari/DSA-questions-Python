#ip - [1,2,4,7,10,11,7,12,6,7,16,18,19]
#op - [3,9]

#O(n) time | O(1) space
def subarraySortBound(array):
	minOutofOrder = float("inf")
	maxOutofOrder = float("-inf")
	for i in range(len(array)):
		num = array[i]
		if OutofBound(i, num, array):
			minOutofOrder = min(minOutofOrder, num)
			maxOutofOrder = max(maxOutofOrder, num)
	if minOutofOrder == float("inf"):
		return[-1,-1]
	subarrayLeftIdx = 0
	while minOutofOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1

	subarrayRightIdx = len(array) - 1
	while maxOutofOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	
	return [subarrayLeftIdx, subarrayRightIdx]
	
def OutofBound(i, num, array):
	if i == 0 :
		return num > array[i+1]
	if i == len(array) - 1:
		return num < array[i-1]
	return num > array[i+1] or num < [i-1]
