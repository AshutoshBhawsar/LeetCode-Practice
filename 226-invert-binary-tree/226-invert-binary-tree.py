# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterative simulation #############
        # if not root:
        #     return root
        # queue=[root]
        # for ele in queue:
        #     if ele.left and ele.right:
        #         queue.append(ele.left)
        #         queue.append(ele.right)
        #         ele.left,ele.right=ele.right,ele.left
        #     elif ele.left:
        #         queue.append(ele.left)
        #         ele.right=ele.left
        #         ele.left=None
        #     elif ele.right:
        #         queue.append(ele.right)
        #         ele.left=ele.right
        #         ele.right=None
        # return root
        
        # Crazy recursive ! #################
        if not root:
            return root
        root.left, root.right=self.invertTree(root.right), self.invertTree(root.left)
        return root