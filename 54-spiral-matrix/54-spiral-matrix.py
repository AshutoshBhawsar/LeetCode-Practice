class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # credits to Lord Stefan (https://leetcode.com/StefanPochmann)
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])