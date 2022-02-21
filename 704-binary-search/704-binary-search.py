class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        mid=n//2
        l,r=0,n-1
        while(l<=r):
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
                mid=(r+l)//2
            else:
                r=mid-1
                mid=(r+l)//2
        return -1