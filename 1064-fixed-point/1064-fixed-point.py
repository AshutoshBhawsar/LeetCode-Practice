class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # Simple search
        # for i in range(0,len(arr)):
        #     if i == arr[i]:
        #         return i
        # return -1
        
        # Binary Search
        l,r=0,len(arr)-1
        while(l<r):
            m=(l+r)//2
            if arr[m]-m<0:
                l=m+1
            else:
                r=m
        return l if arr[l]==l else -1