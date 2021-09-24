# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
# Time - n^2 in worst case, space = O(1)
#You are creating a new list object each time by concatenating. 
# This requires copying all elements from the old list into a new one, plus one extra. 
# So yes, using l = l + [i] is an O(N) algorithm, not O(1).
#At the very least, don't use + concatenation; use += augmented concatenation, 
# which is the same thing as list.extend() with a re-assignment to the same reference:

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        reverse = []
        
        for i in s:
            if i == ")" :
                top = stack.pop()
                while top != "(" :
                    reverse.append(top)
                    top = stack.pop()
                stack += reverse
                reverse = []
            else:
                stack.append(i)
				
        return "".join(stack)

