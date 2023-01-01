# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force
        # if not head:
        #     return None
        # hmap={}
        # temp=head
        # i=0
        # while temp is not None:
        #     if temp in hmap:
        #         return temp
        #     hmap[temp]=i
        #     i+=1
        #     temp=temp.next
        # return None
        
        # FLoyd's magic
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
            