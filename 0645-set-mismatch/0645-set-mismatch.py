class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set()
        n=len(nums)
        for num in nums:
            if num in seen:
                repeat=num
            seen.add(num)
        return [repeat,sum(range(n+1))-sum(nums)+repeat]
            
            
        