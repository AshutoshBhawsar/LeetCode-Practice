class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap={}
        for i in range(len(nums)):
            if nums[i] in hmap and hmap[nums[i]]==1:
                return True
            hmap[nums[i]]=1
            if len(hmap)>k:
                hmap[nums[i-k]]=0
        return False