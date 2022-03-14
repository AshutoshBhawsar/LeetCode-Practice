class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Linear scan
        start,end=-1,-1
        for i,ele in enumerate(nums):
            if ele==target:
                if start==-1:
                    start,end=i,i
                else:
                    end=i
        return [start,end]