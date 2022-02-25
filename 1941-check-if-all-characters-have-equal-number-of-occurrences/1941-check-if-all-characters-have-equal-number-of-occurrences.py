class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=="":
            return True
        counts=collections.Counter(s)
        max1=counts[s[0]]
        for i in counts:
            if counts[i]!=max1:
                return False
        return True