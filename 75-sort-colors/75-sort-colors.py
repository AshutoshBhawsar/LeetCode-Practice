class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # simple bubble sort
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]<nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        # return nums
        
        # using lib function 'Illegal'
        #return nums.sort()
        
        # dutch partitioning problem
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1