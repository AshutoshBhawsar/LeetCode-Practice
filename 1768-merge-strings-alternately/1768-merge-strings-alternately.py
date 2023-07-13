class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m=len(word1),len(word2)
        output=""
        for i in range(max(n,m)):
            if i+1<=n:
                output+=word1[i]
            if i+1<=m:
                output+=word2[i]
        return output