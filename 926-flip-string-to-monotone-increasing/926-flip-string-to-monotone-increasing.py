class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        count1,flip=0,0
        for i in s:
            if i=='1':
                count1+=1
            else:
                flip+=1
            flip=min(count1,flip)
        return flip