class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1

        # Find first decreasing element
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        # Descending case
        if i == 0:
            nums.reverse()
            return 
        
        # Find next larger element
        while nums[j] <= nums[i-1]:
            j -= 1
        
        # Swap
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # Reverse
        nums[i:]= nums[len(nums)-1:i-1:-1]