class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force TLE :(
        # n=len(nums)
        # answer=[0]*n
        # for i in range(n):
        #     prod=1
        #     for j in range(n):
        #         if i==j:
        #             continue
        #         prod=prod*nums[j]
        #     answer[i]=prod
        # return answer
        
        # Left and right prefix product
        n=len(nums)
        left,right,answer=[1]*n,[1]*n,[1]*n
        i,j=1,n-2
        while(i<n):
            left[i]=left[i-1]*nums[i-1]
            right[j]=right[j+1]*nums[j+1]
            i+=1
            j-=1
        #print(left,right)
        for i in range(n):
            answer[i]=left[i]*right[i]
        return answer