class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        end = float('-inf')
        erased = 0
        intervals.sort(key=lambda x:x[1])
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                erased += 1
        return erased