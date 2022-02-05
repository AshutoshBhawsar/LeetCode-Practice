class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i]*=-1
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -heappop(nums)