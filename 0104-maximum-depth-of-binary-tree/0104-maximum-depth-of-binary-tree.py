# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0) if root else 0
        
    def helper(self,root,depth):
        if not root:
            return depth
        left = self.helper(root.left,depth+1)
        right = self.helper(root.right,depth+1)
        return max(left,right)