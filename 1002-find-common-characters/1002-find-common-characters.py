class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=collections.Counter(words[0])
        for _ in words:
            res&=collections.Counter(_)
        return list(res.elements())
            