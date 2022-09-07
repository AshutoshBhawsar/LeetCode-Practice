class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        A=[]
        for i in mat:
            for j in i:
                A.append(j)
        if r * c == len(A):
            return [A[i*c : (i + 1)*c] for i in range(r) ]
        else:
            return mat