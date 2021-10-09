#ARRAYS

# SORTED SQUARE ARRAY

# O(NlogN) time and O(N) space
def sortedSquaredArray(array):
    # Write your code here.
	squares = []
    for number in array:
		squares.append(number ** 2)
	return sorted(squares)

# O(N) time and space
def sortedSquaredArray(array):
    # Write your code here.
    squares = []
	leftIndex = 0
	rightIndex = len(array) - 1
	while leftIndex <= rightIndex:
		leftValue = abs(array[leftIndex])
		rightValue = abs(array[rightIndex])
		if leftValue > rightValue:
			squares.append(leftValue ** 2)
			leftIndex += 1
		else:
			squares.append(rightValue ** 2)
			rightIndex -= 1
	return list(reversed(squares))
	
	
###############################################################################################

# TOURNAMENT WINNER

# O(N+K) time and O(K) space
def tournamentWinner(competitions, results):
    # Write your code here.
    teams = {}
	i = 0
	while i < len(competitions):
		homeTeam = str(competitions[i][0])
		awayTeam = str(competitions[i][1])
		if results[i] == 1:
			if homeTeam in teams:
				teams[homeTeam] += 3
			else:
				teams[homeTeam] = 3
				
		else:
			if awayTeam in teams:
				teams[awayTeam] += 3
			else:
				teams[awayTeam] = 3
		i += 1
	
	return max(teams, key=teams.get)
			
# O(N) time and O(K) space
def tournamentWinner(competitions, results):
    # Write your code here.
    teams = {"": 0}
	i = 0
	currentBestTeam = ""
	while i < len(competitions):
		homeTeam = str(competitions[i][0])
		awayTeam = str(competitions[i][1])
		if results[i] == 1:
			if homeTeam in teams:
				teams[homeTeam] += 3
			else:
				teams[homeTeam] = 3
			currentBestTeam = homeTeam if teams[currentBestTeam] < teams[homeTeam] else currentBestTeam
				
		else:
			if awayTeam in teams:
				teams[awayTeam] += 3
			else:
				teams[awayTeam] = 3
			currentBestTeam = awayTeam if teams[currentBestTeam] < teams[awayTeam] else currentBestTeam
		i += 1
	
	return currentBestTeam
	
#############################################################################################################

# NON-CONSTRUCTIBLE CHANGE

# O(NlogN) time, O(1) space
def nonConstructibleChange(coins):
    # Write your code here.
    if not coins:
		return 1
	
	coins.sort()
	ChangeGenerated = 0
	i = 0
	while i < len(coins):
		ChangeGenerated = ChangeGenerated + 1
		if coins[i] > ChangeGenerated:
		    return maxChangeGenerated + 1
			
		ChangeGenerated += coins[i]
		i += 1
	
	return ChangeGenerated + 1
	
#####################################################################################################################

# FIRST DUPLICATE VALUE

# O(N) time and space
def firstDuplicateValue(array):
    # Write your code here.
    store = set()
	for x in array:
		if x not in store:
			store.add(x)
		else:
			return x
	return -1

# O(N) time and O(1) space
def firstDuplicateValue(array):
    # Write your code here.
	i = 0
	while i < len(array):
		x = abs(array[i])
		if array[x-1] < 0:
			return x
		array[x-1] *= -1
		i += 1
		
	return -1
	
####################################################################################################################


# MERGE OVERLAPPING INTERVALS

# O(NlogN) time and O(N) space
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])
	final = [intervals[0]]
	
	for index in range(1, len(intervals)):
		interval = intervals[index]
		if interval[0] > final[-1][1]:
			final.append(interval)
		else:
			final[-1][1] = max(interval[1], final[-1][1])
	
	return final
