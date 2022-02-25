# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        temp=head
        list1=[]
        while(temp):
            list1.append(temp.val)
            temp=temp.next
        list1.sort()
        newHead=ListNode(list1[0])
        tempPointer=newHead
        for ele in list1[1:]:
            temp=ListNode(ele)
            tempPointer.next=temp
            tempPointer=tempPointer.next
        return newHead