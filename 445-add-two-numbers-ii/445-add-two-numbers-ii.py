# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp=l1
        str1,str2='',''
        while temp:
            str1+=str(temp.val)
            temp=temp.next
        temp=l2
        while temp:
            str2+=str(temp.val)
            temp=temp.next
        str2=str(int(str1)+int(str2))
        l3=ListNode(0)
        temp=l3
        for i in str2:
            temp.next=ListNode()
            temp=temp.next
            temp.val=i
        return l3.next