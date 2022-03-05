class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Force ######## TLE -_-
        # max_count=0
        # for i in nums:
        #     hmap={}
        #     count=0
        #     while(nums[i] not in hmap):
        #         hmap[nums[i]]=nums[i]
        #         count+=1
        #         i=nums[i]
        #     max_count=max(max_count,count)
        # return max_count
        
        # optimised Brute Force
        hmap_g={}
        max_count=0
        for i in nums:
            hmap={}
            count=0
            while(nums[i] not in hmap):
                if nums[i] in hmap_g:
                    break
                hmap[nums[i]]=nums[i]
                count+=1
                i=nums[i]
            max_count=max(max_count,count)
            hmap_g.update(hmap)
        return max_count
        
        