class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        for i, a in enumerate(prices):
            while stack and prices[stack[-1]] >= a:
                prices[stack.pop()] -= a
            stack.append(i)
        return prices