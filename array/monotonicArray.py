#time-O(N) 
#space - O(1)

def isMonotonicArray(array):
	Increasing = True
	Decreasing = True
	
	for i in range(1, len(array)):
		if array[i] < array [i-1]:
			Increasing = False
		if array[i] > array [i-1]:
			Decreasing =False
	return Increasing or Decreasing
	
