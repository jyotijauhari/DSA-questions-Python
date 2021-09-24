# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

# algo:
# remove valid parenthesis
# push other all things
# return size of stack
#time , space = n, n

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack and char == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)

        if stack:
            return len(stack)
        else:
            return 0

#algo:
#if (, count += 1
#elif ) and count > 0, this means ( is counted , do count -= 1
#else (stack is empty and ")" is ip , increment another temp var, correction += 1
#return count + correction
# time, space - n, 1

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stk = count = 0
        for c in S:
            if c == '(':
                stk += 1
            elif stk > 0:
                stk -= 1
            else:
                count += 1
        return stk + count