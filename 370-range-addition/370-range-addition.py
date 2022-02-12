class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        # Brute force TLE ###############
        # answer = [0] * length
        # for tup in updates:
        #     incr=tup[2]
        #     for i in range(tup[0],tup[1]+1):
        #         answer[i]+=incr
        # return answer
        
#         Partial Sum ##########
        ans = [0] * length
        for start, end, value in updates:
            ans[start] += value
            end += 1
            if end < len(ans):
                ans[end] -= value

        for i in range(1, len(ans)):
            ans[i] += ans[i-1]

        return ans