# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder=self.helperInorder(root)
        for i in range(len(inorder)-1):
            if inorder[i]>=inorder[i+1]:
                return False
        return True
        
    def helperInorder(self,root):
        return self.helperInorder(root.left)+[root.val]+self.helperInorder(root.right) if root else []
        