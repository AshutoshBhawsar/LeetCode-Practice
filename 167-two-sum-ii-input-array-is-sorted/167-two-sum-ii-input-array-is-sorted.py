class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1
        while l<r:
            sum1=numbers[l]+numbers[r]
            if sum1==target:
                return [l+1,r+1]
            elif sum1<target:
                l+=1
            else:
                r-=1
        