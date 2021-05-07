#brute force 
# time - O(n2) , space - O(1)

def twoNumberSum(array, targetSum):
	for i in range(Len(array - 1)):
		for j in range(i+1, len(array) ):
			if array[i] + array[j] == targetSum :
				return [array[i], array[j]]
	return []


#using hashtables
#time - O(N), space - O(N)

def twoNumberSum(array, targetSum):
	nums= {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch, num]
		else:
			nums[num] = True
	return []

#usingSlidingWindowTechnique
# time - O(nlogn), space - O(1)

def twoNumberSum(array, targetSum):
	array.sort()
	leftptr = 0
	rightptr = len(array)-1
	while leftptr < rightptr:
	  Sum = array[leftptr] + array[rightptr]
		if Sum == targetSum :
			return [array[leftptr], array[rightptr]]
		elif Sum < targetSum:
			leftptr += 1
		elif Sum > targetSum :
			rightptr -= 1
	return []
