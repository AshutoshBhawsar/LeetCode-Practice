class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute Force
        counts=collections.Counter(nums)
        for key,value in counts.items():
            if value==1:
                return key
            