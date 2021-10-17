#O(d) time (d is max depth) | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendantDepth(descendantOne, topAncestor)
	depthTwo = getDescendantDepth(descendantTwo, topAncestor)
	if depthOne > depthTwo :
		return backAncestralTree(descendantOne, descendantTwo, depthOne-depthTwo)
	else:
		return backAncestralTree(descendantTwo , descendantOne, depthTwo - depthOne )

def getDescendantDepth(descendant, topAncestor) :
	depth = 0
	while descendant != topAncestor :
		depth += 1
		descendant = descendant.ancestor
	return depth

def backtrackAncestralTree( lowerDescendant, higherDescendant, diff):
	while diff > 0 :
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1

	while lowerDescendant != higherDescendant :
		loweDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	return lowerDescendant

#other method require space
#https://www.youtube.com/watch?v=13m9ZCB8gjw
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(D) time and space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    visited = set()
	while descendantOne != topAncestor:
		visited.add(descendantOne)
		descendantOne = descendantOne.ancestor
		
	while descendantTwo != topAncestor:
		if descendantTwo in visited:
			return descendantTwo
		descendantTwo = descendantTwo.ancestor
		
	return topAncestor
