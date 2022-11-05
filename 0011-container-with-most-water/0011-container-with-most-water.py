class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force TLE
        # answer=0
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         temp=min(height[i],height[j])
        #         answer=max(answer,temp*(j-i))
        # return answer
        
        left,right=0,len(height)-1
        water=0
        while left<right:
            temp_height=min(height[left],height[right])
            water=max(water,(right-left)*temp_height)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return water
        