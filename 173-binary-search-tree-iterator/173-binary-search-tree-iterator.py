# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list1=self.inorderTraversal(root)
        #print(self.list1)
        self.maxIndex=len(self.list1)-1
        self.index1=0

    def next(self):
        """
        :rtype: int
        """
        self.index1+=1
        return self.list1[self.index1-1]
    

    def hasNext(self):
        """
        :rtype: bool
        """
        #temp=self.index1+1
        return True if self.maxIndex>=self.index1 else False
        
    def inorderTraversal(self,root):
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()