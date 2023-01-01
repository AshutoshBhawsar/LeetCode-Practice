class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts=collections.Counter(s)
        for ele in t:
            if ele not in counts or counts[ele]==0:
                return ele
            else:
                counts[ele]-=1