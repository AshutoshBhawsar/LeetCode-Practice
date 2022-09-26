class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            formula_result=a*(nums[i]**2)+b*nums[i]+c
            result.insert(bisect.bisect(result,formula_result),formula_result)
        return result