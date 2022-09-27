# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        hmap={}
        pseudo=ListNode()
        pseudo.next=head
        temp=head
        while(temp):
            if temp.val in hmap:
                hmap[temp.val]+=1
            else:
                hmap[temp.val]=1
            temp=temp.next
        temp=pseudo
        while(temp.next):
            if hmap[temp.next.val]>1:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return pseudo.next