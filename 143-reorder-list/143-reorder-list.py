# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp=head
        list1=[]
        while(temp):
            list1.append(temp.val)
            temp=temp.next
        start,end=0,len(list1)-1
        temp=head
        while(True):
            if not temp:
                return
            if start==end:
                temp.val=list1[start]
                return
            temp.val=list1[start]
            start=start+1
            temp=temp.next
            temp.val=list1[end]
            end=end-1
            temp=temp.next
            