class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        if not n: return []
        
        def formatRanges(start, end):
            if start==end:
                return str(start)
            return str(start)+"->"+str(end)
        
        
        ranges=[]
        start=end=nums[0]
        
        for i in range(1,n):
            if nums[i]==end+1:
                end=nums[i]
            else:
                ranges.append(formatRanges(start,end))
                start=end=nums[i]
        
        ranges.append(formatRanges(start,end))
        
        return ranges
        