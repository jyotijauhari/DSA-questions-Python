#time - O(N2) , space - O(N)

def threeNumberSum(array, targetSum):
	array.sort()
	triplets = []
	for i in range (len(array) - 2):
		leftptr = i + 1
		rightptr = len(array) - 1
		while leftptr < rightptr :
			currentSum = array[i] + array[leftptr] + array[rightptr]
			if currentSum == targetSum:
				triplet.append([array[i], array[left], array[right]])
			elif currentSum < targetSum :
				leftptr += 1
			elif currentSum > targetSum :
				rightptr -= 1
	return triplets
