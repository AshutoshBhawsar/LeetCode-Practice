class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(n+1):
            t=collections.Counter(bin(i)[2:])
            ans.append(t['1'])
        return ans