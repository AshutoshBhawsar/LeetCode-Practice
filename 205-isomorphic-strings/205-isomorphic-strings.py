class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return [s.find(i) for i in s] == [t.find(j) for j in t]
        
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))