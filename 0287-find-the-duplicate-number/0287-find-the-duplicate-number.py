class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force
        # counts=collections.Counter(nums)
        # for key,value in counts.items():
        #     if value>=2:
        #         return key
        
        # Cycle detection
        for ele in nums:
            if nums[abs(ele)]<0:
                return abs(ele)
            nums[abs(ele)]*=-1
        