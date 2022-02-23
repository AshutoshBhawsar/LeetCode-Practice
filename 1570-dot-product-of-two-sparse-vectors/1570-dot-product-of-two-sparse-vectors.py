class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vector=list(nums)
        self.length=len(self.vector)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        sum1=0
        for i in range(self.length):
            sum1+=(self.vector[i]*vec.vector[i])
        return sum1
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)