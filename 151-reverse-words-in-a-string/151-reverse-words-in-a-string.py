class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(x+" " for x in reversed(s.split()))[:-1]