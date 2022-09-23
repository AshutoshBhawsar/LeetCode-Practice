# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        string1=""
        while(temp):
            string1+=str(temp.val)
            temp=temp.next
        return string1==string1[::-1]