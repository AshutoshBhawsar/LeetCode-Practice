class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # for i in range(1,len(arr)-1):
        #     if arr[i]>arr[i+1]:
        #         return i
        
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) / 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l