class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # str1=''
        # for i in num:
        #     str1+=str(i)
        # answer=int(str1)+k
        # list1=[]
        # for i in str(answer):
        #     list1.append(int(i))
        # return list1
    
        return list(str(int("".join(map(str,num)))+k))