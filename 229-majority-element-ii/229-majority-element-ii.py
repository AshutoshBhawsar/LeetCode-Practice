class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1=set()
        n=len(nums)
        counts=collections.Counter(nums)
        for i in nums:
            if counts[i]>n/3:
                l1.add(i)
        return list(l1)