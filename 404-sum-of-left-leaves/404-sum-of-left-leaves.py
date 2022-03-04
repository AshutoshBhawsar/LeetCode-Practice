# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    count=0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0
        def helper(root):
            if not root:
                return
            if root.left and not root.left.right and not root.left.left:
                self.count+=root.left.val
            helper(root.left)
            helper(root.right)
            
        helper(root)
        return self.count