# 939 MINIMUM AREA RECTANGLE

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        table={}
        minimum=float('inf')
        
        # adding all the y co-ordinates with the x co-o as key
        for i in range(len(points)):
            if points[i][0] not in table:
                table[points[i][0]]=[points[i][1]]
            else:
                table[points[i][0]].append(points[i][1])

        # checking for all combinations of points A=(x1,y1), B=(x2,y2)
        for i in range(len(points)):
            x1=points[i][0]
            y1=points[i][1]
            for j in range(len(points)):
                x2=points[j][0]
                y2=points[j][1]
                
                # A and B are in diagonal position, not in the same line
                if x1>x2 and y1>y2:
                    # there exists C=(x1,y2) and D=(x2,y1)
                    if y2 in table[x1] and y1 in table[x2]:
                        minimum=min(minimum, abs(x1-x2) * abs(y1-y2))
        
        # if no such rectangle exists return 0
        if minimum==float('inf'):
            return 0
        return minimum
