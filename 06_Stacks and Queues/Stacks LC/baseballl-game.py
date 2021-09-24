# https://leetcode.com/problems/baseball-game/


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