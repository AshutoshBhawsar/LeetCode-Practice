class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # brute force
        l1,l2=[],[]
        for i,word in enumerate(wordsDict):
            if word1==word:
                l1.append(i)
            if word2==word:
                l2.append(i)
        min1=float('inf')
        for i in l1:
            for j in l2:
                if abs(i-j)<min1:
                    min1=abs(i-j)
        return min1