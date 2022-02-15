class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counts=Counter(nums)
        for element in counts:
            if counts[element]==1:
                return element
        