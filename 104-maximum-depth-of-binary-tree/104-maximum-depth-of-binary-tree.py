# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Simple Recursion 
        # if root:
        #     count1=self.maxDepth(root.left)
        #     count2=self.maxDepth(root.right)
        #     return 1+max(count1,count2)
        # return 0
        
        # Same but one liner
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right)) if root else 0