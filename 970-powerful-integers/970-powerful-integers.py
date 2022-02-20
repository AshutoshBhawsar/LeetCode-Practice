class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        xs = {x**i for i in range(20) if x**i < bound}
        ys = {y**i for i in range(20) if y**i < bound}
        return list({i + j for i in xs for j in ys if i + j <= bound})