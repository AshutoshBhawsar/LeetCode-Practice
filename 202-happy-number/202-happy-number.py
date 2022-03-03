class Solution(object):
    hmap={}
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.hmap={}
        while(n>1):
            n=self.helper(n)
            if n==0:
                return False
        return True if n==1 else False    
        
    def helper(self,n):
        #return sum(x*x for int(x) in list(str(n)))
        sum1=0
        for i in str(n):
            i=int(i)
            sum1+=i*i
        if sum1 not in self.hmap:
            self.hmap[sum1]=sum1
        else:
            return 0
        return sum1