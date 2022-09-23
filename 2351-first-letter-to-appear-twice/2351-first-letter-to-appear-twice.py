class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hmap={}
        for item in s:
            if item in hmap:
                return item
            hmap[item]=0