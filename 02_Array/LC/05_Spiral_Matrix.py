# LC 54 Spiral Matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        startcol = 0
        startrow = 0
        endcol = len(matrix[0]) - 1
        endrow = len(matrix) - 1

        result = []
        while startrow <= endrow and startcol <= endcol:
            for i in range(startcol, endcol + 1):
                result.append(matrix[startrow][i])

            for i in range(startrow + 1, endrow + 1):
                result.append(matrix[i][endcol])

            if startrow < endrow:
                for i in range(endcol - 1, startcol - 1, -1):
                    result.append(matrix[endrow][i])

            if startcol < endcol:
                for i in range(endrow - 1, startrow, -1):
                    result.append(matrix[i][startcol])

            startrow += 1
            startcol += 1
            endrow -= 1
            endcol -= 1

        return result
# s = Solution()
# ans = s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(ans)
