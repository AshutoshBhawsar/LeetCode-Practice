# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
    
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        for i in range(candidate):
            if knows(candidate, i) or not(knows(i, candidate)):
                return -1
        
        for i in range(candidate+1, n):
            if not knows(i, candidate):
                return -1
            
        return candidate