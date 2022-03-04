class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap={}
        for element in nums:
            if element in hashmap:
                return True
            hashmap[element]=element
        return False