class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results=[]
        def backtrack(new_target,comb,start_index):
            if new_target==0:
                results.append(list(comb))
                return
            elif new_target<0:
                return
            
            for i in range(start_index,len(candidates)):
                comb.append(candidates[i])
                backtrack(new_target-candidates[i],comb,i)
                comb.pop()
        
        backtrack(target,[],0)
        return results