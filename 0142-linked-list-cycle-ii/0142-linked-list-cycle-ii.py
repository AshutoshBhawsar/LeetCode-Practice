# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        hmap={}
        temp=head
        i=0
        while temp is not None:
            if temp in hmap:
                return temp
            hmap[temp]=i
            i+=1
            temp=temp.next
        return None
        
            