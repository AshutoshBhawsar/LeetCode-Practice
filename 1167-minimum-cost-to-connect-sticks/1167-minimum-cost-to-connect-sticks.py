class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks)<2:
            return 0
        heapq.heapify(sticks)
        count=0
        while len(sticks)>1:
            val=heappop(sticks)+heapq.heappop(sticks)
            count+=val
            heapq.heappush(sticks,val)
        return count