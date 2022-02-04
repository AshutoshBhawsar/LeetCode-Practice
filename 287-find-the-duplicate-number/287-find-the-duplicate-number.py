class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=collections.Counter(nums)
        for element in counts:
            if counts[element]>1:
                return element