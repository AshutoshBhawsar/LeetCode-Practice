class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # TIME LIMIT EXCEEDED SOLUTION ######################
        # if len(nums)<2 or k==1:
        #     return nums
        # list1 = []
        # i, j = 0, k-1
        # current_max=max(nums[i:j])
        # while (j < len(nums)):
        #     if nums[j]>current_max:
        #         current_max=nums[j]
        #     #print(i,j)
        #     list1.append(current_max)
        #     i += 1
        #     j += 1
        #     if current_max==nums[i-1]:
        #         current_max = max(nums[i:j])
        # return list1
        
        # Simpler yet TIME LIMIT EXCEEDED SOLUTION #####################
#         n = len(nums)
#         if n * k == 0:
#             return []
        
#         return [max(nums[i:i + k]) for i in range(n - k + 1)]

        # Using Deque data structure ##############
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out