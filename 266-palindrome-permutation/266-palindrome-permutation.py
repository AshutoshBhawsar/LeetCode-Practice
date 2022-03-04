class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==s[::-1]:
            return True
        flag_even = True if len(s)%2==0 else False
        counts=collections.Counter(s)
        final_c=0
        for c in counts:
            if counts[c]%2!=0:
                final_c+=1
        return final_c<=1