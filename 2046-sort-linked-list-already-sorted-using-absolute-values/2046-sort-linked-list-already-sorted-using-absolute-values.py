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
        # Using extra space
        # if not head:
        #     return None
        # deque=collections.deque()
        # temp=head
        # while(temp):
        #     if temp.val>=0:
        #         deque.append(temp.val)
        #     else:
        #         deque.appendleft(temp.val)
        #     temp=temp.next
        # newHead=ListNode(deque.popleft())
        # temp=newHead
        # while(deque):
        #     temp.next=ListNode(deque.popleft())
        #     temp=temp.next
        # return newHead
        
        
        
        # Insert at head
        curr = head
        while curr.next:
            if curr.val > curr.next.val:
                temp = curr.next
                curr.next = temp.next
                temp.next = head
                head = temp
            else:
                curr = curr.next
        return head
                