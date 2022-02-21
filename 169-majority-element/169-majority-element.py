class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        counts=collections.Counter(nums)
        for i in nums:
            if counts[i]>(n/2):
                return i
