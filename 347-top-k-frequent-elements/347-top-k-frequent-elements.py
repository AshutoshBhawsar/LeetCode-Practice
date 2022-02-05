class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Noob approach ############
        # maxlist,answer=[],[]
        # counts=collections.Counter(nums)
        # for key,value in counts.items():
        #     maxlist.append([value,key])
        # maxlist.sort(key=lambda x : x[0],reverse=True)
        # for i in range(k):
        #     answer.append(maxlist[i][1])
        # return answer
        
        
        # using nlargest function of heap #######
        if k==len(nums):
            return nums
        
        counts=collections.Counter(nums)
        return nlargest(k,counts.keys(),key=counts.get)