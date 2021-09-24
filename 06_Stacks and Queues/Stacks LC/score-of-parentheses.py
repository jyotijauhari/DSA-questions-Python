#https://leetcode.com/problems/score-of-parentheses/submissions/

# (() ()) , ()() , (())
class Solution:
    def scoreOfParentheses(self, S):
        stack = []
        for char in S:
            if char == "(":
                stack.append(-1)
            else:
                if stack[-1] == -1 :
                    stack.pop()
                    stack.append(1)
                else:
                    val = 0
                    while stack[-1] != -1:
                        val += stack.pop()
                    stack.pop()
                    stack.append(2*val)
        val = 0          
        while len(stack) > 0:
            val += stack.pop()
        return val
            

                
                    
#another sol                    
class Solution:
    def scoreOfParentheses(self, S):
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur


     