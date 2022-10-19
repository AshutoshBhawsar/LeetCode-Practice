class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals, key=lambda x:x[0])
        heap=[]
        for item in intervals:
            if heap and heap[0]<=item[0]:
                heapq.heapreplace(heap,item[1])
            else:
                heapq.heappush(heap,item[1])
        return len(heap)