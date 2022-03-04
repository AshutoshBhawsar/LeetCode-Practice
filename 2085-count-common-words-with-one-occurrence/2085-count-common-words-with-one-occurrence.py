class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count=0
        d1=collections.Counter(words1)
        d2=collections.Counter(words2)
        if len(d1)>len(d2):
            d1,d2=d2,d1
        for i in d1:
            if i in d2 and d2[i]==1 and d1[i]==1:
                count+=1
        return count