class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        transpose = map(None, *words)
        return transpose == map(None, *transpose)