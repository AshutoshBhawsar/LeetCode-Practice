class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Cascading subsets ######### O(n * 2^n)
        answer = [[]]
        for num in nums:
            answer += [curr + [num] for curr in answer]
        return answer