class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        left_max,right_max=height[0],height[-1]
        water=0
        left,right=1,len(height)-2

        while(left<=right):
            if left_max<=right_max:
                left_max=max(left_max,height[left])
                water+=left_max-height[left]
                left+=1
            else:
                right_max=max(right_max,height[right])
                water+=right_max-height[right]
                right-=1
        return water