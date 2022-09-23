class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while(abs(left-right)>1):
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid
        return min(nums[left],nums[right])