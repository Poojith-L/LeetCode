class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        arrow=1
        i=1
        j=points[0][1]
        while i<len(points):
            if points[i][0]<=j:
                if points[i][1]<j:
                    j=points[i][1]
            else:
                arrow+=1
                j=points[i][1]
            i+=1
        return arrow
