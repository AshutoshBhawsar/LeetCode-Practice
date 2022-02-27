class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # 2 Liner
        counts=collections.Counter(arr).values()
        return len(counts)==len(set(counts))
        
        
        # Full Simulation using counter and hmap
        # counts=collections.Counter(arr)
        # hmap={}
        # for element in counts:
        #     temp=counts[element]
        #     if temp in hmap:
        #         return False
        #     hmap[temp]=element
        # return True