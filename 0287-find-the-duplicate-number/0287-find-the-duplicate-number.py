class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force
        # counts=collections.Counter(nums)
        # for key,value in counts.items():
        #     if value>=2:
        #         return key
        
        # Negative Marking
        # for ele in nums:
        #     if nums[abs(ele)]<0:
        #         return abs(ele)
        #     nums[abs(ele)]*=-1
        
        # Floyd's Tortoise and Hare cycle detection
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
        