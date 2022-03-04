class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rcounts,mcounts=collections.Counter(ransomNote),collections.Counter(magazine)
        for i in ransomNote:
            if rcounts[i]>mcounts[i]:
                return False
        return True