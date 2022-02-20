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
        results=[]
        
        def backtrack(remain,comb,next_start):
            if remain==0 and len(comb)==k:
                results.append(list(comb))
                return
            elif remain<0 or len(comb)==k:
                return
            
            for i in range(next_start,9):
                comb.append(i+1)
                backtrack(remain-i-1,comb,i+1)
                comb.pop()
        
        backtrack(n,[],0)
        
        return results