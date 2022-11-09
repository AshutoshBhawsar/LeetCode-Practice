# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        n=1
        temp=head
        while(temp.next):
            temp=temp.next
            n+=1
        if n==1:
            return head
        shift=k%n
        temp.next=head
        for i in range(n-shift):
            temp=temp.next
        head=temp.next
        temp.next=None
        return head