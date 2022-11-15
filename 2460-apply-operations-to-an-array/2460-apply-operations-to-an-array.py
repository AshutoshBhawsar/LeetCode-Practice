class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        while(i<n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            i+=1
        zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero+=1
        return nums