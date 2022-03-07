# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev=ListNode(0)
        temp=prev
                
        while(l1 and l2):
            if l1.val>l2.val:
                temp.next=l2
                l2=l2.next
            else:
                temp.next=l1
                l1=l1.next
            temp=temp.next
        temp.next=l1 if l1 else l2
        return prev.next