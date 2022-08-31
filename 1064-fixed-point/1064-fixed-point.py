class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i in range(0,len(arr)):
            if i == arr[i]:
                return i
        return -1