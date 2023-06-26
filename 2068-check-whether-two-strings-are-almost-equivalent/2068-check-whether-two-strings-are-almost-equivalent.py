class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hmap = [0] * 26
        
        for char in word1: 
            hmap[ord(char) - ord("a")] += 1
        
        for char in word2: 
            hmap[ord(char) - ord("a")] -= 1
        return not any ([(abs(freq)>3) for freq in hmap])
            