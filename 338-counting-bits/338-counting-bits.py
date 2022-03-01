class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # brute force solution #######
        # ans=[]
        # for i in range(n+1):
        #     t=collections.Counter(bin(i)[2:])
        #     ans.append(t['1'])
        # return ans
        
        
        # pop count approach ###########
#         def pop_count(x):
#             count = 0
#             while x != 0:
#                 x &= x - 1 # zeroing out the least significant nonzero bit
#                 count += 1
#             return count
            
#         ans = [0] * (n + 1)
#         for x in range(n + 1):
#             ans[x] = pop_count(x)
    
#         return ans  

        
        # DP ########
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 

        