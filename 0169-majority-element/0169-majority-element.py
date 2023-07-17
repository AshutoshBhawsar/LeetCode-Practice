class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0

        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1

        return majority
            