class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # traditional combinations TLE##################
        # l1=[x for x in range(1,n)]
        # ans=[]
        # comb=itertools.combinations(l1,k)
        # for ele in comb:
        #     if sum(ele)==n:
        #         ans.append(ele)
        # return ans
    
        # backtracking###########
#         results=[]
        
#         def backtrack(remain,comb,next_start):
#             if remain==0 and len(comb)==k:
#                 results.append(list(comb))
#                 return
#             elif remain<0 or len(comb)==k:
#                 return
            
#             for i in range(next_start,9):
#                 comb.append(i+1)
#                 backtrack(remain-i-1,comb,i+1)
#                 comb.pop()
        
#         backtrack(n,[],0)
        
#         return results
    
        #DFS
        
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret
    
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)