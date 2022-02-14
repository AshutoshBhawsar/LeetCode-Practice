class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap={}
        for i,val in enumerate(nums):
            if target-val in hmap:
                return [hmap[target-val],i]
            hmap[val]=i
        