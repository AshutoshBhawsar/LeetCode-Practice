class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using Sort #########
        # nums.sort()
        # for i in range(len(nums)):
        #     if i!=nums[i]:
        #         return i
        # return i+1
        
        # Using hashmap##########
        # hashmap={}
        # for i in range(len(nums)):
        #     hashmap[nums[i]]=i
        # #print(hashmap)
        # for i in range(len(nums)):
        #     if i not in hashmap:
        #         return i
        # return i+1
        
        # Using Sum########## gaussian formula : n(n+1)/2
        original_sum= len(nums)*(len(nums)+1)//2
        actual_sum=sum(nums)
        return original_sum-actual_sum