#https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        final = ''
        stack = []

        # temp string to store prev values
        temp = ""

        for p in S:

            if p == '(':
                stack.append(p)

            else:
                stack.pop()

            temp += p

            # if stack is empty then it means one complete ( and ) are done
            # so store the result and let loop iterate if another () is remaining in string
            # clear temp so that new prev val will be stored for next () substring

            if not stack:
                final += temp[1:-1]
                temp = ''

        return final
