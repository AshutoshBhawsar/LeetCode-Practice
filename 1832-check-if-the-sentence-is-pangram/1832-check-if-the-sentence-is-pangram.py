class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # set1={}
        # for i in sentence:
        #     set1.add(i)
        # return True if len(set1)==26 else False
    
        return True if len(set(x for x in sentence))==26 else False