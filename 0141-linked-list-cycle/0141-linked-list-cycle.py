# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute Force
#         temp=head
#         while temp!=None:
#             if temp.val==float('-inf'):
#                 return True
#             temp.val=float('-inf')
#             temp=temp.next
            
#         return False

        # FLoyd's Tortoise and Hare cycle detection
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
            