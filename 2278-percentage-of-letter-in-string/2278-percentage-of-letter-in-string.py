class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return floor(s.count(letter)*100/len(s))