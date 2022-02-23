class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=heapq.nlargest(3,nums)
        smallest=heapq.nsmallest(2,nums)
        return max(largest[0]*largest[1]*largest[2],largest[0]*smallest[0]*smallest[1])