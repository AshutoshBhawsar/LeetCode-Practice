class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                if prev == 1: # violation!
                    count -= 1
                prev = 1
            else:
                if prev == 1: # can't plant
                    prev = 0 
                else:
                    count += 1
                    prev = 1 # the cur plot gets taken
            
        return count >= n