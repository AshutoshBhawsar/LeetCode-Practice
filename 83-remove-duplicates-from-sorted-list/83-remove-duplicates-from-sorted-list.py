# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # simple one pass    
        # temp=head
        # while(temp and temp.next):
        #     if temp.val==temp.next.val:
        #         temp.next=temp.next.next
        #     else:
        #         temp=temp.next
        # return head
    
        # Kind of optimised
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head