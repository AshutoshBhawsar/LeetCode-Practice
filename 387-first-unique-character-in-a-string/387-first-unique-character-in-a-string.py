class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts=collections.Counter(s)
        for i in range(len(s)):
            if counts[s[i]]==1:
                return i
        return -1