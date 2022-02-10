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
        string1,string2="",""
        temp=l1
        while(temp is not None):
            string1+=str(temp.val)
            temp=temp.next
        temp=l2
        while(temp is not None):
            string2+=str(temp.val)
            temp=temp.next
        sum1=str(int(string1[::-1])+int(string2[::-1]))[::-1]
        l3=ListNode()
        temp=l3
        for i in sum1:
            temp.next=ListNode()
            temp=temp.next
            temp.val=int(i)
        return l3.next