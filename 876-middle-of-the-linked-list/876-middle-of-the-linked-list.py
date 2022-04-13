# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        slow,fast=head,head
        flag=False
        while True:
            if fast.next is None:
                flag=True
                break
            if fast.next.next is None:
                break
            slow=slow.next
            fast=fast.next.next
            
        return slow if flag else slow.next