class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        str1=''
        for i in num:
            str1+=str(i)
        answer=int(str1)+k
        return list(str(answer))
    
        #return list(str(int("".join(map(str,num)))+k))