class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        
        # if len(intervals)<=1:
        #     return True
        # intervals.sort(key=lambda x:x[0])
        # temp=[intervals[0]]
        # for start,end in intervals[1:]:
        #     if temp[-1][1]>start:
        #         return False
        #     else:
        #         temp.append([start,end])
        # return True
        
        intervals.sort()
        return all(intervals[i][0] >= intervals[i-1][1] for i in range(1, len(intervals)))