# O(n) time || O(1)  space
def longestPeak(array) :
	longestPeakLength = 0
	i = 0
	while i < len(array) - 1:
		isPeak = array[i-1] < array[i] and array[i] > array [i+1] 
		if not isPeak:
			i = i + 1
			continue
	
		leftIdx = i - 2
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]
			leftIdx -= 1
		
		rightIdx = i + 2
		while rightIdx <= len(array) and array[rightIdx] < array[rightIdx -1 ]:
			rightIdx += 1
	
		currentPeakLength = rightIdx - leftIdx - 1
		longestPeakLength = max(longestPeakLength , currentPeakLength )
		i = rightIdx
	return longestPeakLength
