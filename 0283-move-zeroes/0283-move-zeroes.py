class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force extra memory, worst solution possible
#         arr=[]
#         for num in nums:
#             if num!=0:
#                 arr.append(num)
#         n,a=len(nums),len(arr)
#         for i in range(n):
#             if i<a:
#                 nums[i]=arr[i]
#             else:
#                 nums[i]=0
        
        # Optimized swapping 2 pointers, O(n), O(1)
        zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero+=1