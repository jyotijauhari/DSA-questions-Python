# time nd space = O(m*n) , m = row, n = col

#river sizes
'''
input:
1 0 0 1 0
1 0 1 0 0 
0 0 1 0 1
1 0 1 0 1 
1 0 1 1 0
'''
#ouput : [1,2,2,2,5]

def riverSizes(matrix):
	sizes = []
	visited = [[False for value in row]for row in matrix]:
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			if visited[i][j]:
				continue
			traverseNode(i, j, matrix, visited, sizes):
	return sizes

def traverseNode(i,j,matrix, visited, sizes):
	currentRiverSize = 0
	nodesToExplore = [[i,j]] #stack dfs
	while len(nodesToExplore):
		currentNode = nodeToExplore.pop()	
		i = currentNode[0]
		j = currentNode[1]
		if visited [i][j] :
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
		for neighbor in unvisitedNeighborss:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i,j,matrix,visited):
	unvisitedNeighbors = []
	if i>0 and not visited[i-1][j]:
		unvisitedNeighbors.append([i-1,j])
	if i<len(matrix) and not visited[i+1][j]:
		unvisitedNeighbors.append([i+1,j])
	if j>0 and not visited[i][j-1]:
		unvisitedNeighbors.append([i,j-1])
	if j<len(matrix) and not visited[i][j+1]:
		unvisitedNeighbors.append([i,j+1])
	return unvisitedNeighbors
