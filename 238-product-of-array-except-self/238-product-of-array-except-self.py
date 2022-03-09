class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute force ##########
        # result=[]
        # for i in range(len(nums)):
        #     mul=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             mul*=nums[j]
        #     result.append(mul)
        # return result
        
        # cumulative products : left and right of element
        n=len(nums)
        left,right,answer=[0]*n,[0]*n,[0]*n
        left[0]=1
        for i in range(1,n):
            left[i]=nums[i-1]*left[i-1]
        right[n-1]=1
        for i in reversed(range(n-1)):
            right[i]=nums[i+1]*right[i+1]
        for i in range(n):
            answer[i]=left[i]*right[i]
        return answer
        