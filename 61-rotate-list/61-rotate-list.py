# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        temp=head
        c=0
        while(temp):
            temp=temp.next
            c+=1
        for i in range(k%c):
            temp=head
            prev=temp
            while(temp.next):
                prev=temp
                temp=temp.next
            temp.next=head
            prev.next=None
            head=temp
            temp=prev
        return head
        