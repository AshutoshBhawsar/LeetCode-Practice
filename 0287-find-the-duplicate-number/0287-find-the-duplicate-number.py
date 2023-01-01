class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force
        counts=collections.Counter(nums)
        for key,value in counts.items():
            if value>=2:
                return key
        