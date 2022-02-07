class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        answer=[intervals[0]]
        
        for start,end in intervals[1:]:
            last_end=answer[-1][1]
            if start<=last_end:
                answer[-1][1]=max(last_end,end)
            else:
                answer.append([start,end])
        return answer