#time- O(N) 
#space - O(n) space

#ip = [8,4,2,1,3,6,7,9,5]
#sol i.e rewards arr = [4,3,2,1,2,3,4,5,1] 
#op= max rewards needed = sum(rewards) = 25

def minRewards(scores):
	rewards = []
	for i in range (len(scores)):
		rewards.append(1)

	for i in range (1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1

#excluding last index= i.e len(scores) - 1 that means loop runs from len(scores) -2 to 0
	for i in reversed(range(len(scores) - 1)):
		if scores[i] > scores[i+1]:
			rewards[i] = max[rewards[i], rewards[i+1]+1]
	return sum(rewards)
