#smallest difference - arrays
#time - O(nlogn + mlogm) | space - O(1)

def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	smallestPair = []
	current = float("inf")
	smallest = float("inf")
	idx1 = 0
	idx2 = 0
	while (idx1 < len(arrayOne) and idx2 <len(arrayTwo)):
		firstNum = arrayOne[idx1]
		secondNum = arrayTwo[idx2]
		if(firstNum < secondNum):
			currrent = secondNum - firstNum
			idx1 += 1
		elif(firstNum > secondNum):
			current = firstNum - secondNum
			idx2 += 1
		else:
			return [firstNum, secondNum]

		if smallest > current :
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair
