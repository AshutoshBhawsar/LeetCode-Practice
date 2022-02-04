class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Traditional counter data structure #######
        # counts=collections.Counter(nums)
        # for element in counts:
        #     if counts[element]>1:
        #         return element
        
        
        # Using Hashmap ######
        # hmap={}
        # for i in nums:
        #     if i in hmap:
        #         return i
        #     hmap[i]=i
        
        # Using negative marking
        # we use indices of arrays to find duplicate
        
        for i in nums:
            current=abs(i)
            if nums[current]<0:
                return current
            nums[current]=-nums[current]
        
        
            