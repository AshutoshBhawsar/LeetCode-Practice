class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hmap = {}
        for i, j in enumerate(nums):
            if j in hmap and i - hmap[j] <= k:
                return True
            hmap[j] = i
        return False