class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts=collections.Counter(arr)
        hmap={}
        for element in counts:
            temp=counts[element]
            if temp in hmap:
                return False
            hmap[temp]=element
        return True