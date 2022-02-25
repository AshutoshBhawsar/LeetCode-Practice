# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortLinkedList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        deque=collections.deque()
        temp=head
        while(temp):
            if temp.val>=0:
                deque.append(temp.val)
            else:
                deque.appendleft(temp.val)
            temp=temp.next
        newHead=ListNode(deque.popleft())
        temp=newHead
        while(deque):
            temp.next=ListNode(deque.popleft())
            temp=temp.next
        return newHead
                