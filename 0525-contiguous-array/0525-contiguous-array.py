class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        answer=0
        hmap={0:-1}
        prefix=[0]
        for i in range(len(nums)):
            if nums[i]==0:
                prefix.append(prefix[-1]-1)
            else:
                prefix.append(prefix[-1]+1)
            if prefix[-1] not in hmap:
                hmap[prefix[-1]]=i
            else:
                answer=max(answer,i-hmap[prefix[-1]])
        
        return answer