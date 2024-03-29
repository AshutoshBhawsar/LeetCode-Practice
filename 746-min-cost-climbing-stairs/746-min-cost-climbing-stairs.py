class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(0,n):
            if i<2:
                dp[i]=cost[i]
            else:
                dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])