class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap={}
        for i in nums:
            hmap[i]=i
        for i in range(len(nums)):
            if i+1 not in hmap:
                return i+1
        return i+2