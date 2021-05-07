#4 number sum
#O(n) space , O(n3) time
def fourNoSum(array, target):
	array.sort() #[7,6,4,-1,1,2] = [-1,1,2,4,6,7]
	quadruplet = []
	for i in range (0, len(array)):	
		for j in range (i+1, len(array):
			target_now = target - array[i] - array[j]
			leftptr = j+1
			rightptr = len[array] - 1
			while leftptr < rightptr:
				if array[leftptr] + array[rightptr] < target_now : 
					leftptr += 1
				elif array[leftptr] + array[rightptr] > target_now : 
					rightptr -= 1
				else : 
					q1 = array[i]
					q2 = array[j]
					q3 = array[leftptr]
					q4 = array[rightptr]
					quadruplet.append( q1, q2, q3, q4)
					while(leftptr < rightptr and array[leftptr] == q3):
						leftptr += 1	
					while(leftptr < rightptr and array[rightptr]== q4):
						rightptr -= 1
			while( j+1 < len(array) and array[j+1] == array[j]:
				j += 1
		while( i+1 < len(array) and array[i+1] == array[i]):
			i += 1
	return quadruplet
		
#(another method  use 3 variable as marker for position and binary search on remaining part to get missing 4th no)				