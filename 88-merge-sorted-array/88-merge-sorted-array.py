class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        for i in range(n):
            nums1.pop()
        for i in range(n):
            nums1.insert(bisect.bisect(nums1,nums2[i]),nums2[i])