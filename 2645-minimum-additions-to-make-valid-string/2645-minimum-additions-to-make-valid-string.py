class Solution:
    def addMinimum(self, word: str) -> int:
        return 3 + sum(a >= b for a,b in pairwise(word)) * 3 - len(word)