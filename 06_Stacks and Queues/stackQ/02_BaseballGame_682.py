#dirty code
# class Solution:
#     def calPoints(self, ops):
#
#         solution = []
#         sum = 0
#
#         for i in range(len(ops)):
#             if ops[i] == "+":
#                 solution.append(solution[-1] + solution[-2])
#
#             elif ops[i] == "D":
#                 val = solution[-1]
#                 solution.append(2*val)
#
#             elif ops[i] == "C":
#                 solution.pop()
#
#             else:
#                 solution.append(int(ops[i]))
#
#         for i in solution:
#             sum += i
#
#         return sum

#systematic code

class Solution:
    def calPoints(self, ops: List[str]) -> int:

        solution = []

        for op in ops:

            if op == "+":
                first = solution.pop()
                second = solution.pop()
                summation = first + second
                solution.append(second)
                solution.append(first)
                solution.append(summation)
            elif op == "D":
                top = solution.pop()
                solution.append(top)
                solution.append(top * 2)
            elif op == "C":
                solution.pop()
            else:
                solution.append(int(op))

        return sum(solution)

x = Solution()
ans = x.calPoints(["5","2","C","D","+"])
print(ans)