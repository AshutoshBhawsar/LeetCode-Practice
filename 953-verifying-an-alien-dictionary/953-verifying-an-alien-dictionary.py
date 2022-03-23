class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if hmap[s1] < hmap[s2]:
                    break
                elif hmap[s1] > hmap[s2]:
                    return False
        return True