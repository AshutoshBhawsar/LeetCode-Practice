class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for _ in letters:
            if ord(_)<=ord(target):
                continue
            return _
        return letters[0]