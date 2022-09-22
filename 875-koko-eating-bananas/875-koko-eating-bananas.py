class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        while(left<right):
            mid=(left+right)//2
            temp_count=0
            for i in piles:
                temp_count+=math.ceil(i/mid)
            if temp_count>h:
                left=mid+1
            else:
                right=mid
        return right