class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # simple recursion
        # if n<2:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
    
    
        # DP
        if n<2:
            return n
        dp=[0]*(n+1)
        dp[0],dp[1]=0,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]