#ip: [1,11,3,0,15,5,2,4,10,7,12,6]
#op: longest range= [0,7]

#O(n) time | O(n) space

def largestRange(array):
	bestRange = []
	longestRange = 0
	nums = {}
	
	for num in array:
		nums[num] = True

	for num in array:
		if not nums[num]:
			continue
		nums[num] = False
		currentLength = 1
		leftIdx = num - 1
		rightIdx = num + 1
		while left in nums :
			currenLength += 1
			nums[left] = False
			left - = 1
		while right in nums :
			currenLength += 1
			nums[right] = False
			right  += 1
		if currentLength > longestLength:
			longestLength = currentLength
			bestRange = [left+1, right-1]
	return bestRange	