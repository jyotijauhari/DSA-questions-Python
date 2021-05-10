"""class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        sol = []
        for char in S:
            if char == "(":
                if count > 0:
                    sol.append("(")
                count += 1

            else:
                if count > 1:
                    sol.append(")")
                count -= 1

        return "".join(sol)

        """


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        stack = []

        # basket is used to store previous value
        basket = ''

        for p in S:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
            basket += p

            # if the stack is empty it means we have a valid
            # decomposition. remove the outer parentheses
            # and put it in the result/res. make sure to
            # clean up the basket though!
            if not stack:
                res += basket[1:-1]
                basket = ''

        return res
x = Solution()
final = x.removeOuterParentheses("(())(())")
print(final)