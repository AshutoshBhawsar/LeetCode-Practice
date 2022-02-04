class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # for i in range(len(nums)):
        #     if i!=nums[i]:
        #         return i
        # return i+1
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        #print(hashmap)
        for i in range(len(nums)):
            if i not in hashmap:
                return i
        return i+1