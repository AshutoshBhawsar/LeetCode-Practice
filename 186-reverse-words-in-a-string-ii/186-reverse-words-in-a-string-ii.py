class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s1="".join(x for x in s)
        s2=" ".join(x for x in reversed(s1.split()))
        s[:]=s2[:]