class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # rcounts,mcounts=collections.Counter(ransomNote),collections.Counter(magazine)
        # for i in ransomNote:
        #     if rcounts[i]>mcounts[i]:
        #         return False
        # return True
        
        if len(ransomNote)>len(magazine):
            return False
        counts=collections.Counter(magazine)
        for i in ransomNote:
            if counts[i]<=0:
                return False
            counts[i]-=1
        return True