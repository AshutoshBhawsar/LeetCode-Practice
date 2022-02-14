class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Cascading subsets ######### O(n * 2^n)
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])
        return res
        