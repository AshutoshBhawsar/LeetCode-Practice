class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count=0
        # i=1
        # while n>=0:
        #     n-=i
        #     count+=1
        #     i+=1
        # return count-1
        
        # Do your math homework !!!
        return int(-0.5+(sqrt(2*n+0.25)))
            