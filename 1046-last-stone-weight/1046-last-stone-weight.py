class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        pq=[-x for x in stones]
        heapify(pq)
        while(len(pq)>1):
            x=heappop(pq)
            y=heappop(pq)
            if x-y<0:
                heappush(pq,x-y)
        return -pq[0] if pq else 0