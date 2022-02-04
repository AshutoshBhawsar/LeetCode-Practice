class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Traditional counter data structure
        # counts=collections.Counter(nums)
        # for element in counts:
        #     if counts[element]>1:
        #         return element
        
        hmap={}
        for i in nums:
            if i in hmap:
                return i
            hmap[i]=i