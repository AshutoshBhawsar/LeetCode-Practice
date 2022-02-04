class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using hmap for O(n) time and O(n) space, but the question wants O(1) space, see below for solution
        # hmap={}
        # for i in nums:
        #     hmap[i]=i
        # for i in range(len(nums)):
        #     if i+1 not in hmap:
        #         return i+1
        # return len(nums)+1                  #base case
        
        
        
        
        # Convert all out of index values to 0
        for i,num in enumerate(nums):
            if num <= 0:
                nums[i] = 0
        
        # make all values as negatives for corresponding values as indices (nums[values])
        for i,num in enumerate(nums):
            index = abs(num)-1
            if index >= 0 and index < len(nums):
                if nums[index] == 0:
                    nums[index] = float('-inf')
                elif nums[index] > 0: # we dont want to make negative to be positive again, when its duplicated num
                    nums[index] *= -1

        # find the missing element
        for index,num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1
        
        