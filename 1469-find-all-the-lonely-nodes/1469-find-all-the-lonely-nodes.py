# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self, list1=[]):
        self.list1=[]
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        if not root.left and root.right: self.list1.append(root.right.val)
        if not root.right and root.left: self.list1.append(root.left.val)
        self.getLonelyNodes(root.left)
        self.getLonelyNodes(root.right)
        return self.list1