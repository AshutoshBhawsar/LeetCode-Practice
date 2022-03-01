class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        max_height,ans=0,collections.deque()
        for i in reversed(range(len(heights))):
            if heights[i]>max_height:
                max_height=heights[i]
                ans.appendleft(i)
        return ans