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