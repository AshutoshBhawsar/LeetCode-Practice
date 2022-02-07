class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries)==0:
            return 0
        answer=0        
        for i in range(len(timeSeries)-1):
            answer+=min(timeSeries[i+1]-timeSeries[i],duration)
        return answer+duration