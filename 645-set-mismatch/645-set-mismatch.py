class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in nums:
        #     current_num=abs(i)
        #     if nums[current_num]<0:
        #         duplicate=current_num
        #         break
        #     nums[current_num]=-nums[current_num]
        return [sum(nums) - sum(set(nums)),sum(range(1, len(nums)+1)) - sum(set(nums))]