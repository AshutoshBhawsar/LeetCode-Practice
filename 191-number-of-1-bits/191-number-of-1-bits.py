class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # counter
        return collections.Counter(bin(n)[2:])['1']
    
        # pop count
        # sum1=0
        # while(n!=0):
        #     sum1+=1
        #     n&=(n-1)
        # return sum1