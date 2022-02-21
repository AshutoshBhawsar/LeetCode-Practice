class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key= lambda x:self.distance(x))[:k]
    
    def distance(self,x):
        return x[0]**2 + x[1]**2