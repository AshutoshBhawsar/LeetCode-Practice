class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        arrows, end = 0, -float('inf')
        for i in points:
            if i[0] > end:
                arrows += 1
                end = i[1]
        return arrows