class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Simple recursion Fibonacci (TLE) O(2^n)
        # if n<3:
        #     return n
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
    
        
        # Dynamic programming
        if n < 3:
            return n
        dp=[0]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]