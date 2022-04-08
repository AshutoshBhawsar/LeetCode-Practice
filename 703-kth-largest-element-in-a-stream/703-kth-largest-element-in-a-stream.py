class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.numStack=sorted(nums)
        self.k=k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        i=bisect.bisect_left(self.numStack,val)
        self.numStack.insert(i,val)
        return self.numStack[-self.k]
            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)