class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i]*=-1
            
        heapify(stones)
        while(len(stones)>1):
            x=heappop(stones)
            y=heappop(stones)
            if x-y<0:
                heappush(stones,x-y)
        return -stones[0] if stones else 0