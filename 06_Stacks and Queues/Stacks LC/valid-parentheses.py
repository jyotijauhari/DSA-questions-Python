#https://leetcode.com/problems/valid-parentheses/

# time space - n, n
class Solution:
    def isValid(self, s: str) -> bool:

        bracket = {"(": ")",
                   "[": "]",
                   "{": "}"}

        stack = []
        ip = ["(", "[", "{"]

        for char in s:
            if char in ip:
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if bracket[top] != char:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
# time - more than initial n - but approx n
#space - little less than prev but approx n



# time comp - O(n2) in worst case
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l==len(s): return False
        return True