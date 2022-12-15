class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts=collections.Counter(text)
        balloon=collections.Counter('balloon')
        res=len(text)
        for c in balloon:
            res=min(res,counts[c]//balloon[c])
        return res
