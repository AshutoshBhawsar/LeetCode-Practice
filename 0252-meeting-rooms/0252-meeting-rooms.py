class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<2:
            return True
        new_intervals=sorted(intervals,key=lambda x:x[0])
        prev=new_intervals[0]
        for item in new_intervals[1:]:
            if prev[1]>item[0]:
                return False
            prev=item
        return True