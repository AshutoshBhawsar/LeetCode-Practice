class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n==1:
        #     return True
        # if n%4!=0 or n<=0:
        #     return False
        # return self.isPowerOfFour(n/4)
        
        # Power of Math -_-
        return n>0 and math.log(n,2)%2==0