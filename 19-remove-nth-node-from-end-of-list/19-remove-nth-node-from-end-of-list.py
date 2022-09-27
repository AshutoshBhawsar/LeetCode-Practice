# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        list1=[]
        temp=head
        while(temp):
            list1.append(temp.val)
            temp=temp.next
        temp=ListNode(0)
        pseudo=temp
        temp.next=head
        for i in range(len(list1)-n):
            temp=temp.next
        temp.next=temp.next.next
        return pseudo.next