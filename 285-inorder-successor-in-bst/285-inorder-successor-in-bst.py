# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        flag=False
        reqVal=0
        inorder=self.inorderTraversal(root)
        queue=[root]
        for i in inorder:
            if flag:
                reqVal=i
                break
            if i==p.val:
                flag=True
        if reqVal==0:
            return None
        for element in queue:
            if element.val==reqVal:
                return element
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        
    def inorderTraversal(self,root):
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else[]