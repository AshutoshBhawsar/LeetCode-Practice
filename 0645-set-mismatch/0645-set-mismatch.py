class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # My normal map approach
        # seen=set()
        # n=len(nums)
        # for num in nums:
        #     if num in seen:
        #         repeat=num
        #     seen.add(num)
        # return [repeat,sum(range(n+1))-sum(nums)+repeat]
            
        # One liner by Lord Stefan Pochmann
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]