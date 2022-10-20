class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return sorted(nums, reverse=True)[k-1]
        heapq.heapify([-x for x in nums])
        return heapq.nlargest(k,nums)[-1]