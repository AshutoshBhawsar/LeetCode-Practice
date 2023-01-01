# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute Force
        temp=head
        while temp!=None:
            if temp.val==float('-inf'):
                return True
            temp.val=float('-inf')
            temp=temp.next
            
        return False
            