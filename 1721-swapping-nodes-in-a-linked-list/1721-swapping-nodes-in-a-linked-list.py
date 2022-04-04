# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        list1=[]
        temp=head
        while(temp):
            list1.append(temp.val)
            temp=temp.next
        list1[k-1],list1[-k]=list1[-k],list1[k-1]
        newtemp=ListNode(0)
        temp=newtemp
        for i in list1:
            newNode=ListNode(i)
            temp.next=newNode
            temp=temp.next
        return newtemp.next